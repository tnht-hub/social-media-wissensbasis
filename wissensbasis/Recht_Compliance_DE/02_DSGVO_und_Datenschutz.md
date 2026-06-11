# 02 - DSGVO und Datenschutz

**Disclaimer:** Awareness, keine Rechtsberatung. Datenschutz ist stark einzelfallabhängig. Bei konkreten Verarbeitungen, Tools oder Aufsichtsbehörden-Anfragen ist Beratung durch Datenschutzbeauftragte oder Fachanwält:innen erforderlich.

Die DSGVO (Datenschutz-Grundverordnung) regelt den Umgang mit personenbezogenen Daten EU-weit. In der Social-Media-Arbeit betrifft sie vor allem: Tracking und Werbe-Pixel, das Betreiben von Unternehmensseiten/Fanpages, Gewinnspiel- und Kontaktdaten sowie Personenfotos.

---

## Grundprinzip: keine Verarbeitung ohne Rechtsgrundlage

Jede Verarbeitung personenbezogener Daten braucht eine **Rechtsgrundlage** (Art. 6 DSGVO). Die zwei für Social Media wichtigsten:

| Rechtsgrundlage | Wann | Beispiel |
|---|---|---|
| **Einwilligung** (Art. 6 Abs. 1 lit. a) | Aktive, freiwillige, informierte Zustimmung | Tracking-Cookies, Newsletter, Gewinnspiel-Daten zu Werbezwecken |
| **Berechtigtes Interesse** (Art. 6 Abs. 1 lit. f) | Interesse überwiegt, keine vorrangigen Betroffenen-Rechte | je nach Konstellation z.B. bestimmte Reichweiten-Auswertungen (umstritten, einzelfallabhängig) |

**Faustregel:** Sobald es um Tracking, Werbe-Pixel oder das Sammeln von Adressdaten zu Marketingzwecken geht, ist die sichere Grundlage fast immer die **Einwilligung**.

---

## Einwilligung: die Anforderungen

Eine wirksame Einwilligung muss laut DSGVO sein (vgl. Art. 7 DSGVO, Quellen IHK Köln, Cortina Consult):

- **Aktiv (Opt-In):** Eine eindeutige, bestätigende Handlung. Vorangekreuzte Kästchen, Stillschweigen oder bloße Weiternutzung genügen **nicht**.
- **Freiwillig:** Ohne Druck oder Zwang, mit echter Wahlfreiheit. „Nur akzeptieren möglich" ist problematisch.
- **Informiert:** Vorher verständlich über Art, Zweck der Verarbeitung und das Widerrufsrecht aufklären.
- **Widerrufbar:** Der Widerruf muss so einfach sein wie die Erteilung.
- **Nachweisbar:** Die Einwilligung muss dokumentiert werden (wer, wann, wofür).

---

## Tracking und Pixel (Meta Pixel, TikTok Pixel etc.)

Werbe-Pixel auf der eigenen Website (z.B. zur Conversion-Messung oder für Retargeting) sind ein Datenschutz-Klassiker.

### Die zwei Ebenen: TDDDG und DSGVO

- **TDDDG** (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz, seit 14. Mai 2024 Nachfolger des TTDSG): Nach **§ 25 Abs. 1 TDDDG** darf das Speichern oder Auslesen von Informationen auf dem Endgerät (Cookies, Pixel-IDs) erst nach **aktiver Einwilligung** erfolgen.
- **DSGVO:** Regelt zusätzlich die anschließende Verarbeitung der so erhobenen personenbezogenen Daten.

### Praktische Konsequenz

| Cookie-/Pixel-Typ | Einwilligung nötig? |
|---|---|
| **Technisch notwendige Cookies** (Betrieb der Seite, Warenkorb, Login) | Nein |
| **Werbe-, Tracking-, Marketing-Cookies und -Pixel** (Meta Pixel, TikTok Pixel, Analytics mit Tracking) | **Ja, aktive Einwilligung vor dem Setzen** |

**Wichtig:** Der Pixel darf erst feuern, **nachdem** die Person zugestimmt hat. Häufiger Fehler: Pixel lädt beim Seitenaufruf, bevor das Cookie-Banner bedient wurde (vgl. Quellen Complianty, audatis).

### Cookie-Banner / Consent

- Vor dem Setzen nicht-notwendiger Cookies muss ein **Consent-Banner** abgefragt werden.
- Verstöße gegen § 25 TDDDG können mit Bußgeldern bis zu **300.000 Euro** geahndet werden (vgl. Quellen Cortina Consult).
- Seit dem **1. April 2025** ist eine Verordnung zur Einwilligungsverwaltung nach dem TDDDG in Kraft, die die „Cookie-Banner-Flut" über anerkannte Dienste reduzieren soll (vgl. Quellen Usercentrics). Die praktische Verbreitung entwickelt sich, der Banner-Standard bleibt vorerst der Normalfall.

