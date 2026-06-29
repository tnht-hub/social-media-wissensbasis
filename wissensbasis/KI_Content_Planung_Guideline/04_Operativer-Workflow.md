# Säule 4: Operativer Workflow (Monatszyklus)

Inspiriert von AdVenture Media (Claude-Code-Workflow) und JPK Design (Prompt-Sequenzen).

> Quellen:
> - https://adventuremedia.ai/blog/how-to-build-a-social-media-content-calendar-with-claude-code-in-20-minutes
> - https://www.jpkdesignco.com/blog/create-content-calendar-with-ai-prompts

---

## Übersicht der vier Phasen

| Phase | Aufwand | Frequenz | Output |
|---|---|---|---|
| **A, Monatsstrategie** | 1 Stunde | 1× pro Monat | Themenplan |
| **B, Themen-zu-Posts** | 2 Stunden | 1× pro Monat | Konkrete Post-Entwürfe |
| **C, Qualitäts-Check** | 15 Min pro Wochen-Batch | wöchentlich | Brand-Compliance |
| **D, Multi-Plattform-Repurposing** | 30 Min pro Hauptbeitrag | nach Bedarf | Plattform-Varianten |

**Gesamt: ca. 4 bis 5 Stunden pro Monat** für einen vollen Multi-Plattform-Content-Plan.

---

## Phase A: Monatsstrategie

**Prompt 1, Monats-Themen-Plan generieren:**

```
[Brand-Brief einfügen, aus 01_Fundament_Brand-Brief.md]

Generiere mir einen Monatsplan für [MONAT/JAHR] mit:
- 4 Wochenthemen, rotiere durch unsere Content-Pillars
- Pro Woche: relevante Anlässe, saisonale Bezüge, Branchen-Termine
- Empfohlene Cadence pro Plattform
- Pro Woche ein "Kampagnen-Fokus" (z.B. Produkt-Launch, Awareness-Push)

Berücksichtige unsere strategischen Prinzipien aus dem Brand-Brief.
Output als strukturiertes Markdown.
```

**Kritische Nachfrage an die KI:**

> „Welche dieser Themen riskieren, in verbrannte Sprache zu kippen oder unsere Tonalität zu verletzen? Markiere sie."

Das ist eine Mini-Adversarial-Verifikation, die unbrauchbaren Output vor Phase B aussortiert.

---

## Phase B: Themen-zu-Posts

**Prompt 2, Wochen-Posts ausarbeiten:**

```
[Brand-Brief einfügen]
[Monatsplan aus Phase A einfügen]

Für Woche 1 ([WOCHE]) generiere:
- [Anzahl] Posts pro Plattform
- Format-Mix entsprechend unserer Plattform-Personas

Pro Post:
- Hook-Satz (max 10-12 Wörter, Plattform-passend)
- Visual-Konzept (Was wird gezeigt, mit welchem Ankerelement)
- Caption-Entwurf
- Hashtags (an Plattform-Limit angepasst)
- Posting-Zeit-Empfehlung

Wichtig: Jeder Post muss sich für die Zielgruppe lesen wie etwas, das
sie ihrer Freund:in per DM schicken würden (Shareability-Test).

Output als CSV-Tabelle.
```

**Output-Tipp:** Direkt als CSV anfordern. Lässt sich sofort in Notion, Asana, Google Sheets, Buffer, Later importieren.

---

## Phase C: Qualitäts-Check

Der wichtigste Filter, KI prüft sich selbst gegen den Brand-Brief.

**Prompt 3, Brand-Compliance & Shareability-Check:**

```
[Generierte Posts einfügen]

Überprüfe alle Posts gegen:
1. Verbrannte Begriffe-Liste (nie verwenden)
2. Pathos-Risiko (übersteigerte Sprache, Helden-Frame)
3. Tonalität: Stimmt die Voice mit unseren Voice-Beispielen überein?
4. Shareability: Welche Posts würde jemand seiner Freund:in schicken?
   Welche eher nicht?
5. Plattform-Tonalität: Klingen verschiedene Plattformen zu ähnlich?
6. Faktentreue: Werden Versprechen gemacht, die nicht belegbar sind?

Output: Tabelle mit Bewertung pro Post + konkrete
Verbesserungs-Vorschläge für jede Schwachstelle.
```

---

## Phase D: Multi-Plattform-Repurposing

Buffer und Postiv zeigen: Ein gut gemachter Hauptbeitrag wird zu **5 bis 7 Plattform-Varianten**.

**Spezialtools (siehe `05_Tool-Stack.md`):**
- **Opus Clip** für Video-Schnitte
- **Repurpose.io** für Text-zu-Video
- **Contentdrips** für plattform-spezifische Adaptionen

**Prompt 4, Cross-Plattform-Adapt:**

```
[Originalpost einfügen]

Adaptiere diesen Post für:
- [Plattform 1]: [spezifische Tonalität, Format-Vorgaben]
- [Plattform 2]: [spezifische Tonalität, Format-Vorgaben]
- [Plattform 3]: [spezifische Tonalität, Format-Vorgaben]

Jede Adaption muss sich plattform-nativ lesen, nicht wie
Copy-Paste mit anderer Auflösung.

Berücksichtige die Plattform-Personas aus dem Brand-Brief.
```

### Suchgetriebenes Sourcing und TikTok-zu-Instagram (Stand Juni 2026)

