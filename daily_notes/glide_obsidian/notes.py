"""Approved project-progress notes: immutable daily output from retained Git evidence."""
from __future__ import annotations

import contextlib
from datetime import date, datetime, timedelta, timezone
import errno
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import quote
from zoneinfo import ZoneInfo

from glide_memory.pipeline import _read_state, _commit_evidence, PROJECT_STATE_ID
from glide_memory.store import StoreError, ConflictError, IntegrityError, atomic_write, digest, no_symlinks, safe_child, slug

CATEGORY = 'project-progress'
GRANT_ID = 'obsidian-daily-notes:project-progress'
MARKER = '<!-- glide:daily-note-state -->\n```json\n'


def pack(introduction, payload):
    return introduction + '\n\n' + MARKER + json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + '\n```'


def unpack(record):
    body = record['body']
    if body.count(MARKER) != 1 or not body.endswith('\n```'):
        raise IntegrityError('Unrecognized daily-note record')
    return json.loads(body.split(MARKER, 1)[1][:-4])


@contextlib.contextmanager
def lock(store):
    path = no_symlinks(store.state_dir / 'daily-notes.lock')
    with path.open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def validate_policy(store, supplied):
    required = {'enabled', 'timezone', 'start_date', 'projects'}
    allowed = required | {'titles', 'project_notes', 'tags', 'category_note'}
    if not isinstance(supplied, dict) or set(supplied) - allowed or not required <= set(supplied):
        raise StoreError('Policy needs enabled, timezone, start_date and projects; unknown fields are rejected')
    p = {'titles': {}, 'project_notes': {}, 'tags': ['note', 'journal', 'progress'], 'category_note': None, **supplied}
    if type(p['enabled']) is not bool:
        raise StoreError('enabled must be boolean')
    try:
        ZoneInfo(p['timezone'])
        if date.fromisoformat(p['start_date']).isoformat() != p['start_date']:
            raise ValueError('Noncanonical date')
    except (KeyError, TypeError, ValueError) as error:
        raise StoreError('Use an IANA timezone and an ISO start date') from error
    def index_path(value):
        return isinstance(value, str) and re.fullmatch(r'projects/[A-Za-z0-9_.-]+\.md', value) and '..' not in value
    if p['projects'] != 'all' and (not isinstance(p['projects'], list) or not p['projects'] or len(p['projects']) > 100 or not all(index_path(x) for x in p['projects'])):
        raise StoreError('projects must be all or a nonempty list of exact project-index paths')
    for key in ('titles', 'project_notes'):
        if not isinstance(p[key], dict) or len(p[key]) > 100 or not all(index_path(k) for k in p[key]):
            raise StoreError('Invalid project mapping')
    for title in p['titles'].values():
        if not isinstance(title, str) or not title.strip() or len(title) > 80 or any(ord(c) < 32 for c in title):
            raise StoreError('Use a short readable project title')
    for path in [*p['project_notes'].values(), p['category_note']]:
        if path is not None:
            file = safe_child(store.vault, path)
            if file.suffix != '.md' or not file.is_file() or '[' in path or ']' in path or '|' in path or '#' in path:
                raise StoreError('Optional links must name existing Markdown notes with unambiguous wiki paths')
    if not isinstance(p['tags'], list) or len(p['tags']) > 8 or not all(isinstance(x, str) and re.fullmatch(r'[\w/-]{1,40}', x) for x in p['tags']):
        raise StoreError('Use at most eight simple tags')
    return p


