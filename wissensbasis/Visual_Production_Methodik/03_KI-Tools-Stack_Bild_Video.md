# Säule 3: KI-Tools-Stack (Bild + Video)

**Wichtiger Hinweis:** Diese Säule ist die mit der **kürzesten Halbwertszeit** in der gesamten Guideline. KI-Tools entwickeln sich monatlich. Stand: Mai 2026. Refresh halbjährlich Pflicht.

Diese Säule dokumentiert die aktuelle Tool-Landschaft, mit konkreten Empfehlungen für In-House-Workflow in 2 bis 5-Personen-Teams.

---

## Grundprinzip: Mehrere Tools, je nach Use Case

Es gibt 2026 kein „bestes Tool". Es gibt **das beste Tool für den konkreten Use Case**. Die Profis nutzen meistens 2 bis 3 Tools parallel.

> „Rather than choosing a single tool, the professionals producing the best AI-generated imagery in 2026 use all three, or at least two, matching each tool to its strength."

---

## KI-Bild-Tools (Stand Mai 2026)

### Übersicht der Markt-Führer

| Tool | Stärke | Preis | Beste für |
|---|---|---|---|
| **Midjourney V7** | Aesthetic, artistic stylization | $30 bis 120/mo | Kampagnen-Hero-Visuals, künstlerische Konzepte |
| **Flux 2 Pro** | Photorealism, Allrounder | $0.06 bis 0.08/image | Produkt-/Personen-Fotorealismus, Standard-Workhorse |
| **Ideogram 3** | Text in image, Typography | $20/mo Plus | Plakate, Marketing-Materialien mit Text |
| **Imagen 4** (Google) | Product photography, Text-Rendering | API-basiert | Produkt-Shots, Werbe-Bildwelten |
| **DALL-E 4 / GPT Image 2** | Accessibility, abstract concepts | mit ChatGPT Plus | Abstrakte Konzepte, schnelle Iteration |

### Detail-Empfehlung pro Tool

**Midjourney V7**
- Pricing: $10/mo (Basic) bis $120/mo (Mega). **Realistische Pro-Nutzung: $60/mo (Pro)**
- Stärken: Beste künstlerische Anmutung, sehr starke Style-Kohärenz
- Schwächen: Kein API-Zugriff für API-Workflow, schwach bei Text-im-Bild
- Workflow: Discord-Server oder Web-Interface
- Wann nutzen: Wenn Aesthetic > Realismus, wenn Hero-Visuals, wenn Editorial-Look

**Flux 2 Pro**
- Pricing: pay-per-image, $0.06 bis 0.08/image
- Stärken: Photorealismus auf Spitzen-Niveau, gute Character-Konsistenz, API-Zugriff
- Schwächen: weniger künstlerisch als Midjourney
- Workflow: Über Provider wie Replicate, fal.ai, oder direkter API-Zugriff
- Wann nutzen: Standard-Production, Personen-Bilder, Produkt-Shots

**Ideogram 3**
- Pricing: $20/mo Plus (1.000 Credits)
- Stärken: Beste Text-in-Image-Generierung (Logos, Plakate, Captions)
- Schwächen: weniger fotorealistisch als Flux
- Wann nutzen: Wenn Text auf dem Bild stehen soll

### Tool-Stack-Empfehlung für In-House-Team

**Minimum-Stack (Solo-Creator):**
- **1 Tool:** Flux 2 Pro über fal.ai oder Replicate (~$50/mo nach Volumen)
- Gesamtkosten: $50/mo

**Standard-Stack (2 bis 5-Personen-Team):**
- **Midjourney V7 Pro** ($60/mo) für Aesthetic-Visuals
- **Flux 2 Pro** über Provider ($50 bis 100/mo nach Volumen)
- **Ideogram 3 Plus** ($20/mo) für Text-Bilder
- Gesamtkosten: ~$130 bis 180/mo

**Advanced-Stack (Volle Produktion):**
- Standard-Stack +
- **GPT Image 2 / DALL-E 4** ($20/mo via ChatGPT Plus) für Brainstorming
- Gesamtkosten: ~$150 bis 200/mo

---

## KI-Video-Tools (Stand Mai 2026)

### Übersicht der Markt-Führer

| Tool | Stärke | Preis | Beste für |
|---|---|---|---|
| **Veo 3.1** (Google) | Allrounder, native Audio, 4K | $0.15/sec | Narrative Szenen, Establishing Shots, Produkt-Visualisierung |
| **Kling 3.0** | Cinematic, multi-shot consistency | ~$0.10/sec | Cinematic-Stories, mehrere Cuts mit derselben Person |
| **Runway Gen-4.5** | Granular Control, Camera Moves | Credit-basiert | Spezialeffekte, Motion Brush, Reference-driven |
| **Higgsfield** | Multi-Tool-Hub | pay-as-you-go | Wenn ihr Veo/Kling/Seedance an einer Stelle nutzen wollt |
| **Sora 2** (OpenAI) | Story-led | $0.75/sec | **ACHTUNG: Wird im September 2026 eingestellt** |
| **Seedance 2.0** | Image-to-Video | API-basiert | Wenn ihr ein Standbild animieren wollt |

