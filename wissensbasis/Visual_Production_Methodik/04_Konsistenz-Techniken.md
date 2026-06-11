# Säule 4 — Konsistenz-Techniken (Charakter, Brand, Look)

Eine Marke wird erkennbar durch **Konsistenz**, nicht durch Einzelbilder. KI macht es einfach, beliebige Bilder zu generieren — und schwierig, **wiederholbare** Bilder zu generieren.

Diese Säule dokumentiert die Techniken, mit denen ihr Konsistenz über viele Generierungen aufbaut.

---

## Drei Konsistenz-Ebenen

| Ebene | Was bleibt gleich | Beispiel |
|---|---|---|
| **Brand-Konsistenz** | Farb-Welt, Lichtsprache, Komposition | Alle Visuals einer Marke wirken zusammengehörig |
| **Look-Konsistenz** | Stil über eine Kampagne | Alle Bilder einer Kampagne haben denselben Look |
| **Charakter-Konsistenz** | Eine Person über mehrere Bilder/Cuts | Dieselbe Person in Bild 1, 5 und 8 wiedererkennbar |

Alle drei Ebenen brauchen unterschiedliche Techniken.

---

## Ebene 1: Brand-Konsistenz

Brand-Konsistenz wird über **strukturelle Vorgaben** erzeugt — nicht über Trickserei.

### Methode 1: Style-Anker im Prompt

Jeder Prompt enthält **denselben Style-Anker-Block** am Ende. Beispiel:

```
[Bild-Beschreibung]

Style: [Brand-Look-Spezifika]
Color palette: [Farben aus Brand-Manual]
Lighting: [Lichtsprache aus Brand-Manual]
Camera: [Kamera-Mood aus Brand-Manual]
Aesthetic: [3-5 Style-Adjektive]
```

Dieser Block wird in jedem Prompt **identisch** mitgegeben.

### Methode 2: Negative Prompts

Negative Prompts schließen aus, was NICHT zur Marke passt:

```
--no [verbotene Elemente]
```

Bei Midjourney: `--no <element>`.
Bei Flux/anderen: über Parameter „negative_prompt".

### Methode 3: Seeds (für Reproducible Outputs)

Wenn ihr einen bestimmten Look erfolgreich generiert habt, **speichert den Seed** (die numerische ID der Generation). Mit demselben Seed + ähnlichem Prompt bekommt ihr ähnliche Outputs.

Bei Midjourney: `--seed [zahl]`.
Bei Stable Diffusion / Flux: direkt im API.

### Methode 4: Custom Models / LoRA

Für Marken mit hohem Volumen lohnt sich **eigenes LoRA-Training**:

- 15–30 Beispiel-Visuals der Marke
- Training-Dauer: 30–60 Minuten auf modernen GPUs
- Ergebnis: Ein custom Adapter, der den Brand-Look auf jeden Output anwendet

**Tools für LoRA-Training:**
- **Replicate** — Server-basiertes Training (~$5–20 pro Training)
- **Civit.AI** — Community-Plattform für LoRAs
- **RunDiffusion** — Hosted Training mit Templates

LoRA-Training ist eine **Investition**: Einmal trainiert, viele Generierungen mit konsistentem Look.

---

## Ebene 2: Look-Konsistenz (über eine Kampagne)

Look-Konsistenz ist enger als Brand-Konsistenz. Eine Marke kann mehrere Looks haben (Hauptkampagne vs. Saison-Kampagne).

### Methode 1: Reference-Image-Conditioning

Modernste Methode 2026. Du gibst dem Tool **1–3 Referenz-Bilder**, das Tool extrahiert die Stil-Merkmale und überträgt sie auf neue Generationen.

**Wo es funktioniert:**
- Midjourney: `--cref [URL]` für Character + `--sref [URL]` für Style
- Flux 2: über IP-Adapter (im API)
- Kling 3.0: Reference-Image-Funktion eingebaut
- Runway Gen-4.5: Reference-driven Character Consistency

**Stärke:** Schnell, kein Training nötig.
**Schwäche:** Funktioniert nicht perfekt für jede Variation.

### Methode 2: Image-to-Image (mit Stärke-Steuerung)

Statt rein aus Text zu generieren: Du gibst dem Tool ein Bestandsbild + Prompt + „Stärke" (wie stark soll das Tool davon abweichen?). Damit kannst du Variationen erzeugen, die zum Original passen.

Verfügbar bei: Stable Diffusion / Flux (über UIs), Midjourney (Image Prompts mit `--iw`), Runway.

### Methode 3: Master-Prompt-Bibliothek

Für jede Kampagne eine **Prompt-Bibliothek** in Notion:

```markdown
# Prompt-Bibliothek Kampagne X

## Master-Style-Block
[Identischer Style-Anker für alle Prompts dieser Kampagne]

## Successful Prompts
### Cover Hero
[Prompt mit Seed, der gut funktioniert hat]

### Detail-Shot Variante 1
[Prompt]

### Detail-Shot Variante 2
[Prompt]
```

Diese Bibliothek wächst über die Kampagne und ist eine **Wiederverwendungs-Ressource**.

### Methode 4: Color Grading in Post

Selbst wenn Generierungen leicht abweichen: Ein einheitliches **Color Grading in der Post-Production** (siehe Säule 07) bringt 80 % der Look-Konsistenz nachträglich. LUTs (Look-Up Tables) sind das Werkzeug der Wahl.

---

## Ebene 3: Charakter-Konsistenz

Die schwierigste Disziplin: **Dieselbe Person über mehrere Bilder oder Video-Cuts erkennbar halten.**

### Methode 1: Reference-Image (Single)

