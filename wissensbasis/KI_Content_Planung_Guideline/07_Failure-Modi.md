# Säule 7: Failure-Modi: Was schief gehen kann (und wie ihr es vermeidet)

Aus den Quellen extrahiert + ergänzt um Erfahrungswerte aus der Praxis.

---

## Übersicht-Tabelle

| Risiko | Symptom | Gegenmittel |
|---|---|---|
| **Generischer Content** | Posts klingen wie aus jeder anderen Kampagne | Brand-Brief schärfen, Voice-Beispiele einfügen |
| **Plattformen klingen identisch** | Post auf Plattform A liest sich 1:1 wie auf Plattform B | Plattform-Personas explizit definieren |
| **KI-Output wird erkennbar** | Zielgruppe scrollt weg, Engagement bleibt aus | Echte Stimmen einbauen, nicht alles KI |
| **Verbrannte Begriffe schleichen ein** | Floskeln tauchen wieder auf | Phase C Brand-Compliance-Check ist Pflicht |
| **Reaktionsverlust** | Kampagne wirkt mechanisch | 5 bis 8 freie Slots pro Monat für reaktiven Content |
| **Compliance-Risiko** | Versprechen, die fact-checkbar problematisch sind | KI-Output gegen Quellen spiegeln |
| **Tool-Lock-In** | Schon nach 2 Jahren abhängig von einem Anbieter | Standard-Formate (.md, .csv) bevorzugen |
| **Team-Wissensverlust** | Personalwechsel → System bricht zusammen | Workflow-Dokumentation außerhalb der KI-Tools |
| **Algorithmus-Drift** | Plattformen ändern Regeln, Performance fällt ohne Erklärung | Jährliches Algorithmus-Audit |
| **KI-Halluzinationen** | Zahlen, Fakten, Personen werden erfunden | Faktencheck vor Veröffentlichung |
| **Trend-Hetze** | Marke wirkt rastlos, ohne eigene Identität | Disziplin bei der Pillar-Erweiterung |
| **Voice-Erosion** | Voice driftet über Monate vom Original ab | Quartalsweise Voice-Beispiele aktualisieren |

---

## Im Detail

### Problem 1: Generischer Content

**Cause:** Brand-Brief zu vage formuliert. „Junge Zielgruppe, modern, locker" reicht nicht.

**Fix:**
1. Drei bis fünf Beispiel-Captions in `01_Fundament_Brand-Brief.md` einfügen unter „Voice-Beispiele"
2. Prompt-Erweiterung: „Match the tone and style of these examples exactly when writing new content"
3. Konkrete Beispiele schlagen geschriebene Beschreibungen jedes Mal

### Problem 2: Plattformen klingen identisch

**Cause:** Formatierungs-Regeln definiert, aber keine Tonalitäts-Personas.

**Fix:** Personas in einem Satz pro Plattform definieren. Beispielsweise:

```
Instagram = der/die kreative Berater:in der Marke.
TikTok = der/die jüngere Geschwister-Stimme.
LinkedIn = der/die Kommunikationsleiter:in.
YouTube = der/die Reportage-Macher:in.
X = der/die scharfsinnige Beobachter:in.
```

KI mit Personas produziert dramatisch differenziertere Outputs als KI mit reinen Formatregeln.

### Problem 3: KI-Output wird erkennbar

**Cause:** Zu viel KI, zu wenig echte Menschen.

**Fix:** Mindestens 30 % des Contents kommt aus echten Stimmen (Personality-Posts, Behind-the-Scenes, User-Stories). KI ist Beschleuniger für die anderen 70 %, nicht Ersatz.

**Faustregel:** Wenn ein Post eine Person mit Gesicht zeigt, sollte die Stimme/Geschichte echt sein. KI für Bühne, Daten, Hintergrund.

### Problem 4: Verbrannte Begriffe schleichen ein

**Cause:** Phase C (Brand-Compliance-Check) wird übersprungen.

**Fix:** Phase C ist Pflicht, nicht optional. Eine einzige Verwendung eines verbrannten Begriffs zerstört Strategiearbeit, weil Zielgruppen genau auf solche Signale achten.

### Problem 5: Reaktionsverlust

**Cause:** 100 % der Posts vor-geplant. Wirkt mechanisch.

**Fix:** 5 bis 8 Slots pro Monat freilassen. Diese werden manuell gefüllt mit:
- Trend-Reaktionen
- News-Bezüge
- Community-Antworten (z.B. besonders gute Kommentare als eigener Post aufgreifen)
- Spontane Momente (z.B. unerwartetes Ereignis kommentieren)

### Problem 6: Compliance-Risiko

**Cause:** KI macht Behauptungen, die nicht belegbar sind.

