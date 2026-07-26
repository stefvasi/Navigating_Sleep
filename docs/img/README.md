# Graphic for the listen page

The page expects one explanatory graphic here:

    overview.png

Save it as `overview.png` and it appears automatically, replacing the dashed
"Diagram coming soon" box. For a different format or filename, update the
`<img src="…">` in `../index.html`.

## Two things to do when you add it

1. **Write a real `alt` description** in `../index.html`. The placeholder text
   there describes a generic pipeline diagram; replace it with what your
   graphic actually shows. Someone using a screen reader should get the same
   information a sighted reader gets from looking at it. Describe the content,
   not the file ("EEG bandpower feeds three RAVE models, gated by sleep
   stage…", not "diagram of the system").

2. **Check the `width` and `height` attributes** match the real pixel
   dimensions. They stop the page from jumping around while the image loads.

## Format

- PNG for diagrams and anything with text. SVG is even better if the graphic
  is vector — it stays sharp on a phone and is usually smaller.
- Target roughly 1200–1600 px wide. The page renders it at column width, and
  the extra pixels cover high-density phone screens.
- Keep it under about 500 KB.
- Make sure any labels are legible at phone size — a diagram that only reads
  at A1 poster scale will be unusable here.
