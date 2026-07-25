## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific icon set.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** a set of small birthday-party **icons and badges** for cupcake toppers, favour labels, thank-you tags, mini stickers, straw flags, and envelope seals. Full colour, flat vector, designed tiny-first and scaling up cleanly.

**Critical: this produces ONE image containing MANY icons.** The output is a single square **icon sheet** — separate badges on a regular grid against plain flat white, evenly spaced so each can be lifted out. Not a scene, not a composed illustration.

**Design tiny-first.** These are the smallest assets in the whole set, often printed under an inch. Anything that survives at that size will survive everywhere else, so every rule here should be written for the smallest use and not the largest.

**The failure mode to design against:** shrunken illustrations — detailed little pictures that look fine on screen and turn to mush at 20 mm.

---

## What to produce

Six sections. **Budget: about 900 words total, 1,100 hard ceiling** — roughly 100–150 words each, section 6 allowed the most. Tight bullets, numbers wherever a number applies, and cut any sentence that restates this brief back at me.

**1. System directions**
Exactly three directions worth using — for example flat symbolic icons, tiny mascot badges, label-like emblems. One or two lines each: what it gives the set, how it holds at 20 mm, what it costs.

**2. Badge shapes**
The containing shapes worth using — circle, scalloped circle, shield, tab, ribbon, rounded square, simple seal — and what each signals. State how many distinct shapes a set should use before it stops looking like a system, and the rule for keeping every badge inside one shared bounding size so the set looks even on the sheet.

**3. Tiny-size survival**
The hardest constraint, so be concrete. Give minimum feature size and minimum stroke weight as fractions of badge diameter, minimum gap between two interior elements before they merge, the maximum number of distinct elements inside one badge, and the rule for how many levels of detail a 20 mm badge can carry. List what always dies: micro text, thin internal lines, delicate protrusions, subtle tonal differences, small isolated dots.

**4. Simplification method**
How to reduce a subject to an icon: find the one identifying feature, drop everything else, merge adjacent shapes, prefer silhouette over interior line, and use the containing shape to do work the icon would otherwise have to. Give the squint test plainly.

**5. Cohesion and palette**
One shared stroke weight, one shared corner radius, one shared simplification level, one shared face style if faces are used, and every badge on the same visual footing. Then a tight palette: a working colour count for the whole set, dominant / support / accent, and value separation strong enough that two badges never blur into each other.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow. Use **short labelled blocks**, not one long paragraph:

```
Format:       single square icon sheet, separate badges, flat vector style
Concept:      one line on the theme and mood
Icons:        a numbered list, one line each, with badge shape
Layout:       regular grid, equal cell size, even spacing, nothing overlapping
Line & fill:  shared stroke weight, flat fills, simplified interiors
Palette:      named colours shared across the whole set
Background:   plain flat white behind all badges
Constraints:  exclusions, LAST
```

State that the finished prompt should land at **180–250 words**, and that exclusions always come last, after every positive descriptor — a model reading negatives early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with: no scene or background setting, no badges overlapping or touching, nothing cropped at the edge, no micro text, no thin hairlines, no fine interior detail, no perspective or 3D, no drop shadows, no gradients, no texture or raster noise, no text unless explicitly quoted, no watermark, no signature.

Also state the two things the prompt must say in plain words no matter what: it is a **single sheet of separate small icons on a plain flat white background**, and each icon is **simplified enough to read clearly at about 20 mm**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete over aspirational — "no more than four distinct elements per badge" beats "keep it simple". No preamble, no restating this brief, no summary of what you are about to do. Skip the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
