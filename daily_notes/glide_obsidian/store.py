"""Preserve generated-note lineage when ordinary intake sees a later file edit."""
from glide_memory import Store
from .notes import unpack


class ObsidianStore(Store):
    def note_lineages(self):
        return {unpack(r)['path']: (r['id'], unpack(r)['sha256'])
                for r in self._load()['records'].values()
                if r['id'].startswith('daily-note:') and r['kind'] == 'receipt' and r['origin'] == 'ai'}

    @staticmethod
    def mark_note(source, lineages):
        previous = lineages.get(source.get('path'))
        if previous:
            rid, original_hash = previous
            changed = source.get('sha256') != original_hash
            return {**source, 'canonical_uri': 'glide-daily-note:' + rid,
                    'source_kind': 'derived-daily-note-edited' if changed else 'derived-daily-note',
                    'provenance_role': 'derived-view-not-independent',
                    'verification': 'Later edits require separate attribution' if changed else 'Matches retained generated output'}
        return source

    def index_sources(self, sources, *, idempotency_key):
        lineages = self.note_lineages()
        return super().index_sources([self.mark_note(s, lineages) for s in sources], idempotency_key=idempotency_key)