### Detail-Empfehlung pro Tool

**Google Veo 3.1**
- Pricing: $0.15/sec (Fast Mode), höher für Premium
- Stärken: Bestes Audio (native 48kHz synchronisierte Dialoge), starke Prompt-Adherence, 4K-Output
- Schwächen: relativ teuer
- Wann nutzen: Wenn Audio synchron sein muss, wenn Premium-Look gefordert, wenn narrativ

**Kling 3.0**
- Pricing: ca. $0.10/sec, **das günstigste Premium-Modell 2026**
- Stärken: Cinematic lighting, komplexe Bewegung (Haar, Flüssigkeiten, Stoff), Multi-Shot mit Subject Consistency
- Schwächen: Audio-Sync etwas schwächer als Veo
- Wann nutzen: Standard-Cinematic-Workhorse, mehrteilige Story-Reels

**Runway Gen-4.5**
- Pricing: Credit-Subscription (vorhersehbarer als per-second)
- Stärken: Granular Control, Motion Brush, Reference-driven Character Consistency
- Schwächen: weniger fotorealistisch als Veo/Kling
- Wann nutzen: Wenn ihr genaue Kontrolle braucht (Kamera-Moves, spezifische Bewegung)

**Higgsfield**
- Pricing: pay-as-you-go über Hub
- Stärken: Multi-Tool an einer Stelle (Veo, Kling, Seedance, Pika unter einem Account)
- Schwächen: Aufschlag auf Tool-Preise
- Wann nutzen: Wenn ihr nicht für jedes Tool eine eigene Subscription wollt

**Sora 2 (Auslaufmodell)**
- Pricing: $0.75/sec
- **Wichtig:** Sora Web/App wird am 26. April 2026 eingestellt, API am 24. September 2026
- Wann nutzen: Aktuell nicht mehr empfohlen für neue Workflows

### Tool-Stack-Empfehlung für In-House-Team

**Minimum-Stack (Video-Anfänger):**
- **1 Tool:** Kling 3.0 (~$50 bis 100/mo nach Volumen)
- Gesamtkosten: $50 bis 100/mo

**Standard-Stack (regelmäßige Reel-Produktion):**
- **Veo 3.1** für Hero-Cuts (~$100/mo nach Volumen)
- **Kling 3.0** für Standard-Cuts (~$50/mo)
- **Runway Gen-4.5** für Spezial-Effekte (subscription)
- Gesamtkosten: ~$200 bis 300/mo

**Advanced-Stack (intensive Produktion):**
- Standard-Stack +
- **Higgsfield** als Aggregator-Backup
- **Seedance 2.0** für Image-to-Video-Animationen
- Gesamtkosten: ~$300 bis 500/mo

---

## Verwandte Tools (Bild- und Video-Bearbeitung)

Über die reinen Generierungs-Tools hinaus:

### Bild-Bearbeitung

| Tool | Beste für | Preis |
|---|---|---|
| **Adobe Photoshop + Firefly** | Profi-Bearbeitung, Generative Fill | $23/mo Creative Cloud |
| **Krea AI** | Real-Time-Generation, Image Enhancement | $35/mo Pro |
| **Magnific** | Upscaling, Detail-Verbesserung | $39+/mo |
| **Photoroom** | Background-Removal, Produkt-Shots | $13/mo Pro |

### Video-Bearbeitung (KI-erweitert)

| Tool | Beste für | Preis |
|---|---|---|
| **Adobe Premiere + Firefly** | Profi-Editing mit KI-Enhancements | $23/mo |
| **CapCut Pro** | Mobile/Schnell-Editing mit KI-Features | $8/mo |
| **DaVinci Resolve Studio** | Color Grading, Professional | Einmalig $295 |
| **Descript** | Audio-zu-Text, Edit-by-Text | $24/mo Creator |
| **Opus Clip** | Long-Form zu Short-Form | $20/mo |
| **Submagic** | Auto-Captions, Highlight-Effekte | $25/mo |

---

## Tool-Auswahl-Kriterien

Bei Tool-Wechsel oder Neueinführung prüfen:

### Kriterium 1: Output-Qualität
- Macht der Output das, was ihr braucht? (Aesthetic / Photorealistic / Cinematic)
- Wie konsistent über mehrere Generierungen?