Statt Themen frei zu erfinden, lässt sich der Hauptbeitrag aus realer Suchnachfrage ableiten. Auf TikTok liefert Creator Search Insights (Reiter „Content gap") Themen mit hoher Nachfrage bei geringem Angebot. Ein so validierter Suchbegriff dient als gemeinsame Klammer für beide Kanäle.

Ablauf pro Thema:

1. Suchbegriff aus „Content gap" festlegen (deutsche Begriffe setzen Sprach-/Region-Klassifizierung auf DACH voraus, siehe `tiktok/01-algorithmus.md`).
2. TikTok-Original: Begriff in den ersten Sekunden als gesprochenes Wort und als Text-Overlay, 15 bis 30 Sekunden, Begriff zusätzlich in Caption und Keyword-Metadata (zahlt auf den Search Value ein).
3. Instagram-Fassung neu aufbereiten, nicht das TikTok-Video mit Wasserzeichen querposten. Das eigene Logo ist zulässig, das TikTok-Wasserzeichen kostet Reichweite.
4. Format wählen: bewegtes Thema als Reel unter 90 Sekunden mit eigener Tonspur, erklärendes Thema zusätzlich als Carousel.
5. Instagram-Caption mit demselben Begriff für die Google-Suche optimieren (Instagram-Posts seit Juli 2025 dort indexiert).
6. Stärkeres Reel als Story nachschieben für eine zweite Reichweitenwelle.

Messung: Suchanteil der Views auf TikTok, Speicherquote, Sends auf Instagram, mittelfristig Google-Impressionen auf indexierte Captions. Vorbehalt: Suchgetriebener Content senkt Streuverlust, ersetzt aber keine Retention. Watch Time und Completion Rate bleiben die stärksten Ranking-Signale.

---

## Häufige Fehler in der Workflow-Anwendung

### Fehler 1: Zu viele Plattformen auf einmal
KI verliert Plattform-Nuancen, wenn mehr als 3 bis 4 Plattformen gleichzeitig bedient werden. Lieber zwei Sessions: erst visuelle Plattformen (IG, TikTok, Pinterest), dann textuelle (LinkedIn, X, Threads).

### Fehler 2: Wochen-Batch zu groß
Wenn ein Prompt für 30+ Posts auf einmal generiert wird, kippt die Qualität in der Mitte. Lieber Woche für Woche.

### Fehler 3: Phase C übersprungen
„Sieht doch gut aus" reicht nicht. Brand-Compliance-Check ist Pflicht, nicht optional. Eine einzige Verwendung eines verbrannten Begriffs zerstört monatelange Strategiearbeit.

### Fehler 4: Keine Reaktiv-Slots
KI plant 100 % der Posts vor. Behalte **5 bis 8 Slots pro Monat frei** für reaktiven, handgemachten Content (Trending Topics, Krisenreaktion, spontane Gelegenheiten). Hybrid schlägt vollautomatisch.

### Fehler 5: Workflow wird Selbstzweck
KI generiert effizient, aber wenn der Output mittelmäßig bleibt, hat Effizienz keinen Wert. Lieber **weniger Posts in höherer Qualität** als ein Volllast-Kalender mit generischem Content.

---

## Time-Boxing: Realistische Zeiten

Ehrlich verteilt:

| Aufgabe | Geübte Person | Einsteiger:in |
|---|---|---|
| Monatsstrategie (Phase A) | 30 Min | 90 Min |
| Wochen-Posts (Phase B, eine Woche) | 30 Min | 60 Min |
| Qualitäts-Check (Phase C) | 15 Min | 30 Min |
| Cross-Plattform (Phase D, ein Beitrag) | 15 Min | 45 Min |

Geübte Anwender:innen schaffen einen Monatsplan in 3 bis 4 Stunden. Einsteiger:innen brauchen das Doppelte, werden aber nach 2 bis 3 Monaten schneller.

---

## Rollen, Selbst-Klonen und Batching (Praktiker-Sicht)

> **Quelle:** Kane Callaway (Kallaway / Open Residency), YouTube, Juni 2026. Praktiker-Heuristik, keine belegte Forschung.

**Rollenteilung.** Ideenfindung ist ein bodenloses Fass und der größte Zeitfresser, der Schnitt ist klar abgrenzbar. Wer skaliert, lagert zuerst die Ideen aus. Mögliches Setup: ein „Content Operator" (sammelt und pitcht Ideen wie ein Showrunner), dedizierte Editor:innen und bei Bedarf eine Person, die nur Tools und Visuals testet.

**Selbst-Klonen über ein Curriculum.** Die eigene Arbeitsweise lässt sich in eine andere Person übertragen, indem man Auswahlkriterien, Beispiele und Nuancen schriftlich und über Mitschnitte festhält. Das dauert mehrere Monate, macht die Person danach aber weitgehend eigenständig. Dasselbe Curriculum dient als Onboarding-Material und als Prompt-Grundlage für KI.

**Batching nach Skill-Level.** Einsteiger:innen arbeiten Stück für Stück, weil sie die Lernschleife pro Wiederholung brauchen (die eigentliche Fähigkeit ist die kurze Iterationsdistanz, nicht die Strategie). Wer die Grundlagen sicher beherrscht, kann bündeln, um Volumen zu erreichen. Das deckt sich mit „Fehler 2" oben: Volumen vor sicheren Fundamenten kippt die Qualität.

---

## Erweiterung: Performance-Lernschleife

Siehe `06_Feedback-Loop.md`, der Workflow wird nach 30 Tagen mit echten Daten gefüttert und lernt iterativ besser zu prompten.
