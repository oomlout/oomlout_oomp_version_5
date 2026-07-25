## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific banner family.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** a family of birthday **banners, frames, and signage backers** — headers, shaped panels, ribbon banners, arches, medallions, and corner pieces that other people will later drop names, ages, and event text into. Full colour, flat vector, built to scale from an invitation accent up to a welcome sign.

**Critical: this produces ONE image containing SEVERAL elements.** The output is a single square **element sheet** — separate framing pieces arranged against plain flat white with clear gaps. Not a finished invitation, not a composed sign.

**The text zones must be EMPTY.** This is the defining constraint and the one thing most likely to go wrong. These are backers for text added later, so the interior of every frame and banner must be left as clean blank space. Modern image models render text readily and will happily fill an empty banner with invented or garbled words unless told plainly to leave it blank. "Blank interior, no lettering of any kind inside the frames" is the instruction that prevents it.

**The failure mode to design against:** a finished invitation — one composed layout with fake names and dates baked in, which cannot be reused for anything.

---

## What to produce

Six sections. **Budget: about 900 words total, 1,100 hard ceiling** — roughly 100–150 words each, section 6 allowed the most. Tight bullets, numbers wherever a number applies, and cut any sentence that restates this brief back at me.

**1. Framing logics**
Exactly three framing systems worth using — for example ribbon banner, arch or medallion, layered badge panel. One or two lines each: the mood it gives, how it scales up, what it costs.

**2. Element mix**
Which pieces the family should contain and why: a large header or arch, one or two shaped panels, a ribbon banner, a medallion or seal, and a corner or divider set. Give a working count that keeps each element large on the sheet, and note which two carry the family.

**3. Text-zone rules**
The most important practical section. For each element: where the text zone sits, its proportion of the element, the minimum clear margin between ornament and zone edge, and the rule that ornament never intrudes into the zone. State plainly that the zones ship **empty** — no lettering, no placeholder words, no lorem text, no squiggles standing in for text. Note which shapes give a generous horizontal zone and which fight the text.

**4. Scale behaviour**
What has to hold from a 50 mm invitation accent to a metre-wide welcome sign: border weight as a fraction of element width, ornament size floors, why detail tuned to one exact size fails, and which parts should stay simple so they survive being enlarged and cropped.

**5. Cohesion and palette**
What makes a family rather than a pile: one shared border weight, one shared corner logic, one shared ornament vocabulary, one shared palette. Give a dominant / support / accent split, a working colour count, and a rule that the interior of each text zone stays light and flat so dark text will sit on it legibly.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow. Use **short labelled blocks**, not one long paragraph:

```
Format:       single square sheet of separate banner and frame elements, flat vector
Concept:      one line on the theme and mood
Elements:     a numbered list, one line each
Text zones:   where each sits, and that all are left completely blank
Layout:       grid, even spacing, nothing overlapping or touching
Line & fill:  shared border weight, flat fills, shared corner logic
Palette:      named colours, with light flat interiors inside text zones
Background:   plain flat white behind all elements
Constraints:  exclusions, LAST
```

State that the finished prompt should land at **180–250 words**, and that exclusions always come last, after every positive descriptor — a model reading negatives early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with, led by the text group because that is the likeliest failure: no text anywhere in the image, no words, no letters, no numbers, no names or dates, no placeholder or lorem text, no squiggles or lines standing in for text, no calligraphy. Then: no finished invitation layout, no scene or background setting, no elements overlapping or touching, nothing cropped at the edge, no photorealism or 3D, no drop shadows, no gradients, no texture or raster noise, no watermark, no signature.

Also state the two things the prompt must say in plain words no matter what: it is a **single sheet of separate blank frame and banner elements on a plain flat white background**, and every **text zone is left completely empty**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete over aspirational — "text zone at least 1/2 the element width" beats "generous text area". No preamble, no restating this brief, no summary of what you are about to do. Skip the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
