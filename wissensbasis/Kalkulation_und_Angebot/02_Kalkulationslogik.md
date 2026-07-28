# Säule 2: Kalkulationslogik

Von Stunden zu Preis. Diese Säule beantwortet: **Was muss die Stunde kosten, damit es sich trägt, und wie wird daraus ein Angebotspreis?**

Hier stehen Rechenwege und Regeln, keine konkreten Sätze. Der eigene Satz ist eine unternehmerische Entscheidung, siehe `00_Index.md`.

---

## Die vier Zahlen, die man auseinanderhalten muss

Sie werden regelmäßig verwechselt, und jede Verwechslung kostet Geld.

| Zahl | Definition | Wofür |
|---|---|---|
| **Kostensatz** | Was eine Arbeitsstunde die Agentur kostet, inklusive Gemeinkosten | Untergrenze, darf nie unterschritten werden |
| **Zielsatz** | Kostensatz plus gewünschter Gewinn | interne Kalkulationsbasis |
| **Angebotssatz** | Was im Angebot steht oder implizit drinsteckt | Verhandlungsgröße |
| **Realisierter Satz** | Angebotssumme geteilt durch tatsächlich geleistete Stunden | die einzige Zahl, die die Wahrheit sagt |

**Der realisierte Satz ist die Kennzahl, die zählt.** Ein Angebot mit 120 € Angebotssatz, das durch drei ungeplante Korrekturschleifen 40 Prozent mehr Stunden verbraucht, hat einen realisierten Satz von rund 86 €. Ob das noch trägt, weiß nur wer den Kostensatz kennt.

---

## Kostensatz: der Rechenweg

Der Kostensatz ist keine Meinung, er ist eine Division. Zwei Größen braucht man.

### Größe 1: Jahreskosten einer produktiven Person

Was eine Vollzeitstelle im Jahr wirklich kostet, inklusive Lohnnebenkosten, Arbeitsplatz, Tools, Fortbildung. Marktreferenzen aus verifizierten Quellen:

| Referenz | Wert | Quelle |
|---|---|---|
| Interne Marketing-Vollzeitstelle, Vollkosten | 80.000 bis 110.000 € pro Jahr | designenergie, Mai 2026 |
| Senior Content Creator, Vollkosten | 65.000 bis 90.000 € pro Jahr | chaerry, Juni 2026 |
| Junior Content Creator, Vollkosten | 45.000 bis 55.000 € pro Jahr | chaerry, Juni 2026 |

Die Spanne zwischen den beiden Quellen ist erklärbar: Die höhere Zahl umfasst zusätzlich Arbeitsplatz, Tools und Fortbildung, die niedrigere primär Personalkosten. Für einen Kostensatz braucht man die Vollkostenvariante.

Dazu kommen Gemeinkosten, die sich nicht einer Person zuordnen lassen: Miete, Versicherungen, Buchhaltung, Software-Lizenzen, Vertrieb und Akquise, nicht abrechenbare Zeit der Geschäftsführung. Diese werden auf die produktiven Stunden umgelegt.

**Referenz für Tool-Kosten:** Social-Media-Management-Tools kosten kleine Teams 30 bis 100 € pro Monat, größere Agenturen mehrere Hundert (agenturfinder, Juli 2026). KI-Tool-Stacks für Bild und Video liegen je Ausbaustufe bei 50 bis 500 US-Dollar pro Monat, siehe `Visual_Production_Methodik/03_KI-Tools-Stack_Bild_Video.md`.

### Größe 2: Verrechenbare Stunden pro Jahr

Hier passiert der häufigste Kalkulationsfehler: Man rechnet mit zu vielen.

| Position | Stunden |
|---|---|
| Kalendertage im Jahr, abzüglich Wochenenden | circa 252 Tage |
| abzüglich Feiertage (regional unterschiedlich) | circa 10 bis 13 Tage |
| abzüglich Urlaub | circa 25 bis 30 Tage |
| abzüglich Krankheit (statistischer Erfahrungswert) | circa 8 bis 15 Tage |
| **verbleibende Arbeitstage** | **circa 195 bis 210** |
| Bruttostunden bei 8 Stunden | circa 1.560 bis 1.680 |

Davon ist aber nur ein Teil beim Kunden abrechenbar. Der Rest geht in interne Abstimmung, Akquise, Angebotsschreiben, Weiterbildung, Tool-Pflege, Leerlauf zwischen Projekten.

