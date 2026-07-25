## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific pack.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** a coordinated birthday-party clip-art pack — a kit of standalone assets to be cut apart and reused across invitations, favour tags, cupcake toppers, stickers, and signs. Full colour, flat vector style.

**Critical: this produces ONE image containing MANY assets.** The output is a single square **asset sheet** — separate items arranged on a grid against plain flat white, generously spaced so each can be lifted out cleanly. It is not a scene, not a composed illustration, and not one hero graphic. The old version of this brief described a "pack" and a "family" without ever telling the model it was making a single sheet, which is the most likely way this goes wrong.

**The failure mode to design against:** a party scene — the assets arranged into a picture, overlapping, sharing a background, and impossible to separate.

---

## What to produce

Six sections. **Budget: about 900 words total, 1,100 hard ceiling** — roughly 100–150 words each, section 6 allowed the most. Tight bullets, numbers wherever a number applies, and cut any sentence that restates this brief back at me.

**1. Style directions**
Exactly three vector styles worth using — for example flat playful, soft retro, geometric modern. One or two lines each: the mood it gives, how it scales down, what it costs.

**2. Pack composition**
The asset mix that makes a kit useful: how many characters, how many objects, how many decorative fillers, and a total count. State a total that keeps each item large enough on the sheet to be usable — more items means each one is smaller and worse. Name the categories worth covering and which two or three carry the pack.

**3. Sheet layout rules**
The rules that make the sheet separable: an even grid, consistent gap between items as a fraction of cell size, nothing overlapping or touching, nothing cropped at the sheet edge, plain flat white behind everything, and roughly balanced visual weight per cell so the sheet does not look lopsided. Note that items may differ in size but should sit on a shared grid.

**4. Cohesion rules**
What makes a pack look designed rather than assembled: one shared outline weight across every asset, one shared corner radius, one shared face style on anything with a face, one shared palette, and consistent simplification level. State that a single asset drawn at a different detail level ruins the set.

**5. Scale survival and palette**
Minimum feature size as a fraction of asset height, why interior detail should be sparse, and what to simplify so items survive at cupcake-topper size. Then dominant / support / accent split, a working colour count shared across the whole pack, and value separation between adjacent fills.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow. Use **short labelled blocks**, not one long paragraph:

```
Format:       single square asset sheet, separate clip-art items, flat vector style
Concept:      one line on the theme and mood
Assets:       a numbered list, one line each
Layout:       grid, even spacing, nothing overlapping, nothing cropped
Line & fill:  shared outline weight, flat fills, shared corner radius
Palette:      named colours shared across every asset
Background:   plain flat white behind all items
Constraints:  exclusions, LAST
```

State that the finished prompt should land at **180–250 words**, and that exclusions always come last, after every positive descriptor — a model reading negatives early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with: no scene or background setting, no items overlapping or touching, no items cropped at the edge, no ground line or shadow connecting items, no perspective or 3D, no drop shadows, no gradients, no texture or raster noise, no text or labels, no watermark, no signature.

Also state the two things the prompt must say in plain words no matter what: it is a **single sheet of separate clip-art assets on a plain flat white background**, and the items are **evenly spaced with clear gaps and never overlapping**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete over aspirational — "gap at least 1/5 of cell width" beats "well spaced". No preamble, no restating this brief, no summary of what you are about to do. Skip the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
