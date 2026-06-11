# Säule 2 - Metriken-Definitionen und Berechnungsformeln

Diese Säule ist das Glossar. Sie definiert jede Kernmetrik sauber und nennt die Formel. Ziel: dass im Report jede Zahl dieselbe Bedeutung hat, egal wer sie zieht. Die häufigste Quelle für falsche Schlüsse ist, dass zwei Leute „Engagement-Rate" sagen und Verschiedenes meinen.

---

## Reichweiten-Metriken

### Reach (Reichweite)
**Definition:** Anzahl der **einzigartigen** Nutzer:innen, die einen Inhalt mindestens einmal gesehen haben.
**Besonderheit:** Reach zählt jede Person nur einmal, unabhängig davon, wie oft sie den Inhalt sah.

### Impressionen
**Definition:** **Gesamtzahl** der Ausspielungen, inklusive Mehrfach-Ansichten durch dieselbe Person.
**Verhältnis zu Reach:** Impressionen sind immer gleich hoch oder höher als Reach.
**Lesehilfe:** 10.000 Impressionen bei 2.000 Reach bedeutet, dass dieselben 2.000 Menschen den Content im Schnitt fünfmal gesehen haben. Frequenz = Impressionen / Reach.

---

## Engagement-Metriken

### Engagement (absolut)
**Definition:** Summe der aktiven Interaktionen: Likes, Kommentare, Shares, Saves und je nach Plattform Klicks.
**Warnung:** Welche Interaktionen mitgezählt werden, ist plattform- und tool-abhängig. Vor jedem Vergleich offenlegen, was in der Summe steckt.

### Engagement-Rate (drei Varianten)
Es gibt nicht *die* Engagement-Rate. Drei gängige Berechnungsbasen, die zu deutlich unterschiedlichen Werten führen:

| Variante | Formel | Wann nutzen |
|---|---|---|
| **ER by Reach (ERR)** | (Engagements / Reach) x 100 | Genaueste Variante, wenn Reach verfügbar. Standard auf Instagram. |
| **ER by Impressions** | (Engagements / Impressionen) x 100 | Konservativster Wert, da Impressionen am höchsten. |
| **ER by Followers** | (Engagements / Follower) x 100 | Für Account-Vergleich, aber verzerrt bei viralen Posts und bei Reichweite außerhalb der Follower. |

**Regel für den Report:** Eine Variante festlegen, dokumentieren und konsequent halten. Beim Plattform-Vergleich immer die Berechnungsbasis dazuschreiben.

### Saves (Speichern)
**Definition:** Eine Nutzerin hat den Inhalt zum späteren Wiederfinden gespeichert.
**Bedeutung:** Starkes Qualitätssignal. Ein Save signalisiert höheren wahrgenommenen Wert als ein Like, weil er eine Wieder-Nutzung impliziert. Auf Instagram und TikTok ein Ranking-relevantes Signal.

### Sends / Shares (Weiterleiten / Teilen)
**Definition:** Weiterleitung des Inhalts an andere, per DM (Sends) oder öffentlich (Shares).
**Bedeutung:** Stärkstes Reach-Signal. Sends gelten auf Instagram aktuell als wichtigster Treiber organischer Reichweite. Teilbarkeit ist ein direkter MOFU-Indikator.

---

## Bewegtbild-Metriken

### Video View
**Definition:** Achtung, Plattform-abhängig. Ein „View" zählt je nach Plattform nach unterschiedlicher Dauer (z.B. bereits ab dem Anspielen, ab 2 oder 3 Sekunden). Vor jedem Vergleich die Definition prüfen.

### Watchtime (Wiedergabezeit)
**Definition:** Gesamte oder durchschnittliche Zeit, die mit dem Ansehen verbracht wurde.
**Bedeutung:** Zentrale Ranking-Größe auf YouTube und TikTok. Misst Tiefe statt nur Breite der Aufmerksamkeit.

### Retention / Completion Rate
**Definition:** Retention zeigt, welcher Anteil der Zuschauer:innen über die Video-Länge erhalten bleibt. Completion Rate = Anteil, der bis zum Ende schaut.
**Formel Completion Rate:** (Vollständige Ansichten / Gesamt-Views) x 100.
**Bedeutung:** Bester Qualitäts-Indikator für Bewegtbild. Ein starker Abfall in den ersten Sekunden weist auf einen schwachen Hook hin.

---

## Klick- und Conversion-Metriken

### CTR (Click-Through-Rate)
**Definition:** Anteil der Ansichten, die zu einem Klick führten.
**Formel:** (Klicks / Impressionen) x 100.
**Beispiel:** 1.000 Impressionen, 50 Klicks = 5 Prozent CTR.
**Abgrenzung:** CTR misst nur Klicks, Engagement-Rate misst alle Interaktionen. Hohe Engagement-Rate bei niedriger CTR bedeutet: interessant, aber nicht handlungsauslösend.

### Conversion-Rate
**Definition:** Anteil der Nutzer:innen, die nach dem Klick die definierte Zielhandlung ausführen (Kauf, Anmeldung, Download).
**Formel:** (Conversions / Klicks oder Sitzungen) x 100.
**Voraussetzung:** Ein klar definiertes Conversion-Ereignis und ein Tracking, das es erfasst (siehe Säule 05).

### CPA, CPM, CPC (Kosten-Metriken, bei Paid)
| Metrik | Formel | Bedeutung |
|---|---|---|
| CPM | (Kosten / Impressionen) x 1.000 | Kosten pro 1.000 Kontakte (Reichweiten-Effizienz) |
| CPC | Kosten / Klicks | Kosten pro Klick (Traffic-Effizienz) |
| CPA | Kosten / Conversions | Kosten pro Conversion (BOFU-Effizienz) |

---

## Plattformspezifische Besonderheiten

Dieselbe Metrik heißt nicht überall gleich oder rechnet nicht gleich. Die wichtigsten Stolpersteine:

| Plattform | Besonderheit | Konsequenz fürs Reporting |
|---|---|---|
| **Instagram** | Views sind seit August 2024 die primäre Metrik (statt Likes/Reach). Engagement-Rate üblich auf Reach-Basis. Sends sind das stärkste Reach-Signal. | „Views" nicht mit „Reach" verwechseln. |
| **TikTok** | Engagement-Rate üblich auf Follower-Basis, dieselbe Berechnungsgrundlage wie bei Instagram und Facebook. Watchtime und Completion zentral. | TikTok-Engagement-Rate liegt real deutlich höher als bei Instagram und Facebook, nicht wegen einer anderen Berechnungsbasis. |
| **LinkedIn** | Engagement-Rate oft auf Impressionen. Karussells und Dokumente performen deutlich über Video. | B2B-Benchmark gilt, nicht B2C. Format-Unterschiede mitdenken. |
| **YouTube** | Watchtime und durchschnittliche Wiedergabedauer sind die Leitgrößen, nicht Views allein. | Views ohne Watchtime sind eine Vanity-Zahl. |
| **Facebook** | Organische Reichweite stark gesunken, Engagement-Raten niedrig. | Niedrige Werte nicht als Versagen lesen, Benchmark beachten (Säule 04). |
| **X (Twitter)** | Impressionen prominent, Engagement-Rate auf Impressions-Basis. | Hohe Impressionen, niedrige Interaktion ist normal. |

**Faustregel:** Vor jedem plattformübergreifenden Vergleich in einer Fußnote festhalten, auf welcher Basis die jeweilige Rate berechnet ist. Das ist der wichtigste Schutz vor falschen Schlüssen im Cross-Channel-Report.