**Auslastungsquote:** Der Anteil abrechenbarer an gesamten Arbeitsstunden. In Agenturen liegt sie erfahrungsgemäß bei 60 bis 75 Prozent, in kleineren Einheiten mit hohem Vertriebsanteil niedriger. Belegstatus C, das ist eine Erfahrungsgröße, kein Branchenreport.

**Rechenbeispiel, rein illustrativ:**

```
Vollkosten Person:            90.000 €
Gemeinkostenumlage (30 %):    27.000 €
Gesamtkosten:                117.000 €

Bruttostunden:                 1.600 h
Auslastung 65 %:               1.040 h abrechenbar

Kostensatz: 117.000 / 1.040 = circa 113 € pro Stunde
```

**Was diese Rechnung zeigt:** Der Kostensatz liegt deutlich über dem, was viele intuitiv annehmen. Bei einer Auslastung von 50 statt 65 Prozent steigt er auf rund 146 €. Auslastung ist der stärkste Hebel im Kostensatz, stärker als das Gehalt.

**Wichtig:** Die Zahlen im Beispiel sind Platzhalter. Der eigene Kostensatz muss mit den eigenen Werten gerechnet werden.

---

## Marktvergleich: liegt der eigene Satz im Rahmen?

Verifizierte Marktspannen für Agentur-Stundensätze, Stand Juli 2026:

| Markt | Stundensatz |
|---|---|
| Deutschland | circa 60 bis 180 € |
| Österreich | circa 60 bis 160 € |
| Schweiz | circa 100 bis 250 CHF |

Quelle: agenturfinder, Stand 6. Juli 2026, Belegstatus A.

**Wie diese Spanne zu lesen ist:** Sie ist breit, weil sie Seniorität, Spezialisierung, Agenturgröße und Region zusammenwirft. Der untere Rand von 60 € liegt für eine Agentur mit Vollkosten nahe oder unter dem Kostensatz aus dem Rechenbeispiel oben. Das ist ein Hinweis darauf, dass Angebote am unteren Rand entweder mit Juniors besetzt, sehr hoch ausgelastet oder unrentabel sind.

**Sanity Check:** Liegt der eigene Kostensatz über dem Marktmittel, gibt es drei Erklärungen. Erstens hohe Seniorität, dann muss die im Angebot als Wert kommuniziert werden. Zweitens niedrige Auslastung, dann ist es ein Vertriebs- oder Kapazitätsproblem, kein Preisproblem. Drittens hohe Gemeinkosten, dann ist es ein Strukturproblem. Nur im ersten Fall ist der Preis die Lösung.

---

## Von Kostensatz zu Angebotspreis

Vier Wege, in absteigender Verbreitung im Markt.

### Weg 1: Aufwandsbasiert, Stunden mal Zielsatz

Am transparentesten, am leichtesten nachzukalkulieren, am angreifbarsten in der Verhandlung. Der Kunde diskutiert dann über Stunden statt über Wert.

Geeignet für: klar abgegrenzte Projekte, Beratungsleistung, alles wo der Umfang vorab bekannt ist.

### Weg 2: Paketpreis mit definiertem Output

Preis steht fest, Leistung ist als Menge definiert. Intern trotzdem in Stunden gerechnet, nach außen nicht ausgewiesen.

Der Markt macht das offen so: Ein Anbieter im KMU-Segment kommuniziert ausdrücklich "kein Stundensatz-Versteckspiel", nennt aber genaue Mengen pro Paket und keine Stundensätze (designenergie, Mai 2026). Gleichzeitig beschreibt ein Agenturvermittler, dass Retainer intern meist nach Stunden kalkuliert werden (agenturfinder, Juli 2026). Beides ist kein Widerspruch, sondern die Trennung von Innenrechnung und Außenkommunikation.

Geeignet für: laufende Betreuung, wiederkehrende Produktion, alles was standardisierbar ist.

**Bedingung:** Der Output muss in Mengen definiert sein, sonst ist der Paketpreis eine offene Flanke. Siehe `04_Scoping_und_Annahmen.md`.

### Weg 3: Wertbasiert

Preis leitet sich vom Nutzen für den Kunden ab, nicht vom Aufwand. Der Aufwand bleibt die Untergrenze.

Geeignet für: Leistungen mit klar zurechenbarem Geschäftswert, hoher Spezialisierung, starker Marktposition.

