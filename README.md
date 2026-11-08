# Watercolor Skills

Turn a photo's object into an isolated watercolor illustration. Two portable [Agent Skills](https://agentskills.io), by Mori Liu.

| Skill | Creates | Requires |
| --- | --- | --- |
| [`watercolor-object`](skills/watercolor-object/SKILL.md) | A watercolor image, transparent by default | Vision + an image editing/generation tool that accepts reference images |
| [`watercolor-object-p5-brush`](skills/watercolor-object-p5-brush/SKILL.md) | Editable p5.js / p5.brush sketch and an exported PNG, white by default | Vision + file/code tools; a browser with WebGL for rendering and export |

Both preserve the object's shape, viewpoint and colors, remove surroundings, and expose independent **detail / transparency / softness** controls. Defaults: **35 / 75 / 55**. These are artistic directions, not pixel measurements.

## Quick start

Download or clone this repository, then choose your setup below. Python 3.9+ is only needed for the installer and packaging tools; the skills themselves are Markdown.

### ChatGPT

1. Run `python3 scripts/package.py` to create one upload ZIP per skill in `dist/`.
2. Where custom skills are available, open **Plugins → Skills → Create → Upload from your computer** and upload each skill separately. Availability depends on your account, workspace and product surface.
3. Attach a photo and ask:

> Use watercolor-object to paint the cup in this photo on a transparent background. Detail 35, transparency 75, softness 55.

If your account has no skill upload UI, attach the relevant `SKILL.md` to a chat and ask ChatGPT to follow it for the attached photo. This provides the instructions for that conversation; it does not install a persistent skill.

### Claude.ai / Claude Desktop / Cowork

1. Run `python3 scripts/package.py`.
2. Open **Customize → Skills**, choose **Create skill → Upload a skill**, and upload each ZIP separately. Enable code execution and file creation where required.
3. Attach a photo and name the skill in your request.

Start with **watercolor-object-p5-brush** in an environment with code and browser tools. The image-editing skill additionally needs a connected image tool; installing a skill does not add that capability to Claude. If browser rendering is unavailable, the assistant can provide code but must report that no verified PNG was produced.

### Claude Code

From the downloaded repository:

```sh
python3 scripts/install.py --target claude
```

This copies both skills into `~/.claude/skills/`. For a project installation:

```sh
python3 scripts/install.py --target claude --project /path/to/project
```

Then attach/reference your photo and invoke:

```text
/watercolor-object-p5-brush Paint this drink on white, detail 35, transparency 75, softness 55. Save the PNG and editable sketch.
```

### Codex and agents using .agents/skills

```sh
python3 scripts/install.py --target agents
# Or install only in a project:
python3 scripts/install.py --target agents --project /path/to/project
```

This uses `~/.agents/skills/` or the project's `.agents/skills/`. For a Codex installation that uses `$CODEX_HOME/skills` (default `~/.codex/skills`), use:

```sh
python3 scripts/install.py --target codex
```

Invoke by name, for example `$watercolor-object`, with a source image. Local copies and ChatGPT workspace skills have separate installation lifecycles; this installer does not upload to your ChatGPT account.

### Other harnesses / custom agents

Copy the skill folders into the directory your harness discovers:

```sh
python3 scripts/install.py --destination /path/to/harness/skills
```

Or have the agent read `skills/<name>/SKILL.md` explicitly before the task. For a custom harness, expose each skill's `name` and `description` for selection, load its full instructions when selected, supply the source image through your model's image input, and provide the required tools. See the [Agent Skills integration guide](https://agentskills.io/integrate-skills).

**Portable instructions do not guarantee execution in every harness.** The image variant needs reference-image editing; the p5 variant needs code execution and browser/WebGL rendering for a verified export. No API keys, image service, p5 runtime or browser are included. Do not claim an image was rendered when those tools are missing.

## Examples

- “Use watercolor-object to turn the shoe on the left into watercolor, transparent background.”
- “用 watercolor-object 把照片里的花瓶画成水彩，只留花瓶，白底。”
- “Use watercolor-object-p5-brush to paint this iced coffee on white. Detail 20, transparency 85, softness 65. Give me the editable sketch and PNG.”

Always supply a source photo. Attach style references separately and label them as style references.

## Install behavior

The installer copies files locally and makes no network requests. It installs both skills unless you select `--skill watercolor-object` or `--skill watercolor-object-p5-brush`. It refuses to overwrite any existing skill, including symlinks; choose another destination or remove your old copy yourself. It never edits your original source skills.

To uninstall, remove only the named skill folders from the installation destination. Other skills remain untouched.

## Development and releases

```sh
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

Packaging creates reproducible per-skill ZIPs with one named top-level folder containing `SKILL.md`, plus `SHA256SUMS`. Upload the individual skill ZIPs, not an archive of this whole repository.

CI checks packaging and installation on Linux, macOS and Windows. Push a version tag such as `v0.1.0` to publish the upload ZIPs and checksums to GitHub Releases. The release job needs GitHub Actions enabled and repository permission to create releases.

The original skill instructions are preserved. This repository adds distribution tooling and documentation; it does not include example paintings or a prebuilt p5 rendering application. Visual output has to be verified in the user's chosen harness.

## License and dependencies

MIT for this repository's original instructions and tooling. p5.js and p5.brush are external projects with their own licenses; neither is bundled here. The p5 skill directs the agent to verify compatibility and pin exact versions for each generated sketch.

## Platform documentation

Setup instructions checked November 8, 2026. Product UI and eligibility can change.

- [ChatGPT skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Agent Skills specification](https://agentskills.io/specification)
- [p5.brush documentation](https://github.com/acamposuribe/p5.brush)
