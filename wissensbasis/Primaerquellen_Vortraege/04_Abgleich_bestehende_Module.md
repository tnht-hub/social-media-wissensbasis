# 04 Abgleich mit bestehenden Modulen

**Stand:** Juli 2026

Diese Datei beantwortet eine Frage, die sonst niemand beantwortet: Was macht das
neue Wissen mit dem alten? Ohne sie stünden zwei Wahrheiten unverbunden
nebeneinander, und der Orchestrator würde je nach gezogenem Modul
unterschiedliche Auskünfte geben.

Drei Kategorien: **bestätigt**, **ergänzt**, **widerspricht**.

---

## A. Bestätigt

Fälle, in denen die Keynotes den bestehenden Stand stützen. Kein Handlungsbedarf,
aber die Beleglage wird stärker.

### A1 – Zweistufiges LLM-Ranking

| | |
|---|---|
| **Bestehend** | `linkedin/08-profil-optimierung.md`: LinkedIn betreibt Such- und Empfehlungssystem zweistufig (Retrieval per Embedding, Reranking per SLM), belegt durch LinkedIn-Forschungspublikationen |
| **Keynote** | Behrens: die neue Newsfeed-Architektur ist eine **Two-Stage-Ranking-Architektur** auf LLM-Basis `[B 16:14]`, `[B 18:18]` |
| **Ergebnis** | Richtungsgleich, nicht deckungsgleich. Das bestehende Modul belegt die Zweistufigkeit für AI Job Search, AI People Search und Feed-Retrieval und schränkt selbst ein, dass die Verallgemeinerung keine wörtliche Quellenaussage ist. Behrens spricht vom Newsfeed. Beide beschreiben denselben Aufbau, das Bestandsmodul ist die belastbarere Quelle |

### A2 – Automatisierte Kommentare werden sanktioniert

| | |
|---|---|
| **Bestehend** | `linkedin/01-algorithmus.md`: "Kommentare, die von Automatisierungs-Tools stammen, werden in ihrer Sichtbarkeit reduziert (seit August 2025)" |
| **Keynote** | Behrens spielt O-Ton von Gyanda Sachdeva (VP Product LinkedIn) ein, der **drei** konkrete Maßnahmen nennt `[B 7:01]` bis `[B 8:52]` |
| **Ergebnis** | Bestätigt und **präzisiert**. Siehe B1 |

### A3 – Menschen schlagen Marken

| | |
|---|---|
| **Bestehend** | `linkedin/01-algorithmus.md`, Tabelle Profil vs. Unternehmensseite. `Corporate_Influencing_Employee_Advocacy/00_Index.md`: unter 2 Prozent der Corporate Pages werden im Feed ausgespielt (van der Blom) |
| **Keynote** | Behrens: Menschen kaufen von Menschen und vertrauen Menschen mehr als Logos `[B 22:24]`. Raman: Talent, nicht nur Technologie `[R 18:47]` |
| **Ergebnis** | Bestätigt. Die Keynotes liefern die Argumentation, das bestehende Modul die Zahl |

### A4 – AI Slop wird abgestraft

| | |
|---|---|
| **Bestehend** | `linkedin/01-algorithmus.md`: LinkedIn erkennt generische KI-Inhalte mit 94 Prozent Trefferquote und reduziert Reichweite |
| **Keynote** | Behrens `[B 3:45]`, `[B 5:07]`, Raman `[R 7:05]`, `[R 7:40]` |
| **Ergebnis** | Bestätigt aus zwei unabhängigen Richtungen. Die 94-Prozent-Zahl kommt nicht aus den Keynotes und bleibt beim bestehenden Modul |

### A5 – Profil als Ankerpunkt

| | |
|---|---|
| **Bestehend** | `linkedin/08-profil-optimierung.md`: Profil wird zusammengefasst und als Kontext ins Ranking eingespeist |
| **Keynote** | Behrens: LinkedIn analysiert Profil, Content und sämtliche Aktivitäten, jeden Like, jeden Kommentar `[B 18:59]` |
| **Ergebnis** | Bestätigt. Behrens' Zusatz zu Likes und Kommentaren ist Sprecherangabe, nicht belegt, und sollte nicht als Fakt übernommen werden |

---

## B. Ergänzt

Fälle, in denen die Keynotes echte Lücken schließen.

### B1 – Die drei Maßnahmen gegen automatisierte Kommentare

**Lücke:** `linkedin/01-algorithmus.md` nennt nur "Sichtbarkeit reduziert". Die
Eskalationsstufe bis zur Nutzungseinschränkung fehlt.

**Neu, plattformoffiziell** `[B 7:01]` bis `[B 8:52]`:

1. Entfernung aus der Standardsortierung "Most relevant"
2. Mögliche Entfernung aus dem weiteren Kommentar-Netzwerk
3. Bei Wiederholung: Einschränkung der LinkedIn-Nutzung

**Status:** Querverweis gesetzt in `linkedin/01-algorithmus.md`. Der volle
Wortlaut bleibt im Dossier, damit die Quellenzuordnung nicht verloren geht.

