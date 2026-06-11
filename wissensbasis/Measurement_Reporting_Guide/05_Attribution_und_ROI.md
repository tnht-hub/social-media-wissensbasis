# Säule 5 - Attribution und ROI

Diese Säule verbindet Social-Media-Aktivität mit Geschäftswert: Welcher Kanal hat welche Conversion verdient (Attribution), und was hat sie eingebracht (ROAS/ROI). Und ehrlich: wo die Messung an ihre Grenzen stößt.

---

## Attribution: Wer bekommt die Gutschrift?

Attribution ist die Zuordnung einer Conversion zu den Berührungspunkten (Touchpoints) auf dem Weg dorthin. Das Problem: Eine Conversion hat heute selten einen einzigen Auslöser. B2B-Käufe durchlaufen im Schnitt sechs bis acht Touchpoints, Enterprise-Käufe zehn und mehr.

### Die Attributions-Modelle im Überblick

| Modell | Wie es Gutschrift verteilt | Stärke | Schwäche |
|---|---|---|---|
| **First-Click** | 100 % an den ersten Touchpoint | Zeigt, was Aufmerksamkeit erzeugt (TOFU) | Ignoriert alles danach |
| **Last-Click** | 100 % an den letzten Touchpoint | Einfach, Standard vieler Tools | Überschätzt BOFU, unterschätzt Awareness völlig |
| **Linear** | Gleich verteilt über alle Touchpoints | Fair, einfach | Behandelt schwache und starke Touchpoints gleich |
| **Time-Decay** | Mehr Gewicht für spätere Touchpoints | Realistisch für kurze Zyklen | Unterschätzt frühe Awareness |
| **Position-Based (U / W)** | Mehr Gewicht für ersten und letzten (plus Lead) | Würdigt Anfang und Abschluss | Mittelteil wird systematisch klein gerechnet |
| **Data-Driven** | Algorithmus verteilt nach beobachtetem Beitrag | Genaueste Variante, GA4-Standard | Braucht Datenvolumen, Blackbox |

### Welches Modell wählen?

Die Wahl hängt von drei Faktoren ab: **Länge des Kaufzyklus**, **Kanal-Mix** und **Datenvolumen**.
- Kurzer Zyklus, wenige Kanäle: Last-Click oder Time-Decay reichen oft.
- Langer Zyklus, viele Kanäle: Multi-Touch oder Data-Driven.
- Social Media als Awareness-Kanal: Last-Click bestraft Social systematisch, weil der letzte Klick oft Search oder Direct ist. Wer Social nur per Last-Click bewertet, wird seinen Wert dramatisch unterschätzen.

**Wirkung der Modellwahl:** Unternehmen, die von Last-Click auf Multi-Touch wechseln, stellen oft fest, dass 20 bis 30 Prozent ihres Budgets falsch zugeordnet waren. Multi-Touch liefert laut Branchenstudien deutlich genauere ROI-Messung als Single-Touch.

---

## ROAS und ROI

Beide messen den Ertrag, aber unterschiedlich. Verwechslung führt zu falschen Budget-Entscheidungen.

| Kennzahl | Formel | Was sie misst | Bezug |
|---|---|---|---|
| **ROAS** (Return on Ad Spend) | Umsatz aus Werbung / Werbeausgaben | Umsatz-Rückfluss je Werbe-Euro | Nur Media-Spend, vor Kosten |
| **ROI** (Return on Investment) | (Gewinn - Investment) / Investment x 100 | Gewinn relativ zum Gesamteinsatz | Inklusive aller Kosten (Produktion, Honorar, Tools) |

**Beispiel:** Ein ROAS von 4 (vier Euro Umsatz je Euro Werbung) klingt gut. Wenn die Marge aber nur 20 Prozent beträgt und Produktion plus Honorar dazukommen, kann der ROI trotzdem negativ sein. ROAS ist eine Media-Effizienz-Zahl, ROI die Geschäfts-Wahrheit. Im Report beide trennen und nie als Synonym verwenden.

---

## UTM-Parameter: die Basis sauberer Attribution

UTM-Parameter sind Anhänge an eine URL, die einer Web-Analytics-Lösung sagen, woher ein Klick kam. Ohne konsistente UTMs ist kanalgenaue Attribution unmöglich.

| Parameter | Funktion | Beispiel |
|---|---|---|
| `utm_source` | Plattform / Quelle | `instagram` |
| `utm_medium` | Kanal-Typ | `social`, `paid-social` |
| `utm_campaign` | Kampagnen-Name | `fruehjahr-launch-2026` |
| `utm_content` | Variante / Creative | `reel-hook-a` |
| `utm_term` | Keyword (bei Paid Search) | meist leer bei Social |

**Regeln für saubere UTMs:**
- Eine verbindliche Namens-Konvention festlegen (kleinschreiben, Bindestriche, keine Leerzeichen).
- Konsequenz schlägt Kreativität: `social` bleibt immer `social`, nicht mal `Social`, mal `sozial`.
- Eine zentrale UTM-Tabelle führen, damit niemand frei erfindet.
- Inkonsistente UTMs zerstören die Auswertung rückwirkend und sind nicht reparierbar.

---

## Die Grenzen der Messbarkeit

Ein ehrlicher Report benennt, was er nicht messen kann. 2026 ist der unsichtbare Anteil groß und wachsend.

**Dark Social.** Inhalte werden über private Kanäle geteilt: Messenger, DMs, geschlossene Gruppen, zunehmend auch über KI-Assistenten. Dieser Traffic erscheint in der Web-Analytics als „Direct" und ist nicht auf Social rückführbar. Ein erheblicher Teil der Wirkung bleibt damit unsichtbar.

**iOS-Tracking-Opt-out.** Ein hoher Anteil der iOS-Nutzer:innen hat das Tracking deaktiviert. Attributionsfenster wurden verkürzt (bei Meta teils auf sieben Tage). Conversions werden dadurch unterzählt.

**Cookieless Tracking.** Mit dem Rückzug von Third-Party-Cookies verschiebt sich die Messung auf First-Party-Daten, Conversion-APIs und server-seitiges Tracking. Rein cookie-basierte Attribution wird zunehmend lückenhaft.

### Konsequenzen für das Reporting

- **Erwartungen managen:** Klarstellen, dass die berichteten Conversions eine **Untergrenze** sind, nicht die volle Wahrheit.
- **First-Party-Daten priorisieren:** Eigene CRM- und Conversion-Daten sind belastbarer als Plattform-Pixel.
- **Triangulieren:** Plattform-Daten, Web-Analytics und Geschäftszahlen nebeneinanderlegen, statt einer Quelle blind zu vertrauen.
- **Direkte Signale ergänzen:** „Wie sind Sie auf uns aufmerksam geworden?" im Formular oder Self-Reported-Attribution fängt einen Teil des Dark Social ein.
- **Brand-Lift und Korrelation nutzen:** Wenn Awareness-Wirkung nicht klickbar attribuierbar ist, helfen Umfragen und der zeitliche Zusammenhang zwischen Kampagne und Anstieg bei Direct-Traffic oder Branded Search.

**Merksatz:** Attribution ist ein Modell, keine Wahrheit. Jedes Modell trifft eine Annahme darüber, wie Gutschrift fair verteilt wird. Im Report gehört dazu, welches Modell genutzt wurde und welche Annahme es trifft.
