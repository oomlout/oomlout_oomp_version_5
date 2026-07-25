## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific logo.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** a square, single-colour, pure-black-on-pure-white mascot logo, generated as a raster image, then **auto-traced to vector and cut/engraved on a laser cutter**. The trace step is unforgiving — it is the hardest constraint in this brief and should shape most of your recommendations.

**Target feel:** charming, original, cute, polished, instantly readable at ~20 mm. A designed branded icon, not a doodle page and not generic kawaii clip art.

---

## What to produce

Write these six sections. **Budget: about 900 words total, 1,100 hard ceiling.** That is roughly 100–150 words per section, with section 6 allowed the most. This is a working reference, not an essay — every line should be a rule someone could check a drawing against. Prefer tight bullets over prose paragraphs, and cut any sentence that only restates the brief back at me.

**1. Line language menu**
Exactly three distinct black-on-white line-art approaches (e.g. uniform monoline, weight-varied outline with sparse interior, chunky sticker-outline, geometric constructed line). One or two lines each: what it does for charm, how it survives auto-tracing, what it costs.

**2. Cuteness that isn't generic**
The handful of levers that make a line mascot lovable — eye shape and spacing, head-to-body ratio, pose energy, mouth simplicity, restraint on blush marks — each as a one-line rule with a number where a number applies. Then a short do-not list of the clichés that make an AI mascot look stock (dead-centre symmetrical stare, sparkle confetti, floating hearts, blob bodies), each with its one-line replacement.

**3. Trace-safety rules**
A flat list of concrete, checkable rules for the auto-trace-to-cut pipeline — one line each, no explanatory paragraphs:
- minimum stroke thickness relative to the square's width, stated as a fraction (so it scales)
- minimum gap between two adjacent strokes before they blur into one traced blob
- why every shape should read as a closed path, and how to spot one that won't
- island/floating-part handling and where to add connective bridges
- what to do about interior detail that a tracer will turn into noise (crosshatching, stippling, tapering hairlines, single stray dots)
- why large solid black fills are avoided here, and the acceptable exceptions (small eyes, pupils, a tiny accent shape)

**4. Composition and hierarchy**
Bulleted rules only: square framing, margin as a fraction of the square, centre of visual mass, minimum negative space, the mascot-leads / props-support / text-reinforces hierarchy, and the shared traits that make it read as one illustrator's hand (same stroke weight, same corner radius, same eye style, same spacing rhythm).

**5. Text and badge treatments**
Text is **optional**. Briefly: when a word helps versus clutters, a maximum letter count that stays cuttable, how to specify literal text so it renders verbatim (quotes, exact casing), the letterform to ask for, and when a badge ring earns its place versus just boxing the mark in. Six bullets is plenty.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow — and state that the finished prompt should land at **180–250 words**, long enough to carry the spec, short enough that no single instruction gets diluted. Order it to match how the image model weights a prompt:

1. **Medium and style up front** — the first sentence states it is a square black-and-white line-art mascot logo, because opening words set the mode for everything after.
2. **Subject** — the mascot, its identity, expression, pose.
3. **Key details** — props, supporting motifs, any literal text in quotes.
4. **Layout** — centring, margins, hierarchy, where each element sits.
5. **Line and manufacturing spec** — stroke weight, closed paths, interior-detail limits.
6. **Exclusions last** — negatives go at the very end, after every positive descriptor, because a model reading them early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with (no grey, no shading, no gradients, no halftone, no dithering, no texture, no colour, no transparency, no background scene, no drop shadow, no outer glow, no frame border unless specified, no watermark, no signature, no extra text beyond what is quoted).

Also state the two facts the prompt must say in plain words no matter what: the image is **square**, and it is **pure black on a pure white background**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete and checkable over abstract and aspirational — "stroke no thinner than 1/100 of the square's width" beats "confident lines". No preamble, no restating this brief back at me, no summary of what you are about to do. Skip the caveats and the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
