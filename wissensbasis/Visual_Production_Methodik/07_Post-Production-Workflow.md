# Säule 7 — Post-Production-Workflow

Die letzte Meile entscheidet. Auch ein technisch sauberes Compositing kann durch schlechte Post-Production verlieren. Diese Säule dokumentiert den Editing- und Export-Workflow.

---

## Tool-Stack-Empfehlung

### Profi-Editing-Tools

| Tool | Stärke | Pricing |
|---|---|---|
| **DaVinci Resolve Studio** | All-in-One, beste Color-Tools | $295 einmalig |
| **Adobe Premiere Pro** | Branchenstandard, integriert mit anderen Adobe-Tools | $23/mo |
| **Final Cut Pro** | Mac-only, schnell, intuitiv | $300 einmalig |
| **CapCut Pro (Desktop)** | Schnell, Mobile-Style auf Desktop | $8/mo |

**Empfehlung für In-House-Standard:** **DaVinci Resolve Studio**. Einmal-Kauf, mächtig, professionell, Color-Grading-Tools sind führend.

### Spezialisierte Tools

| Tool | Was es macht |
|---|---|
| **Submagic** | Auto-Untertitel mit Animation |
| **Opus Clip** | Long-Form zu Short-Form (z.B. Podcast zu Reels) |
| **Descript** | Edit-by-Text (Text-Transkript editieren = Video editieren) |
| **Topaz Video AI** | KI-Upscaling, Frame-Interpolation |
| **Boris FX Continuum** | Plug-in-Suite für Effekte |

---

## Editing-Workflow Schritt für Schritt

### Schritt 1: Asset-Import & Organisation

Bevor ihr schneidet, **organisiert die Assets**:

```
Projekt-Ordner/
├── 01_Raw/
│   ├── Live-Aufnahmen/
│   ├── KI-Generierte-Backgrounds/
│   └── Audio/
├── 02_Edits/
│   ├── Cut_1/
│   ├── Cut_2/
│   └── Final/
├── 03_Exports/
│   ├── Instagram/
│   ├── TikTok/
│   └── LinkedIn/
└── 04_Source-Files/
    └── (.drp / .prproj / etc.)
```

Mehr zu Asset-Management in Säule 08.

### Schritt 2: Rough Cut

Erster Durchlauf: **Strukturieren ohne Politur**.

- Alle Clips chronologisch ablegen
- Erste Schnitte machen (lange Clips kürzen, schlechte Takes raus)
- Storyboard-Pacing prüfen (zu lang? zu kurz?)
- Audio grob synchronisieren

Ziel: **Funktioniert die Story?** Polish kommt erst danach.

### Schritt 3: Fine Cut

- Schnitt-Rhythmus präzisieren
- Pattern-Interrupts setzen (siehe unten)
- Übergänge wählen (Hard Cut / Crossfade / J-Cut / L-Cut)
- Text-Overlays positionieren

### Schritt 4: Color Grading

**Zwei Phasen:**

**Phase A — Color Correction (Technical):**
- Belichtung normalisieren
- White-Balance ausgleichen
- Schwächen ausgleichen

**Phase B — Color Grading (Creative):**
- Look-Vision umsetzen (LUT, manuelle Anpassungen)
- Stimmung etablieren
- Konsistenz über Cuts

**Tools:** DaVinci Resolve hat hier die besten Werkzeuge.

### Schritt 5: Audio-Mix

(Siehe Säule 06.)

### Schritt 6: Text-Overlays & Captions

- Brand-Typografie verwenden (siehe Säule 01)
- Position konsistent
- Timing präzise (nicht zu schnell, nicht zu langsam)

### Schritt 7: Untertitel (Pflicht für BFSG)

Auto-Captions als Start, dann manuell prüfen:

- **Auto-Caption-Tools:** Submagic, CapCut, Descript
- **Pflicht-Check:** Sind die Untertitel korrekt? Erkennen sie Eigennamen, Fachbegriffe?
- **Style:** Konsistent zum Brand-Look (Typografie, Position, Farbe)

### Schritt 8: Final Review

- Auf verschiedenen Geräten testen (Smartphone, Desktop)
- Mit und ohne Ton testen
- Plattform-Vorschau mental simulieren