def configure(store, policy, approval):
    """Trusted setup only; intentionally not an MCP tool or an automatic overlay."""
    with lock(store):
        p = validate_policy(store, policy)
        records = store._load()['records']
        previous = records.get(GRANT_ID)
        record = {'id': GRANT_ID, 'title': 'Daily project-progress note permission', 'kind': 'workflow', 'origin': 'ai',
                  'body': pack('Explicit category permission for new daily project-progress notes. Existing notes remain untouched. Changing this scope requires a new user decision.', {'schema': 1, 'category': CATEGORY, 'policy': p}),
                  'sources': [approval]}
        revs = {GRANT_ID: previous['revision'] if previous else 0}
        proposal = store.propose([record], expected_revisions=revs, rationale='Retain the user-approved daily-note category and scope', idempotency_key='daily-note-policy:' + digest([p, revs, approval]))
        receipt = store.apply(proposal['proposal_id'], expected_revisions=revs, actor='user-authorized-setup', decision='approved')
        config = {'schema': 1, 'instance_id': store.config['instance_id'], 'grant_revision': receipt['revisions'][GRANT_ID], 'policy': p}
        atomic_write(store.state_dir / 'daily-notes.json', json.dumps(config, indent=2) + '\n')
        return receipt


def settings(store):
    path = no_symlinks(store.state_dir / 'daily-notes.json')
    if not path.exists():
        return {'enabled': False, 'category': CATEGORY, 'reason': 'Category not approved on this host'}
    config = json.loads(path.read_text())
    if set(config) != {'schema', 'instance_id', 'grant_revision', 'policy'} or config['schema'] != 1 or config['instance_id'] != store.config['instance_id']:
        raise IntegrityError('Daily-note configuration does not match this instance')
    grant = store._load()['records'].get(GRANT_ID)
    if not grant or grant['review'] != 'approved' or grant['revision'] != config['grant_revision'] or unpack(grant)['policy'] != config['policy']:
        raise ConflictError('Daily-note approval/configuration mismatch; reconcile setup before writing')
    p = validate_policy(store, config['policy'])
    return {**p, 'category': CATEGORY, 'grant_revision': grant['revision'], 'policy_hash': digest(config)}


def plain(value):
    value = ' '.join(str(value).split())
    return re.sub(r'([\\`*{}\[\]()<>!#|])', r'\\\1', value)


def wiki(path):
    return '[[' + str(Path(path).with_suffix('')) + ']]'


def _day(p, requested, moment):
    today = moment.astimezone(ZoneInfo(p['timezone'])).date()
    day = date.fromisoformat(requested) if requested else today - timedelta(days=1)
    if not requested and day.isoformat() < p['start_date']:
        return None
    if day.isoformat() < p['start_date'] or not today - timedelta(days=7) <= day < today:
        raise StoreError('Only completed days in the approved start-date/last-seven-day window are admitted; no implicit backfill')
    return day


