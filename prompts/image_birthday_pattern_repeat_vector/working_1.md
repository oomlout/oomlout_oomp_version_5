## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific pattern.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** a square, full-colour, all-over birthday-party pattern tile in flat vector style, for wrapping paper, backdrops, cupcake wrappers, table cards, and signage panels.

**Be realistic about seams.** An image model cannot reliably produce a mathematically seamless tile — asking for "seamless" alone tends to produce a pattern that simply stops at the edges. What actually works is asking for an **evenly distributed all-over pattern that fills the entire square edge to edge with no border, no frame, and no margin**, with motif density consistent right up to all four edges. Treat true edge-matching as a later manual step; the job here is to produce a tile that is worth matching.

**The failure mode to design against:** scattered clip art on a page — a few motifs floating in the middle with empty corners and a visible frame of blank space.

---

## What to produce

Six sections. **Budget: about 900 words total, 1,100 hard ceiling** — roughly 100–150 words each, section 6 allowed the most. Tight bullets, numbers wherever a number applies, and cut any sentence that restates this brief back at me.

**1. Repeat logics**
Exactly three repeat structures worth using — for example tossed with rotation, structured grid or half-drop, stripe-assisted band. One or two lines each: the energy it gives, how obvious the grid becomes, what it costs.

**2. Motif hierarchy**
The three-tier system that stops a pattern reading as random: hero motifs, secondary motifs, tiny filler. Give a working count and relative size for each tier, the ratio between them, and the spacing rule that keeps heroes from clustering or lining up into accidental rows.

**3. Density and rhythm**
Target coverage as a rough percentage of the tile, minimum gap between motifs as a fraction of hero size, how much rotation variation keeps it lively without looking chaotic, and how to avoid the two classic tells — visible diagonal lanes and one obvious repeat unit the eye locks onto.

**4. Edge behaviour**
The rules that make it usable: motifs run right off all four edges rather than stopping short, no border or frame, no vignette, no drop shadow, consistent density in the corners, and no single motif dead-centre acting like a focal point.

**5. Palette and scale**
Dominant / support / accent split, a working colour count, background field colour and why it should stay light and flat, value separation so motifs stay distinct when the pattern is shrunk, and what to simplify so the design survives being printed small on a cupcake wrapper.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow. Use **short labelled blocks**, not one long paragraph:

```
Format:       square all-over repeating pattern, flat vector style
Concept:      one line on the theme and mood
Hero motifs:  the 2-3 largest elements, described
Secondary:    mid-size supporting motifs
Filler:       tiny elements that fill the gaps
Layout:       repeat logic, density, spacing, rotation variation
Palette:      background field colour plus named motif colours
Edges:        fills the square edge to edge, motifs run off all four sides
Constraints:  exclusions, LAST
```

State that the finished prompt should land at **180–250 words**, and that exclusions always come last, after every positive descriptor — a model reading negatives early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with: no border, no frame, no margin, no blank corners, no vignette, no single centred focal motif, no photorealism, no 3D render, no drop shadows, no gradients, no texture or raster noise, no text, no watermark, no signature.

Also state the two things the prompt must say in plain words no matter what: it is a **square flat-vector all-over repeating pattern**, and it **fills the entire image edge to edge with motifs running off all four sides**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete over aspirational — "minimum gap about 1/3 of hero motif width" beats "well spaced". No preamble, no restating this brief, no summary of what you are about to do. Skip the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