**Fix:** Vor jeder Veröffentlichung Faktencheck der Kernaussagen:
- Sind die genannten Zahlen aktuell?
- Sind die genannten Orte/Personen/Produkte korrekt?
- Werden Versprechen über die Zukunft gemacht?
- Bei regulierten Branchen (Gesundheit, Finanzen, Recht): Sind die Aussagen rechtskonform?

KI-Output ist nie automatisch faktenrichtig. Sie ist eloquent, aber nicht zuverlässig in Fakten.

### Problem 7: Tool-Lock-In

**Cause:** Alles in einem proprietären Tool, kein Export möglich.

**Fix:**
- Brand-Brief als Markdown halten (nicht Tool-only)
- Content-Pläne als CSV exportierbar halten
- Prompt-Bibliothek in einem Format, das auch ohne den aktuellen Tool funktioniert
- Quartalsweises Backup aller Assets

### Problem 8: Team-Wissensverlust

**Cause:** Eine Person beherrscht den Workflow, geht, System bricht zusammen.

**Fix:**
- Workflow-Dokumentation in einer geteilten Wissensbasis (Notion / Confluence)
- Quartalsweise Onboarding-Session für neue Teammitglieder
- Master-Prompt-Bibliothek mit Erklärungen, warum welcher Prompt was tut

### Problem 9: Algorithmus-Drift

**Cause:** Plattformen ändern Regeln (z.B. Hashtag-Limit, Video-Längen-Empfehlungen, Format-Präferenzen).

**Fix:**
- Jährliches Algorithmus-Audit (siehe `06_Feedback-Loop.md`)
- Plattform-Wissensdatenbanken regelmäßig aktualisieren
- Bei plötzlichem Performance-Einbruch: Erst Algorithmus prüfen, dann Content

### Problem 10: KI-Halluzinationen

**Cause:** KI generiert plausibel klingende, aber falsche Fakten, Zahlen, Daten, Personen, Quellen.

**Fix:**
- Jede konkrete Behauptung gegen mindestens eine Quelle prüfen
- Bei Zitaten: Quelle nennen und verlinken
- Bei Statistiken: Quelle nennen und Aktualität prüfen
- KI nie als finalen Faktencheck-Stand nehmen, sie ist Recherche-Hilfe, kein Beleg

### Problem 11: Trend-Hetze

**Cause:** Versuchung, jeden Trend mitzunehmen. Verwässert die Marke.

**Fix:** Ein Trend wird erst dann zum Pillar / Stil, wenn die Marke ihn **mindestens 3-mal** erfolgreich umgesetzt hat. Vorher ist es ein Experiment.

Marken mit klarem Profil widerstehen mehr Trends, als sie mitmachen.

### Problem 12: Voice-Erosion

**Cause:** Voice driftet über Monate vom Original ab, weil KI sich an eigene Outputs gewöhnt.

**Fix:** Quartalsweise Voice-Beispiele im Brand-Brief erneuern, möglichst aus aktuellen erfolgreichen Posts. Voice ist kein „set it and forget it"-Element.

---

## Spezifische Risiken bei sensiblen Themen / Branchen

Bei manchen Themen sind Standard-Workflows nicht genug:

- **Politisch sensible Themen:** Manueller Review zwingend, KI macht oft taktlose Aussagen
- **Persönliche Krisen / Trauer:** KI hat kein Feingefühl, hier nur Mensch
- **Gesundheits- / Medizinthemen:** Disclaimers Pflicht, regulatorische Vorgaben prüfen
- **Finanz- / Investitions-Empfehlungen:** Rechtliche Vorgaben extrem streng
- **Minderjährige Zielgruppen:** Besondere Sorgfaltspflicht, Werbe-Regulierung

**Gegenmittel:** Phase C explizit erweitern um die Frage: „Könnte dieser Post aus dem Kontext gerissen problematisch wirken? Wer könnte ihn missverstehen?" Bei heiklen Themen immer manueller Review.

---

## Recovery-Plan: Wenn ein Post viral schiefgeht

KI hilft hier nicht. Drei Schritte:

1. **Stunde 1:** Post stehen lassen, aber sofort intern Krisenstab aktivieren. Niemals reflexartig löschen, das verstärkt Aufmerksamkeit.
2. **Stunde 2 bis 6:** Lage analysieren. Echte Stellungnahme verfassen (Mensch, nicht KI). Klarstellung als Folge-Post veröffentlichen.
3. **Tag 2 bis 7:** Lehren in Brand-Brief einbauen, damit derselbe Fehler nie wieder passiert.

Marken, die transparent mit Fehlern umgehen, kommen oft gestärkt aus Krisen heraus. Marken, die vertuschen, fast nie.
