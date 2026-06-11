# Säule 2 - Performance-Bestandsaufnahme: Zahlen sammeln, bevor man urteilt

Diese Säule beantwortet vier Fragen: Welche Kennzahlen erheben wir, über welchen Zeitraum, aus welchen Quellen, und wie sichern wir die Rohdaten so, dass der Befund später belegbar bleibt. Reihenfolge ist wichtig: erst sammeln und sichern, dann auswerten (Säule 04).

Grundregel: Jede Zahl bekommt drei Etiketten, sonst ist sie wertlos. **Quelle** (woher), **Zeitraum** (wann), **Formel** (wie gerechnet).

---

## 1. Welche Kennzahlen erheben

Erhebe je Plattform die nativen Kennzahlen. Gewichte sie nach Aussagekraft: Outcome-nahe Zahlen zählen mehr als Reichweiten-Zahlen, Reichweite zählt mehr als reine Bestandszahlen (siehe Grundprinzip 5 im Index).

| Stufe | Kennzahl | Aussagekraft |
|---|---|---|
| **Bestand** | Followerzahl, Follower-Wachstum (absolut und Prozent) | niedrig, beschreibt nur Größe |
| **Reichweite** | Reach, Impressions, Views, Reichweiten-Rate | mittel, beschreibt Sichtbarkeit |
| **Engagement** | Likes, Kommentare, Shares, Saves, Engagement-Rate | mittel bis hoch, je nach Bezug |
| **Outcome** | Profilbesuche, Link-Klicks, Conversions, gespeicherte Beiträge, DMs | hoch, am nächsten am Geschäftsziel |

**Engagement-Rate: Formel festlegen und dokumentieren.** Es gibt mehrere gängige Definitionen, und sie liefern stark unterschiedliche Werte. Lege eine fest und nutze sie konsequent, auch im Wettbewerbsvergleich:

- **ER auf Reach** = (Interaktionen / Reach) x 100. Am fairsten, weil sie misst, wie viele der Erreichten reagieren. Braucht native Insights.
- **ER auf Impressions** = (Interaktionen / Impressions) x 100.
- **ER auf Follower** = (Interaktionen / Follower) x 100. Die einzige Variante, die auch von außen (für Wettbewerber) berechenbar ist, weil Reach extern nicht sichtbar ist.

Wichtig für den Benchmark: Wettbewerber-ER lässt sich meist nur auf Follower-Basis rechnen, weil deren Reach nicht öffentlich ist. Die eigene ER dann ebenfalls auf Follower-Basis daneben stellen, sonst vergleicht man Äpfel mit Birnen.

> Eine dokumentierte Reel-Beobachtung bestätigt diese Methodik: Erst der Vergleich am Kanal-Median, getrennt nach Konto und nach Reichweite gegen Engagement, macht aus Aufrufen einen belastbaren Befund.

---

## 2. Über welchen Zeitraum

| Zweck | Zeitraum | Begründung |
|---|---|---|
| **Standard-Bestandsaufnahme** | letzte 90 Tage | genug Posts für Muster, kurz genug für Aktualität |
| **Saisonale Marken** | letzte 12 Monate | erfasst saisonale Spitzen und Täler |
| **Wachstums-Trend** | letzte 6 bis 12 Monate, monatlich aufgeschlüsselt | zeigt Richtung, nicht nur Stand |
| **Top-Content-Analyse** | letzte 90 Tage, Top 5 bis 10 je Plattform | identifiziert, was funktioniert |

Wichtig: Für alle Plattformen denselben Zeitraum verwenden. Sonst ist der plattformübergreifende Vergleich nicht sauber. Den gewählten Zeitraum oben im Dokument festschreiben.

---

## 3. Aus welchen Datenquellen

**Native Insights (Pflicht, höchste Konfidenz):**

| Plattform | Quelle | Reichweite zurück |
|---|---|---|
| Instagram / Facebook | Meta Business Suite, Insights-Bereich | bis zu 2 Jahre, CSV/XLSX-Export |
| TikTok | TikTok Analytics (Business-Konto) | meist 60 Tage live, daher früh exportieren |
| LinkedIn | LinkedIn Page Analytics | bis 12 Monate, Export verfügbar |
| X / Twitter | X Analytics (je nach Kontotyp eingeschränkt) | begrenzt |
| YouTube | YouTube Studio Analytics | langer Verlauf, CSV-Export |

In Meta Business Suite führt der Weg über Insights, dann Tab wählen (Overview, Results, Audience, Content), dann „Export data" mit Format (CSV oder XLSX) und Datumsbereich. Native Daten haben die höchste Konfidenz, weil sie direkt von der Plattform stammen.

**Drittanbieter-Tools (optional, für Vergleichbarkeit und Wettbewerb):**
- Aggregieren mehrere Kanäle in ein Dashboard (Sprout Social, Metricool, Rival IQ, Socialinsider, Hootsuite).
- Liefern berechnete ER nach einheitlicher Formel, oft auch für Wettbewerber.
- Achtung: Tool-Zahlen können von nativen Zahlen abweichen, weil die Formeln und Bezugsgrößen anders sind. Im Dokument vermerken, welches Tool welche Zahl geliefert hat.

**Was extern (für Wettbewerber) NICHT verfügbar ist:** Reach, Impressions, Saves, Klicks, demografische Daten. Für Wettbewerber bleiben nur öffentlich sichtbare Zahlen (Follower, Likes, Kommentare, Postfrequenz). Das begrenzt den Benchmark, siehe Säule 03.

---

## 4. Rohdaten und Screenshots sammeln

Plattform-Insights verschwinden mit der Zeit (TikTok teils nach 60 Tagen, andere nach Monaten). Wer nicht sichert, kann später weder belegen noch Veränderung messen. Das ist der häufigste vermeidbare Fehler.

**Checkliste Datensicherung:**
- [ ] Native CSV/XLSX-Exporte je Plattform gezogen und mit Datum im Dateinamen abgelegt
- [ ] Screenshot der Profil-Übersicht je Kanal (zeigt Follower, Bio, Visual zum Stichtag)
- [ ] Screenshot der Audience-/Demografie-Ansicht je Kanal
- [ ] Top-Posts je Plattform als Screenshot plus Kennzahlen festgehalten
- [ ] Alle Dateien in einem datierten Ordner (z. B. `IST_[Kunde]_2026-06`)
- [ ] Jede Screenshot-Datei mit Plattform und Datum benannt

**Ablage-Konvention (Vorschlag):**
```
IST_[Kunde]_2026-06/
  rohdaten/      CSV- und XLSX-Exporte
  screenshots/   Profil, Audience, Top-Posts je Plattform
  wettbewerb/    Screenshots und Notizen der Wettbewerber
  IST-Bericht.md
```

---

## Output dieser Säule

Am Ende von Säule 2 liegen vor:
1. Eine **Kennzahlen-Tabelle** je Plattform mit Quelle, Zeitraum, Formel.
2. Ein **datierter Rohdaten-Ordner** mit Exporten und Screenshots.
3. Eine **Top-Content-Liste** je Plattform (Top 5 bis 10) mit Kennzahlen.

Diese Zahlen werden in Säule 03 dem Wettbewerb gegenübergestellt und in Säule 04 bewertet. Hier wird nur erhoben und gesichert, nicht interpretiert.
