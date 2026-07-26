# Audio for the listen page

Drop the finished files in this folder using **these exact filenames** — the
page already points at them, so nothing in `index.html` needs editing. Each
player's "Coming soon" notice disappears by itself once its file is present.

| Filename                      | Clip on the page      |
|-------------------------------|-----------------------|
| `01-wake-to-deep-voice.mp3`   | Wake → deep sleep (voice model) |
| `02-rem-modular-voice.mp3`    | REM (modular + voice models)    |
| `03-organ-soundscape.mp3`     | Organ soundscape (organ model)  |
| `04-full-composition.mp3`     | The full composition (~14:20)   |

Changing the line-up is fine — edit or delete the matching
`<article class="clip">` block in `../index.html`, and keep the `src` and the
download link pointing at the same filename.

## Encoding

Phones on conference wifi, so keep the files small. 128 kbps joint-stereo MP3
is plenty for these textures and gives roughly 1 MB per minute — about 14 MB
for the full composition.

```bash
# One file
ffmpeg -i source.wav -codec:a libmp3lame -b:a 128k -ar 44100 04-full-composition.mp3

# Excerpt: 90 seconds starting at 12:30, with short fades so it doesn't
# start or stop abruptly
ffmpeg -i source.wav -ss 12:30 -t 90 \
       -af "afade=t=in:d=1.5,afade=t=out:st=88.5:d=1.5" \
       -codec:a libmp3lame -b:a 128k -ar 44100 01-wake-to-deep-voice.mp3
```

Aim for excerpts of 60–120 seconds: long enough to hear the material develop,
short enough that someone standing at a poster will listen to the end.

## Size limits

Keep any single file well under 100 MB (GitHub rejects files over 100 MB and
warns above 50 MB). At 128 kbps you would need over 100 minutes of audio to
get near that, so this is not a real constraint — but do **not** commit WAV or
AIFF masters here. Those belong outside the repo, or the whole clone gets
heavy and Pages gets slow.
