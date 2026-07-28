# Social-Media-Agentur: Wissensbasis und Orchestrator

Dieses Paket ist eine Wissens- und Simulations-Engine für Social-Media-Arbeit.
Es bündelt eine strukturierte Wissensbasis und einen Orchestrator-Skill, mit dem
sich eine komplette Agenturleistung über einen einzigen Einstieg durchspielen
lässt. Anfänger werden Schritt für Schritt geführt, Experten können direkt
durchsteuern.

## Wie man es benutzt

Es gibt zwei Wege:

1. Als Skill (Command): Der Ordner `socialmedia-agentur/` ist ein installierbarer
   Skill. Installiert man ihn, steht der Befehl `socialmedia-agentur` bereit. Der
   Skill enthält nur die Logik und liest die Wissensmodule aus diesem Ordner.
   Wichtig: Der Skill erwartet, dass dieser Gesamtordner vorhanden ist. Findet er
   ihn nicht, fragt er einmal nach dem Pfad. Haltet Skill und Wissensbasis also
   zusammen.

2. Als Nachschlagewerk: Alle Module sind normale Markdown-Dateien und lassen sich
   direkt lesen.

## Was drin ist

Plattform-Module (Algorithmus, Formate, Postingzeiten, Best Practices, Analytics,
Ads): `facebook/`, `instagram/`, `linkedin/`, `tiktok/`, `x-twitter/`, `youtube/`.

Methodik-Guides: `KI_Content_Planung_Guideline/`, `Copywriting_Storytelling_Guide/`,
`Visual_Production_Methodik/`, `KI_Sichtbarkeit_Guide/`, `Krisenkommunikation_Playbook/`.

Strategie- und Betriebs-Module (neu): `Profilanalyse_IST_Analyse/`,
`ICP_USP_Positionierung/`, `Measurement_Reporting_Guide/`,
`Community_Management_Playbook/`, `Paid_Performance_Methodik/`,
`Recht_Compliance_DE/`, `Competitor_Profiling/`,
`Aktuelle_Themen_und_Newsjacking/`, `Format_und_Thumbnail_Guidelines/`.

Primärquellen (Ergänzung Juli 2026): `Primaerquellen_Vortraege/` enthält benannte
Vorträge und Keynotes mit Volltranskript, Aussagen-Extrakt und Anwendungsregeln.
Anders gebaut als die übrigen Module: drei Ebenen (Quelle, Aussage, Regel), jede
Aussage mit Zeitmarke und Belegstatus. Einstieg immer über `00_Index.md`, dort
steht eine Trigger-Tabelle. Aktuell: Britta Behrens "The State of LinkedIn 2026"
und Aneesh Raman "Future of Work", beide OMR Festival 2026.