### Kriterium 2: Workflow-Integration
- API-Zugriff? (für Automatisierung)
- Web-Interface oder nur Discord (Midjourney historisch)
- Plug-in für eure Editing-Software?

### Kriterium 3: Kosten-Modell
- Per-Image / per-Sec (variabel mit Volumen)
- Subscription (vorhersehbar, aber bezahlt auch bei Nicht-Nutzung)
- Pay-as-you-go vs. Credit-Pakete

### Kriterium 4: Lizenz / Rechte
- Kommerzielle Nutzung erlaubt? (Bei den meisten Premium-Tools ja, bei Free-Versions oft nein)
- Wer hält die Rechte am Output?
- DSGVO-konform für eure Branche?

### Kriterium 5: Lernkurve
- Wie steil ist die Lernkurve?
- Welche Tutorials / Communities gibt es?
- Wie gut ist die Dokumentation?

### Kriterium 6: Update-Frequenz
- Wie oft kommen neue Features?
- Wie stabil sind bisherige Features (Breaking Changes)?
- Wie vertrauensvoll ist der Anbieter?

---

## Workflow-Beispiele

### Beispiel 1: Carousel-Produktion (7 Slides)

1. **Concept** (Säule 02) → konkrete Bild-Briefings für 7 Slides
2. **Cover-Slide:** Midjourney V7 (Aesthetic-Hero)
3. **Slides 2 bis 6:** Flux 2 Pro (Photorealistic, mit Character Consistency)
4. **Text-Slides (Daten-Overlays):** Ideogram 3 oder direkt in Figma
5. **Editing:** Figma oder Photoshop für letzten Schliff
6. **Export:** Plattform-Spezifika (siehe Säule 07)

### Beispiel 2: Reel-Produktion (20 Sek mit Hybrid-Workflow)

1. **Concept + Storyboard** (Säule 02)
2. **Live-Aufnahme** (echte Person, Greenscreen oder einfacher Hintergrund), Smartphone reicht
3. **Background-Generierung:** Veo 3.1 oder Kling 3.0 für KI-Hintergrund-Clips (5 × 4 Sek)
4. **Compositing:** Runway Green Screen oder DaVinci Magic Mask
5. **Editing + Audio:** Premiere Pro oder DaVinci
6. **Captions:** Submagic für Auto-Untertitel
7. **Final Export:** Plattform-Spezifika

### Beispiel 3: Daily Content (Single-Image-Post)

1. **Schnell-Briefing** (15 Min, siehe Säule 02)
2. **Bild-Generierung:** Flux 2 Pro über fal.ai (1 bis 3 Generationen)
3. **Schneller Edit:** Photoroom für Hintergrund, Photoshop für Feintuning
4. **Post:** Direkt in Plattform-Scheduler

---

## Häufige Tool-Fehler

| Fehler | Symptom | Korrektur |
|---|---|---|
| **Nur 1 Tool nutzen** | Output sieht aus wie jeder andere, der dasselbe Tool nutzt | Mindestens 2 Tools im Stack, je nach Use Case |
| **Tools wechseln, ohne Look anzupassen** | Inkonsistenz über Posts | Look-Konsistenz (Säule 04) ist Tool-übergreifend |
| **Free-Versionen für kommerzielle Arbeit** | Lizenz-Verstöße | Pro-Lizenzen für alle Tools mit kommerziellem Output |
| **Tools-Aktualität ignorieren** | Verpasste Features, höhere Kosten | Halbjährliches Tool-Review |
| **Nur API, kein Web-UI** | Lange Lernkurve, schwere Iteration | Mix aus API (Bulk) + UI (Iteration) |

---

## Empfehlung für Mai-2026-Start

Wenn ihr **jetzt** einsteigt, empfehle ich:

**Bild:**
- **Flux 2 Pro** über fal.ai oder Replicate (Hauptwerkzeug)
- **Midjourney V7 Pro** für Aesthetic-Hero (zweite Linie)
- **Ideogram 3 Plus** wenn Text-in-Image relevant

**Video:**
- **Kling 3.0** als Hauptwerkzeug (günstigstes Premium)
- **Veo 3.1** für Hero-Cuts mit Audio
- **Runway Gen-4.5** für Spezial-Kontrolle bei Bedarf

**Bearbeitung:**
- **DaVinci Resolve Studio** (Einmalig $295), Full-Profi-Editing
- **CapCut Pro** für Mobile-First-Workflows
- **Submagic** für Auto-Captions

**Asset-Management:**
- Notion + Drive / Dropbox (siehe Säule 08)

**Gesamtkosten:** ca. $200 bis 350/mo + einmalig $295 für DaVinci.

Refresh dieser Empfehlung halbjährlich.
