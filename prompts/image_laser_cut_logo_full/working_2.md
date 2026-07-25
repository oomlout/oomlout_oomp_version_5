## Step 2 of 2 — the theme

The theme is: **{image_detail}**

Apply the house style you just wrote to this theme. Everything you need is now in hand — do not ask questions, just work.

---

## Part A — exploration

**Budget: about 450 words, 600 hard ceiling.** Push past the theme's first obvious reading, but do it briskly. No preamble, no restating the theme back at me.

- **Angles:** exactly four mascot interpretations, **one or two sentences each**. Include at least one that anthropomorphises an object or concept from the theme rather than reaching for the obvious animal, and at least one built on a visual pun. Then name your pick in a single sentence saying why it beats the other three — no full comparison table.
- **The chosen design:** one short paragraph fixing the pose, expression, props, and line strategy. Prefer gesture or a moment of character over a static front-on stare. Cut any prop that is decoration rather than signal.
- **Text:** one line — the exact string in quotes with exact casing, or "no text". Text is optional and a clean wordless mark often wins.
- **Trace and small-size check:** a short bullet list of fixes only — every stroke to thicken, gap to widen, island to bridge, detail to delete. Just the fixes, not the reasoning, and not a description of what the design looks like at size.

Skip anything not on that list: no tradeoff essays, no runner-up post-mortems, no notes on your own process.

## Part B — the final prompt

End your response with the final image-generation prompt for the chosen direction, and nothing after it.

Format it as a single fenced code block labelled `FINAL IMAGE PROMPT`, so it can be copied cleanly. Follow the six-part architecture from step 1 exactly, in order: medium and style → subject → key details → layout → line and manufacturing spec → exclusions last.

**Length: 180–250 words.** Long enough to carry the full spec, short enough that no single instruction gets diluted. If you are over, cut adjectives and repeated style words before you cut any manufacturing rule.

Hard requirements for that prompt:

- It opens by stating it is a **square black-and-white line-art mascot logo**.
- It says in plain words that the image is **square** and **pure black on a pure white background**.
- It states stroke weight as a fraction of the image width, and requires every shape to be a **closed path** with **no floating disconnected islands**.
- It caps interior detail explicitly and forbids crosshatching, stippling, and hairline tapers.
- Any literal text appears in quotes with exact casing, spelled out character by character if it is unusual.
- The exclusion list comes **last**, after every positive descriptor.
- It is self-contained: someone pasting it cold, with no memory of this conversation, gets the same image. No "as discussed above", no "the mascot from earlier".
- One prompt only. No variants, no alternates, no commentary after the code block.
