# Primärquellen: Vorträge und Keynotes

**Stand:** Juli 2026
**Scope:** Fachvorträge, Keynotes und Panels, die als benannte Primärquelle in die Wissensbasis eingehen
**Zielanwender:innen:** Orchestrator (Persona Primärquellen-Kurator), Strateg:innen, Content-Planer:innen, Berater:innen im Kundengespräch

Dieses Modul ist anders gebaut als die übrigen. Es enthält kein destilliertes
Methodenwissen, sondern **benannte Quellen mit vollständigem Kontext**. Es
existiert, weil eine Aussage wie "LinkedIn ist die Nummer 1 im B2B bei
KI-Zitierungen" nach drei Monaten sonst als anonymer Fakt durch die Wissensbasis
geistert, ohne dass noch jemand weiß, wer das wann in welchem Kontext gesagt hat.

---

## Inhalt

| Datei | Thema |
|---|---|
| `00_Index.md` | Diese Übersicht, Trigger-Tabelle, Drei-Ebenen-Modell |
| `01_OMR26_Behrens_LinkedIn.md` | Dossier Britta Behrens, "The State of LinkedIn 2026", OMR 2026 |
| `02_OMR26_Raman_FutureOfWork.md` | Dossier Aneesh Raman (LinkedIn), Future of Work, OMR 2026 |
| `03_Anwendungsregeln.md` | Ebene 3: Wenn-Dann-Regeln für die Agenturarbeit |
| `04_Abgleich_bestehende_Module.md` | Was bestätigt, ergänzt oder widerspricht dem bisherigen Wissensstand |
| `05_Failure-Modi.md` | Typische Fehlinterpretationen genau dieser beiden Quellen |
| `06_Quellen.md` | Quellen mit Konfidenz-Label, inkl. externer Gegenprüfung |
| `transkripte/01_OMR26_Behrens_transkript.md` | Volltranskript mit Zeitmarken |
| `transkripte/02_OMR26_Raman_transkript.md` | Volltranskript mit Zeitmarken |

---

## Das Drei-Ebenen-Modell

Der Zweck dieses Moduls ist, zwei Anforderungen gleichzeitig zu erfüllen, die
sich normalerweise ausschließen: **nichts verlieren** und **schnell anwendbar
sein**. Das geht nur über getrennte Ebenen.

| Ebene | Was | Wo | Wird gelesen wenn |
|---|---|---|---|
| **1 Quelle** | Unveränderter Originalwortlaut mit Zeitmarken | `transkripte/` | Eine Aussage angezweifelt oder wörtlich zitiert wird |
| **2 Aussage** | Atomare Einzelaussagen, jede mit Herkunftsstempel und Belegstatus | `01_`, `02_` | Man den Argumentationsbogen oder eine konkrete Zahl braucht |
| **3 Regel** | Was sich dadurch an unserer Arbeit ändert, als Wenn-Dann-Regel | `03_` | Man operativ etwas entscheidet |

**Im Normalbetrieb wird nur Ebene 3 gelesen.** Ebene 2 bei Rückfragen, Ebene 1
bei Zweifel. Wer Ebene 3 zitiert, ohne Ebene 2 geprüft zu haben, riskiert genau
den Fehler, den dieses Modul verhindern soll.

### Herkunftsstempel

Jede Aussage in Ebene 2 und 3 trägt einen Stempel:

- `[B 9:29]` = Behrens, Video-Zeitmarke 9:29
- `[R 12:50]` = Raman, Video-Zeitmarke 12:50

Damit ist jede Ableitung in einem Schritt zum Originalwortlaut rückverfolgbar.
Zeitmarken im Transkript stehen etwa alle 30 bis 40 Sekunden, der Stempel
verweist auf die nächstliegende vorangehende Marke.

### Belegstatus

Neben dem Herkunftsstempel trägt jede Aussage einen Status. Das ist der
wichtigste Mechanismus gegen Fehlinterpretation, weil er verhindert, dass die
Meinung eines Speakers zum Fakt aufsteigt.

