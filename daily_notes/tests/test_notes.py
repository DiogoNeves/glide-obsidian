from datetime import datetime, timezone
import errno
import os
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from glide_memory import StoreError, ConflictError, IntegrityError
from glide_obsidian.store import ObsidianStore as Store
from glide_memory.pipeline import _activity_record, _body, PROJECT_STATE_ID
from glide_memory.store import digest
from glide_obsidian.notes import configure, settings, preview, write, unpack, GRANT_ID, _create
from glide_obsidian.bridge import ObsidianServer

NOW = datetime(2026, 9, 6, 8, tzinfo=timezone.utc)
DAY = '2026-09-05'

class DailyNotesTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='glide-obsidian-notes-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.vault = self.root / 'vault'; self.vault.mkdir()
        self.original = self.vault / 'A thought.md'; self.original.write_text('Keep my words unchanged.\n')
        self.approval_file = self.vault / 'Decision.md'; self.approval_file.write_text('Enable daily project progress notes for the fictional garden project.\n')
        self.store = Store.initialize(self.vault, self.root / 'state')
        self.store.activate_writer(old_writer_stopped=True)
        self.approval = {'path':'Decision.md','sha256':hashlib.sha256(self.approval_file.read_bytes()).hexdigest(),'quote':self.approval_file.read_text()}
        self.policy = {'enabled':True,'timezone':'Europe/London','start_date':DAY,'projects':['projects/garden.md'],'titles':{'projects/garden.md':'Garden'},'project_notes':{'projects/garden.md':'A thought.md'}}
        self.events = []

    def tearDown(self):
        self.assertEqual('Keep my words unchanged.\n', self.original.read_text())

    def commit(self, record):
        old = self.store._load()['records'].get(record['id'])
        revs = {record['id']:old['revision'] if old else 0}
        p = self.store.propose([record], expected_revisions=revs, rationale='Synthetic activity fixture', idempotency_key=digest([record,revs]))
        return self.store.apply(p['proposal_id'])

    def event(self, n=1, when='2026-09-05T12:23:00+01:00', project='garden'):
        commit = str(n).zfill(40)
        repo = 'git:' + digest(project)
        return {'commit':commit,'committed_at':when,'event_id':'commit:'+digest([repo,commit]),'repo_id':repo,'index_path':f'projects/{project}.md','source_ref':f'git:github.com/example/{project}@{commit}','url':f'https://github.com/example/{project}/commit/{commit}','title':f'Improve seed labels {n}'}

    def intake(self, events=None, status='complete', pending=0):
        events = events or [self.event()]
        self.events = events
        grouped = {}
        for e in events:grouped.setdefault(e['repo_id'],[]).append(e)
        for repo, group in grouped.items():
            self.commit(_activity_record('activity:'+repo[4:44]+':2026-09',repo,'2026-09',group))
        coverage = [{'repo_id':repo,'index_path':group[0]['index_path'],'status':status,'pending':pending} for repo,group in grouped.items()]
        self.commit({'id':PROJECT_STATE_ID,'title':'Project intake','kind':'receipt','origin':'imported','body':_body('Synthetic intake',{'schema':1,'kind':'project-intake','coverage':coverage}),'sources':[self.approval]})

    def enable(self, **changes):
        return configure(self.store,{**self.policy,**changes},self.approval)

    def test_start_today_does_not_backfill_yesterday(self):
        self.intake();self.enable(start_date='2026-09-06')
        before=self.store.export()
        self.assertEqual('not-started',write(self.store,now=NOW)['status'])
        self.assertEqual(before,self.store.export())
        with self.assertRaises(StoreError):preview(self.store,day=DAY,now=NOW)

    def test_invalid_timezone_is_a_handled_policy_error(self):
        with self.assertRaises(StoreError):self.enable(timezone='Mars/Olympus')

    def test_disabled_until_category_approved(self):
        self.intake()
        before=self.store.export()
        self.assertEqual('disabled',write(self.store,now=NOW)['status'])
        self.assertEqual(before,self.store.export())
        self.assertFalse(list(self.vault.glob('*progress.md')))

    def test_preview_does_not_publish_and_write_has_real_receipt_links_and_provenance(self):
        self.intake();self.enable()
        before=self.store.export()
        item=preview(self.store,now=NOW)['notes'][0]
        self.assertEqual(before,self.store.export())
        self.assertFalse((self.vault/item['path']).exists())
        result=write(self.store,now=NOW)['notes'][0]
        self.assertEqual('written',result['status'])
        note=(self.vault/result['path']).read_text()
        self.assertIn('origin: ai',note)
        self.assertIn('[[A thought]]',note)
        self.assertIn('[[Agent HQ/Memory/Records/receipt/',note)
        self.assertIn(self.events[0]['commit'],note)
        self.assertNotIn('\n# ',note)
        record=self.store.get(result['id'])
        self.assertEqual('complete',record['status'])
        self.assertEqual(item['text'],unpack(record)['text'])
        self.assertTrue(result['receipt']['committed'])
        self.assertTrue(self.store.verify()['ok'])

    def test_no_project_page_required(self):
        self.intake();self.enable(project_notes={})
        self.assertEqual('written',write(self.store,now=NOW)['notes'][0]['status'])
        self.assertFalse((self.vault/'Garden.md').exists())

    def test_repeat_is_write_free_after_database_loss(self):
        self.intake();self.enable()
        write(self.store,now=NOW)
        before=self.store.export()
        self.store.db_path.unlink();self.store.rebuild()
        self.assertEqual('already-written',write(self.store,now=NOW)['notes'][0]['status'])
        self.assertEqual(before,self.store.export())

    def test_existing_human_progress_blocks_duplicate_without_claiming_coverage(self):
        self.intake();self.enable()
        old=self.vault/(DAY+' 1000 Garden progress.md');old.write_text('My original progress.\n')
        result=write(self.store,now=NOW)
        self.assertEqual('existing-daily-note-needs-review',result['notes'][0]['status'])
        self.assertEqual('My original progress.\n',old.read_text())
        self.assertEqual(1,len(list(self.vault.glob('*progress.md'))))

    def test_human_edits_and_deletions_are_not_overwritten_or_recreated(self):
        self.intake();self.enable()
        result=write(self.store,now=NOW)['notes'][0]
        target=self.vault/result['path'];target.write_text('Human revision\n')
        self.assertEqual('existing-note-changed',write(self.store,now=NOW)['notes'][0]['status'])
        self.assertEqual('Human revision\n',target.read_text())
        target.unlink()
        self.assertEqual('previous-note-missing',write(self.store,now=NOW)['notes'][0]['status'])
        self.assertFalse(target.exists())

    def test_interruption_after_intent_rebuilds_from_files(self):
        self.intake();self.enable()
        with patch('glide_obsidian.notes._create',side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):write(self.store,now=NOW)
        self.store.db_path.unlink();self.store.rebuild()
        result=write(self.store,now=NOW)['notes'][0]
        self.assertEqual('written',result['status'])
        self.assertEqual(1,len(list(self.vault.glob('*progress.md'))))

    def test_interruption_after_note_before_receipt_does_not_duplicate(self):
        self.intake();self.enable()
        with patch.object(self.store,'index_sources',side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):write(self.store,now=NOW)
        before=list(self.vault.glob('*progress.md'))[0].read_bytes()
        self.assertEqual('written',write(self.store,now=NOW)['notes'][0]['status'])
        self.assertEqual(before,list(self.vault.glob('*progress.md'))[0].read_bytes())

    def test_late_events_surface_for_review(self):
        self.intake();self.enable();write(self.store,now=NOW)
        self.intake([self.event(),self.event(2)])
        self.assertEqual('late-activity-needs-review',write(self.store,now=NOW)['notes'][0]['status'])
        self.assertEqual(1,len(list(self.vault.glob('*progress.md'))))

    def test_partial_intake_does_not_publish(self):
        self.intake(status='partial',pending=3);self.enable()
        result=write(self.store,now=NOW)
        self.assertEqual([],result['notes']);self.assertTrue(result['coverage_gaps'])

    def test_scope_and_local_day_boundaries(self):
        self.intake([self.event(1,'2026-09-04T23:30:00Z'),self.event(2,'2026-09-05T23:30:00Z'),self.event(3,project='other')]);self.enable()
        item=preview(self.store,now=NOW)['notes'][0]
        self.assertEqual([self.events[0]['event_id']],item['event_ids'])
        self.assertIn('0030',item['path'])
        with self.assertRaises(StoreError):write(self.store,day='2026-09-06',now=NOW)
        with self.assertRaises(StoreError):write(self.store,day='2026-08-20',now=NOW)

    def test_revocation_and_tampered_local_policy_block(self):
        self.intake();self.enable();self.enable(enabled=False)
        self.assertEqual('disabled',write(self.store,now=NOW)['status'])
        path=self.store.state_dir/'daily-notes.json';data=json.loads(path.read_text());data['policy']['enabled']=True;path.write_text(json.dumps(data))
        with self.assertRaises(ConflictError):write(self.store,now=NOW)

    def test_source_evidence_mismatch_fails(self):
        self.intake();self.enable()
        rid=next(r for r in self.store._load()['records'] if r.startswith('activity:'))
        record=self.store.get(rid);record['body']=record['body'].replace('Improve seed labels 1','Invented result')
        self.commit(record)
        with self.assertRaises(IntegrityError):preview(self.store,now=NOW)

    def test_symlink_destination_is_rejected(self):
        self.intake();self.enable()
        item=preview(self.store,now=NOW)['notes'][0]
        (self.vault/item['path']).symlink_to(self.original)
        with self.assertRaises(StoreError):write(self.store,now=NOW)

    def test_cross_filesystem_does_not_fall_back_to_partial_write(self):
        self.intake();self.enable()
        real_link = os.link
        def fake_link(*args, **kwargs):
            if 'dst_dir_fd' in kwargs:raise OSError(errno.EXDEV,'cross-device')
            return real_link(*args, **kwargs)
        with patch('glide_obsidian.notes.os.link',side_effect=fake_link):
            with self.assertRaises(StoreError):write(self.store,now=NOW)
        self.assertFalse(list(self.vault.glob('*progress.md')))
        self.assertEqual('written',write(self.store,now=NOW)['notes'][0]['status'])

    def test_new_machine_needs_local_permission_config(self):
        self.intake();self.enable();write(self.store,now=NOW)
        copied=self.root/'copy';shutil.copytree(self.vault,copied)
        reader=Store.initialize(copied,self.root/'reader')
        self.assertFalse(settings(reader)['enabled'])
        self.assertFalse(reader.config['writer_active'])

    def test_large_batch_makes_progress_past_completed_first_twenty(self):
        self.intake([self.event(n+1,project=f'garden-{n:02}') for n in range(22)])
        self.enable(projects='all',project_notes={})
        first=write(self.store,now=NOW)
        self.assertEqual(2,first['pending_projects'])
        second=write(self.store,now=NOW)
        self.assertEqual(0,second['pending_projects'])
        self.assertEqual(22,len(list(self.vault.glob('*progress.md'))))

    def test_pending_record_cannot_inject_arbitrary_root_output(self):
        self.intake();self.enable()
        with patch('glide_obsidian.notes._create',side_effect=OSError('interrupted')):
            with self.assertRaises(OSError):write(self.store,now=NOW)
        rid=preview(self.store,now=NOW)['notes'][0]['id']
        r=self.store.get(rid)
        from glide_obsidian.notes import pack
        payload=unpack(r);payload['path']='Unapproved new note.md';payload['text']='Invented text'
        r['body']=pack('Modified plan',payload);self.commit(r)
        with self.assertRaises(IntegrityError):write(self.store,now=NOW)
        self.assertFalse((self.vault/'Unapproved new note.md').exists())

    def test_derived_source_reader_keeps_non_independent_label(self):
        self.intake();self.enable()
        path=write(self.store,now=NOW)['notes'][0]['path']
        reader=ObsidianServer(self.store)
        source=reader.call_tool('glide_read_source',{'path':path})
        self.assertEqual('derived-view-not-independent',source['provenance_role'])
        self.assertTrue(any(x.get('provenance_role')=='derived-view-not-independent' for x in reader.call_tool('glide_search',{'query':'seed labels','kind':'source'})))

    def test_later_intake_keeps_generated_lineage_after_user_edit(self):
        self.intake();self.enable()
        item=write(self.store,now=NOW)['notes'][0]
        path=self.vault/item['path'];path.write_text(path.read_text()+'\nMy later reflection.\n')
        sha=hashlib.sha256(path.read_bytes()).hexdigest()
        self.store.index_sources([{'path':item['path'],'sha256':sha,'source_kind':'original-markdown'}],idempotency_key='later-intake')
        source=ObsidianServer(self.store).call_tool('glide_read_source',{'path':item['path']})
        self.assertEqual('derived-daily-note-edited',source['source_kind'])
        self.assertEqual('derived-view-not-independent',source['provenance_role'])
        self.assertEqual('glide-daily-note:'+item['id'],source['canonical_uri'])
        self.store.db_path.unlink();self.store.rebuild()
        registered=next(s for s in self.store.export()['sources'] if s['path']==item['path'])
        self.assertEqual(source['canonical_uri'],registered['canonical_uri'])

    def test_mcp_preserves_core_and_rejects_arbitrary_body_or_configuration(self):
        server=ObsidianServer(self.store)
        server.handle({'jsonrpc':'2.0','id':1,'method':'initialize','params':{}})
        result=server.handle({'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})
        names={t['name'] for t in result['result']['tools']}
        self.assertIn('glide_get',names);self.assertIn('glide_project_notes_write',names)
        self.assertFalse(any('configure' in n for n in names))
        with self.assertRaises(ValueError):server.call_tool('glide_project_notes_write',{'body':'Overwrite my diary'})
        with self.assertRaises(ValueError):server.call_tool('glide_project_notes_write',{'day':'2026-09-05','enabled':True})

    def test_adapter_profile_defaults_preserve_core_and_companion_inventory(self):
        from glide_memory.bridge import TOOLS
        from glide_obsidian.bridge import EXTRA
        server = ObsidianServer(self.store)
        server.handle({'jsonrpc':'2.0','id':1,'method':'initialize','params':{}})
        tools = server.handle({'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})['result']['tools']
        self.assertEqual({item[0] for item in TOOLS} | set(EXTRA), {item['name'] for item in tools})
        self.assertEqual(len(TOOLS) + 3, len(tools))
        self.assertTrue(next(t for t in tools if t['name']=='glide_project_notes_preview')['annotations']['readOnlyHint'])
        self.assertFalse(next(t for t in tools if t['name']=='glide_project_notes_write')['annotations']['readOnlyHint'])

    def test_adapter_tools_cannot_bypass_narrowed_live_profile(self):
        from glide_memory.bridge import TOOL_CAPABILITIES
        from glide_obsidian.bridge import EXTRA
        server = ObsidianServer(self.store)
        server.handle({'jsonrpc':'2.0','id':1,'method':'initialize','params':{}})
        before = self.store.export()
        config = json.loads(self.store.config_path.read_text())
        config['tool_capabilities'] = ['reader']
        self.store.config_path.write_text(json.dumps(config))
        tools = server.handle({'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})['result']['tools']
        self.assertEqual(TOOL_CAPABILITIES['reader'], {item['name'] for item in tools})
        for name in EXTRA:
            with self.subTest(tool=name):
                with self.assertRaises(ValueError):
                    server.call_tool(name, {})
                response = server.handle({'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':name,'arguments':{}}})
                self.assertTrue(response['result']['isError'])
        self.assertEqual(before, self.store.export())
        config['tool_capabilities'] = ['project_progress']
        self.store.config_path.write_text(json.dumps(config))
        tools = server.handle({'jsonrpc':'2.0','id':4,'method':'tools/list','params':{}})['result']['tools']
        self.assertEqual(set(EXTRA), {item['name'] for item in tools})
        self.assertFalse(server.call_tool('glide_project_notes_settings', {})['enabled'])
        with self.assertRaises(ValueError):
            server.call_tool('glide_get', {'record_id':'anything'})

    def test_empty_and_invalid_adapter_profiles_fail_closed(self):
        server = ObsidianServer(self.store)
        server.handle({'jsonrpc':'2.0','id':1,'method':'initialize','params':{}})
        config = json.loads(self.store.config_path.read_text())
        config['tool_capabilities'] = []
        self.store.config_path.write_text(json.dumps(config))
        self.assertEqual([], server.handle({'jsonrpc':'2.0','id':2,'method':'tools/list','params':{}})['result']['tools'])
        with self.assertRaises(ValueError):
            server.call_tool('glide_project_notes_write', {})
        for profile in [['project_progress','project_progress'], ['unrestricted'], 'project_progress']:
            config['tool_capabilities'] = profile
            self.store.config_path.write_text(json.dumps(config))
            with self.subTest(profile=profile), self.assertRaises(ValueError):
                ObsidianServer(self.store)

if __name__=='__main__':unittest.main()
