# Repository guidance

This is a portable distribution of two independent Agent Skills. Keep canonical skills under category folders such as `watercolor-skills/`, using standard `name` and `description` YAML frontmatter. Keep platform installation details in the root README. Do not add vendor-specific tool names to the shared painting instructions.

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/package.py` after distribution changes. Never include source photos, personal paths, secrets or generated outputs in skill archives. Preserve the distinction between image generation and procedural p5.brush painting. Do not claim visual validation from packaging tests.