Du gibst dem Tool ein klares Foto der Person. Tool nutzt es als Referenz für Charakter-Merkmale.

**Wo es gut funktioniert:**
- Midjourney V7 mit `--cref`
- Flux 2 (über IP-Adapter)
- Kling 3.0 (eingebaut)
- Runway Gen-4.5 (Reference-driven)

**Wo es Grenzen hat:**
- Multiple Personen im Bild
- Extreme Posen
- Vom Referenz-Foto weit abweichende Beleuchtung

### Methode 2: Character Sheet (Multiple References)

Statt **einem** Referenz-Foto: ein **Character Sheet** mit 4–6 Bildern derselben Person aus verschiedenen Winkeln und Beleuchtungs-Situationen.

**Vorgehen:**
1. Erstes Referenz-Bild generieren oder fotografieren
2. Mit diesem Bild als Anker weitere Bilder in verschiedenen Posen/Lichtsituationen generieren
3. Die besten 4–6 als „Character Sheet" sichern
4. Bei neuen Generationen alle gemeinsam als Reference einfügen

Stärke: deutlich konsistenter als Single-Reference.
Schwäche: Aufwendiger in der Vorbereitung.

### Methode 3: Custom LoRA für Charaktere

Für Marken mit **wiederkehrenden Personen** (Tastemaker, Markenbotschafter, fiktive Charaktere): Eigenes LoRA für diesen Charakter trainieren.

- 15–30 Beispiel-Bilder derselben Person
- Training auf Replicate / Civit / etc.
- Resultat: Dieser Character ist über tausende Generierungen reproduzierbar

**Forschungs-Daten (2025/26):**
> „Reference-based approaches with FLUX 2 Pro have pushed feature retention to 85–95 % for distinctive characters."

LoRA ist die einzige Methode für **echte Langzeit-Konsistenz** (über Monate, mehrere Kampagnen).

### Methode 4: Hybrid (echte Person + KI-Background)

Die zuverlässigste Methode für höchste Charakter-Konsistenz: **Echte Person live filmen, KI nur für Background.**

Details in Säule 05 (Hybrid-Produktion).

Faustregel: **Wenn das Gesicht/die Person das Kernelement ist, immer live filmen.** KI für Setting, Atmosphäre, Hintergrund.

---

## Konsistenz-Workflow im Detail

### Schritt 1: Brand-Anker definieren (einmalig)

Aus dem Visual Identity Manual (Säule 01) den **Style-Anker-Block** extrahieren. Das ist der wiederverwendbare Block.

### Schritt 2: Kampagnen-Look festzurren

Pro Kampagne:
- Master-Prompt erstellen (Style-Anker + Kampagnen-Spezifika)
- 5–10 erste Generierungen → besten Seed merken
- Reference-Bilder identifizieren

### Schritt 3: Bei jeder Generierung

- Master-Prompt verwenden, nur Bild-Beschreibung variieren
- Reference-Image mitgeben (wenn Tool unterstützt)
- Seed setzen (für Reproduzierbarkeit)
- Negative Prompts beibehalten

### Schritt 4: Post-Production-Veredelung

- Einheitliches Color Grading mit LUT
- Gleiche Grain-/Noise-Einstellungen
- Konsistente Typografie

### Schritt 5: Quality Control vor Veröffentlichung

Letzte Stufe: 5–10 letzte Outputs nebeneinander legen. Visuell prüfen: Wirken sie als eine Familie?

---

## Häufige Konsistenz-Fehler

| Fehler | Symptom | Korrektur |
|---|---|---|
| **Keinen Style-Anker definiert** | Output-Variabilität explodiert | Style-Anker im Brand-Manual definieren |
| **Bei jeder Generierung neuer Prompt** | Look driftet von Bild zu Bild | Master-Prompt + Variationen |
| **Reference-Image nicht genutzt** | Charakter inkonsistent | Immer 1–3 Reference-Images mitgeben |
| **Verschiedene Tools ohne Look-Anpassung** | Tool-eigener Stil dominiert | Color Grading in Post angleichen |
| **Kein LoRA, trotz hohem Volumen** | Manuelle Konsistenz-Arbeit pro Bild | Ab ~50 Generierungen pro Monat: LoRA-Training überlegen |
| **Charakter mit nur 1 Reference** | Erkennt sich aus verschiedenen Winkeln nicht | Character Sheet mit 4–6 Bildern |

---

## Wann welche Methode?

| Use Case | Methode |
|---|---|
| **Einmaliger Look-Test** | Reference-Image + Style-Anker |
| **Eine Kampagne (10–30 Bilder)** | Master-Prompt + Reference-Images + Seed-Tracking |
| **Wiederkehrende Marken-Visuals (50+ Bilder)** | LoRA-Training für Look |
| **Eine wiederkehrende Person (Tastemaker)** | Character LoRA + Live-Aufnahmen als Backup |
| **Sehr wichtige Person (CEO, Markengesicht)** | Hybrid-Produktion: Live filmen, KI nur Background |

---

## Konsistenz-Checkliste

Vor jeder größeren Generierungs-Session:

- [ ] Style-Anker aus Brand-Manual verfügbar
- [ ] Reference-Images vorbereitet (1–3)
- [ ] Master-Prompt für diese Kampagne definiert
- [ ] Seed-Tracking aktiviert (Notion-Sheet oder ähnlich)
- [ ] Negative-Prompts definiert
- [ ] Tool-Auswahl passt (siehe Säule 03)

Nach der Session:
- [ ] Erfolgreiche Prompts + Seeds in Prompt-Bibliothek dokumentiert
- [ ] Outputs visuell nebeneinander geprüft (als „Familie"?)
- [ ] Color Grading in Post angeglichen
