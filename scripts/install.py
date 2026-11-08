#!/usr/bin/env python3
"""Install portable watercolor skills without replacing existing files."""
import argparse
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('watercolor-object', 'watercolor-object-p5-brush')


def install(destination, names):
    destination = Path(destination).expanduser().resolve()
    # Preflight all targets before writing any skill.
    for name in names:
        if name not in SKILLS:
            raise ValueError('Unknown skill: ' + name)
        if not (ROOT / 'skills' / name / 'SKILL.md').is_file():
            raise ValueError('Missing source skill: ' + name)
        if os.path.lexists(destination / name):
            raise FileExistsError('Refusing to overwrite: ' + str(destination / name))
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for name in names:
            target = destination / name
            target.mkdir()  # Exclusive creation: do not adopt an existing folder.
            created.append(target)
            shutil.copytree(ROOT / 'skills' / name, target, dirs_exist_ok=True)
    except Exception:
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    return created


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--target', choices=('claude', 'codex', 'agents'))
    group.add_argument('--destination', type=Path, help='Custom skills directory')
    parser.add_argument('--project', type=Path, help='Project root instead of user scope')
    parser.add_argument('--skill', choices=SKILLS, action='append', help='Install only this skill')
    args = parser.parse_args()
    if args.project and args.destination:
        parser.error('--project cannot be combined with --destination')
    if args.destination:
        destination = args.destination
    else:
        base = args.project.expanduser().resolve() if args.project else Path.home()
        folder = {'claude': '.claude', 'codex': '.codex', 'agents': '.agents'}[args.target]
        destination = base / folder / 'skills'
        if args.target == 'codex' and not args.project and os.environ.get('CODEX_HOME'):
            destination = Path(os.environ['CODEX_HOME']).expanduser() / 'skills'
    try:
        for target in install(destination, tuple(dict.fromkeys(args.skill or SKILLS))):
            print('Installed ' + str(target))
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
