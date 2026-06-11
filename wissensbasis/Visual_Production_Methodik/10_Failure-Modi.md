# Säule 10 — Failure-Modi: Was bei Visual Production schiefgeht

Aus den Quellen und aus Erfahrung extrahiert. Diese Säule dokumentiert die häufigsten Fehler bei Visual Production und ihre Korrekturen.

---

## Übersicht-Tabelle

| Fehler | Häufigkeit | Schwere |
|---|---|---|
| **Look ohne Strategie** | Sehr häufig | Hoch |
| **Tool-Falle (nur ein Tool nutzen)** | Häufig | Mittel |
| **Charakter-Inkonsistenz** | Häufig | Hoch |
| **Compositing-Probleme (Licht/Farben)** | Sehr häufig | Hoch |
| **KI-Sichtbarkeit** | Sehr häufig | Hoch |
| **Audio vernachlässigt** | Sehr häufig | Hoch |
| **Untertitel fehlen / fehlerhaft** | Häufig | Mittel (rechtlich hoch) |
| **Lizenz-/Rechte-Probleme** | Mittel | Sehr hoch |
| **Asset-Chaos** | Häufig | Mittel (langfristig hoch) |
| **Format-Mismatch (Plattform-Specs)** | Häufig | Mittel |
| **Hook-Schwäche** | Sehr häufig | Hoch |
| **Voice-Drift in Visuals** | Mittel | Mittel |
| **Pre-Production übersprungen** | Häufig | Hoch |
| **Trend-Hetze** | Mittel | Mittel |
| **Tool-Aktualität ignoriert** | Mittel | Mittel (langfristig hoch) |

---

## Im Detail

### Fehler 1: Look ohne Strategie

**Symptom:** Schöne Einzelbilder, aber keine Wiedererkennung. Marke wirkt visuell beliebig.

**Ursache:** Direkt zu Tools gegriffen, ohne Look-Konzept (Säule 01) entwickelt zu haben.

**Korrektur:** Visual Identity Manual erstellen, **bevor** die erste Produktion startet. Mindestens: Farb-Palette, Lichtsprache, Komposition, Brand-Don'ts.

### Fehler 2: Tool-Falle

**Symptom:** Nur Midjourney genutzt → Output sieht aus wie jedes andere Midjourney-Output.

**Ursache:** Ein Tool ist Standard, ohne dass es bewusst gewählt wurde.

**Korrektur:** Mindestens 2 Tools im Stack (siehe Säule 03). Jedes Tool für seine Stärke nutzen.

### Fehler 3: Charakter-Inkonsistenz

**Symptom:** Dieselbe „Aylin" sieht in Cut 1, 3 und 5 anders aus.

**Ursache:** Reference-Image nicht genutzt, kein Character LoRA, kein Master-Prompt.

**Korrektur:** Bei wiederkehrenden Charakteren: Character Sheet + ggf. LoRA-Training (siehe Säule 04).

### Fehler 4: Compositing-Probleme (Licht/Farben)

**Symptom:** Person und KI-Background wirken zwei verschiedene Welten — Lichtrichtung passt nicht, Farben matchen nicht.

**Ursache:** Licht beim Live-Dreh ohne Background-Plan, kein Color-Match in Post.

**Korrektur:** Pre-Production-Phase: Licht-Plan zwischen Dreh und KI-Background abstimmen. In Post: Light Wrap + Color Match (siehe Säule 05).

### Fehler 5: KI-Sichtbarkeit

**Symptom:** Audience erkennt, dass es KI-Content ist. Engagement bricht ein.

**Ursache:** Zu viel KI in einem Visual, zu wenig Doku-Rauheit, perfekt-glatte Outputs.

**Korrektur:**
- Hybrid-Workflow (echte Person + KI-Background)
- Doku-Look in Post (Grain, leichte Handheld-Bewegung)
- 30 % der Visuals manuell, nicht KI-generiert

