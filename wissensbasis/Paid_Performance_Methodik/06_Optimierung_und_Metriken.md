# Säule 6: Optimierung & Metriken

Die meisten Paid-Accounts verlieren Geld nicht an schlechten Creatives, sondern an nervösem Eingreifen. Diese Säule erklärt die Kernmetriken, die Lernphase und die schwierigste Disziplin im Performance-Marketing: **wann man eingreift und wann man die Finger stillhält.**

---

## Die Kernmetriken

| Metrik | Berechnung | Was sie sagt | Funnel-Stufe |
|---|---|---|---|
| **CPM** | Kosten pro 1.000 Impressionen | Wie teuer ist Reichweite, wie effizient das Creative-Signal | alle |
| **CPC** | Kosten pro Klick | Wie gut zieht das Creative zur Aktion | TOFU/MOFU |
| **CTR** | Klicks / Impressionen | Relevanz und Anziehungskraft des Creatives | alle |
| **Hook-Rate** | 3-Sek-Views / Impressionen | Halten die ersten 3 Sekunden (siehe Säule 04) | alle (Video) |
| **CPA** | Kosten pro Conversion / Akquisition | Effizienz auf das eigentliche Ziel | BOFU |
| **CPL** | Kosten pro Lead | Effizienz der Lead-Gen | B2B / MOFU |
| **ROAS** | Umsatz / Werbeausgaben | Rentabilität | BOFU |
| **Frequency** | Ø Impressionen pro Person | Fatigue-Frühwarnung (siehe Säule 05) | Retargeting |

### Die wichtigste Unterscheidung: Steuer- gegen Ergebnis-Metriken

> **ROAS ist ein Ergebnis der Vergangenheit, das man am Monatsende kennt. Gesteuert wird täglich über CPA, CPM und Frequency.**

ROAS sagt, ob es funktioniert hat. CPM, CPC, Hook-Rate und Frequency sagen, **warum** und geben Handlungsrichtung. Wer nur auf ROAS starrt, reagiert immer zu spät.

### Diagnose über die Metrik-Kette

Eine schwache Conversion-Performance hat eine Ursache irgendwo in der Kette. Man liest sie von vorne:

| Wo bricht es | Symptom | Wahrscheinliche Ursache |
|---|---|---|
| **CPM hoch** | Reichweite teuer | Creative-Signal schwach, Audience zu eng, hohe Auktions-Konkurrenz |
| **Hook-Rate niedrig** | Niemand bleibt | Hook schwach (siehe Säule 04) |
| **CTR niedrig** | Kein Klick | Angle/Botschaft trifft nicht |
| **CPC ok, CPA hoch** | Klick ja, Conversion nein | Landingpage, Angebot oder falsches Optimierungs-Event |

---

## Die Lernphase

Jede Kampagne durchläuft eine Lernphase, in der der Algorithmus die optimale Aussteuerung sucht. Bei Meta gilt als Richtwert: **circa 50 Optimierungs-Events (Conversions) pro Woche pro Ad-Set**, um die Lernphase zu verlassen.

### Drei Regeln zur Lernphase

1. **Performance in der Lernphase ist volatil und KEINE Entscheidungsgrundlage.** CPMs sind hier typischerweise höher, weil der Algorithmus bewusst ineffizient ausliefert, um Signal zu sammeln. Performance verbessert sich meist deutlich, sobald die Phase abgeschlossen ist.
2. **Nicht eingreifen während des Lernens.** Jede substanzielle Änderung (Budget, Zielgruppe, Creative, Optimierungs-Event) kann die Lernphase zurücksetzen.
3. **Die 50 sind eine Richtgröße, keine Garantie.** Sie sind das Mindest-Signalvolumen für statistisch verlässliche Entscheidungen, nicht ein Versprechen auf stabile Performance.

### "Learning Limited"