| Status | Bedeutung |
|---|---|
| **plattformoffiziell** | Von LinkedIn selbst kommuniziert (Blog, Interview, offizieller Sprecher im Einspieler) |
| **extern verifiziert** | Von uns unabhängig an einer Drittquelle gegengeprüft, Quelle in `06_Quellen.md` |
| **Sprecherangabe** | Der Speaker sagt es, wir haben es nicht gegengeprüft. Zitierfähig nur mit Namensnennung |
| **Meinung** | Bewertung oder Empfehlung des Speakers. Keine Tatsachenbehauptung |
| **Ableitung** | Unsere eigene Schlussfolgerung. Steht nicht so im Vortrag |

---

## Trigger-Tabelle: Wann ziehe ich dieses Modul?

Diese Tabelle ist der eigentliche Abrufweg. Sie beschreibt Anlässe, nicht Themen,
damit die Entscheidung zum Ziehen fällt, **bevor** der Inhalt gelesen wurde.

| Anlass | Zieh diese Datei | Konkret |
|---|---|---|
| Kunde nennt Reichweite oder Impressionen als Ziel auf LinkedIn | `03_` Regel R1 | Impact statt Impressionen, Messgröße ist keine KPI |
| LinkedIn-Content-Strategie oder Redaktionsplan wird gebaut | `03_` R2, R3 | Thought Leadership als tragende Säule, Kontinuität schlägt Viralität |
| Frage nach KI-Sichtbarkeit, GEO, AEO, "wie komme ich in ChatGPT" | `03_` R3, R4, dazu `KI_Sichtbarkeit_Guide/` | LinkedIn Platz 2 aller Zitierquellen, Schwerpunkt B2B |
| Jemand nennt eine Follower-Schwelle für KI-Sichtbarkeit | `05_` FM-10 | Die 2.000-Follower-Zahl ist falsch zugeordnet |
| Jemand erwähnt "360 Brew" | `03_` R11, `05_` FM-1 | Der Name existiert nicht. Sofort korrigieren |
| Automatisierungs- oder Outreach-Tool wird vorgeschlagen | `03_` R5 | Sperrrisiko, Sichtbarkeitsverlust, Reputationsschaden |
| Corporate-Influencer-Programm wird gepitcht oder verteidigt | `03_` R6, dazu `Corporate_Influencing_Employee_Advocacy/` | Beispielrechnung, vier Impact-Faktoren |
| Management fragt "was bringt das denn" bei Personenmarken | `03_` R6, `01_` Abschnitt Key People Indicator | TKP-Äquivalent plus Recruiting plus Fluktuation |
| Link-Platzierung im Post oder im ersten Kommentar | `03_` R7 | Link in den Beitrag |
| Employer Branding, Recruiting, Skills-Argumentation | `03_` R8, R9, `02_` | Skills statt Titel, 70-Prozent-Zahl, Climbing Wall |
| KI-Einsatz im eigenen Team oder beim Kunden wird strukturiert | `03_` R10, `02_` Drei-Buckets | Bucket 1 bis 3, Cognitive Debt |
| Argumente gegen AI Slop werden gebraucht | `03_` R5, `01_`, `02_` | Zwei unabhängige Quellen sagen dasselbe |
| Jemand zitiert eine der beiden Keynotes | `05_` gesamt | Erst Failure-Modi prüfen, dann zitieren |

---

## Aufnahmekriterium für weitere Vorträge

Damit dieses Modul nicht zur Materialhalde wird, gilt: Ein Vortrag kommt nur
hinein, wenn er mindestens eines erfüllt.

1. Er enthält eine **Zahl oder Aussage einer Plattform über sich selbst**, die
   nirgends sonst so klar dokumentiert ist.
2. Er **korrigiert einen verbreiteten Irrtum** in unserem Feld.
3. Er liefert eine **Argumentationslinie**, die wir im Kundengespräch brauchen
   und die ohne den Kontext des Vortrags nicht funktioniert.

Reine Trend- oder Motivationsvorträge ohne Beleglage gehören nicht hierher.

---

## Pflegehinweis

Aussagen mit Status **Sprecherangabe** sollten bei nächster Gelegenheit
gegengeprüft und hochgestuft oder verworfen werden. Die offene Liste steht am
Ende von `06_Quellen.md`.

Aussagen zu Algorithmus und Plattformverhalten veralten schnell. Beide Vorträge
stammen vom **6. Mai 2026**. Ab etwa Frühjahr 2027 ist der Algorithmus-Teil als
historischer Stand zu lesen, die Prinzipien-Teile bleiben länger tragfähig.
