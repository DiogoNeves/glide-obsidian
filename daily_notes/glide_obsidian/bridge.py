"""Add bounded Obsidian output tools to the pinned Glide MCP broker."""
import argparse
import sys
from .store import ObsidianStore
from glide_memory.bridge import MemoryServer, obj, string, serve
from .notes import settings, preview, write

EXTRA = {
    'glide_project_notes_settings': ('Read the approved project-progress category; never enables it.', obj(), settings, True),
    'glide_project_notes_preview': ('Preview daily unique project-progress notes from retained Git evidence. No file writes.', obj({'day': string()}), preview, True),
    'glide_project_notes_write': ('Create new daily unique notes only within the locally approved project-progress category. Existing notes are never replaced. Return actual receipts and unresolved cases.', obj({'day': string()}), write, False),
}

class ObsidianServer(MemoryServer):
    def tool_inventory(self):
        return super().tool_inventory() + [(name, description, schema, readonly)
                for name, (description, schema, _, readonly) in EXTRA.items()]

    def capability_groups(self):
        return {**super().capability_groups(), 'project_progress': set(EXTRA)}

    def _source(self, relative):
        source = self.store.mark_note(super()._source(relative), self.store.note_lineages())
        if source.get('source_kind', '').startswith('derived-daily-note'):
            source['provenance_role'] = 'derived-view-not-independent'
            source['instruction'] = 'Follow related memory and its original commit evidence; this daily note is not another corroborating source.'
        return source

    def call_tool(self, name, arguments):
        if name in EXTRA:
            self.validate_call(name, arguments)
            _, _, fn, _ = EXTRA[name]
            return fn(self.store, **arguments)
        result = super().call_tool(name, arguments)
        if name == 'glide_search':
            lineages = self.store.note_lineages()
            result = [self.store.mark_note(hit, lineages) for hit in result]
        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    serve(ObsidianServer(ObsidianStore(args.config)), sys.stdin, sys.stdout)
