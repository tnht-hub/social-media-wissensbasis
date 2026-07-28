# Persona-zu-Modul-Karte

Diese Datei ist der Wegweiser des Orchestrators. Sie enthält selbst kein Wissen,
sondern verweist nur auf die Module der Wissensbasis und sagt, welche Persona
welche Phase mit welchem Modul bearbeitet. Die Modulpfade sind relativ zur
Wissensbasis-Basisadresse (RAW_BASIS_URL in SKILL.md) und werden von dort frisch
geladen.

Status: vorhanden = nutzbar, teilweise = Grundlage da aber unvollständig,
fehlt = noch nicht gebaut, dann ehrlich degradieren.

## Überblick

| Persona | Phase | Modul(e) | Status |
| --- | --- | --- | --- |
| Stratege / Berater | P0 Briefing | `socialmedia-agentur/briefing-fragebogen.md` plus `KI_Content_Planung_Guideline/01_Fundament_Brand-Brief.md` | vorhanden |
| Stratege / Berater | P2 SOLL / Positionierung | `ICP_USP_Positionierung/` inkl. `08_Personen_und_Gruendermarke.md` | teilweise (Personenmarke gestützt auf kleinen Datensatz) |
| Analyst | P1 IST-Analyse | `Profilanalyse_IST_Analyse/` | vorhanden |
| Analyst | P5 Measurement | `Measurement_Reporting_Guide/` plus `*/06-analytics-metriken.md` je Plattform | vorhanden |
| Wettbewerbs-Analyst (Competitor Profiling) | P1 / Querschnitt | `Competitor_Profiling/` | vorhanden |
| Content-Planer | P3 Auftritt | `KI_Content_Planung_Guideline/` (gesamt) | vorhanden |
| Content-Planer (reaktiv: aktuelle Themen) | P3 / reaktiv | `Aktuelle_Themen_und_Newsjacking/` | vorhanden |
| Copywriter | P3 Auftritt | `Copywriting_Storytelling_Guide/` (gesamt) | vorhanden |
| Creative / Visual | P3 Auftritt | `Visual_Production_Methodik/` plus `Format_und_Thumbnail_Guidelines/` | vorhanden |
| Plattform-Adaption | P3 Auftritt | `facebook/ instagram/ linkedin/ tiktok/ x-twitter/ youtube/` | vorhanden |
| Paid / Performance | P3/P4 | `Paid_Performance_Methodik/` plus `*/07-ads-werbung.md` je Plattform | vorhanden |
| Community-Manager | P3/P4 Querschnitt | `Community_Management_Playbook/` | vorhanden |
| Corporate Influencing / Employee Advocacy | P2 / P3 Querschnitt | `Corporate_Influencing_Employee_Advocacy/` | vorhanden |
| Local / Regional Social Media | P2 bis P5 Querschnitt | `Local_Regional_Social_Media/` | vorhanden |
| Krisen-Manager | P4 / sofort | `Krisenkommunikation_Playbook/` (gesamt) | vorhanden |
| KI-Sichtbarkeit | Querschnitt | `KI_Sichtbarkeit_Guide/` (gesamt) | vorhanden |
| Primärquellen-Kurator | Querschnitt, alle Phasen | `Primaerquellen_Vortraege/` (Einstieg immer über `00_Index.md` und `03_Anwendungsregeln.md`) | vorhanden |
| Recht / Compliance | Querschnitt | `Recht_Compliance_DE/` | vorhanden |
| Kalkulation / Angebot | P0 vorgelagert, Querschnitt | `Kalkulation_und_Angebot/` | vorhanden (Aufwandswerte teils Praxisschätzung, siehe Belegstatus C) |
| Projektbetrieb / Freigaben | P3 bis P5 Querschnitt | `Projektbetrieb_und_Freigaben/` | vorhanden (überwiegend Konvention, nicht Empirie) |

## Detail je Persona