### B2 – LinkedIn im KI-Sichtbarkeit-Guide

**Lücke:** `KI_Sichtbarkeit_Guide/02_Plattform-Matrix.md` führte LinkedIn zwar,
aber mit nur zwei Sätzen, ohne Quellenangabe (Vermerk "Stand der LinkedIn-DB"),
mit der Einstufung "Mittel" und **ohne die B2B-Unterscheidung**. Damit fehlte
genau die Zahl, die im B2B-Kundengespräch zählt.

**Bearbeitet in `KI_Sichtbarkeit_Guide/`:**

- LinkedIn-Abschnitt in `KI_Sichtbarkeit_Guide/02_Plattform-Matrix.md` ausgebaut:
  Semrush-Methodik (325.000 Prompts, Jan bis Feb 2026, 89.000 LinkedIn-URLs),
  Zitieranteil je Modell, semantische Ähnlichkeit, Company Page gegen
  Einzelperson je Modell, Abgrenzung Zitierung gegen Training, Faktorentabelle
- Einstufung in der Überblickstabelle von "Mittel" auf "Hoch (Platz 2 aller
  Domains), Schwerpunkt B2B" korrigiert
- Semrush-Studie und zwei PPC-Land-Artikel in
  `KI_Sichtbarkeit_Guide/05_Quellen.md` nachgetragen, Behrens als Primärquelle
  für die Einordnung ergänzt
- Stand in `KI_Sichtbarkeit_Guide/00_Index.md` und
  `KI_Sichtbarkeit_Guide/05_Quellen.md` auf Juli 2026 gezogen

**Wichtig zur B2B-Aussage:** Die Studie weist **kein** B2B-Ranking aus. Sie sagt
nur, der Effekt gelte besonders für professionelle und B2B-Kategorien. Behrens'
"im B2B Nummer 1" `[B 10:09]` ist Sprecherangabe und wurde in allen ergänzten
Dateien entsprechend gekennzeichnet.

**Hinweis zum Silo-Effekt:** Die Grundzahl (Platz 2, rund 11 Prozent) stand
bereits in `linkedin/01-algorithmus.md` und `linkedin/08-profil-optimierung.md`,
war aber nie in den plattformübergreifenden Guide durchgereicht und dort nie mit
einer Quelle versehen worden. Die B2B-Unterscheidung fehlte in allen drei
Dateien. Sie ist jetzt in `01-algorithmus.md` und in der Plattform-Matrix
ergänzt.

### B3 – Der 360-Brew-Irrtum

**Lücke:** Der Begriff kam in der gesamten Wissensbasis **nirgends** vor. Damit
gab es auch keine Immunisierung dagegen.

**Neu:** Kurze Begriffsklärung in `linkedin/01-algorithmus.md`, ausführlicher
Kasten in `01_OMR26_Behrens_LinkedIn.md`, Regel R11 in `03_Anwendungsregeln.md`.

**Passt methodisch zu** den bestehenden Begriffsklärungen in
`linkedin/08-profil-optimierung.md` ("Grounding Page"). Gleiches Muster: ein
kursierender Begriff, der so nicht existiert.

### B4 – Vier Impact-Faktoren für Corporate Influencing

**Lücke:** `Corporate_Influencing_Employee_Advocacy/04_Messung_und_KPIs.md`
behandelt Messung. Die **Argumentation gegenüber Geschäftsführung**, die das
Programm als Investment statt als Kosten rahmt, war nicht ausformuliert.

**Neu:** Vier-Faktoren-Argumentation und Beispielrechnung, siehe
`03_Anwendungsregeln.md` R6. Mit ausdrücklicher Warnung, dass die Rechnung eine
Werbeäquivalenz und kein ROI ist.

### B5 – Skills-Argumentation für Employer Branding

**Lücke:** Kein Modul begründete bisher, **warum** Skills-basierte Kommunikation
wirkt. Es gab die Praxis (`linkedin/08-profil-optimierung.md`, Skills-Sektion),
aber nicht die Arbeitsmarkt-Begründung.

**Neu, aus Raman:** 70 Prozent Skill-Veränderung bis 2030 `[R 12:50]`,
Verschiebung von Pedigree zu Skills `[R 15:37]`, doppelt so viele Jobs pro
Erwerbsleben `[R 16:09]`, interne Beweglichkeit als Retention-Hebel `[R 16:40]`.
Siehe R8 und R9.

### B6 – Struktur für den KI-Einsatz

**Lücke:** `KI_Content_Planung_Guideline/` beschreibt Workflow und Tool-Stack,
aber kein Modell, mit dem man den **Reifegrad** eines KI-Einsatzes beurteilt.

**Neu:** Drei-Bucket-Modell und Cognitive Debt `[R 8:49]`, `[R 13:29]`. Der
diagnostische Wert liegt in der Frage "in welchem Bucket nutzt ihr KI", nicht in
der Frage ob. Siehe R10.

---

## C. Widerspricht

Der wichtigste Abschnitt. Hier wird nichts stillschweigend überschrieben.

### C1 – Link im Post oder im ersten Kommentar

