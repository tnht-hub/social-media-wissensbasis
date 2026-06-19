# Säule 5: Hybrid-Produktion: Echte Person + KI-Background

Die zuverlässigste Methode für 2026, wenn ihr Personen in der Marke zeigen wollt: **Echte Person live filmen, Hintergrund per KI ersetzen.**

Lippenbewegung, Mikro-Mimik, Augenbewegung bleiben echt. Setting wird kontrollierbar. Das löst die größten Schwächen reiner KI-Personenvideos.

Diese Säule dokumentiert den Hybrid-Workflow.

---

## Warum Hybrid statt rein KI?

Rein KI-generierte Personen-Videos haben 2026 noch erkennbare Schwächen:

- **Lippensynchronisation** wirkt oft minimal künstlich
- **Augenbewegungen** sind weniger lebendig
- **Mikro-Mimik** (Stirnfalten, Lächeln-Kanten) zu glatt
- **Hände** und feine Details oft fehlerhaft
- **Charakter-Konsistenz** über mehrere Cuts riskant

Das alles **fliegt bei Late-Gen-Z-Zielgruppen oft auf**, und macht die Marke unecht.

Reine Live-Produktion ohne KI-Hilfe hat andere Nachteile:
- Setting (z.B. Offshore-Plattform, Nordsee) ist teuer/aufwendig
- Logistik, Genehmigungen, Wetter-Abhängigkeit
- Geringere Flexibilität bei Konzept-Änderungen

**Hybrid kombiniert die Stärken:** Authentische Person + flexible, kontrollierbare Umgebung.

---

## Hybrid-Workflow im Überblick

| Schritt | Was passiert | Dauer (pro Reel/Spot) |
|---|---|---|
| **1. Pre-Production** | Storyboard + Shotlist + Background-Briefing | 1 bis 2 Tage |
| **2. Live-Aufnahme** | Person filmen vor Greenscreen oder einfachem Hintergrund | 0.5 Tage |
| **3. Background-Generierung** | KI generiert passende Backgrounds | 0.5 bis 1 Tag |
| **4. Compositing** | Person und Background zusammenfügen | 0.5 bis 1 Tag |
| **5. Light-Matching & Color** | Lichtangleichung, Farb-Grading | 0.5 Tag |
| **6. Final Edit + Audio** | Schnitt, Audio, Captions | 0.5 Tag |

**Gesamt: 4 bis 6 Tage pro Reel** bei mittlerer Komplexität.

---

## Schritt 1: Pre-Production für Hybrid-Workflow

### Wichtigste Entscheidung VOR dem Dreh: Licht

Lichtmatching ist **die häufigste Schwachstelle** im Compositing. Wenn die Person im Studio mit Frontallicht gefilmt wird, das KI-Background aber Seitenlicht von rechts zeigt, wirkt es sofort falsch.

**Pre-Production-Pflicht:**
1. KI-Background-Look festlegen (Licht-Richtung, -Farbe, -Härte)
2. Studio-Setup entsprechend planen
3. Test-Shot vorab, um Match zu prüfen

### Background-Briefing für KI-Generierung

```markdown
# KI-Background-Briefing

## Szene
[Was wird gezeigt? z.B. "Nordsee-Plattform, 30 km vor der Küste"]

## Bildausschnitt
- Wie weit ist die Kamera von der Person entfernt (für Perspektive)?
- Welcher Bildwinkel (weit / normal / nah)?
- Vordergrund / Mitte / Hintergrund, was ist in welcher Tiefenebene?

## Licht
- Lichtrichtung: [z.B. seitlich von rechts]
- Lichtfarbe: [z.B. kühl-blau, bewölkt]
- Lichthärte: [z.B. diffus]
- Tageszeit: [z.B. Vormittag]

## Bewegung (Video)
- Statisch / leichte Drohnen-Bewegung / starke Bewegung?
- Welche Richtung?
- Welches Tempo?

## Atmosphäre
- Wetter:
- Stimmung:
- Detail-Elemente (Spray, Möwen, Wellen, etc.):

## Style
- Referenz-Look (siehe Säule 01):
- Color Mood:
```

---

## Schritt 2: Live-Aufnahme

### Setup-Optionen

**Option A: Greenscreen-Studio**
- Klassisch, beste Compositing-Qualität
- Voraussetzung: gleichmäßig ausgeleuchteter grüner Hintergrund
- Person mindestens 1.5 m vom Greenscreen entfernt (Spill-Vermeidung)

**Option B: Bluescreen**
- Wenn Person grüne Kleidung trägt
- Sonst wie Greenscreen

**Option C: Einfacher neutraler Hintergrund (kein Greenscreen)**
- Hellgrau oder schwarz
- KI-Tools wie Runway oder DaVinci Magic Mask können auch ohne Greenscreen freistellen
- Schneller im Setup, höhere Post-Production-Aufwand

**Option D: Echter Hintergrund mit AI-Erweiterung**
- Person vor halb-realem Setting filmen, dann KI nur ergänzt / erweitert
- Beste Authentizität, aber komplexes Compositing