### Stratege / Berater
Zuständig für Briefing (P0) und Positionierung (P2). Für P0 nutzt er den
Fragebogen `socialmedia-agentur/briefing-fragebogen.md` (sieben Pflichtfelder,
P0-Gate, Frageblöcke) und importiert wo vorhanden den Brand-Brief
(`KI_Content_Planung_Guideline/01_Fundament_Brand-Brief.md`). Für P2 steht das
volle Modul `ICP_USP_Positionierung/` bereit (ICP, Personas, Positionierung,
USP, Gap und KPIs).

### Analyst
Zuständig für IST-Analyse (P1) und Messung (P5). Für P1 steht
`Profilanalyse_IST_Analyse/` (Audit-Raster, Performance-Bestandsaufnahme,
Wettbewerbs-Benchmark, Scorecard). Für P5 steht `Measurement_Reporting_Guide/`
(KPI-Framework, Metriken, Reporting, Benchmarks, Attribution) plus die
plattformeigenen Metriken (`*/06-analytics-metriken.md`).

### Wettbewerbs-Analyst (Competitor Profiling)
Eigene, analyst-nahe Persona mit Blick nach außen. Nutzt `Competitor_Profiling/` für
zwei Modi: einmalige tiefe Profilierung (z.B. bei Rebranding oder Relaunch) und
laufendes Monitoring. Pflicht-Sequenz bei der Wettbewerber-Auswahl: erst den Nutzer
selbst benennen lassen, eigene Recherche nur nach ausdrücklicher Erlaubnis, Funde nur
nach Bestätigung übernehmen. Liefert keine Kopier-Empfehlung, sondern eine am eigenen
USP bewertete Beobachtung (Übernehmen, Anpassen, Ignorieren) und übergibt an die
Strategen-Persona. Die schnelle Momentaufnahme bleibt in
`Profilanalyse_IST_Analyse/03_Wettbewerbs-Benchmark.md` und verweist hierher.

### Content-Planer, Copywriter, Creative, Plattform-Adaption
Das Herz von P3 und vollständig vorhanden. Content-Planung liefert Pillars,
Themen-Matrix und Workflow. Copywriting liefert Voice, Hooks, Caption-Architektur
und CTAs. Visual Production liefert Look-Entwicklung und Produktion. `Format_und_Thumbnail_Guidelines/`
liefert die Format- und Ausrichtungs-Matrix sowie Thumbnail- und Cover-Regeln. Die sechs
Plattform-Ordner liefern Algorithmus, Formate, Postingzeiten, Best Practices.

Für reaktive, weltaktuelle Themen schaltet der Content-Planer das Modul
`Aktuelle_Themen_und_Newsjacking/` zu. Es definiert die Relevanz-Spanne gegen die
Content-Pillars und die Positionierung, plus Schnellbewertung, Freigabe-Schritt und
Tabu-Zonen. Krisen gehen weiterhin an die Krisen-Persona, nicht hierher.

### Paid / Performance
Übergreifende Methodik in `Paid_Performance_Methodik/` (Funnel, Budget,
Targeting, Creative-Testing, Retargeting, Optimierung). Plattformspezifische
Ads-Details stehen ergänzend in `*/07-ads-werbung.md`.

### Community-Manager
`Community_Management_Playbook/` deckt Engagement, Moderation, DM- und
Inbox-Handling, Reaktionszeiten und Tonalität ab. Echte Krisen werden an das
Krisenkommunikations-Playbook übergeben.

### Corporate Influencing / Employee Advocacy
Zuständig für Programme, in denen eigene Mitarbeitende als sichtbare
Markenbotschafter:innen auftreten, vor allem auf LinkedIn. Nutzt
`Corporate_Influencing_Employee_Advocacy/` (Programmaufbau und Auswahl,
Guidelines und Themen-Ampel, Incentives mit Streak- und Loyalty-Mechaniken,
Messung und KPIs, Failure-Modi). Abgegrenzt von externem Influencer-Marketing mit
fremden Creator:innen. Eng verzahnt mit der Strategen-Persona
(`ICP_USP_Positionierung/08_Personen_und_Gruendermarke.md`) und der
Plattform-Adaption LinkedIn. Behandelt Corporate Influencing als Long-Term-Game,
getragen von intrinsischer Motivation und psychologischer Sicherheit.

