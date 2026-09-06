"""Add bounded Obsidian output tools to the unchanged, pinned Glide MCP broker."""
import argparse
import sys
from .store import ObsidianStore
from glide_memory.bridge import MemoryServer, obj, string, validate, serve
from .notes import settings, preview, write

EXTRA = {
    'glide_project_notes_settings': ('Read the approved project-progress category; never enables it.', obj(), settings, True),
    'glide_project_notes_preview': ('Preview daily unique project-progress notes from retained Git evidence. No file writes.', obj({'day': string()}), preview, True),
    'glide_project_notes_write': ('Create new daily unique notes only within the locally approved project-progress category. Existing notes are never replaced. Return actual receipts and unresolved cases.', obj({'day': string()}), write, False),
}

class ObsidianServer(MemoryServer):
    def _source(self, relative):
        source = self.store.mark_note(super()._source(relative), self.store.note_lineages())
        if source.get('source_kind', '').startswith('derived-daily-note'):
            source['provenance_role'] = 'derived-view-not-independent'
            source['instruction'] = 'Follow related memory and its original commit evidence; this daily note is not another corroborating source.'
        return source

    def call_tool(self, name, arguments):
        if name in EXTRA:
            _, schema, fn, _ = EXTRA[name]
            validate(arguments, schema)
            return fn(self.store, **arguments)
        result = super().call_tool(name, arguments)
        if name == 'glide_search':
            lineages = self.store.note_lineages()
            result = [self.store.mark_note(hit, lineages) for hit in result]
        return result

    def handle(self, request):
        response = super().handle(request)
        if isinstance(request, dict) and request.get('method') == 'tools/list' and response and 'result' in response:
            response['result']['tools'].extend({'name': name, 'description': description, 'inputSchema': schema, 'annotations': {'readOnlyHint': readonly}} for name, (description, schema, _, readonly) in EXTRA.items())
        return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    serve(ObsidianServer(ObsidianStore(args.config)), sys.stdin, sys.stdout)
