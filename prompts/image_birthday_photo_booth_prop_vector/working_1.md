## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific prop set.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** a set of large handheld **photo-booth props** — speech-bubble signs, masks, hats, glasses, themed objects — printed, cut out, mounted on sticks, and held up in birthday photos. They must read instantly from several feet away.

**This is one image containing several separate props.** The output is a single square sheet with the props laid out side by side on a plain white background, spaced so each can be cut out. It is not a scene, not a photo of people holding props, and not one prop filling the frame.

**Text matters more here than anywhere else in this set.** Photo-booth props are largely made of short shouted phrases, and the image model now renders in-image text reliably when the exact string is quoted. Use that.

**The failure mode to design against:** generic novelty props — a plain speech bubble saying "PARTY!", a moustache on a stick, and a pair of glasses, with nothing tying them to the theme.

---

## What to produce

Six sections. **Budget: about 900 words total, 1,100 hard ceiling** — roughly 100–150 words each, section 6 allowed the most. Tight bullets, numbers wherever a number applies, and cut any sentence that restates this brief back at me.

**1. Prop categories**
The prop types worth including and what each contributes: phrase signs, speech and thought bubbles, wearables held to the face, themed objects, and reaction props. Give a working set size and a recommended mix, noting which one or two categories carry the set.

**2. Distance readability**
The rules that make a prop work from across a room: minimum feature size as a fraction of prop height, bold single-weight outlines, high value contrast against a photo background, and why interior detail should be almost absent. State the squint test plainly.

**3. Text treatment**
Maximum word and character count per phrase, letter height as a fraction of prop height, heavy geometric sans letterforms, tight but not touching letter spacing, and why a phrase should be one line where possible. State that every phrase must be given in quotes with exact casing so it renders verbatim, and that unusual words should be spelled out character by character. Note what makes a phrase actually funny at a birthday rather than generic.

**4. Silhouette and cut-out safety**
These get printed and cut, so: one bold closed outer contour per prop, a white keyline border, no fragile protrusions or thin necks, minimum concave gap, no isolated floating pieces, and a solid area at the base of each prop where a stick attaches.

**5. Cohesion and palette**
What makes the props look like one family rather than assorted clip art: shared outline weight, shared corner radius, shared lettering, shared palette. Give a dominant / support / accent split and a working colour count, with value separation that photographs well.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow. Use **short labelled blocks**, not one long paragraph:

```
Format:       single square sheet of separate photo-booth props, flat vector style
Concept:      one line on the theme and mood
Props:        a numbered list, one line each, with exact quoted text
Layout:       grid arrangement, even spacing, nothing overlapping or touching
Line & fill:  outline weight, flat fills, white keyline border per prop
Palette:      named colours, dominant / support / accent
Lettering:    letterform, size, exact strings repeated in quotes
Background:   plain flat white
Constraints:  exclusions, LAST
```

State that the finished prompt should land at **180–250 words**, and that exclusions always come last, after every positive descriptor — a model reading negatives early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with: no people, no hands, no photo-booth scene or backdrop, no props overlapping or touching, no perspective or 3D, no drop shadows, no gradients, no texture or raster noise, no background scenery, no extra text beyond the quoted phrases, no misspellings, no watermark, no signature.

Also state the two things the prompt must say in plain words no matter what: it is a **single flat sheet of separate props on a plain white background**, and every phrase is **rendered verbatim exactly as quoted**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete over aspirational — "letter height at least 1/5 of prop height" beats "big bold text". No preamble, no restating this brief, no summary of what you are about to do. Skip the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
