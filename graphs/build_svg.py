#!/usr/bin/env python3
"""Generate overview.svg with text wrapped to fit its cards.

SVG <text> does not wrap, so every line is placed explicitly and each card is
sized to the number of lines it ends up with. Line widths are measured with
DejaVu Sans, which runs wider than the Helvetica/Segoe stack the SVG asks
for -- so a line that fits here fits everywhere.
"""
from PIL import ImageFont  # pip install pillow

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W = 1000
PAD_X, CARD_X, CARD_W = 70, 118, 860
RIGHT = PAD_X + CARD_W - 24          # keep 24px clear inside the card
AVAIL = RIGHT - CARD_X

DESC_SIZE, TITLE_SIZE, LINE_H = 27, 44, 34
TOP, GAP = 44, 42


def width(text, size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size).getlength(text)


def wrap(text, size):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if cur and width(trial, size) > AVAIL:
            lines.append(cur)
            cur = w
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


CARDS = [
    ("1", "Sleep EEG", "#D8385A", "#FF6E8F",
     "One full night · 6 scalp electrodes (F3 C3 O1 F4 C4 O2) · subject sub-19"),
    ("2", "Spectral analysis", "#00D4FF", "#00D4FF",
     "Power in five EEG bands per electrode (δ θ α σ β), spectrally flattened"),
    ("3", "Principal components", "#00D4FF", "#00D4FF",
     "Five components per electrode track how each spectrum moves through the night"),
    ("4", "RAVE — latent-space navigation", "#FFD700", "#FFD700",
     "The components are written into a neural model's latent space. The encoder "
     "is bypassed — the sleep data itself becomes a position inside a learned sound."),
    ("5", "Neural audio", "#D8385A", "#FF6E8F",
     "The model synthesises sound. The whole night is compressed 30:1 — "
     "~7 h into 14:20."),
]

FOOT_TITLE = "In the composition"
FOOT_BODY = ("the current sleep stage selects which electrode → model "
             "pairing you hear.")

esc = lambda s: (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---- lay out -------------------------------------------------------------
body, y = [], TOP
for num, title, bar, ink, desc in CARDS:
    lines = wrap(desc, DESC_SIZE)
    h = 122 + LINE_H * (len(lines) - 1) + 28
    tsize = TITLE_SIZE
    while width(title, tsize, bold=True) > AVAIL:      # shrink rather than clip
        tsize -= 1
    body.append(f'''
  <!-- ============ CARD {num} · {title.upper()} ============ -->
  <g>
    <rect x="{PAD_X}" y="{y}" width="{CARD_W}" height="{h}" rx="16" fill="#171e3d" stroke="#2a3358"/>
    <rect x="{PAD_X}" y="{y}" width="9" height="{h}" rx="4" fill="{bar}"/>
    <text x="{CARD_X}" y="{y + 42}" class="step" font-size="24">{num}</text>
    <text x="{CARD_X}" y="{y + 82}" class="title" font-size="{tsize}" fill="{ink}">{esc(title)}</text>''')
    for i, ln in enumerate(lines):
        body.append(f'    <text x="{CARD_X}" y="{y + 122 + LINE_H * i}" '
                    f'class="desc" font-size="{DESC_SIZE}">{esc(ln)}</text>')
    body.append("  </g>")
    bottom = y + h
    if num != CARDS[-1][0]:
        body.append(f'  <path d="M500 {bottom + 6} l16 20 l-32 0 z" fill="#3a4570"/>')
    y = bottom + GAP

# ---- footer note ---------------------------------------------------------
y += 2
flines = wrap(FOOT_BODY, 26)
fh = 48 + 38 + LINE_H * (len(flines) - 1) + 24
body.append(f'''
  <!-- ============ FOOTER NOTE · stage gating ============ -->
  <rect x="{PAD_X}" y="{y}" width="{CARD_W}" height="{fh}" rx="16" fill="#1c1633" stroke="#4a3d16"/>
  <rect x="{PAD_X}" y="{y}" width="9" height="{fh}" rx="4" fill="#FFD700"/>
  <text x="{CARD_X}" y="{y + 48}" font-size="26" font-weight="700" fill="#FFD700">{FOOT_TITLE}</text>''')
for i, ln in enumerate(flines):
    body.append(f'  <text x="{CARD_X}" y="{y + 86 + LINE_H * i}" '
                f'font-size="26" fill="#cbd0e6">{esc(ln)}</text>')

H = y + fh + TOP

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif" role="img" aria-label="How it works: five-stage pipeline turning one night of sleep EEG into neural audio.">
  <defs>
    <style>
      .title{{font-weight:700}}
      .desc{{fill:#9aa3c0}}
      .step{{font-weight:700;fill:#5a6591;letter-spacing:.05em}}
    </style>
  </defs>

  <!-- backdrop -->
  <rect x="0" y="0" width="{W}" height="{H}" rx="26" fill="#0d1228"/>
{chr(10).join(body)}
</svg>
'''

for path in ["/home/stv/projects/personal/navigating-sleep/graphs/overview.svg",
             "/home/stv/projects/personal/navigating-sleep/docs/img/overview.svg"]:
    open(path, "w").write(svg)

# ---- report + assert nothing overflows -----------------------------------
print(f"viewBox 0 0 {W} {H}   (was 1000x1200)\n")
worst = 0
for num, title, _, _, desc in CARDS:
    for ln in [title] + wrap(desc, DESC_SIZE):
        sz = TITLE_SIZE if ln == title else DESC_SIZE
        w = width(ln, sz, bold=(ln == title))
        worst = max(worst, w)
        flag = "  OVERFLOW" if w > AVAIL else ""
        print(f"  {CARD_X + w:6.0f}px / {RIGHT}px  {ln[:58]}{flag}")
for ln in [FOOT_TITLE] + flines:
    w = width(ln, 26)
    worst = max(worst, w)
    print(f"  {CARD_X + w:6.0f}px / {RIGHT}px  {ln[:58]}"
          + ("  OVERFLOW" if w > AVAIL else ""))
print(f"\nwidest line ends at {CARD_X + worst:.0f}px, card inner edge {RIGHT}px "
      f"-> {RIGHT - CARD_X - worst:.0f}px to spare")