**Das ist ein echter, ungelöster Widerspruch.**

| Position | Quelle | Aussage |
|---|---|---|
| **Bestehend** | `linkedin/01-algorithmus.md` ("Externe Links im Post-Text") und `linkedin/05-best-practices.md` (Abschnitt "Links") | Posts mit externen Links im Fließtext erhalten deutlich weniger organische Reichweite. Lösung: Link in den ersten Kommentar |
| **Keynote** | Behrens `[B 21:02]`, `[B 21:41]` | Link gehört in den Beitrag. Ein Link im ersten Kommentar ist in der Relevanz-Ansicht nicht sichtbar; Nutzer müssten erst auf "Neueste" umschalten und scrollen |

**Warum beide recht haben können:** Die Positionen messen unterschiedliche Dinge.
Die bestehende Regel optimiert auf **Reichweite des Posts**. Behrens optimiert auf
**Klick und Nutzen für den Leser** und macht zusätzlich eine Beobachtung zur
Kommentar-Sichtbarkeit, die die Kommentar-Lösung entwertet. Beides kann
gleichzeitig zutreffen: Der Link im Text kostet Reichweite, der Link im Kommentar
kostet Klicks.

**Zusätzlich:** Behrens' Position ist konsistent mit ihrer Gesamtthese (Impact
statt Impressionen, R1). Wer R1 folgt, folgt logisch auch R7.

**Beschlossene Behandlung:**

- **Nichts überschrieben.** Beide Module bleiben wie sie sind.
- In `linkedin/05-best-practices.md` und `linkedin/01-algorithmus.md` steht ein
  Querverweis auf diesen Abschnitt.
- **Offene Aufgabe:** eigener A/B-Test am eigenen Kanal. Bis dahin im
  Kundengespräch beide Positionen mit ihrer jeweiligen Zielgröße benennen, statt
  eine als richtig zu verkaufen.
- Behrens' Sichtbarkeitsbeobachtung (Link im ersten Kommentar in der
  Relevanz-Ansicht unsichtbar) ist die überprüfbarste Teilaussage und sollte
  zuerst getestet werden. Wenn sie stimmt, kippt die alte Regel.

### C2 – Datierung der Algorithmus-Umstellung

| Position | Quelle | Aussage |
|---|---|---|
| **Bestehend** | `linkedin/01-algorithmus.md`, `linkedin/README.md` | Umstellung auf KI-basiertes Ranking im **März 2026** |
| **Keynote** | Behrens `[B 16:14]`, `[B 16:53]` | Sachdeva sprach **Ende 2025** über den neuen Newsfeed; die Umstellung wird nicht auf ein Datum festgelegt |

**Kein harter Widerspruch**, aber eine Unschärfe. Kommunikation über eine
Umstellung und deren Ausrollen fallen typischerweise auseinander. Behrens nennt
kein Umstellungsdatum, sie datiert nur die Kommunikation.

**Behandlung:** Bestehende Datierung bleibt. Vermerk hier, damit niemand die
Keynote als Beleg für ein anderes Datum liest.

### C3 – Reichweiteneinbruch: Ursache

| Position | Quelle | Aussage |
|---|---|---|
| **Bestehend** | `Corporate_Influencing_Employee_Advocacy/` | Corporate Pages verlieren Reichweite, persönliche Profile gewinnen |
| **Keynote** | Behrens zitiert Sachdeva `[B 17:35]`: Reichweiten **einzelner Personen** brechen ein, weil 1,3 Mrd. Mitglieder, mehr Poster und KI-gestützte Content-Produktion die Menge erhöhen |

**Ergänzend, nicht widersprüchlich.** Aber die Nuance ist wichtig: Auch
persönliche Profile verlieren, nicht nur Unternehmensseiten. Wer im
Kundengespräch "persönliche Profile bekommen mehr Reichweite" sagt, sollte
ergänzen, dass die absolute Reichweite auch dort sinkt und der Vorsprung relativ
ist.

**Behandlung:** Vermerkt. Bei nächster Überarbeitung von
`Corporate_Influencing_Employee_Advocacy/00_Index.md` einarbeiten.

---

## Offene Punkte

| # | Punkt | Nächster Schritt |
|---|---|---|
| O1 | Link im Post vs. erster Kommentar (C1) | A/B-Test am eigenen Kanal, mindestens 10 Posts je Variante |
| O2 | Behrens' Beobachtung zur Kommentar-Sichtbarkeit in der Relevanz-Ansicht | Manuell prüfen, dauert 5 Minuten |
| O3 | Reichweiteneinbruch auch bei Personenprofilen (C3) | In `Corporate_Influencing_Employee_Advocacy/00_Index.md` einarbeiten |
| O4 | Namen der LinkedIn-Autoren zur Two-Stage-Architektur | Gegen LinkedIn-Engineering-Blog prüfen, dann in `06_Quellen.md` hochstufen |
| O5 | Ramans Datenpunkte (70 %, doppelt so viele Jobs, Founder-Spike) | Gegen LinkedIn Economic Graph oder Work Change Report prüfen |
