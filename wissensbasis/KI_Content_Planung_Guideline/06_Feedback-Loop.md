# Säule 6 — Feedback-Loop nach 30 Tagen

StoryChief und AdVenture Media sind hier einig: **Der wahre Hebel ist das Lernen.**

> Quellen:
> - https://storychief.io/blog/creating-the-perfect-ai-content-calendar
> - https://adventuremedia.ai/blog/how-to-build-a-social-media-content-calendar-with-claude-code-in-20-minutes

KI-Content-Planung wird erst nach **3–4 Monaten** wirklich gut, wenn die Performance-Daten den Brand-Brief schärfen.

---

## Was nach 30 Tagen Live-Content passiert

### Schritt 1 — Performance-Daten sammeln

**Top 5 und Bottom 5 Posts identifizieren** (nach Reihenfolge der Wichtigkeit gemäß Plattform-Algorithmen):

Generelle Hierarchie der wichtigen Metriken 2026:

1. **Sends / Shares** — stärkstes Reichweite-Signal
2. **Watch Time / Completion Rate** — bei Video-Inhalten
3. **Saves** — signalisiert dauerhaften Wert
4. **Kommentare mit Substanz** — Engagement-Qualität
5. **Likes** — direktes, aber weniger gewichtetes Signal
6. **Profile-Visits / Follower-Growth** — Conversion zu Beziehung

Welche Metriken am wichtigsten sind, hängt von der Plattform ab. Schaut in eure Plattform-Wissensdatenbank oder offizielle Statements (z.B. Mosseri für Instagram).

### Schritt 2 — Performance-Daten dokumentieren

Eine simple Markdown-Datei in der persistenten Wissensbasis:

```markdown
# Performance-Daten Monat [X]

## Top 5 Posts

### Post 1
- Pillar: [Welcher Content-Pillar]
- Format: [Reel/Carousel/Story/Tweet/...]
- Hook: [Erste Zeile / Stoppmoment]
- Sends: [Zahl]
- Watch Time / Saves: [Zahl]
- Vermuteter Erfolgsgrund: [These]

[Weitere 4 Posts...]

## Bottom 5 Posts
[Gleiche Struktur]

## Beobachtete Muster
- [Was funktioniert offensichtlich?]
- [Was funktioniert offensichtlich nicht?]
- [Was überrascht?]
```

### Schritt 3 — KI-Performance-Analyse

**Prompt 5 — Performance-Analyse für nächsten Monat:**

```
[Brand-Brief einfügen]
[Performance-Daten einfügen — Top 5 / Bottom 5]

Analysiere die Performance-Daten:

1. Welche Content-Pillars performen am besten?
2. Welche Hook-Pattern stoppen Scroll?
3. Welche Tageszeiten dominieren?
4. Welche Plattform-Tonalitäten funktionieren bei welcher Zielgruppe?
5. Welche Stile (Versus, Listicle, Hot Take, etc.) bringen Sends?
6. Welche Visual-Elemente kehren bei Top-Performern wieder?

Identifiziere 3 konkrete Anpassungen für das Brand-Brief
(01_Fundament_Brand-Brief.md), die im nächsten Monat ausprobiert
werden sollten.

Identifiziere 3 Sachen, die NICHT mehr gemacht werden sollten
(Bottom-Performer-Muster).

Output als strukturiertes Update für das Brand-Brief.
```

### Schritt 4 — Brand-Brief aktualisieren

Die Erkenntnisse aus Schritt 3 fließen zurück ins Kontext-Dokument:

- **Neue Voice-Beispiele** aus Top-Performern hinzufügen
- **Bottom-Performer-Patterns** explizit als „nicht so machen" notieren
- **Tageszeit-Empfehlungen** verfeinern
- **Pillar-Mix-Logik** anpassen (wenn ein Pillar deutlich besser läuft)
- **Hook-Patterns** dokumentieren, die nachweislich stoppen

---

## Über 3–4 Monate wird das System schlauer

