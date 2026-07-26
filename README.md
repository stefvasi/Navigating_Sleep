# Navigating Sleep

**Neural Audio Synthesis as Compositional Medium for EEG Data Sonification**

Presented at **ICAD 2026**, the International Conference on Auditory Display.

Stefanos Vasilakis¹, Areti Andreopoulou², Thanos Polymeneas Liontiris²
¹ Intelligent Instruments Lab / ACUTE Research Lab, University of Iceland
² Laboratory of Music Acoustics and Technology (LabMAT), National and
Kapodistrian University of Athens

## 🎧 Listen

**<https://stefvasi.github.io/Navigating_Sleep/>**

Audio excerpts and the full composition, playable in a phone browser.

## What this is

A practice-based artistic research project in data-driven composition. EEG
bandpower from one night of sleep navigates the latent spaces of three RAVE
models; the scored sleep stages act as symbolic signifiers deciding which
electrode-and-model combinations are audible at any point in the night.

The pipeline, in short:

1. **Source** — one night from the Bitbrain Open Access Sleep dataset.
2. **Features** — Welch periodogram → power spectral density → five bandpower
   values (Delta, Theta, Alpha, Sigma, Beta) per 2.56-second epoch.
3. **Flattening** — each band is weighted to lift the faster rhythms out from
   under the 1/f aperiodic slope, which Delta would otherwise dominate.
4. **Reduction** — principal component analysis per electrode gives the
   control signals.
5. **Synthesis** — those signals steer the latent spaces of three RAVE models
   (**voice**, **organ**, **modular**) at 48 kHz with a 2048-sample block,
   about a 23.44 Hz control rate. All audio is generated unconditionally — no
   audio is fed to the encoders.
6. **Time** — 2.56-second epochs transmitted every 0.0853 s: a 30:1
   compression that fits a full night into roughly 14 minutes.

## Repository layout

```
docs/            The public listen page (GitHub Pages serves this at the root URL)
  index.html     Self-contained — no build step, no framework, no CDN
  audio/         Audio files (see docs/audio/README.md for names and encoding)
  img/           Explanatory graphic (see docs/img/README.md)
```

Project code lives alongside `docs/` in this repository.

## Publishing the page

GitHub Pages is configured as **Settings → Pages → Source: Deploy from a
branch → `main` / `/docs`**. Push to `main` and the site rebuilds in about a
minute.

To preview locally before pushing:

```bash
python3 -m http.server 8000 --directory docs
# then open http://localhost:8000/
```

## ⚠️ Do not rename this repository

A printed conference poster carries QR codes baked to these exact strings:

- `https://stefvasi.github.io/Navigating_Sleep/` (listen page)
- `https://github.com/stefvasi/Navigating_Sleep` (this repository)

Both are **case-sensitive** and neither can be changed once the poster is
printed. Renaming the repository, renaming the account, or switching the Pages
source away from `/docs` will break the QR codes at the conference. GitHub does
redirect renamed repositories, but that redirect does not reliably cover the
`github.io` Pages URL — so treat the name as fixed.

## Citation

> Vasilakis, S., Andreopoulou, A., & Polymeneas Liontiris, T. (2026).
> *Navigating Sleep: Neural Audio Synthesis as Compositional Medium for EEG
> Data Sonification.* Proceedings of the International Conference on Auditory
> Display (ICAD 2026).
