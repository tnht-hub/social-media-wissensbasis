# Säule 1: Das Fundament: Brand-Brief & Kontext-Datei

Das wichtigste Asset, **bevor** ihr einen einzigen Prompt schreibt: Ein **Kontext-Dokument**, das ihr in jedem Chat / Projekt als Startpunkt verwendet.

Verschiedene Tools nennen es unterschiedlich:
- **Claude.ai:** Projekt-Anweisungen
- **Claude Code / Cowork:** `CLAUDE.md`
- **ChatGPT:** Custom Instructions
- **Gemini:** Gems / System-Instructions
- **Notion AI:** Workspace-Knowledge

Der Inhalt ist immer identisch. Ohne dieses Fundament produziert KI generischen Content, der vom Brief wegdriftet.

---

## Universelle Brand-Brief-Vorlage

Diese Vorlage wird einmal angelegt und dann in jedem Chat referenziert:

```markdown
# Kontext: [PROJEKT- / BRAND-NAME]

## Auftraggeber / Brand
[Wer ist die Marke? Wer ist Absender? Wer kommuniziert?]

## Zielgruppe
[Demografie, Lebensphase, Werte, Sorgen, Sprache.
Möglichst konkret, keine Marketing-Floskeln wie "anspruchsvolle Millennials".
Lieber: "26-32 Jahre, urbaner Berufseinstieg, finanziell unter Druck,
politisch eher links, kauft Bio aber nicht ideologisch."]

## Strategischer Kern
[Die 4-6 Prinzipien, die jede Kommunikation tragen.
Beispielsweise:
- Self-Interest vor Drittnutzen
- Konkret vor abstrakt
- Person vor Marke
- Ironie zulassen, nicht imitieren]

## Verbrannte Begriffe (NIE verwenden)
[Vokabular, das in der Zielgruppe als hohl, abgenutzt oder als
"Marketing-Sprech" erkannt wird. Beispiele variieren stark je Branche.]

## Funktionierende Codes
[Vokabular, das in der Zielgruppe als authentisch gilt.
Aus Customer-Research extrahiert, nicht erfunden.]

## Claim / Markenversprechen
[Falls vorhanden, hier eintragen. Sonst Platzhalter "tbd".]

## Tonalität
[3-5 Adjektive, eine konkrete Persona-Beschreibung.
Beispielsweise: "Wie ein:e ältere:r Kolleg:in, der/die offen redet
aber nicht belehrt."]

## Content-Pillars (siehe 02_Content-Pillars.md)
[4-6 thematische Säulen]

## Plattform-Personas
[Pro Plattform eine Persona-Beschreibung, was diese Plattform
für die Marke bedeutet.]

## Formatierungs-Regeln
[Spezifische Vorgaben:
- Maximale Caption-Länge pro Plattform
- Hashtag-Strategie
- Bildverhältnisse
- CI-Vorgaben]

## Voice-Beispiele
[3-5 echte, gute Beispiele aus bestehender Kommunikation.
DAS ist der wichtigste Teil, konkrete Beispiele schlagen jede
abstrakte Beschreibung der Voice.]
```

---

## Wo dieses Dokument lebt

| Tool | Speicherort | Format |
|---|---|---|
| **Claude.ai** | Projekt-Anweisung im Projekt | Plain Text in Settings |
| **Claude Code / Cowork** | Projektordner | `CLAUDE.md` als Datei |
| **ChatGPT** | Custom Instructions + File per Projekt | Plain Text + .md |
| **Gemini** | Gems-Konfiguration | Plain Text in Settings |
| **Notion** | Master-Brand-Doc + Workspace-Knowledge | Notion-Page |
| **Konzeptuelle Backup-Quelle** | Markdown im Versions-Repository | `.md` mit Git |

**Empfehlung:** Ein Master-`.md` im Versions-Repository der Marke, von dem alle anderen Versionen ableiten. Verhindert Tool-Lock-In.

---

## Lebenszyklus und Aktualisierung

Das Brand-Brief ist ein **Living Document**:

- **Wöchentlich:** Kleine Voice-Beispiele aus erfolgreichen Posts nachpflegen
- **Quartalsweise:** Performance-Erkenntnisse einarbeiten (siehe `06_Feedback-Loop.md`)
- **Jährlich:** Strategischer Refresh, Zielgruppe neu vermessen, Pillars überprüfen
- **Bei Personalwechsel:** Onboarding-Dokument für neue Teammitglieder

---

## Voice-Beispiele: der unterschätzte Hebel

Die häufigste Schwachstelle in Brand-Briefs: **Voice wird beschrieben, statt gezeigt**.

Vergleiche:

**Schwach (beschreibend):**
> „Unsere Tonalität ist warm, witzig, aber nicht oberflächlich. Wir sprechen unsere Zielgruppe auf Augenhöhe an."

**Stark (zeigend):**
> „Beispiel-Caption Sommer 2025 (Post mit 4.300 Sends):
> 'Mit 28 noch keine Therapie? Hut ab. Oder: Vielleicht doch mal kurz checken.'
> Diese Spannung, warm-witzig, aber mit Ernst-Anker, ist unsere Voice."

KI lernt aus konkreten Beispielen exponentiell schneller als aus abstrakten Beschreibungen.

---

## Warnung: das wichtigste Versäumnis

Die häufigste Fehlerquelle bei KI-Content-Planung: **Sofort prompten, ohne Kontext-Dokument**.

Das Ergebnis ist immer derselbe generische Marketing-Stil, den Zielgruppen sofort als Werbung erkennen und wegscrollen.

Investiert die 60 bis 90 Minuten in das Kontext-Dokument, bevor ihr einen produktiven Prompt schreibt. Es ist die wichtigste Investition für den gesamten Projektverlauf.

---

## Mini-Vorlage zum Sofort-Start

Wenn ihr noch keine Zeit für die volle Vorlage habt, hier die absolute Minimal-Version, mit der KI schon deutlich besser arbeitet:

```markdown
# Kontext

**Brand:** [Name]
**Zielgruppe:** [Wer in 2 Sätzen]
**Was wir verkaufen/kommunizieren:** [In 1 Satz]
**Was wir NICHT sind:** [3 Abgrenzungen]
**Tonalität:** [3 Adjektive + 1 Persona-Vergleich]
**Verbotene Wörter:** [5 Begriffe]
**Bevorzugte Wörter:** [5 Begriffe]
**Voice-Beispiel:** [Eine echte, gute Caption]
```

Das ist der Einstieg. Über die ersten Wochen erweitert sich das Dokument organisch.
