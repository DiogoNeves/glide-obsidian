"""Trusted category setup after the user's explicit scope decision; not an MCP tool."""
import argparse
import json
from pathlib import Path
from glide_memory import Store
from .notes import configure

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True)
    parser.add_argument('--decision', required=True, help='Private JSON containing policy and exact approval source')
    args = parser.parse_args()
    data = json.loads(Path(args.decision).read_text())
    if set(data) != {'policy', 'approval'}:
        parser.error('Decision must contain only policy and approval')
    print(json.dumps(configure(Store(args.config), data['policy'], data['approval']), indent=2))
