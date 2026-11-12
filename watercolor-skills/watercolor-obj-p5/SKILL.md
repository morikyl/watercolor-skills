---
name: watercolor-obj-p5
description: Paint an object from a reference photo as an isolated procedural watercolor using p5.js and p5.brush.js, delivering editable sketch code and a PNG. Use for the p5.brush version of watercolor-obj rather than AI image generation.
---

# Watercolor Object with p5.brush

Create an actual p5.brush painting from a supplied photo. This is a separate implementation of watercolor-obj: the assistant interprets the subject into geometry and the library renders the pigment. It is not automatic photo segmentation or a promise of photographic fidelity. Do not substitute an image-generation service, a filtered photo, or a generated raster embedded in a canvas for the painting.

## Subject and visual identity

Inspect the source photo before writing geometry. Select the named object or unmistakable main object. Preserve its proportions, viewpoint, silhouette, palette, and identifying details. Retain attached straws, handles, stems, lids and integral markings; remove hands, props, scenery, detached captions and cast shadows. Reconstruct obscured portions conservatively.

Use a traditional observational watercolor approach: broad translucent washes, reserved highlights, irregular pigment deposits and selective descriptive marks. Glass and plastic need interrupted contours and clear white reserves. Group cereal, seeds and other repeated features into economical shapes instead of tracing every piece. Avoid uniform outlines, confetti-like stippling, vector-flat fills, photorealistic microtexture and whole-image blur.

Default to pure white, reflecting this variant's established project preference. Support transparent output when requested, with verified alpha. Keep paper tooth inside pigment only. No textured background, splash halo, shadow, border or signature. Center the complete object with roughly 10–15% clear margin; account for long straws and fill bleed. Fit geometry uniformly when aspect ratio changes rather than stretching it.

## Independent continuous controls

Expose a small editable settings object with `detail: 35`, `transparency: 75`, `softness: 55`, a fixed seed, canvas dimensions and background mode. User choices override defaults. These are artistic scales, not measured image percentages or native library arguments.

- Detail 0–100: progress from few broad masses to selective fine descriptive marks. Control contour sampling, feature count and stroke precision. Keep major landmarks at all values; use stable seeded feature sets so changing detail does not rearrange the object.
- Transparency 0–100: progress from concentrated pigment to airy washes. Control wash opacity and layering together to avoid many faint layers becoming opaque. Preserve a few darker identifying accents even at 100.
- Softness 0–100: progress from irregular defined edges to mostly feathered or lost secondary edges. Control wash bleed and the proportion of reinforced contours. Keep essential edges readable, and do not implement this with a uniform blur.

Document the actual mapping in the sketch. Use the same seed to compare settings. A change to one control should not silently reset the other two. Controls must alter rendering, not merely labels. A settings object is sufficient unless the user requests an interface.

## Implementation workflow

1. Inspect the image and write a short subject plan: normalized silhouette, structural landmarks, palette, highlights and simplified feature groups. Use the photo as evidence, not as a visible background layer.
2. Resolve a compatible p5.js / p5.brush pair from the official documentation and pin exact versions in the output. Read the documentation for the version actually installed; do not combine snippets from incompatible releases. See [official library documentation](https://github.com/acamposuribe/p5.brush) and [releases](https://github.com/acamposuribe/p5.brush/releases).
3. Build an editable local HTML/JS sketch. Store subject geometry separately from rendering settings. Paint large masses first, then translucent internal regions, then sparse accents. Use p5.brush for the actual pigment and strokes; native canvas/p5 operations may handle setup, compositing and export.
4. Run it in a browser. Verify that dependencies load, painting completes, no console errors occur, and export waits until rendering has finished. Avoid continuous repainting that accumulates pigment. If dependencies or browser rendering are unavailable, report the specific limitation; do not claim a PNG was produced.
5. Inspect the rendered image against the reference for recognizable form, restrained brushwork, clean background and uncropped extremities. Adjust the geometry or washes when necessary. Check the exported PNG too: dimensions, nonblank pixels, and alpha when requested. Test contrasting scale settings once to ensure they produce meaningful differences.
6. Save the sketch and PNG in a new subject-specific workspace folder without replacing the source photo. For a batch, give each source its own geometry and descriptive output name. Show the painting and link the export plus editable sketch, with the three settings and any material limitations.

## Library compatibility notes

Verified against the official documentation on 2026-10-10; recheck for the selected release. The p5 build requires p5.js 2.x and a WEBGL canvas. Load p5 before p5.brush. In instance mode, call `brush.instance(p)` before setup. WEBGL coordinates start at the center; choose a consistent transform for normalized geometry.

Use `brush.fill()` for watercolor regions, `brush.noStroke()` for unoutlined masses, and brush primitives for geometry. Verify fill opacity, `fillBleed`, and `fillTexture` signatures and ranges in the selected version. Reset drawing state deliberately between layers. Scale built-in brushes to the canvas. Current p5-build seeding uses p5's `randomSeed()` and `noiseSeed()`; standalone APIs differ. Do not mix standalone render/seed calls into the p5 build.

For transparent exports, do not paint white into areas intended as holes or empty canvas. Preserve highlight reserves as unpainted space where appropriate; verify that the renderer and export actually preserve alpha.

## Example invocation

“Use $watercolor-obj-p5 to paint this drink on white, detail 35, transparency 75, softness 55. Save the PNG and editable sketch.”
