import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import glide_memory

SOURCE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('daily_install', SOURCE / 'install.py')
installer = importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)
RUNTIME = Path(glide_memory.__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='glide-obsidian-install-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.vault = self.root / 'vault';self.vault.mkdir()
        self.source = self.root / 'source'
        shutil.copytree(SOURCE / 'glide_obsidian', self.source / 'glide_obsidian')
        shutil.copyfile(SOURCE / 'package-manifest.json', self.source / 'package-manifest.json')
        self.pin = json.loads((self.source/'package-manifest.json').read_text())['build']

    def run_install(self, **kwargs):
        return installer.install(self.source, kwargs.get('home',self.root/'home'), self.vault, kwargs.get('runtime',RUNTIME), expected_build=kwargs.get('pin',self.pin))

    def test_runtime_pairing_is_consistent_across_package_and_distribution(self):
        from glide_obsidian import REQUIRED_RUNTIME_BUILD
        manifest = json.loads((SOURCE / 'package-manifest.json').read_text())
        compatibility = json.loads((SOURCE.parent / 'compatibility.json').read_text())
        self.assertEqual(REQUIRED_RUNTIME_BUILD, manifest['required_runtime_build'])
        self.assertEqual(REQUIRED_RUNTIME_BUILD, compatibility['optional_memory_runtime']['build'])
        self.assertEqual(REQUIRED_RUNTIME_BUILD, installer.build(installer.hashes(RUNTIME, 'glide_memory')))

    def test_verified_idempotent_install_does_not_configure_or_write_vault(self):
        first=self.run_install()
        self.assertEqual(first,self.run_install())
        self.assertFalse(first['category_changed'])
        self.assertEqual([],list(self.vault.iterdir()))
        self.assertEqual(installer.hashes(SOURCE,'glide_obsidian'),installer.hashes(Path(first['installed']),'glide_obsidian'))

    def test_wrong_pin_or_source_change_rejected_before_installing(self):
        with self.assertRaises(ValueError):self.run_install(pin='000000000000')
        (self.source/'glide_obsidian/notes.py').write_text('print("changed")')
        with self.assertRaises(ValueError):self.run_install()
        self.assertFalse((self.root/'home').exists())

    def test_wrong_runtime_rejected(self):
        path=self.root/'runtime';(path/'glide_memory').mkdir(parents=True)
        (path/'glide_memory/__init__.py').write_text('')
        with self.assertRaises(ValueError):self.run_install(runtime=path)
        self.assertFalse((self.root/'home').exists())

    def test_vault_and_symlink_install_locations_rejected(self):
        with self.assertRaises(ValueError):self.run_install(home=self.vault/'programs')
        link=self.root/'link';link.symlink_to(self.vault,target_is_directory=True)
        with self.assertRaises(ValueError):self.run_install(home=link/'programs')

    def test_changed_installed_code_not_overwritten(self):
        installed=Path(self.run_install()['installed'])/'glide_obsidian/notes.py'
        installed.write_text('local change')
        with self.assertRaises(ValueError):self.run_install()
        self.assertEqual('local change',installed.read_text())