### Schritt 9: Export

Plattform-Specs befolgen (siehe unten).

---

## Schnitt-Rhythmus für Social Video

### Reel / TikTok (15–60 Sek)
- **Hook (0–3 Sek):** 1–2 Cuts max
- **Mittelteil:** Cuts alle 2–4 Sek
- **Auflösung (letzte 3 Sek):** 1–2 Cuts

Schneller Pace hält Aufmerksamkeit. Aber: nicht so schnell, dass nichts mehr verarbeitet werden kann.

### YouTube Short (bis 60 Sek)
- Ähnlich wie Reel, leicht ruhiger erlaubt

### Long-Form YouTube (3+ Min)
- Cuts alle 5–10 Sek
- Bei Talking-Head: Jump Cuts kaschieren mit B-Roll oder Text-Overlay

### Pattern-Interrupts
Aller 3–5 Sek ein Pattern-Interrupt (siehe Hook-Bibliothek im Copywriting-Guide):
- Cut
- Größenänderung
- Bewegung
- Sound-Wechsel

---

## Color Grading-Workflow

### LUT-Setup

Für konsistenten Brand-Look: **Custom LUT** entwickeln (oder kaufen).

**Wie eine LUT entsteht:**
1. Color-Grading auf einem Reference-Clip machen
2. Diesen Look als LUT exportieren
3. LUT auf alle anderen Clips dieser Marke anwenden

**Quellen für vorgefertigte LUTs:**
- **IWLTBAP** (Frei + Premium)
- **RocketStock** (Premium)
- **Color Grading Central** (Profi-LUTs)
- **Filmmaker Looks** (verschiedene Cinema-Looks)

### Grading-Workflow in DaVinci

1. **Primary Correction:** Belichtung, White Balance pro Clip
2. **Apply LUT** als Basis
3. **Secondary Grade:** Spezifische Anpassungen (z.B. Skin Tones)
4. **Power Windows** für lokale Anpassungen (z.B. nur das Gesicht etwas heller)
5. **Final Look:** Letzter Schliff, Vignette, Grain

### Konsistenz-Check
Alle Clips parallel scrollen — wirken sie wie eine Familie? Wenn nicht: Grade nachschärfen.

---

## Plattform-Specs für Export

### Instagram Reel

- **Format:** MP4 / MOV
- **Codec:** H.264
- **Auflösung:** 1080 × 1920 px (9:16)
- **Framerate:** 30 oder 60 fps (60 für smooth motion)
- **Bitrate:** 5–10 Mbps
- **Audio:** AAC 128–256 kbps
- **Länge:** Max 90 Sek (für volle Distribution)

### TikTok

- **Format:** MP4
- **Auflösung:** 1080 × 1920 px (9:16)
- **Framerate:** 30 fps Standard
- **Bitrate:** 5–10 Mbps
- **Audio:** AAC, ~128 kbps
- **Länge:** 15–60 Sek Sweet Spot

### YouTube Short

- **Format:** MP4
- **Auflösung:** 1080 × 1920 px (9:16) oder 1920 × 1080 (16:9 für Standard)
- **Framerate:** 30 fps (60 fps optional)
- **Bitrate:** 8–15 Mbps
- **Audio:** AAC, 128–384 kbps
- **Länge:** Bis 60 Sek für Shorts

### LinkedIn Video

- **Format:** MP4
- **Auflösung:** 1080 × 1920 (vertikal) oder 1920 × 1080 (horizontal)
- **Framerate:** 30 fps
- **Bitrate:** 5–10 Mbps
- **Audio:** AAC
- **Länge:** 30 Sek bis 10 Min (3 Min Sweet Spot)

### Instagram Story

- **Format:** MP4
- **Auflösung:** 1080 × 1920 px
- **Länge:** 15 Sek pro Card
- **Audio:** Optional

### Instagram Feed (Carousel-Video)

- **Format:** MP4
- **Auflösung:** 1080 × 1350 (4:5) oder 1080 × 1080 (1:1)
- **Länge:** 3–60 Sek

---

## Mehrere Versionen exportieren