def _candidates(store, p, day):
    loaded = store._load()
    records = loaded['records']
    intake = records.get(PROJECT_STATE_ID)
    if not intake:
        return [], [{'status': 'needs-intake', 'reason': 'No successful project intake receipt'}]
    coverage = _read_state(intake).get('coverage', [])
    ready = {x.get('repo_id') for x in coverage if x.get('status') == 'complete' and not x.get('pending')}
    ready -= {x.get('repo_id') for x in coverage if x.get('status') != 'complete' or x.get('pending')}
    gaps = [x for x in coverage if x.get('repo_id') not in ready]
    grouped = {}
    for record in records.values():
        if not record['id'].startswith('activity:') or record['kind'] != 'receipt' or record['origin'] != 'imported':
            continue
        state = _read_state(record)
        if state.get('kind') != 'project-activity':
            continue
        for event in state.get('events', []):
            if p['projects'] != 'all' and event['index_path'] not in p['projects']:
                continue
            if event['repo_id'] not in ready:
                continue
            instant = datetime.fromisoformat(event['committed_at'].replace('Z', '+00:00'))
            if instant.utcoffset() is None:
                raise IntegrityError('Commit date has no timezone')
            if instant.astimezone(ZoneInfo(p['timezone'])).date() != day:
                continue
            evidence = _commit_evidence(event)
            if not any(s['quote'] == evidence['quote'] and s['sha256'] == evidence['sha256'] for s in record['sources']):
                raise IntegrityError('Activity event lacks matching retained commit evidence')
            item = grouped.setdefault(event['repo_id'], {'events': {}, 'records': {}, 'sources': []})
            if event['event_id'] not in item['events']:
                item['events'][event['event_id']] = event
                item['sources'].append(evidence)
            item['records'][record['id']] = record
    candidates = []
    for repo, item in sorted(grouped.items()):
        events = sorted(item['events'].values(), key=lambda e: (e['committed_at'], e['commit']))
        last = max(events, key=lambda e: datetime.fromisoformat(e['committed_at'].replace('Z', '+00:00')))
        index_path = last['index_path']
        title = p['titles'].get(index_path, Path(index_path).stem)
        rid = 'daily-note:' + digest([CATEGORY, repo, day.isoformat()])[:32]
        hour = datetime.fromisoformat(last['committed_at'].replace('Z', '+00:00')).astimezone(ZoneInfo(p['timezone'])).strftime('%H%M')
        filename = f'{day.isoformat()} {hour} {slug(title)} progress.md'
        related = [wiki(str(Path(store.config['store_path']) / r['path'])) for r in item['records'].values()]
        if index_path in p['project_notes']:
            related.insert(0, wiki(p['project_notes'][index_path]))
        lines = ['---', 'tags: ' + json.dumps(p['tags']), 'origin: ai', 'glide_daily_note: ' + json.dumps(rid), 'related: ' + json.dumps(related, ensure_ascii=False)]
        if p['category_note']:
            lines.append('categories: ' + json.dumps([wiki(p['category_note'])]))
        lines += ['---', '', 'Recorded Git activity; release or deployment is not inferred.', '']
        for e in events:
            title_text = plain(e['title'])
            url = e.get('url')
            link = f'[{e["commit"][:8]}]({quote(url, safe=":/?#%&=+@")})' if url and url.startswith('https://') else '`' + e['commit'][:12] + '`'
            lines.append('- ' + title_text + ' · ' + link)
        text = '\n'.join(lines) + '\n'
        previous = records.get(rid)
        status = 'ready'
        if previous:
            saved = unpack(previous)
            if previous['kind'] != 'receipt' or previous['origin'] != 'ai':
                raise IntegrityError('Unexpected ownership for a daily-note record')
            if previous['status'] != 'complete' and saved['policy_hash'] == p['policy_hash'] and saved['event_ids'] == sorted(item['events']):
                expected = {'path': filename, 'text': text, 'sha256': hashlib.sha256(text.encode()).hexdigest(), 'repo_id': repo, 'day': day.isoformat(), 'id': rid}
                if any(saved.get(k) != value for k, value in expected.items()):
                    raise IntegrityError('Pending note differs from deterministic approved output')
            filename = saved['path']
            if saved['event_ids'] != sorted(item['events']):
                status = 'late-activity-needs-review'
            else:
                text = saved['text']
                target = safe_child(store.vault, filename)
                if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != saved['sha256']:
                    status = 'existing-note-changed'
                elif previous['status'] == 'complete':
                    status = 'already-written' if target.exists() else 'previous-note-missing'
                elif saved['policy_hash'] != p['policy_hash']:
                    status = 'policy-changed-needs-review'
        else:
            for f in store.vault.glob(day.isoformat() + ' *.md'):
                no_symlinks(f)
                name = f.stem.casefold()
                if f.name == filename or ('progress' in name and title.casefold() in name):
                    status = 'existing-daily-note-needs-review'
                    break
        candidates.append({'id': rid, 'day': day.isoformat(), 'repo_id': repo, 'index_path': index_path, 'title': title, 'path': filename, 'text': text,
                           'sha256': hashlib.sha256(text.encode()).hexdigest(), 'event_ids': sorted(item['events']), 'policy_hash': p['policy_hash'],
                           'sources': item['sources'], 'records': sorted(item['records']), 'status': status})
    return candidates, gaps


def preview(store, day=None, *, now=None):
    p = settings(store)
    if not p['enabled']:
        return {'status': 'disabled', 'settings': p, 'notes': []}
    actual = _day(p, day, now or datetime.now(timezone.utc))
    if actual is None:
        return {'status': 'not-started', 'start_date': p['start_date'], 'notes': []}
    notes, gaps = _candidates(store, p, actual)
    return {'status': 'preview', 'day': actual.isoformat(), 'notes': notes, 'coverage_gaps': gaps, 'meaning': 'Preview only; no files have been written'}