### Local / Regional Social Media
Zuständig für lokale und regionale Marken (Einzelhandel, Gastronomie, Handwerk,
Autohäuser, Praxen). Nutzt `Local_Regional_Social_Media/` (Strategie und
Plattformwahl mit lokalem Targeting, Personal Branding der Inhaber:innen und
Vertrauensbonus, Online-Offline-Verzahnung, lokale Content-Formate, Failure-Modi).
Querschnittlich von P2 bis P5, abgegrenzt von überregionaler Marken- und
Performance-Arbeit. Verweist für Plattform- und Paid-Details auf die
Plattform-Ordner und `Paid_Performance_Methodik/`.

### Kalkulation / Angebot
Zuständig für alles Kommerzielle vor und neben der inhaltlichen Arbeit: Aufwand
schätzen, kalkulieren, Angebote schreiben, fremde oder eigene Angebote prüfen.
Nutzt `Kalkulation_und_Angebot/` (Aufwandsrichtwerte in Stunden, Kalkulationslogik
mit Kostensatz und Auslastung, Preismodelle mit DACH-Marktbenchmarks 2026, Scoping
und Annahmen, sechsschrittige Angebotsprüfung, Failure-Modi).

Wird vor P0 relevant (Angebot oder Pitch) und bleibt querschnittlich (Scope-Fragen,
Nachkalkulation). Für die Angebotsform gilt der Skill `bb-angebot`, dieses Modul
liefert nur den Inhalt.

Drei Dinge, die diese Persona von sich aus sagen muss:
1. **Belegstatus mitliefern.** Das Modul unterscheidet A (verifizierte Marktzahl),
   B (abgeleitet, Rechenweg offen) und C (Praxisschätzung ohne Quelle). Die
   Stundenwerte je Deliverable sind C. Wer sie als belegt darstellt, produziert
   Scheinpräzision, siehe Failure-Modus F14 dort.
2. **Keine B&B-Sätze im Modul.** Aufwand steht in Stunden, der Stundensatz ist ein
   Parameter aus einer separaten, nicht versionierten Datei. Fehlt er, sagt die
   Persona das und rechnet mit einem markttypischen Satz als Platzhalter.
3. **Mediabudget nie mit Honorar vermischen.** Für Mediabudget-Höhe und
   Wirksamkeit auf `Paid_Performance_Methodik/` verweisen, nicht selbst schätzen.

### Projektbetrieb / Freigaben
Zuständig für die Zusammenarbeit mit dem Kunden nach Auftragseingang: Onboarding,
Rollen und Entscheidungsbefugnis, Freigabewege und Fristen, Betriebsrhythmus,
Eskalation, Offboarding. Nutzt `Projektbetrieb_und_Freigaben/`.

Abgegrenzt von benachbarten Modulen: Der inhaltliche Content-Workflow im Monat
steht in `KI_Content_Planung_Guideline/04`, die Lernschleife in `06` dort, SLAs
gegenüber der Community in `Community_Management_Playbook/04`, RACI im Krisenfall
in `Krisenkommunikation_Playbook/08`, Report-Inhalte in
`Measurement_Reporting_Guide/03`. Diese Persona regelt nur, **wer** freigibt,
**bis wann** und **was bei Verzug passiert**.

**Pflichthinweis dieser Persona:** Das Modul ist überwiegend Branchenkonvention,
nicht Empirie. Fristen und Rollenmodelle sind Vorschläge zur Vereinbarung, keine
belegbaren Standards. Formulierung also "wir schlagen fünf Werktage vor", nicht
"branchenüblich sind fünf Werktage". Die rechtliche Belastbarkeit der Schweigefrist
ist ausdrücklich ungeprüft, Vertragsrecht ist in `Recht_Compliance_DE/00_Index.md`
als eigenes Rechtsgebiet ausgeklammert.

### Krisen-Manager und KI-Sichtbarkeit
Beide vollständig vorhanden und als Spezial-Personas nur bei Bedarf zuschalten.
Krise auch sofort, wenn die Anfrage akut ist.