Aus einem Master-Edit oft **mehrere Plattform-Versionen** exportieren:

| Master | Versionen |
|---|---|
| **9:16 vertical, 60 Sek** | IG Reel, TikTok, YouTube Short |
| **1:1 quadratisch, 30 Sek** | IG Feed, Facebook |
| **16:9 horizontal, 60 Sek** | LinkedIn, YouTube, Website |
| **9:16 vertikal, 15 Sek (Story-Cut)** | IG Story, IG Highlight |

Editing-Tools wie Premiere haben „Auto Reframe"-Funktionen, die das automatisch machen können. Aber: Immer manuell prüfen.

---

## Export-Workflow

### Schritt 1: Master-Export
- Höchste Qualität, ProRes oder H.264 mit hoher Bitrate
- Als Master-Datei speichern (für spätere Anpassungen)

### Schritt 2: Plattform-Versionen
- Pro Plattform exportieren mit den jeweiligen Specs (siehe oben)
- Naming: `Projekt_Plattform_Version.mp4`

### Schritt 3: Plattform-Upload
- Vorschau auf der Plattform prüfen (oft sieht Plattform-Vorschau anders aus als lokal)
- Captions/Hashtags/Cover-Image (Reel) ergänzen

---

## Performance-Optimierung für Algorithmen

Über die reine technische Spec hinaus gibt es Plattform-Algorithmen-Tricks:

### Cover Image (Thumbnail)
- **Instagram Reel:** Eigenes Cover hochladen, nicht Frame 1 nehmen lassen
- **YouTube Short:** Cover kommt aus dem Video, also Anfang stark gestalten
- **TikTok:** Eigener Thumbnail-Frame wählen

### Loop-Fähigkeit
Wenn Ende und Anfang nahtlos zusammenpassen, läuft das Video oft mehrfach durch → bessere Watch-Time → bessere Algorithm-Signale.

### Hook-Optimization
Die ersten 0–2 Sek müssen sofort funktionieren — sonst wird weggescrollt. Das ist Editing-Arbeit, nicht nur Konzept.

### Audio-On Optimization
Wenn 20 % der Audience mit Ton schaut, ist deren Engagement höher gewichtet. Sound muss attraktiv genug sein, um Hand-zum-Lautstärke zu triggern.

---

## Häufige Post-Production-Fehler

| Fehler | Symptom | Korrektur |
|---|---|---|
| **Kein Color Grading** | Material wirkt unzusammenhängend | LUT-basiertes Grading pro Kampagne |
| **Auto-Captions ohne Prüfung** | Falsche Wörter, peinliche Errors | Manuelle Caption-Korrektur Pflicht |
| **Plattform-Specs ignoriert** | Komprimierung, Qualitäts-Verlust | Pro Plattform separater Export |
| **Master-File überschrieben** | Spätere Anpassungen unmöglich | Master immer separat sichern |
| **Cover nicht definiert** | Algorithmus wählt schlechten Frame | Manuelles Cover für Reel/Short |
| **Audio-Loudness ignoriert** | Plattform-Algorithm normalisiert ungünstig | -14 LUFS Standard |
| **Schnitt zu schnell** | Verarbeitungsstress, geringe Watch Time | Min 1.5 Sek pro Cut bei komplexer Info |
| **Schnitt zu langsam** | Aufmerksamkeit verloren | Max 4 Sek pro Cut im Mittelteil |

---

## Post-Production-Checkliste

### Vor Export
- [ ] Color Grading auf allen Clips konsistent
- [ ] Audio-Mix nach Säule 06
- [ ] Untertitel manuell geprüft (BFSG)
- [ ] Text-Overlays brand-konform
- [ ] Cover/Thumbnail definiert
- [ ] Hook in ersten 2 Sek getestet
- [ ] Loop-Fähigkeit geprüft (wo sinnvoll)

### Export pro Plattform
- [ ] Plattform-Spec eingehalten
- [ ] Master-Datei separat gesichert
- [ ] Naming konsistent

### Vor Upload
- [ ] Plattform-Vorschau geprüft
- [ ] Caption + Hashtags vorbereitet
- [ ] Cover/Thumbnail definiert
- [ ] Posting-Zeit gewählt
