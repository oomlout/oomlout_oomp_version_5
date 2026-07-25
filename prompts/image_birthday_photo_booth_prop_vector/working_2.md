## Step 2 of 2 — the theme

The theme is: **{image_detail}**

Apply the house style you just wrote to this theme. Everything you need is now in hand, so do not ask questions, just work.

---

## Part A — exploration

**Budget: about 450 words, 600 hard ceiling.** Push past the theme's first obvious reading, but do it briskly. No preamble, no restating the theme back at me.

- **Angles:** exactly three directions for the set, **one or two sentences each** — for example phrase-led, wearable-led, themed-object-led. Then name your pick in a single sentence saying why it beats the other two.
- **The prop list:** a numbered list of the props in the set, one line each, covering shape and what it does at a party. Include a mix of categories. Keep the set to a number that still leaves each prop large on the sheet.
- **The phrases:** every piece of text as an exact quoted string with exact casing, one per line. Keep them short and make them theme-native and actually funny — a generic "PARTY TIME!" is a wasted prop.
- **Cohesion:** one or two lines fixing shared outline weight, lettering, and the palette with named colours.
- **Readability and cut fixes:** a short bullet list only — anything to enlarge, thicken, shorten, or delete so each prop reads at distance and cuts cleanly. Just the fixes, not the reasoning.

Skip anything not on that list: no tradeoff essays, no runner-up post-mortems, no notes on your own process.

## Part B — the final prompt

End your response with the final image-generation prompt for the chosen set, and nothing after it.

Format it as a single fenced code block labelled `FINAL IMAGE PROMPT`, so it can be copied cleanly. Use the labelled-block template from step 1 in order: Format → Concept → Props → Layout → Line & fill → Palette → Lettering → Background → Constraints last.

**Length: 180–250 words.** Long enough to carry the full spec, short enough that no single instruction gets diluted. If you are over, cut adjectives and props before you cut any lettering or layout rule — fewer, bigger, correct props beat more crowded ones.

Hard requirements for that prompt:

- Its **first sentence** states this is a **single flat sheet of separate photo-booth props in flat vector style on a plain white background**. Opening words set the mode for everything after.
- It lists the props explicitly and states the **grid arrangement with even spacing and nothing overlapping or touching**.
- Every phrase appears **in quotes with exact casing**, and the full set of strings is restated in the Lettering block so the model sees them twice.
- It gives letter height relative to prop height and calls for a heavy geometric sans.
- It calls for a **bold closed outline and white keyline border on each prop**.
- The exclusion list comes **last**, after every positive descriptor, and includes no people, no hands, no photo-booth scene, no overlapping props, no extra or misspelled text.
- It is self-contained: someone pasting it cold, with no memory of this conversation, gets the same image. No "as described above", no "the props from earlier".
- One prompt only. No variants, no alternates, no commentary after the code block.