### Lichtsetup-Standards

Für Compositing-tauglichen Dreh:

**Key Light (Hauptlicht)**
- Aus der Richtung, die dem KI-Background entspricht
- Diffuse Softbox bevorzugt (außer wenn hart-licht Szene)
- Farbtemperatur passend zum Background (warm / kalt)

**Fill Light**
- Schwächer als Key, von der gegenüberliegenden Seite
- Reduziert harte Schatten

**Rim Light (Backlight)**
- **Pflicht** für sauberes Compositing!
- Macht die Kante der Person sichtbar, vermeidet „ausgeschnitten" wirkenden Look
- Eine LED-Tube hinter der Person reicht

**Hintergrund-Licht (bei Greenscreen)**
- Greenscreen separat ausleuchten (gleichmäßig)
- Sonst entstehen Schatten, die das Keying erschweren

### Wind, Bewegung, Atmosphäre

KI kann den Hintergrund machen, aber **Wind im Haar, Bewegung der Kleidung, echte Mimik** sind live nötig:

- **Standventilator** für Haare/Kleidung (wichtig wenn Outdoor-Setting im Background)
- **Person darf sich natürlich bewegen**, Compositing kommt damit klar
- **Vordergrund-Elemente live mitnehmen**, wenn möglich (Stahlrelief, Halme, etc.)

### Kamera-Setup

| Aspekt | Empfehlung |
|---|---|
| **Auflösung** | Mindestens 4K (Spielraum für Crop und Stabilisierung) |
| **Framerate** | 60fps (Spielraum für Slow-Motion-Cuts) |
| **Format** | LOG-Profil wenn möglich (mehr Color-Grading-Spielraum) |
| **Verschluss** | 1/50 oder 1/60 (für natural motion blur) |
| **Stabilisierung** | Stativ oder Gimbal, Handheld nur bewusst |

**Smartphone reicht** für viele Anwendungen, moderne iPhones (15+) und Samsung Galaxy S24+ haben 4K/60fps + LOG-Optionen.

---

## Schritt 3: Background-Generierung mit KI

### Tool-Empfehlungen für Backgrounds

| Tool | Beste für |
|---|---|
| **Veo 3.1** | Cinematic Backgrounds mit nativer Audio-Atmo |
| **Kling 3.0** | Cinematic Backgrounds, mehrere Cuts mit kohärentem Look |
| **Runway Gen-4.5** | Backgrounds mit spezifischer Kamera-Bewegung |
| **Higgsfield** | Wenn mehrere Modelle parallel verglichen werden sollen |

### Prompt-Strategie

Background-Prompts sollten **bewusst Person-frei** sein, damit die KI Vordergrund-Platz für die echte Person lässt:

**Schwach:**
> „Eine Frau auf einer Offshore-Plattform"

**Stark:**
> „Empty offshore wind farm platform, view from approximately 30 km offshore, soft side lighting from upper right, overcast sky, calm sea, very slight drone movement, cinematic color grade, leave foreground space empty for compositing"

Wichtig:
- **„Leave foreground space empty"** oder Equivalent, sonst füllt KI den Vordergrund mit Personen/Objekten
- **Lichtbeschreibung explizit**, passend zum Live-Light-Setup
- **Kamera-Bewegung explizit**, statisch oder leichte Bewegung; sonst kann es problematisch sein

### Längen-Strategie für Video

KI-Video-Tools generieren oft nur 4 bis 8 Sek pro Clip. Für längere Reels:

- Storyboard so planen, dass max. 4 bis 8 Sek pro Background-Clip nötig sind
- Cuts zwischen verschiedenen Backgrounds
- Bei langsamen Szenen: 4 Sek Clip mit leichter Bewegung loopen

---

## Schritt 4: Compositing

### Tools für Compositing

| Tool | Beste für | Preis |
|---|---|---|
| **DaVinci Resolve (Studio), Magic Mask** | Profi-Standard für Greenscreen + AI-Masken | Einmalig $295 |
| **Runway ML, Green Screen** | Sehr akkurat besonders bei komplexem Haar | Subscription |
| **Beeble** | Spezialisiert auf AI-Video-Compositing | Subscription |
| **Adobe Premiere + Roto Brush** | Wenn ihr eh Adobe nutzt | Creative Cloud |
| **CapCut Pro, Background Removal** | Mobile/Schnell-Compositing | $8/mo |

**Empfehlung für In-House-Standard:** DaVinci Resolve Studio. Einmal-Kauf, mächtig, professionell.

### Compositing-Workflow

