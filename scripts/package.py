#!/usr/bin/env python3
"""Build deterministic upload archives, using only the Python standard library."""
import argparse
import hashlib
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('watercolor-object', 'watercolor-object-p5-brush')


def build(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    sums = []
    archives = []
    for name in SKILLS:
        source = ROOT / 'watercolor-skills' / name
        skill = source / 'SKILL.md'
        text = skill.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\nname: ' + name + '\n' not in text:
            raise ValueError('Invalid skill frontmatter: ' + name)
        archive = output / (name + '.zip')
        with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for path in sorted(source.rglob('*')):
                if path.is_symlink():
                    raise ValueError('Do not package symlinks: ' + str(path))
                if not path.is_file() or any(p.startswith('.') or p == '__pycache__' for p in path.relative_to(source).parts):
                    continue
                info = zipfile.ZipInfo(name + '/' + path.relative_to(source).as_posix(), (2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                z.writestr(info, path.read_bytes())
        sums.append(hashlib.sha256(archive.read_bytes()).hexdigest() + '  ' + archive.name)
        archives.append(archive)
    (output / 'SHA256SUMS').write_text('\n'.join(sums) + '\n', encoding='utf-8')
    return archives


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    for archive in build(parser.parse_args().output):
        print(archive)
