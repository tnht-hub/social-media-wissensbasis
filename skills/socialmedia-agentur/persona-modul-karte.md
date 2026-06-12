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
| Krisen-Manager | P4 / sofort | `Krisenkommunikation_Playbook/` (gesamt) | vorhanden |
| KI-Sichtbarkeit | Querschnitt | `KI_Sichtbarkeit_Guide/` (gesamt) | vorhanden |
| Recht / Compliance | Querschnitt | `Recht_Compliance_DE/` | vorhanden |

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

### Krisen-Manager und KI-Sichtbarkeit
Beide vollständig vorhanden und als Spezial-Personas nur bei Bedarf zuschalten.
Krise auch sofort, wenn die Anfrage akut ist.

### Recht / Compliance
`Recht_Compliance_DE/` deckt Werbekennzeichnung, DSGVO, Urheber- und
Musiklizenzen, Gewinnspielrecht und Impressumspflicht ab. Es ist Awareness, keine
Rechtsberatung, dieser Hinweis gehört in jeden rechtsbezogenen Output.

## Pflegehinweis
Wird ein Modul ergänzt oder ein fehlendes gebaut, hier den Status pflegen und den
Pfad eintragen. So bleibt diese Karte die einzige Stelle, an der der Orchestrator
nachsieht, was er nutzen darf.
