import hashlib
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load('install')
packager = load('package')


class DistributionTests(unittest.TestCase):
    def test_install_matches_sources(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'skills'
            installer.install(destination, installer.SKILLS)
            for name in installer.SKILLS:
                source = ROOT / 'watercolor-skills' / name
                for file in source.rglob('*'):
                    if file.is_file():
                        self.assertEqual(file.read_bytes(), (destination / name / file.relative_to(source)).read_bytes())

    def test_conflict_leaves_all_targets_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            existing = dest / installer.SKILLS[1]
            existing.mkdir()
            (existing / 'custom.txt').write_text('keep me')
            with self.assertRaises(FileExistsError):
                installer.install(dest, installer.SKILLS)
            self.assertFalse((dest / installer.SKILLS[0]).exists())
            self.assertEqual((existing / 'custom.txt').read_text(), 'keep me')

    @unittest.skipIf(os.name == 'nt', 'Windows symlinks can require elevated privileges')
    def test_dangling_symlink_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)
            target = dest / installer.SKILLS[0]
            target.symlink_to(dest / 'missing', target_is_directory=True)
            with self.assertRaises(FileExistsError):
                installer.install(dest, installer.SKILLS)
            self.assertTrue(target.is_symlink())

    def test_project_cli_and_single_skill(self):
        with tempfile.TemporaryDirectory() as temp:
            for target, folder in [('claude', '.claude'), ('codex', '.codex'), ('agents', '.agents')]:
                result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--target', target,
                                         '--project', temp, '--skill', installer.SKILLS[0]], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertTrue((Path(temp) / folder / 'skills' / installer.SKILLS[0] / 'SKILL.md').is_file())
                self.assertFalse((Path(temp) / folder / 'skills' / installer.SKILLS[1]).exists())

    def test_custom_destination_cli(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / 'custom skills'
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/install.py'), '--destination', str(dest)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in installer.SKILLS:
                self.assertTrue((dest / name / 'SKILL.md').exists())

    def test_archives_reproducible_and_complete(self):
        with tempfile.TemporaryDirectory() as temp:
            archives = packager.build(Path(temp) / 'first')
            again = packager.build(Path(temp) / 'second')
            for archive, second in zip(archives, again):
                self.assertEqual(archive.read_bytes(), second.read_bytes())
                with zipfile.ZipFile(archive) as z:
                    self.assertIsNone(z.testzip())
                    self.assertIn(archive.stem + '/SKILL.md', z.namelist())
                    for name in z.namelist():
                        self.assertTrue(name.startswith(archive.stem + '/'))
                        self.assertNotIn('..', Path(name).parts)
                        self.assertEqual(z.read(name), (ROOT / 'watercolor-skills' / name).read_bytes())
                checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
                self.assertIn(checksum + '  ' + archive.name, (archive.parent / 'SHA256SUMS').read_text())

    def test_skill_metadata_and_no_personal_paths(self):
        for name in installer.SKILLS:
            text = (ROOT / 'watercolor-skills' / name / 'SKILL.md').read_text()
            fields = text.split('---', 2)[1]
            self.assertIn('\nname: ' + name + '\n', fields)
            self.assertIn('\ndescription: ', fields)
            self.assertNotIn('/Users/', text)
            self.assertNotIn('/home/', text)


if __name__ == '__main__':
    unittest.main()