### Fehler 6: Audio vernachlässigt

**Symptom:** Visual ist gut, Reel performt trotzdem schwach. Sound-On-Audience scrollt schnell weg.

**Ursache:** Audio als „Wir machen das später" behandelt. Generische Tracks, kein Mix.

**Korrektur:**
- Audio in Pre-Production planen
- Voice-Over auf -6 bis -12 dB, Music ducken
- SFX strategisch
- (Siehe Säule 06)

### Fehler 7: Untertitel fehlen / fehlerhaft

**Symptom:** Auto-Captions enthalten Fehler. BFSG-Verstoß-Risiko.

**Ursache:** Auto-Captions ohne manuelle Prüfung übernommen.

**Korrektur:**
- Auto-Captions als Start
- Manuelles Review Pflicht (Eigennamen, Fachbegriffe, korrekte Pluralformen)
- (Siehe Säule 09 für BFSG-Vorgaben)

### Fehler 8: Lizenz-/Rechte-Probleme

**Symptom:** Take-Down-Notice, Account-Sperrung, oder Schadenersatz-Forderung.

**Ursache:** Trending Sound ohne Lizenz, KI-Bild mit nicht-kommerzieller Lizenz für Werbung, Personen-Foto ohne Einwilligung.

**Korrektur:**
- Premium-Music-Library (Epidemic, Artlist) als Standard
- Tool-Lizenzen prüfen (Pro-Versions für kommerzielle Arbeit)
- Modell-Verträge bei Personen-Aufnahmen
- (Siehe Säule 09)

### Fehler 9: Asset-Chaos

**Symptom:** In 6 Monaten findet niemand mehr was. Re-Edit nicht möglich, weil Source-Files fehlen.

**Ursache:** Keine Naming-Convention, keine Ordnerstruktur, „Final-FINAL"-Versionen.

**Korrektur:** Asset-Management-System einrichten **vor** der ersten Produktion (siehe Säule 08).

### Fehler 10: Format-Mismatch (Plattform-Specs)

**Symptom:** Reel sieht auf Instagram cropt aus, TikTok zeigt schwarze Balken, LinkedIn-Vorschau ist falsch.

**Ursache:** Ein Master-Export für alle Plattformen.

**Korrektur:**
- Pro Plattform separater Export mit korrekten Specs
- Vorschau auf jeder Plattform vor finalem Upload
- (Siehe Säule 07)

### Fehler 11: Hook-Schwäche

**Symptom:** Reel performt schlecht, hohe Skip-Rate in Sek 0-2.

**Ursache:** Hook visuell und textuell nicht stark genug.

**Korrektur:**
- Hook in 0-2 Sek mit Pattern-Interrupt
- Text-Overlay ab Sek 1
- (Siehe Copywriting-Storytelling-Guide Säule 03)

### Fehler 12: Voice-Drift in Visuals

**Symptom:** Visuals von vor 12 Monaten sehen anders aus als aktuelle. Marke wirkt unentschlossen.

**Ursache:** Look-Manual nicht aktualisiert, Team-Wechsel, KI-Tool-Wechsel.

**Korrektur:**
- Quartalsweise Visual-Audit
- Brand-Visual-Manual gepflegt halten
- Neue Teammitglieder onboarden

### Fehler 13: Pre-Production übersprungen

**Symptom:** Endlose Iterations-Schleifen in Produktion. Projekt-Verzögerungen.

**Ursache:** „Wir machen das jetzt einfach mal" — ohne Briefing, ohne Storyboard.

**Korrektur:** Mindestens 1-Tag Pre-Production für jedes mittlere Projekt (siehe Säule 02).

### Fehler 14: Trend-Hetze

**Symptom:** Visuals folgen Trends, aber Marke wirkt rastlos und ohne eigene Identität.

**Ursache:** Versuchung, jeden viralen Look mitzumachen.

**Korrektur:**
- Eigenen Look priorisieren
- Trends nur aufnehmen, wenn sie passen
- Nicht jeder Trend ist für die Marke richtig