**Sonderfall Advanced Matching beim Meta Pixel:** Wenn der Pixel zusätzlich gehashte Kontaktdaten (E-Mail, Telefonnummer) überträgt, steigt das Datenschutz-Risiko deutlich. Hier ist besonders sorgfältige Prüfung und klare Einwilligung nötig (vgl. Quellen audatis).

---

## Gemeinsame Verantwortlichkeit bei Fanpages

Ein zentrales und oft übersehenes Thema: Wer eine **Unternehmensseite/Fanpage** auf einer Plattform betreibt, ist nicht „nur Gast", sondern datenschutzrechtlich **mitverantwortlich**.

### Das Fanpage-Urteil des EuGH

Der EuGH hat am **5. Juni 2018** (Rechtssache **C-210/16**, Wirtschaftsakademie Schleswig-Holstein) entschieden:

> Der Betreiber einer Facebook-Fanpage ist **gemeinsam mit der Plattform verantwortlich** für die Verarbeitung personenbezogener Daten der Besucher:innen (gemeinsame Verantwortlichkeit nach **Art. 26 DSGVO**).

Das bedeutet:
- Die Pflicht zu datenschutzkonformem Verhalten trifft **beide**: Plattform und Seitenbetreiber.
- Eine Datenschutzaufsichtsbehörde kann den Betrieb einer Fanpage untersagen (vgl. Folge-Rechtsprechung BVerwG 2019, Quellen Noerr, LTO).

### Praktische Konsequenz für Brand-Accounts

- Für Reichweiten-/Insights-Funktionen sollte eine **Vereinbarung zur gemeinsamen Verantwortlichkeit** mit der Plattform vorliegen (Meta stellt dafür ein „Page Insights"-Addendum bereit).
- In der **Datenschutzerklärung** auf die gemeinsame Verantwortlichkeit und die Datenverarbeitung durch die Plattform hinweisen.
- Im Zweifel mit Datenschutzbeauftragten klären, welche Funktionen genutzt werden und wie das dokumentiert ist.

---

## Umgang mit Nutzerdaten

Daten, die im Social-Media-Alltag anfallen (Gewinnspiel-Adressen, DM-Kontakte, Kommentar-Daten, Kundendaten für Custom Audiences), unterliegen der DSGVO. Wichtige Pflichten:

- **Zweckbindung:** Daten nur für den Zweck nutzen, für den sie erhoben wurden. Gewinnspiel-Adressen nicht ungefragt für Newsletter verwenden (siehe `04_Gewinnspielrecht.md`).
- **Datenminimierung:** Nur erheben, was wirklich nötig ist.
- **Speicherbegrenzung:** Daten löschen, wenn der Zweck erfüllt ist (z.B. Gewinnspiel-Daten nach Abschluss).
- **Betroffenenrechte:** Auskunft, Berichtigung, Löschung, Widerspruch. Anfragen müssen fristgerecht bearbeitet werden.
- **Custom/Lookalike Audiences:** Das Hochladen von Kundenlisten zu Werbezwecken ist datenschutzrechtlich heikel und braucht eine saubere Rechtsgrundlage. Vor dem Einsatz prüfen lassen.

---

## Personenfotos (Verweis)

Fotos und Videos mit erkennbaren Personen fallen unter DSGVO **und** das Recht am eigenen Bild (§ 22 KUG). Das ist im Detail in `03_Urheber_und_Musiklizenzen.md` und im Modul `Visual_Production_Methodik/09_Rechtliches.md` behandelt. Kurzregel: **Vor Veröffentlichung Einwilligung einholen, schriftlich dokumentieren.**

---

## Checkliste: Datenschutz im Social-Media-Alltag

- [ ] Feuern Werbe-Pixel erst **nach** aktiver Einwilligung (Consent-Banner)?
- [ ] Ist das Consent-Banner Opt-In (keine vorangekreuzten Kästchen, echte Wahl)?
- [ ] Liegt für die Fanpage eine Vereinbarung zur gemeinsamen Verantwortlichkeit vor?
- [ ] Weist die Datenschutzerklärung auf die Plattform-Datenverarbeitung hin?
- [ ] Werden gesammelte Daten nur für den ursprünglichen Zweck genutzt?
- [ ] Werden Daten gelöscht, wenn der Zweck erfüllt ist?
- [ ] Ist für Custom Audiences eine geprüfte Rechtsgrundlage vorhanden?
- [ ] Sind Einwilligungen dokumentiert und Widerruf einfach möglich?

---

## Wann Datenschutzbeauftragte oder Anwält:in einbeziehen

- Bei neuem Tracking-/Analytics-Setup oder neuem Pixel
- Beim Einsatz von Custom/Lookalike Audiences mit hochgeladenen Daten
- Bei Datenschutz-Vorfall oder Aufsichtsbehörden-Anfrage
- Bei Unsicherheit zur Rechtsgrundlage einer Verarbeitung
- Bei internationalem Daten-Transfer (Drittland-Problematik)

Datenschutz ist das Rechtsgebiet mit den schnellsten Änderungen (neue EuGH-Urteile, neue Behörden-Praxis). Dieses Kapitel braucht einen jährlichen Refresh.