def _save(store, record, revision, key):
    expected = {record['id']: revision}
    proposal = store.propose([record], expected_revisions=expected, rationale='Retain an approved daily-note output plan or publication receipt', idempotency_key=key)
    return store.apply(proposal['proposal_id'], expected_revisions=expected, actor='approved-daily-notes', decision='unreviewed')


def _create(store, candidate):
    """Link a completed same-filesystem staged file atomically; never replace a target."""
    target = safe_child(store.vault, candidate['path'])
    if target.exists():
        if hashlib.sha256(target.read_bytes()).hexdigest() != candidate['sha256']:
            raise ConflictError('Existing daily note differs; preserve it and ask for review')
        return
    stage = no_symlinks(store.state_dir / ('daily-note-' + candidate['sha256'] + '.tmp'))
    atomic_write(stage, candidate['text'], immutable=True)
    try:
        # Destination is one generated filename in the configured vault root.
        with contextlib.ExitStack() as stack:
            src = os.open(store.state_dir, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            stack.callback(os.close, src)
            dst = os.open(store.vault, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
            stack.callback(os.close, dst)
            try:
                os.link(stage.name, candidate['path'], src_dir_fd=src, dst_dir_fd=dst, follow_symlinks=False)
                os.fsync(dst)
            except FileExistsError:
                raise ConflictError('A note appeared during publication; retry to inspect it')
            except OSError as e:
                if e.errno == errno.EXDEV:
                    raise StoreError('Atomic daily-note output requires local state and vault on the same filesystem') from e
                raise
    finally:
        stage.unlink(missing_ok=True)


def write(store, day=None, *, now=None):
    with lock(store):
        store._require_writer()
        result = preview(store, day, now=now)
        if result['status'] in {'disabled', 'not-started'}:
            return result
        outcomes = [{k: candidate[k] for k in ('id', 'path', 'status')} for candidate in result['notes'] if candidate['status'] != 'ready']
        eligible = [candidate for candidate in result['notes'] if candidate['status'] == 'ready']
        for candidate in eligible[:20]:
            p = settings(store)
            if not p['enabled'] or p['policy_hash'] != candidate['policy_hash']:
                raise ConflictError('Category permission changed before publication')
            previous = store._load()['records'].get(candidate['id'])
            record = previous or {'id': candidate['id'], 'title': candidate['title'] + ' progress - ' + candidate['day'], 'kind': 'receipt', 'origin': 'ai', 'status': 'open',
                                  'body': pack('Approved daily-note publication plan. This record does not yet prove a file was created.', candidate), 'sources': candidate['sources'],
                                  'relationships': [{'type': 'summarizes', 'target': rid, 'reason': 'This daily note presents the same retained Git evidence; it is not independent corroboration.'} for rid in candidate['records']]}
            if not previous:
                _save(store, record, 0, candidate['id'] + ':prepare')
                record = store.get(candidate['id'])
            _create(store, candidate)
            # Register lineage before completion so a retry never mistakes this derived copy for independent evidence.
            store.index_sources([{'path': candidate['path'], 'sha256': candidate['sha256'], 'canonical_uri': 'glide-daily-note:' + candidate['id'], 'source_kind': 'derived-daily-note'}], idempotency_key=candidate['id'] + ':source')
            record = dict(record)
            record['status'] = 'complete'
            record['body'] = pack('Published ' + wiki(candidate['path']) + '. The daily note is a derived view of linked Git evidence, not an independent source or proof of delivery.', candidate)
            receipt = _save(store, record, record['revision'], candidate['id'] + ':complete')
            outcomes.append({'id': candidate['id'], 'path': candidate['path'], 'status': 'written', 'receipt': receipt})
        return {'status': 'processed', 'day': result['day'], 'notes': outcomes, 'pending_projects': max(0, len(eligible) - 20), 'coverage_gaps': result['coverage_gaps']}