Wenn ein Ad-Set in "Learning Limited" hängt, sagt der Algorithmus: das aktuelle Setup liefert zu wenig Signal. Das löst sich **nicht** durch Geduld, sondern braucht eine strukturelle Korrektur. Entscheidungsbaum:

| Frage | Wenn ja → Maßnahme |
|---|---|
| **Ist das Budget zu klein?** | Budget erhöhen oder auf ein häufigeres Optimierungs-Event wechseln |
| **Ist die Audience zu eng?** | Audience verbreitern oder auf Advantage+ wechseln (siehe Säule 03) |
| **Ist Creative/Angebot zu schwach?** | CTR und Hook-Rate prüfen, Creative überarbeiten (siehe Säule 04) |

---

## Wann eingreifen, wann nicht

> **Die teuerste Handlung im Paid-Bereich ist das Eingreifen aus Nervosität.**

### Nicht eingreifen, wenn:

- Die Kampagne noch in der Lernphase ist (Performance ist hier per Definition unzuverlässig)
- Es weniger als 7 bis 10 Tage Daten gibt
- Die Schwankung normales Rauschen ist (einzelner schlechter Tag)
- Man nur die Metrik nicht mag, aber keine Ursache benennen kann

### Eingreifen, wenn:

- Die Lernphase abgeschlossen ist UND CPA/ROAS außerhalb des Zielkorridors liegen
- 7 bis 10 Tage stabile Daten einen klaren Trend zeigen (nicht einen Ausreißer)
- Ein Fatigue-Signal vorliegt (steigende Frequency, fallende CTR über 7 bis 14 Tage)
- Eine Ursache klar benannt werden kann (siehe Metrik-Kette oben)

### Wie eingreifen

- **Budget:** in 10-20-%-Schritten alle 48 bis 72 Std., nicht abrupt (siehe Säule 02)
- **Creative:** neue Varianten dazustellen statt den Gewinner zu töten
- **Eine Änderung zur Zeit**, sonst weiß man nicht, was gewirkt hat (gleiche Logik wie Creative-Testing, Säule 04)

---

## Tracking als Voraussetzung

Optimierung ohne sauberes Tracking ist wertlos: Der Algorithmus optimiert ins Leere und die Auswertung lügt.

| Baustein | Zweck |
|---|---|
| **Pixel / Tag** | Browserseitiges Event-Tracking |
| **Conversions API / serverseitig** | Rückgewinnung von Signal nach iOS-/Browser-Signalverlust (siehe Säule 03) |
| **Korrektes Optimierungs-Event** | Auf das richtige Event optimieren (z. B. Kauf, nicht "Add to Cart"), sonst kauft man günstige, aber wertlose Signale |
| **Consent-Management (DACH)** | DSGVO-konform, Voraussetzung für rechtssicheres Tracking |

**Häufiger Fehler:** Auf "Add to Cart" optimieren, während der Checkout-Abbruch hoch ist. Man kauft scheinbar günstige Signale, aber keinen Umsatz.

---

## Checkliste Optimierung

- [ ] Tracking steht (Pixel + Conversions API + korrektes Event + Consent)
- [ ] Steuer-Metriken (CPM, CPC, Hook-Rate, Frequency) täglich, ROAS als Ergebnis betrachtet
- [ ] Lernphase respektiert, kein Eingreifen während des Lernens
- [ ] Mindestens 7 bis 10 Tage Daten vor jeder Entscheidung
- [ ] Vor jedem Eingriff: Ursache über die Metrik-Kette benannt
- [ ] Eine Änderung zur Zeit
- [ ] Budget-Änderungen schrittweise, nicht abrupt
- [ ] "Learning Limited" strukturell gelöst, nicht ausgesessen

---

## Verweis

Plattformspezifische Benchmarks (CPM/CPC/CPA/ROAS je Branche und Land) und Pixel-Setup stehen in den Plattform-Ordnern. Diese Säule liefert die übergreifende Mess- und Optimierungs-Methodik.