Disziplin-Module (Ergänzung Juni 2026, Quelle SocialHub Mag #30):
`Corporate_Influencing_Employee_Advocacy/` (Markenbotschafter-Programme mit
eigenen Mitarbeitenden) und `Local_Regional_Social_Media/` (Social Media für
lokale und regionale Unternehmen). In derselben Runde erweitert wurden
`Community_Management_Playbook/02` (Hate Speech, Empowerment-Moderation,
proaktives CM), `Recht_Compliance_DE/08` (Messenger- und DM-Marketing) und
`ICP_USP_Positionierung/09` (Trend-Annex Future of Social).

Agentur-Betriebs-Module (Ergänzung Juli 2026): `Kalkulation_und_Angebot/`
(Aufwandsschätzung, Kalkulationslogik, Preismodelle mit DACH-Marktbenchmarks 2026,
Scoping, Angebotsprüfung) und `Projektbetrieb_und_Freigaben/` (Kundenonboarding,
Rollen und Entscheidungsbefugnis, Freigabe-Workflows und Fristen, Betriebsrhythmus,
Eskalation, Offboarding). Diese beiden Module schließen eine Lücke: Sie decken die
kommerzielle und prozessuale Seite ab, die vor und neben der inhaltlichen Arbeit
läuft und in jedem Projekt anfällt, unabhängig von Plattform und Kunde.

Zwei Besonderheiten dieser beiden Module, die vor der Nutzung wichtig sind:

1. `Kalkulation_und_Angebot/` enthält **bewusst keine B&B-eigenen Stundensätze**.
   Aufwand steht in Stunden, der Satz bleibt ein Parameter, den man einmalig in
   einer separaten, nicht versionierten Datei ablegt. Begründung im `00_Index.md`
   des Moduls. Damit bleibt das Modul repo-tauglich.

2. Beide Module kennzeichnen ihren Belegstatus dreistufig (A verifiziert,
   B abgeleitet, C Praxisschätzung). Das ist nötig, weil es für Agenturhonorare
   und Prozessstandards keine Branchenreports in der Qualität gibt, die für CPM
   oder Engagement-Raten vorliegen. `Projektbetrieb_und_Freigaben/` ist
   überwiegend Konvention, nicht Empirie, und sagt das im `08_Quellen.md`
   ausdrücklich. Fristen und Rollenmodelle dort sind Vorschläge zur Vereinbarung,
   keine belegbaren Standards.

Orchestrator: `socialmedia-agentur/` mit `SKILL.md` (Logik), `persona-modul-karte.md`
(Wegweiser auf die Module) und `briefing-fragebogen.md` (Intake für Phase 0).
Die `persona-modul-karte.md` im Skill-Paket ist auf dem Stand aller Module,
zuletzt ergänzt um die Personas "Kalkulation / Angebot" und "Projektbetrieb /
Freigaben" (Juli 2026). Wird ein Modul ergänzt, dort den Status pflegen und
anschließend `werkzeuge/index_erzeugen.py` ausführen, damit `wissensbasis/index.json`
die neuen Dateien kennt. Der Orchestrator lädt diesen Index zu Beginn jeder
Wissensfrage, ein nicht nachgezogener Index bedeutet also unsichtbare Module.

## Wie der Orchestrator arbeitet

Er nimmt eine Anfrage entgegen, erkennt selbst, ob es eine reine Wissensfrage oder
ein Workflow ist, wählt den Modus (geführt oder Experte), läuft die passenden
Phasen der Kette durch (Briefing, IST-Analyse, Positionierung, Auftritt, Rollout,
Measurement) und hält an drei Freigabepunkten an. Details in
`socialmedia-agentur/SKILL.md`.

## Stand der Quellen

Die Module sind recherchiert und mit Quellen belegt. Die Quellen wurden geprüft
und Fehler korrigiert. Einige wenige Quellen ließen sich technisch nicht abrufen
(Paywall, Login, JavaScript) und sind nicht abschließend bestätigt, ohne Hinweis
auf Erfindung. Das Rechts-Modul ist Awareness, keine Rechtsberatung.

## Bekannte Lücken (Stand Juli 2026)

Bewusst dokumentiert, damit niemand sucht, was nicht da ist, und damit die
Reihenfolge für den Ausbau nachvollziehbar bleibt.

Als **eigene Module fehlen**, nach absteigender Relevanz:

1. **Externes Influencer- und Creator-Marketing.** Auswahl, Briefing, Verträge,
   Honorarlogik, Messung. Vorhanden ist nur die Compliance-Seite in
   `Recht_Compliance_DE/01` und ein Abschnitt zu lokalen Creators in
   `Local_Regional_Social_Media/02`. Preisrahmen steht in
   `Kalkulation_und_Angebot/03`. Die Methodik fehlt.
2. **Employer Branding und Social Recruiting.** Nur über den Annex in
   `Primaerquellen_Vortraege/` abgedeckt. Relevant, weil Recruiting nach
   `Marketing_Psychologie_und_Prinzipien/02` die Ausnahme im Agentur-Paradox ist.
3. **Social Listening als eigene Disziplin.** Monitoring ist abgedeckt:
   `Competitor_Profiling/03_Laufendes-Monitoring.md` grenzt Monitoring gegen
   Listening ab, `Krisenkommunikation_Playbook/08` beschreibt Frühwarnsystem und
   Alert-Schwellen. Was fehlt, ist die darüberliegende Listening-Methodik:
   Themen- und Stimmungsanalyse jenseits der eigenen Kanäle, Tool-Auswahl,
   Auswertung als eigene Leistung.
4. **Social Commerce.** Der Begriff kommt in der Wissensbasis nicht vor, nur
   einzelne Plattform-Features (Shopping, Collection Ads).
5. **Barrierefreiheit im Content.** Das BFSG ist juristisch in
   `Recht_Compliance_DE/` erfasst, eine Umsetzungs-Guideline (Untertitel,
   Alt-Text, Kontrast) fehlt.
6. **Mehrsprachigkeit und Lokalisierung.** Je ein Streiftreffer in
   `linkedin/04` und `tiktok/01`.
7. **Green Claims und Greenwashing.** Ein Treffer im Krisen-Playbook.

**Plattformen ohne Modul:** Pinterest, Snapchat, Reddit, WhatsApp Channels,
Twitch, Bluesky. Ebenfalls nicht abgedeckt: Google Ads und Search als Teil eines
Angebots. Paid ist in dieser Wissensbasis rein Social.

**Strukturfehler, nicht Lücke:** Threads liegt als Abschnitt unter `x-twitter/`,
gehört aber zu Meta. Sollte bei nächster Pflege verschoben werden.

## Pflege

Schnell veraltende Teile sind vor allem Plattform-Algorithmen, Features und
rechtliche Angaben. Empfehlung: regelmäßiger Review, jede Datei trägt einen Stand.
Wird ein Modul ergänzt, den Status in `socialmedia-agentur/persona-modul-karte.md`
nachziehen.

Sonderfall bei den Agentur-Betriebs-Modulen: `Kalkulation_und_Angebot/03`
(Marktbenchmarks) ist marktgekoppelt und braucht jährliche Pflege.
`Kalkulation_und_Angebot/01` (Aufwandsrichtwerte) veraltet nicht durch den Markt,
sondern wird durch eigene Nachkalkulation besser. Die dort als Belegstatus C
markierten Stundenwerte sollen nach fünf nachkalkulierten Projekten durch eigene
Ist-Werte ersetzt werden. `Projektbetrieb_und_Freigaben/` ist das langlebigste
Modul der Wissensbasis, weil Prozesse nicht an Plattform-Features hängen.