1. **Foreground-Layer:** Live-Aufnahme der Person, freigestellt (Greenscreen-Key oder AI-Mask)
2. **Background-Layer:** KI-generiertes Video
3. **Edge Refinement:** Saubere Kante (Spill-Reduktion, Edge-Feathering)
4. **Light-Matching:** Light Wrap (Background-Licht „greift über" auf die Person)
5. **Color-Matching:** Foreground-Farben an Background anpassen
6. **Motion-Matching:** Wenn Background-Bewegung hat, Foreground entsprechend animieren

### Häufige Compositing-Probleme

| Problem | Ursache | Lösung |
|---|---|---|
| **Person wirkt „ausgeschnitten"** | Kein Rim Light beim Dreh | Light Wrap in Post hinzufügen |
| **Greenscreen-Spill auf Person** | Greenscreen zu nah an Person | Spill-Reduktion (DaVinci, Runway) |
| **Kantenflimmern bei Bewegung** | Schwache Mask-Stabilität | Multi-Frame-Refinement, manuelles Rotoscoping bei kritischen Frames |
| **Farben passen nicht** | Color-Grading vergessen | Background und Foreground in derselben Color-Grade-Stufe matchen |
| **Schärfentiefe unterschiedlich** | Foreground scharf, Background unscharf (oder andersrum) | In Post Schärfentiefe anpassen (Lens Blur Tool) |

---

## Schritt 5: Light-Matching & Color

Hier wird **die Plausibilität** gemacht. Selbst technisch sauberes Compositing wirkt falsch, wenn Licht und Farben nicht passen.

### Light Wrap

Eine Technik, bei der Licht aus dem Background **„über die Kante der Person greift"**. Das simuliert, dass das Umgebungslicht die Person beleuchtet.

- In DaVinci: über „Light Wrap" Node im Compositing
- In Premiere: Plug-ins wie „Composite Brush" oder manuell mit Inner Glow
- Schwach einstellen (oft 5 bis 15 %), nicht übertreiben

### Color Matching

Background hat oft eine bestimmte Color Mood (z.B. teal-orange Cinematic). Person muss in derselben Mood landen.

**Workflow:**
1. Background Color-Grade machen (LUT anwenden)
2. **Dieselbe** LUT auf Person anwenden
3. Letzter Schliff: Foreground-Farben manuell an Background-Farbpalette annähern

### Schatten

Wenn die Background-Szene gerichtetes Licht hat, sollte die Person einen **Schatten werfen**, passend zur Lichtrichtung:

- Soft Drop Shadow unter den Füßen
- Bei Sonneneinstrahlung: hinter der Person nach passender Seite

Fehlende Schatten sind eines der häufigsten „dieses Compositing wirkt falsch"-Signale.

---

## Schritt 6: Final Edit + Audio

Wie bei jeder Video-Produktion:
- Schnitt-Rhythmus (siehe Säule 07)
- Audio (siehe Säule 06)
- Text-Overlays
- Untertitel (Pflicht nach BFSG, siehe Säule 09)
- Export-Specs pro Plattform (siehe Säule 07)

---

## Smartphone-Workflow (vollständige In-House-Variante)

Wenn ihr kein Studio habt:

1. **Aufnahme:** iPhone 15 Pro+ oder Samsung Galaxy S24+ in 4K/60fps, LOG-Profil
2. **Hintergrund:** Möglichst einfache, gleichmäßige Wand (hellgrau, kein Greenscreen nötig)
3. **Licht:** Tageslicht vom Fenster + LED-Panel als Rim Light
4. **Compositing:** Runway ML Green Screen oder DaVinci Resolve Magic Mask
5. **Background-Generierung:** Kling 3.0 oder Veo 3.1
6. **Edit:** DaVinci Resolve oder CapCut Pro

**Kosten:** ca. $200 bis 400 (Smartphone vorausgesetzt, Editing-Tool einmalig).

Das reicht für 80 % aller In-House-Hybrid-Produktionen.

---

## Häufige Hybrid-Fehler

| Fehler | Konsequenz |
|---|---|
| **Licht beim Dreh ohne Background-Plan** | Compositing kippt visuell |
| **Greenscreen ohne Rim Light** | Person sieht „ausgeschnitten" aus |
| **KI-Background mit Person darin** | Doppelte Person im Bild |
| **Background-Bewegung übertreibt** | Compositing wirkt unruhig |
| **Color-Matching vergessen** | Foreground und Background sind sichtbar zwei Welten |
| **4K-Aufnahme aber 720p-Background** | Auflösungs-Mismatch sichtbar |
| **Untertitel vergessen** | BFSG-Verstoß |

---

## Hybrid-Checkliste

### Pre-Production
- [ ] Background-Briefing erstellt
- [ ] Licht-Matching-Plan zwischen Dreh und Background definiert
- [ ] Test-Background generiert vorab
- [ ] Wind/Bewegung-Plan für Dreh

### Dreh
- [ ] Greenscreen/neutraler Hintergrund aufgebaut
- [ ] Key Light, Fill Light, Rim Light eingerichtet
- [ ] 4K/60fps in LOG aufgenommen
- [ ] Mehrere Takes pro Shot
- [ ] Vordergrund-Elemente mit aufgenommen

### Post
- [ ] Person sauber freigestellt (Magic Mask / Keying)
- [ ] Background-Clips generiert (matching light direction)
- [ ] Compositing mit Light Wrap
- [ ] Color-Match Foreground/Background
- [ ] Schatten plausibel
- [ ] Untertitel (BFSG)
- [ ] Export in Plattform-Specs
