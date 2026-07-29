# Audio for the listen page

Drop the finished files in this folder using **these exact filenames** — the
page already points at them, so nothing in `index.html` needs editing. Each
player's "Coming soon" notice disappears by itself once its file is present.

| Filename                              | Clip on the page             | Cut from (composition) |
|---------------------------------------|------------------------------|------------------------|
| `Navigating-Sleep-composition.mp3`    | The full composition (14:28) | — |
| `Navigating-Sleep-voices.mp3`         | Voices soundscape (14:28)    | — |
| `Navigating-Sleep-organ.mp3`          | Organ soundscape (14:26)     | — |
| `01-sleep-onset*.mp3`                 | Sleep onset (0:32)           | 0:33.00 – 1:04.98 |
| `02-first-deep-sleep*.mp3`            | First deep sleep (0:28)      | 2:43.98 – 3:12.00 |
| `03-first-rem*.mp3`                   | First REM (0:37)             | 3:34.98 – 4:12.00 |
| `04-sustained-rem*.mp3`               | Sustained REM (0:53)         | 6:12.00 – 7:04.98 |
| `05-deep-to-arousal*.mp3`             | Deep sleep → arousal (0:45)  | 12:30.00 – 13:15.00 |
| `06-ending-in-rem*.mp3`               | Ending in REM (0:28)         | 13:52.02 – 14:20.10 |
| `07-full-cycle*.mp3`                  | Full NREM–REM cycle (2:37)   | 4:46.02 – 7:22.98 |

Each excerpt exists in all three renders: no suffix = composition,
`-voices`, `-organ`. The page puts all three in one card so the same moment
can be heard through each model.

## Excerpt loudness

The three renders differ by ~9 LU as delivered (composition −12.2 LUFS,
voices −19.8, organ −21.2). Left alone, A/B-ing them in a single card would
just be a loudness test, so the **excerpts** are matched to **−19 LUFS**,
gain only — no compression, no limiting. −19 rather than a more usual −16
because −16 could not be reached on gain alone: the peakier excerpts hit the
−1 dBTP ceiling first, and capping the gain left some cards 2–3 LU apart.
At −19 every excerpt reaches target exactly; measured spread within a card
is 0.0–0.1 LU, worst true peak −1.70 dBTP, nothing clipping.

**The three full-length pieces are untouched**, still at their delivered
levels, so an excerpt plays quieter than the full work it came from.

## Timeline and stage alignment

Stage boundaries come from `stage_hum` (three-scorer human majority),
10079 epochs at 0.08533 s/epoch = **14:20.075** of scored material.

- **composition** and **voices** are aligned to that timeline from t=0.
  Both files run 14:28; the extra ~8 s is release tail decaying into
  silence, not content.
- **organ** has **2 s trimmed from its head**, so it sits at
  timeline − 2.00 s. Any organ excerpt must subtract 2 s from the times in
  the table above.

Changing the line-up is fine — edit or delete the matching
`<article class="clip">` block in `../index.html`, and keep the `src` and the
download link pointing at the same filename.

## Encoding

Phones on conference wifi, so keep the files small. 128 kbps joint-stereo MP3
is plenty for these textures and gives roughly 1 MB per minute — about 14 MB
for the full composition.

```bash
# One file. Keep the master's own sample rate (48 kHz here) — resampling to
# 44.1 buys nothing and costs a conversion.
ffmpeg -i source.wav -codec:a libmp3lame -b:a 128k -ar 48000 \
       Navigating-Sleep-composition.mp3

# Excerpt: 90 seconds starting at 12:30, with short fades so it doesn't
# start or stop abruptly
ffmpeg -i source.wav -ss 12:30 -t 90 \
       -af "afade=t=in:d=1.5,afade=t=out:st=88.5:d=1.5" \
       -codec:a libmp3lame -b:a 128k -ar 48000 01-wake-to-deep-voice.mp3
```

Cut excerpts from `_masters-320/` (or from the WAV masters, better still) —
not from the published 128k files, which would stack a second generation of
lossy encoding on top of the first.

## `_masters-320/`

The 320 kbps renders live here, gitignored, so excerpts can be re-cut
without hunting for the masters. They are never published; the 128k encodes
beside them are what ships to Pages.

Aim for excerpts of 60–120 seconds: long enough to hear the material develop,
short enough that someone standing at a poster will listen to the end.

## Size limits

Keep any single file well under 100 MB (GitHub rejects files over 100 MB and
warns above 50 MB). At 128 kbps you would need over 100 minutes of audio to
get near that, so this is not a real constraint — but do **not** commit WAV or
AIFF masters here. Those belong outside the repo, or the whole clone gets
heavy and Pages gets slow.
