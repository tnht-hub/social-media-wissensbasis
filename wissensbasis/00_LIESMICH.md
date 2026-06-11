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
`Recht_Compliance_DE/`.

Orchestrator: `socialmedia-agentur/` mit `SKILL.md` (Logik), `persona-modul-karte.md`
(Wegweiser auf die Module) und `briefing-fragebogen.md` (Intake für Phase 0).

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

## Pflege

Schnell veraltende Teile sind vor allem Plattform-Algorithmen, Features und
rechtliche Angaben. Empfehlung: regelmäßiger Review, jede Datei trägt einen Stand.
Wird ein Modul ergänzt, den Status in `socialmedia-agentur/persona-modul-karte.md`
nachziehen.