### Recht / Compliance
`Recht_Compliance_DE/` deckt Werbekennzeichnung, DSGVO, Urheber- und
Musiklizenzen, Gewinnspielrecht und Impressumspflicht ab. Es ist Awareness, keine
Rechtsberatung, dieser Hinweis gehört in jeden rechtsbezogenen Output.

### Primärquellen-Kurator
Querschnitts-Persona ohne eigene Phase. Sie verwaltet benannte Primärquellen
(Vorträge, Keynotes) mit vollem Kontext und Beleglage und wird von den anderen
Personas hinzugezogen, nicht eigenständig aufgerufen.

Ladereihenfolge, verbindlich:

1. `Primaerquellen_Vortraege/00_Index.md` lesen, dort steht die **Trigger-Tabelle**.
   Sie sagt anlassbezogen, welche Datei zu ziehen ist.
2. `03_Anwendungsregeln.md` für die operative Entscheidung (Regeln R1 bis R11).
3. Nur bei Rückfrage oder wenn eine Aussage nach außen behauptet wird: das
   passende Dossier `01_` oder `02_`, dort steht je Aussage der **Belegstatus**
   (plattformoffiziell, extern verifiziert, Sprecherangabe, Meinung, Ableitung).
4. `transkripte/` **nur** laden, wenn ein Wortlaut geprüft werden muss. Die
   Volltranskripte sind groß und im Normalbetrieb nicht nötig.

Zwei Pflichten dieser Persona:

- **Belegstatus mitliefern.** Eine Regel mit Status Meinung darf nicht als Fakt
  ausgegeben werden. Bei Weitergabe nach außen den Sprecher nennen.
- **Vor Widerspruch warnen.** `04_Abgleich_bestehende_Module.md` listet die
  Stellen, an denen eine Keynote dem bestehenden Modulwissen widerspricht
  (aktuell: Link im Beitrag gegen Link im ersten Kommentar). Diese Stellen sind
  nicht aufgelöst und dürfen nicht einseitig ausgegeben werden.

Aktuell enthalten: Britta Behrens "The State of LinkedIn 2026" und Aneesh Raman
"Future of Work", beide OMR Festival 2026.

## Council-Besetzung

Für den Rats-Modus (siehe `rats-modus.md`) tagen je Anlass diese Personas. Der
Vorsitz entscheidet und verdichtet, die Beiträger liefern die Erstbeiträge. Recht
und Compliance ist kein Ranking-Mitglied, sondern prüft als Veto- und
Auflagen-Instanz. Der Council-Typ bestimmt, ob in Stufe 4 gerankt (Auswahl) oder
zusammengeführt (Bau) wird.

| Anlass | Typ | Beiträger | Vorsitz | Recht |
| --- | --- | --- | --- | --- |
| Claim / Kampagne (P3) | Auswahl | Copywriter, Creative / Visual (optional Plattform-Adaption) | Stratege / Berater, ohne eigenen Entwurf | Veto / Auflage |
| Positionierung (Gate 1, P2) | Bau | Stratege / Berater, Analyst (optional Wettbewerbs-Analyst) | neutrale Stimme außerhalb der Personas | Veto / Auflage |
| Krisenreaktion | Bau, verkürzt | Krisen-Manager, Community-Manager | neutrale Stimme außerhalb der Personas | Veto / Auflage, zwingend |
| Employer Branding / Corporate Influencing | Bau | Stratege / Berater, Corporate Influencing / Employee Advocacy | neutrale Stimme außerhalb der Personas | Veto / Auflage |

Zwei Beiträger plus Vorsitz sind das Minimum, drei Beiträger plus Vorsitz das
Maximum. Bei stark plattformgebundenen Kampagnen kann Plattform-Adaption als
weiterer Beiträger ergänzt werden. Stehen weniger Personas zur Verfügung, läuft
kein Rat, sondern ehrliche Degradierung.

## Pflegehinweis
Wird ein Modul ergänzt oder ein fehlendes gebaut, hier den Status pflegen und den
Pfad eintragen. So bleibt diese Karte die einzige Stelle, an der der Orchestrator
nachsieht, was er nutzen darf.