| Monat | Output-Qualität (Schätzung) |
|---|---|
| **Monat 1** | 60 % einsatzbereit — viel Nachbearbeitung nötig |
| **Monat 2** | 70 % einsatzbereit — Brand-Voice schärft sich |
| **Monat 3** | 75 % einsatzbereit — Plattform-Tonalitäten differenzieren sich |
| **Monat 4+** | 80–85 % einsatzbereit — System „kennt" Zielgruppe |

Das Limit von ~85 % ist wichtig: Die letzten 15 % bleiben Menschen-Arbeit. Wer 95 % anstrebt, baut Content, der KI-erkennbar ist.

---

## Quartalsweise: Strategischer Refresh

Alle 3 Monate eine größere Review-Session:

```
[Brand-Brief einfügen]
[Performance-Daten der letzten 3 Monate aggregieren]

Strategischer Refresh für Quartal [X]:

1. Welche Annahmen aus dem Original-Brand-Brief haben sich bestätigt?
2. Welche Annahmen waren falsch oder müssen revidiert werden?
3. Welche neuen Insights über die Zielgruppe sind aufgetaucht?
4. Welche Plattform-Algorithmen-Änderungen müssen wir berücksichtigen?
5. Welche Pillars sollten gestärkt, welche zurückgenommen werden?
6. Gibt es neue Pillars, die wir adden sollten?

Vorschlag für Q-Update am Brand-Brief: [konkrete Änderungen]
```

---

## Jährlich: Großer Audit

Einmal im Jahr — idealerweise in einer ruhigen Phase:

- Komplette Sichtung aller Performance-Daten
- Neuvermessung der Zielgruppe (sind die Personas noch aktuell?)
- Tool-Audit (siehe `05_Tool-Stack.md`)
- Team-Review (was funktioniert im Team-Workflow, was nicht?)
- Prompt-Bibliothek aufräumen (welche Templates werden nicht mehr genutzt?)

---

## Quantitative Performance-Indikatoren über Zeit

Was sich nach 6–12 Monaten verbessert haben sollte, wenn der Loop richtig läuft:

| Indikator | Erwartete Entwicklung |
|---|---|
| **Engagement-Rate** | +20–40 % über 6 Monate |
| **Sends / Shares** | +30–50 % über 12 Monate |
| **Follower-Wachstum** | Stabilisiert sich auf einem höheren Niveau |
| **Time-to-Post-Production** | Halbiert sich, da Workflows ausgereift sind |
| **Brand-Voice-Konsistenz** | Hörbar / lesbar konsistent über Plattformen |

Wenn diese Indikatoren nach 6–12 Monaten nicht klar besser sind: Loop läuft nicht richtig. Mögliche Gründe: Brand-Brief wird nicht aktualisiert, Phase C wird übersprungen, Tool-Stack ist falsch konfiguriert.

---

## Anti-Pattern: Vanity Metrics

Verfolgt nicht zu viele Metriken. Vor allem nicht:

- **Reine Follower-Zahlen** — sagen wenig über Conversion
- **Like-Zahlen ohne Kontext** — sind heute schwach gewichtet
- **Impression-Zahlen ohne Engagement** — können durch Algorithmus-Schwankungen verzerrt sein

Fokus auf **Sends, Saves, Comments mit Substanz** ist meistens das, was wirklich Geschäftswert spiegelt.

---

## Was das ergibt — Strategischer Vorteil

Eine Marke, die nach 18 Monaten *wirklich* ihre Zielgruppe kennt. Nicht aus Annahmen, sondern aus 18 Monaten echtem Engagement.

Das ist der eigentliche Asset, den ihr nach 1–2 Jahren habt — nicht nur einzelne erfolgreiche Posts, sondern ein **lernendes System**, das genau weiß, was eure Zielgruppe bewegt.

Dieses Asset ist auch das stärkste Argument bei Stakeholder-Reviews, Pitch-Verlängerungen oder Erweiterungen des Marketing-Budgets.