**Bedingung:** Der Wert muss argumentierbar sein. "Das ist uns mehr wert" reicht nicht. Belegbar wird es über die Alternative: Eine interne Vollzeitstelle kostet 80.000 bis 110.000 € pro Jahr, ein Full-Retainer im KMU-Segment 24.000 € pro Jahr (designenergie, Mai 2026). Diese Gegenrechnung ist das stärkste wertbasierte Argument, das die Recherche hergibt, weil sie mit einer Zahl arbeitet, die der Kunde selbst kennt.

### Weg 4: Erfolgsbasiert

Vergütung an Ergebnis gekoppelt. Marktübliche Varianten:

| Variante | Marktspanne |
|---|---|
| Prozent des Mediabudgets | 10 bis 15 % |
| Prozent des Kampagnenbudgets bei Influencer-Kampagnen | 10 bis 30 % |
| Cost per Lead | fallabhängig |

Quelle: agenturfinder, Juli 2026, Belegstatus A.

**Warnung aus der Quelle:** Erfolgsbasierte Modelle werden von vielen Agenturen erst nach einer Testphase und meist nur für etablierte Unternehmen angeboten. Der Grund ist Messbarkeit.

**Zusätzliche Warnung aus der eigenen Wissensbasis:** Erfolgsbasierte Modelle setzen sauberes Tracking voraus. Ohne Conversion-Tracking ist die Bemessungsgrundlage nicht belastbar, siehe `Paid_Performance_Methodik/06_Optimierung_und_Metriken.md` und `Measurement_Reporting_Guide/05_Attribution_und_ROI.md`. Und: Ein prozentualer Anteil am Mediabudget setzt einen Fehlanreiz, weil höheres Budget die Vergütung erhöht, unabhängig von der Effizienz.

---

## Die Deckungsbeitrags-Frage

Nicht jedes Projekt muss den vollen Zielsatz erreichen. Aber jedes muss über dem reinen Personalkostenanteil liegen, sonst subventioniert die Agentur den Kunden.

**Regel:** Ein Projekt unter Kostensatz ist eine Investitionsentscheidung, die man treffen darf, wenn man sie benennt. Typische legitime Gründe: Referenz in einer neuen Branche, Türöffner für ein größeres Folgemandat, Auslastung einer sonst leerlaufenden Kapazität.

**Nicht legitim:** "Sonst bekommen wir den Auftrag nicht." Das ist keine Investitionsentscheidung, sondern Preisverfall.

**Prüffrage vor jedem Rabatt:** Was genau ist der Gegenwert, und wann wird er fällig? Lässt sich das nicht beantworten, ist der Rabatt keine Investition.

---

## Nachkalkulation: der einzige Weg, besser zu werden

Ohne Nachkalkulation ist jede Schätzung dauerhaft eine Vermutung.

**Minimalversion, die reicht:** Pro abgeschlossenem Projekt eine Zeile mit angebotener Summe, geschätzten Stunden, Ist-Stunden, realisiertem Satz, und einem Satz zur Hauptabweichung.

**Was man daraus liest:**

| Befund | Was es bedeutet | Was zu tun ist |
|---|---|---|
| Ist-Stunden systematisch über Schätzung | Schätzungs-Bias | Faktor auf die Schätzung legen, siehe `01_Aufwandsrichtwerte.md` |
| Abweichung konzentriert auf Abstimmung und Korrekturen | Scoping-Problem | Inklusiv-Grenzen ins Angebot, siehe `04_Scoping_und_Annahmen.md` |
| Realisierter Satz unter Kostensatz | Projekt war unrentabel | Ursache klären, bevor ein Folgeangebot rausgeht |
| Streuung sehr hoch bei ähnlichen Projekten | Prozessproblem, nicht Preisproblem | siehe `Projektbetrieb_und_Freigaben/` |

**Wann man aufhört zu optimieren:** Wenn die Abweichung zwischen Schätzung und Ist bei vergleichbaren Projekten unter etwa 20 Prozent liegt, ist die Schätzung gut genug. Mehr Präzision kostet mehr Erfassungsaufwand als sie einbringt.

---

## Verweise

- Stunden je Leistung: `01_Aufwandsrichtwerte.md`
- Marktpreise als Paket und Retainer: `03_Preismodelle_und_Marktbenchmarks.md`
- Scope-Grenzen, die die Kalkulation schützen: `04_Scoping_und_Annahmen.md`
- Typische Rechenfehler: `06_Failure-Modi.md`
- ROAS gegen ROI: `Measurement_Reporting_Guide/05_Attribution_und_ROI.md`
