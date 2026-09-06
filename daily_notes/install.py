#!/usr/bin/env python3
"""Install the pinned Obsidian companion outside the vault; never enable a category."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile


def safe(value):
    path = Path(os.path.abspath(os.path.expanduser(str(value))))
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('Symlink installation paths are not supported')
    return path


def hashes(root, package):
    result = {}
    for path in sorted((root / package).rglob('*')):
        safe(path)
        if path.is_file() and path.suffix in {'.py', '.html'}:
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if not result:
        raise ValueError('Package is empty')
    return result


def build(files):
    return hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()[:12]


def install(source, home, vault, runtime, *, expected_build):
    source, home, vault, runtime = map(safe, (source, home, vault, runtime))
    if not vault.is_dir():
        raise ValueError('Vault must already exist')
    for location in (home, runtime):
        if location.is_relative_to(vault) or vault.is_relative_to(location):
            raise ValueError('Executable packages must remain physically separate from the vault')
    manifest = json.loads(safe(source / 'package-manifest.json').read_text())
    files = hashes(source, 'glide_obsidian')
    actual = build(files)
    if manifest != {'schema': 1, 'version': '0.1.0', 'build': actual, 'required_runtime_build': 'df711b913f09', 'files': files} or actual != expected_build:
        raise ValueError('Obsidian package content does not match the expected build')
    # The shared build hashes its complete Python/HTML file manifest. Verify the
    # installed files themselves; an installed runtime need not contain a manifest.
    if build(hashes(runtime, 'glide_memory')) != manifest['required_runtime_build']:
        raise ValueError('Installed shared runtime does not match the required content pin')
    destination = safe(home / 'obsidian-daily-notes' / ('0.1.0-' + actual))
    if destination.exists():
        if hashes(destination, 'glide_obsidian') != files or json.loads(safe(destination / 'package-manifest.json').read_text()) != manifest:
            raise ValueError('Existing installation differs; preserve it for inspection')
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        stage = Path(tempfile.mkdtemp(prefix='.install-', dir=destination.parent))
        try:
            for relative in files:
                target = stage / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(safe(source / relative), target)
            (stage / 'package-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
            if hashes(stage, 'glide_obsidian') != files:
                raise ValueError('Package changed while copying')
            os.rename(stage, destination)
        finally:
            if stage.exists():shutil.rmtree(stage)
    return {'installed': str(destination), 'build': actual, 'required_runtime_build': manifest['required_runtime_build'],
            'pythonpath': os.pathsep.join(map(str, (destination, runtime))), 'module': 'glide_obsidian.bridge',
            'category_changed': False, 'meaning': 'Package installed. Host configuration and category approval are separate; existing permission is unchanged.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source', 'home', 'vault', 'runtime', 'expected-build'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.source, args.home, args.vault, args.runtime, expected_build=args.expected_build), indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + '\n')
