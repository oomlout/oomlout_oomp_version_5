## READ THIS FIRST — no theme is coming in this message, and that is correct

This is **step 1 of 2**. It is deliberately theme-free. You are building a reusable house style, not designing a specific pin.

The theme arrives in step 2. Do **not** ask what the theme is. Do **not** ask any clarifying questions. Do **not** write a final image-generation prompt yet — you cannot, and attempting one is a failure of this step. Do **not** invent a placeholder theme and design for it. If you feel information is missing, that is expected: the missing information is the theme, it is coming next, and nothing in this step requires it.

Your entire output for this step is a **house style guide** that will be applied to whatever theme arrives next.

---

## The product this style serves

**Intended use:** flat, front-view, production-ready **artwork** for a hard-enamel pin roughly 1 to 1.5 inches tall. Full colour, flat fills, every colour region enclosed by a metal line.

**This is artwork, not a photograph of a pin.** That distinction is the most important thing in this brief. The image model is very strong at photorealism and will drift toward a rendered pin on a jacket, a glinting metal mockup, or a product shot on a desk unless told firmly and repeatedly not to. Flat 2D, straight-on, no perspective, no bevel, no gloss, no shadow, no backing card, no hand holding it.

**The failure mode to design against:** generic merch art — a smiling animal in a circle with a banner underneath, in colours that could belong to any theme.

---

## What to produce

Six sections. **Budget: about 900 words total, 1,100 hard ceiling** — roughly 100–150 words each, section 6 allowed the most. Tight bullets, numbers wherever a number applies, and cut any sentence that restates this brief back at me.

**1. Composition archetypes**
Exactly three pin compositions worth using — for example character badge, emblem or crest, object-with-a-face. One or two lines each: what it does for collectibility, how it holds up at 1 inch, what it costs.

**2. Metal-line rules**
The heart of enamel production, so be concrete. Every colour region must be fully enclosed by metal — no colour touching colour directly, no open-ended lines. Give minimum line weight and minimum enamel-well width as fractions of pin height, the smallest enclosed area worth keeping, and the rule for when two adjacent small regions should merge into one. Note that the outer silhouette line is the heaviest line in the piece.

**3. Palette discipline**
A working colour count for hard enamel (state a number and a ceiling), the value-separation rule that keeps neighbouring fills distinct at arm's length, why near-identical shades waste a colour slot, and how to pick a dominant / support / accent split. Gradients, blends, and transparency are impossible here and must be replaced by discrete flat fills.

**4. Small-size survival**
What dies at 1 inch and what to do about it: fragile protrusions, isolated islands, micro text, dense interior detail, thin tapers. Give the minimum feature size as a fraction of pin height and the fix for each failure.

**5. Charm and collectibility**
The levers that make a pin feel giftable rather than stock — one clear idea, a face with one readable emotion, a small joke or story beat, an outer silhouette you could recognise as a black shape. Then a short do-not list: the circle-with-banner cliché, dead-centre symmetry, generic sparkles, each with its fix.

**6. Prompt architecture for step 2**
The most important section, so spend your words here. Specify the exact template the step-2 final prompt must follow. Use **short labelled blocks**, not one long paragraph:

```
Format:       flat front-view vector artwork for an enamel pin, straight-on, 2D
Concept:      one line on the idea and mood
Subject:      what it is, pose, expression, the one clear read
Details:      props, border or badge shape, any short quoted text
Metal lines:  uniform outlines enclosing every colour region, weights
Palette:      named flat colours, dominant / support / accent
Layout:       centred, plain flat background, generous even margin
Constraints:  exclusions, LAST
```

State that the finished prompt should land at **180–250 words**, and that exclusions always come last, after every positive descriptor — a model reading negatives early tends to treat them as things to compose rather than things to omit.

Give the canonical exclusion list to close with, led by the anti-mockup group because that is the likeliest failure: not a photograph, not a product mockup, not a 3D render, no perspective or tilt, no bevelled or raised edges, no metallic sheen or specular highlight, no drop shadow, no reflection, no backing card or packaging, no hand or garment, no desk or surface. Then the flat-art group: no gradients, no blends, no transparency, no airbrush shading, no texture, no raster noise, no micro text, no watermark, no signature, no extra text beyond what is quoted.

Also state the two things the prompt must say in plain words no matter what: it is **flat 2D vector artwork for enamel pin production**, and every colour region is **enclosed by a metal line**.

---

## Response style and length

**About 900 words, 1,100 absolute maximum.** Bullets over prose. Concrete over aspirational — "outer line no thinner than 1/60 of pin height" beats "bold outline". No preamble, no restating this brief, no summary of what you are about to do. Skip the reasoning behind each rule; just state the rule.

Close with a checklist of the rules, 12 lines at most, so step 2 can be graded against it.

Then stop. No final image prompt, no questions, no theme.