### Fehler 15: Tool-Aktualität ignoriert

**Symptom:** Stack ist 18 Monate alt, neue Tools wären deutlich besser oder günstiger.

**Ursache:** „Läuft ja" — keine regelmäßige Tool-Review.

**Korrektur:** Halbjährliches Tool-Audit (siehe Säule 03). Aber nicht jeden Hype mitmachen.

---

## Spezielle Failure-Modi nach Workflow-Typ

### Bei reiner KI-Produktion

| Fehler | Symptom |
|---|---|
| **Generisches Stockphoto-Feeling** | KI ohne Brand-Look |
| **Hände / Augen / Texte falsch** | Klassisches KI-Verraten-Zeichen |
| **Inkonsistente Lichtrichtung** | Sieht aus wie verschiedene Welten |

### Bei Hybrid-Produktion

| Fehler | Symptom |
|---|---|
| **Person sichtbar ausgeschnitten** | Kein Light Wrap / Rim Light |
| **Greenscreen-Spill** | Grüner Schimmer auf Haut/Kleidung |
| **Bewegung passt nicht** | Background statisch, Person bewegt sich |

### Bei reiner Live-Produktion

| Fehler | Symptom |
|---|---|
| **Schlechtes Licht** | Schatten an falscher Stelle, mattes Bild |
| **Audio-Probleme** | Hall, Hintergrundgeräusche |
| **Kein 4K aufgenommen** | Wenig Spielraum in Post |

---

## Recovery-Strategien

### Wenn ein Projekt schiefgegangen ist

**Schritt 1: Diagnose**
Welcher Failure-Modus war es? Strukturell oder einmalig?

**Schritt 2: Sofort-Reparatur (wenn möglich)**
- Untertitel nachträglich hinzufügen
- Color Grade nachjustieren
- Captions korrigieren

**Schritt 3: Wenn nicht reparierbar**
- Aus Post entfernen wenn rechtliches Risiko
- Lessons in Brand-Visual-Manual einbauen

**Schritt 4: Strukturelle Lernkurve**
- Post-Mortem mit Team
- Asset-Management-Updates
- Tool-Stack-Updates

---

## Failure-Modi-Checkliste

Vor jedem Veröffentlichungs-Schritt:

### Look & Brand
- [ ] Look-Manual angewandt?
- [ ] Konsistent mit anderen Brand-Visuals?
- [ ] Brand-Don'ts respektiert?

### KI-Sichtbarkeit
- [ ] Hybrid-Workflow wo möglich?
- [ ] Hände / Augen / Texte fehlerfrei?
- [ ] Doku-Rauheit eingebaut wo nötig?

### Compositing (wenn Hybrid)
- [ ] Lichtrichtung passt zwischen Foreground / Background?
- [ ] Color-Match durchgeführt?
- [ ] Light Wrap / Rim Light vorhanden?

### Audio
- [ ] Voice -6 bis -12 dB?
- [ ] Music ducked wenn Voice?
- [ ] Loudness -14 LUFS?
- [ ] Lizenz für kommerzielle Nutzung?

### Captions / Untertitel
- [ ] Untertitel manuell geprüft?
- [ ] Alt-Texte gesetzt (für Webseite-Posts)?
- [ ] BFSG-konform?

### Format & Export
- [ ] Plattform-Specs eingehalten?
- [ ] Pro Plattform separater Export?
- [ ] Vorschau auf Plattform geprüft?

### Compliance
- [ ] KI-Kennzeichnung (ab August 2026)?
- [ ] Modell-Einwilligung wenn Personen?
- [ ] Tool-Lizenz kommerziell OK?

### Asset-Management
- [ ] Source-Files gesichert?
- [ ] Final-Exports im richtigen Ordner?
- [ ] Naming-Convention eingehalten?

Wenn alle Häkchen gesetzt: Veröffentlichungs-OK.
