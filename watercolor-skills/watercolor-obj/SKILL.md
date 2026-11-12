---
name: watercolor-obj
description: Turn an object in an existing image into an isolated hand-painted watercolor illustration on a transparent or plain white background. Use for watercolor object cutouts from photos or illustrations, not full-scene paintings or poster layouts.
---

# Watercolor Object

Transform the selected object in a supplied image into a recognizable watercolor painting, with only the item on transparent or white background.

Inspired by Minimal Zine Poster v0.1's quiet, tactile, handmade character. Carry over its restraint and imperfect material texture, but not its aged-paper backdrop, tiny subject, typography, forced saturated accent, or 3:5 poster canvas. This skill is self-contained and does not require loading the poster skill.

## Input and defaults

- Use the supplied or clearly referenced existing image as the edit source. If none is available, ask for an image rather than inventing the object.
- Follow any named object selection. Otherwise choose the unmistakable main object. If several objects are equally plausible, ask which to isolate.
- Default to a genuinely transparent PNG. If the user asks for white, use uniform pure white (#FFFFFF).
- Preserve the object's recognizable silhouette, proportions, viewpoint, defining features, and source colors. Do not force blue or another accent. Retain a simple attached part such as a handle or stem; exclude hands, surrounding props, surface, scenery, cast shadows, captions, and decorative marks unless requested.
- Use a canvas that suits the object's proportions, with the entire item centered and approximately 10–15% clear margin on each side. Preserve delicate extremities; do not crop to make the subject fill the frame.

## Watercolor treatment

Use translucent layered pigment washes, subtle pigment pooling, natural granulation, gentle wet-on-wet transitions, and selective dry-brush edges. Keep enough structure to identify the original object. Let a few edges soften naturally without adding a glow or opaque fringe.

Render paper-like tooth inside the painted pigment only. Outside the silhouette, keep the requested transparent or pure-white background completely clean. No beige paper sheet, texture rectangle, vignette, watercolor splash halo, ground shadow, border, typography, signature, watermark, or extra decoration.

Keep the palette faithful but painterly. Avoid glossy photorealism, vector-flat fills, heavy cartoon outlines, oil-paint impasto, and overly uniform digital airbrushing. Do not reproduce detached source text; integral markings can be simplified while preserving identity unless exact lettering is explicitly requested.

## Reference-calibrated painting scale

The default aesthetic is a traditional observational watercolor study: simplified painted shapes, transparent layered washes, reserved white highlights, uneven pigment deposits, and a deliberate mix of found and lost edges. The user's reference examples include a teal glass bottle, cut figs, iced coffee, and a martini glass. Borrow their painting language, not their subjects, signatures, surrounding paper, shadows, or screenshot layout.

Use three independent continuous scales from 0 to 100. Default to **detail 35 / transparency 75 / softness 55** unless the user specifies otherwise. Treat values as artistic direction, not measurable pixel percentages or guaranteed exact visual outcomes. Interpret intermediate positions progressively, not as binary presets.

| Scale | 0 | 50 | 100 |
| --- | --- | --- | --- |
| Brushwork detail | Broad economical washes; small features suggested with a few marks | Recognizable forms with selective detail at focal points | Fine watercolor study with careful brush marks; never photographic microtexture |
| Paint transparency | Rich concentrated pigment and pooling, still visibly watercolor | Translucent layered washes with white reserves | Airy diluted washes and generous untouched highlights; keep the object visible |
| Edge softness | Defined but naturally irregular painted contours, not vector outlines | Balanced crisp focal edges and softly disappearing secondary contours | Mostly feathered or lost edges, retaining essential structural contours; never uniform blur |

At every position preserve natural pigment granulation, pooled edges, subtle warm/cool color variation, and selective white reserves. Avoid a photo traced into thousands of little colored patches, uniform stippling, glossy product rendering, and digital blur masquerading as watercolor. Detail changes the number and precision of descriptive marks; transparency changes pigment density; softness changes edge transitions. Do not let one scale automatically override the other two.

Translate settings into concrete choices for the uploaded object. At the default 35/75/55, suggest reflective glass or plastic with a few incomplete contour strokes and reserved whites; group repeated small features such as cereal into economical color shapes; build large surfaces with broad luminous washes; keep a few identifying edges crisp while letting secondary edges disappear. Preserve source identity and colors while omitting nonessential photographic detail.

If a style reference is attached, distinguish it from the real-photo subject. Use the photo for object identity and the reference for painting technique only. Do not substitute a previous watercolor output for a newly uploaded real photo. Without the original reference file, this written calibration is sufficient; do not require the user to reattach it.

## Workflow

1. Inspect the source and identify the selected object, its defining features, source colors, and background choice. For a local image, view it before editing.
2. Use the built-in image generation/editing tool with the actual source image attached as the edit target. Use its supported image-reference mechanism. Generate the image, not just a prompt. Do not substitute a code-drawn illustration or silently switch to a paid API workflow.
3. Resolve the three scale values, then compile a focused prompt using the structure below. Include each numeric value and its concrete visual interpretation for the subject. State exactly what to preserve, simplify, remove, and repaint. User requests override these defaults.
4. Inspect the result for object fidelity, watercolor character, full silhouette, clean margins, removal of the source surroundings/text, and the requested background. For transparency, inspect alpha information if available; a white preview alone does not prove transparency. Never accept a painted checkerboard as transparency or describe an opaque image as transparent.
5. If there is a clear failure, make one targeted correction using the image editing tool. If the tool cannot supply actual transparency, explain the limitation and offer the permitted white-background version rather than claiming success.
6. Show the final image. For a reusable or project-bound asset, save the selected output in the user's workspace without overwriting the source. Provide a file link and a brief note naming the background. Briefly report the three scale values used so the user can adjust the next test. Include the generation prompt only if requested.

## Prompt scaffold

Adapt the brackets to observed details; do not pass placeholders to the image tool.

"Edit the supplied image. Isolate only [selected object]. Preserve [distinctive silhouette, proportions, viewpoint, details, and source colors]. Repaint the object as a delicate hand-painted watercolor illustration with translucent layered washes, subtle pigment granulation and pooling, soft wet-on-wet transitions, and selective dry-brush edges. Keep it clearly recognizable as the same item. Apply detail [0–100], pigment transparency [0–100], and edge softness [0–100]: [concrete subject-specific brushwork, wash, and contour instructions derived from the scale]. Use a traditional watercolor-study approach with economical marks, white reserves, and natural pigment behavior; never a photo-filter effect.

Remove [source surroundings, props, hands, captions, and shadows as applicable]. Show the entire object centered with comfortable clear margins on a [genuinely transparent background with alpha / uniform pure white #FFFFFF background]. Any paper tooth must be confined to the pigment inside the object. Keep holes and open spaces, such as the interior of a handle, consistent with the chosen background.

No background paper, scenery, ground shadow, halo, splashes outside the object, added text, border, signature, watermark, checkerboard pattern, photorealistic surface, vector-flat rendering, or heavy outlines. Deliver an isolated watercolor item [as PNG with preserved alpha for transparent output]."

## Example requests

- "Use $watercolor-obj to turn the cup in this photo into watercolor, transparent background."
- "用 $watercolor-obj 把这张图里的花瓶画成水彩，只留花瓶，白底。"
- "Turn the shoe on the left into an isolated watercolor illustration."

- "Use $watercolor-obj on this real photo, detail 35, transparency 75, softness 55, white background."
