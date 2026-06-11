# Säule 8 — Prävention & Krisenstab-Setup

Wer Krisen erst dann ernst nimmt, wenn sie kommen, hat schon verloren. Die Arbeit muss **vor** der Krise gemacht werden.

Diese Säule dokumentiert das Setup-Werk, das eure Organisation vor der Krise leisten muss.

---

## Vier Säulen der Prävention

| Säule | Was tun | Wann |
|---|---|---|
| **1. Krisenstab-Setup** | Team definieren, Verantwortlichkeiten klären | Einmalig, dann jährlich-Review |
| **2. Pre-Approved Templates** | Statement-Skelette für häufige Krisen-Typen | Einmalig, dann halbjährlich-Review |
| **3. Stakeholder-Karte** | Wer wird wann informiert | Quartalsweise aktualisieren |
| **4. Monitoring & Frühwarnsystem** | Tools und Prozesse zur Krisen-Erkennung | Setup einmalig, dann fortlaufend |

---

## 1. Krisenstab-Setup

### Wer gehört in den Krisenstab?

**Pflichtmitglieder:**

| Rolle | Verantwortung im Krisenstab |
|---|---|
| **Krisenstab-Leitung** | Gesamtkoordination, Entscheidung bei Eskalations-Fragen |
| **Geschäftsführung / CEO** | Letzte Entscheidung bei strategischen Fragen, externe Repräsentation |
| **Kommunikations-Lead** | Stellungnahmen, Pressekontakt, Social-Media-Koordination |
| **Rechtsteam-Lead** | Rechtliche Bewertung, Meldepflichten, Klagerisiken |
| **Operations-Lead** | Operative Sofortmaßnahmen, Kund:innen-Kontakt |
| **HR-Lead** | Mitarbeiter:innen-Kommunikation, ggf. Personalfragen |
| **IT-Sicherheit** (bei Cyber-Krise) | Technische Analyse, Forensik |

**Optionale Mitglieder je nach Krise:**

- Finance Lead (bei Finanzkrisen)
- Quality Lead (bei Produktkrisen)
- Compliance Officer (bei regulatorischen Themen)
- Externe Berater:innen (PR-Agentur, Krisenkommunikations-Profi)

### Verantwortlichkeiten klären (RACI-Matrix)

Jede Aktion im Krisenstab braucht eine klare RACI-Zuordnung:

- **R**esponsible (wer macht es)
- **A**ccountable (wer entscheidet final)
- **C**onsulted (wer wird gefragt)
- **I**nformed (wer wird informiert)

**Beispiel:**

| Aktion | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Holding Statement schreiben | Comms-Lead | Krisenstab-Lead | Recht | CEO |
| Pressemitteilung freigeben | Comms-Lead | CEO | Recht, Krisenstab | Board |
| Mitarbeiter-Information | HR-Lead | CEO | Krisenstab | alle Mitarbeiter:innen |
| Behörden-Meldung (DSGVO etc.) | Recht | CEO | Krisenstab | Board |

### Erreichbarkeit garantieren

**24/7-Verfügbarkeit** ist Pflicht für den Krisenstab. Das bedeutet:

- Notfall-Telefonnummern (privat) aller Mitglieder
- Backup-Person für jede Rolle definiert
- Eskalations-Hierarchie: Wer wird angerufen, wenn primäre Person nicht erreichbar?
- Pflicht-Übungen: 2x jährlich Notfall-Test (siehe unten)

### Krisenstab-Kommunikationskanal

**Pre-installierter Notfall-Channel** (z.B. dedizierter Slack-/Teams-Kanal „War Room"):

- Mit allen Krisenstab-Mitgliedern als Member
- Mit Backup-Personen als Member
- Mit Push-Notifications-Pflicht
- Mit Document-Sharing aktiviert

**NIE über reguläre Channels** — sonst verlieren sich kritische Updates in Smalltalk.

---

## 2. Pre-Approved Templates

In der Krise habt ihr keine Zeit, Statements von Null zu schreiben. Pre-Approved Templates sind **Skelette für die häufigsten Krisen-Typen**, die im Ernstfall in 15 Minuten auf die konkrete Situation angepasst werden können.

### Welche Templates ihr braucht

Minimum 6 Templates, abgedeckt nach den Coombs-Clustern:

| Template | Anlass |
|---|---|
| **A1** | Cluster A — Cyber-Attacke / externes Versagen |
| **A2** | Cluster A — Falsche Anschuldigungen / Gerüchte |
| **B1** | Cluster B — Technische Panne / Service-Ausfall |
| **B2** | Cluster B — Produkt-Defekt / Rückruf |
| **C1** | Cluster C — Kommunikations-Fehler / Werbe-Panne |
| **C2** | Cluster C — Mitarbeiter:innen-Fehlverhalten / Vorsatz |

Optional, je nach Branche:
- DSGVO-Datenpanne (Sub-Template B/C)
- Finanzkrise (Sub-Template B/C)
- Politische Stellungnahme mit Backlash

### Aufbau eines Templates

Jedes Template hat:

```markdown
# Template [Code]: [Krise-Typ]

## Anwendungs-Kontext
[Wann wird dieses Template aktiviert?]

## Variablen (zu ersetzen)
- [VORFALL_BESCHREIBUNG]
- [BETROFFENE_ANZAHL]
- [DATUM_ZEIT]
- [HILFE_KONTAKT]
- ...

## Holding Statement (Stunde 1–2)
[Skelett mit Variablen]

## Detailliertes Statement (Stunde 6–24)
[Skelett mit Variablen]

## Mitarbeiter-Statement (Mail/Slack)
[Skelett mit Variablen]

## Pressemitteilung (formell)
[Skelett mit Variablen]

## Update-Templates (Tag 2, Tag 3, etc.)
[Skelette mit Variablen]

## Strategische Empfehlung
[Welche Apologia-Strategie passt? Coombs-Cluster?]
[Welche Maßnahmen sind typisch?]
```

### Templates aktualisieren

- **Halbjährlich** Review aller Templates
- **Nach jeder Krise** Lessons in Templates einbauen
- **Bei Branchen-Änderungen** (z.B. neue Regulatorik) Templates ergänzen
- **Bei Plattform-Änderungen** Format-Vorgaben aktualisieren

---

## 3. Stakeholder-Karte vor der Krise

Siehe `02_Stakeholder-Mapping.md` für Methodik.

**Wichtig hier:** Die Stakeholder-Karte muss **gepflegt werden**. Eine veraltete Liste mit Telefonnummern von Personen, die nicht mehr bei der Marke sind, ist im Notfall wertlos.

**Pflege-Rhythmus:**
- **Monatlich:** Quick-Check (Wechsel bei Schlüsselpersonen?)
- **Quartalsweise:** Vollständige Aktualisierung
- **Halbjährlich:** Test-Kommunikation (sind alle Kontaktdaten korrekt?)

---

## 4. Monitoring & Frühwarnsystem

Eine Krise wird umso besser gemeistert, je früher sie erkannt wird.

### Monitoring-Tools

**Pflicht:**
- **Social Listening Tool** (Brandwatch, Talkwalker, Mention, Meltwater)
  - 24/7-Monitoring der wichtigsten Plattformen
  - Alerts bei Reichweiten-Schwellenwerten
  - Sentiment-Tracking
- **Google Alerts** für die Marke + relevante Begriffe
- **Pressemonitoring** (z.B. PressReader, news.spotter)

**Optional:**
- **Forum-Monitoring** (Reddit, branchen-spezifische Foren)
- **Trustpilot / Bewertungs-Monitoring**
- **Mitarbeiter-Plattformen** (Kununu, Glassdoor)

### Alert-Schwellenwerte definieren

Welche Schwellenwerte lösen welche Reaktion aus?

| Schwellenwert | Reaktion |
|---|---|
| **Plötzlicher Mention-Anstieg (z.B. 5x über Baseline)** | Social-Media-Manager prüft sofort |
| **Sentiment-Verschiebung (>30% negativ)** | Comms-Lead wird informiert |
| **Spezifische Keywords (z.B. "Skandal", "Klage")** | Krisenstab-Lead informiert |
| **Multiplikator-Account postet negativ (z.B. >100k Follower)** | Krisenstab-Aktivierung in Bereitschaft |
| **Presse-Anfrage zu kritischem Thema** | Krisenstab-Aktivierung |
| **Behörden-Anfrage** | Krisenstab-Aktivierung + Rechtsteam SOFORT |

### Wer ist „auf Wacht"?

In normalen Zeiten reicht reguläres Social-Media-Management. Während intensiver Phasen (z.B. Produkt-Launch, kontroverse Kampagne) sollte das Monitoring intensiviert werden.

**Zusätzlich:** Vorher Verantwortlichkeiten klären, wer am Wochenende/Feiertag „auf Wacht" ist. Rotations-System für den Krisenstab.

---

## Krisen-Simulationen / Übungen

Theorie reicht nicht. Krisenkommunikation ist **Skill**, der geübt werden muss.

### Empfohlene Übungs-Frequenz

| Übungs-Typ | Frequenz |
|---|---|
| **Tabletop-Übung** (Krisenstab geht ein Szenario durch) | 2x jährlich |
| **Live-Simulation** (mit Mock-Posts, Mock-Presse-Anfragen) | 1x jährlich |
| **Notfall-Erreichbarkeitstest** (alle Stakeholder ohne Vorwarnung) | 1x jährlich |
| **Externer Audit** (PR-Agentur prüft Setup) | Alle 2 Jahre |

### Beispiel Tabletop-Übung

**Szenario:** Ein:e ehemalige:r Mitarbeiter:in postet einen kritischen Twitter-Thread mit Anschuldigungen zur Unternehmenskultur. Thread wird in 4 Stunden auf 80.000 Views verbreitet.

**Übungs-Ablauf:**
1. Krisenstab wird aktiviert (simuliert)
2. Bewertung nach Säule 01 — Krise oder Welle?
3. Stakeholder-Mapping anwenden — wer informieren?
4. Holding Statement entwerfen — gegenseitig kritisch reviewen
5. Detaillierteres Statement entwerfen
6. Recovery-Plan skizzieren

**Dauer:** 3–4 Stunden.

**Auswertung:** Was hat gut funktioniert? Was nicht? Welche Lücken im Playbook?

---

## Rechtliche Awareness vor der Krise

Wann müsst ihr **rechtliche Beratung** in den Krisenstab holen — proaktiv?

### Trigger für Rechtsberatung

- **Daten-Vorfall** (DSGVO Art. 33: 72h-Meldepflicht)
- **Service-Vorfall mit Schadensersatz-Risiko**
- **Produkt-Defekt mit Sicherheitsrelevanz**
- **Mitarbeiter:innen-Vorfall mit arbeitsrechtlichen Konsequenzen**
- **Diskriminierungs-Vorwürfe**
- **Behörden-Anfragen**
- **Werberecht-Verstöße** (UWG, HWG, Markenrecht)
- **Wettbewerber-Klagen-Risiko**

### Grundlegende rechtliche Hinweise (kein Rechtsrat — nur Awareness)

**DSGVO (Art. 33 + 34):**
- Daten-Pannen-Meldung an Behörde binnen 72 Stunden
- Bei hohem Risiko: Information der Betroffenen
- Bußgeld bis 10 Mio € / 2 % Umsatz

**Werberecht (UWG):**
- Krisenkommunikation darf nicht irreführen
- Korrekturmaßnahmen müssen nachweisbar sein

**Sorgfaltspflichten:**
- Bei sicherheitsrelevanten Produkten: Behörden-Meldepflicht oft sofort
- Bei börsennotierten Marken: Ad-hoc-Mitteilung kann Pflicht sein

**Wichtig:** Diese Hinweise sind **keine Rechtsberatung**. Sie sind Awareness-Punkte, damit ihr wisst, wann ein:e Anwält:in einzubeziehen ist. **Im Zweifel immer Rechtsteam fragen.**

---

## Krisen-Playbook physisch verfügbar machen

In der Krise braucht jede:r Zugriff auf das Playbook — auch wenn IT-Systeme ausfallen.

**Verfügbarkeit:**
- Digitale Version im internen Wiki (Notion, Confluence, SharePoint)
- PDF-Backup auf privaten Geräten der Krisenstab-Mitglieder
- Physische Mappen mit Druckversion bei Schlüsselpersonen
- Pre-Approved Templates an mehreren Stellen abgelegt

**Bei System-Ausfällen (z.B. Cyber-Attacke, die IT lahmlegt):**
- Backup-Kommunikationskanal definieren (z.B. private Mobilnummern, alternative E-Mail-Adresse)
- Offline-Templates verfügbar
- Externe Berater:innen erreichbar (PR-Agentur, Rechtsanwält:in)

---

## Setup-Checkliste

### Erstes Setup (einmalig)

- [ ] Krisenstab-Mitglieder definiert und kommuniziert
- [ ] Backup-Personen für jede Rolle festgelegt
- [ ] 24/7-Erreichbarkeit organisiert (Privat-Kontaktdaten)
- [ ] Notfall-Kommunikationskanal eingerichtet (Slack/Teams War Room)
- [ ] RACI-Matrix für Standard-Aktionen erstellt
- [ ] 6 Pre-Approved Templates erstellt
- [ ] Stakeholder-Karte erstellt
- [ ] Monitoring-Tools eingerichtet
- [ ] Alert-Schwellenwerte definiert
- [ ] Playbook digital + physisch verfügbar
- [ ] Externe Berater:innen identifiziert (PR-Agentur, Anwalt:innen)

### Laufendes Pflege (jährlich-monatlich)

- [ ] Monatlich: Quick-Check Stakeholder-Karte
- [ ] Quartalsweise: Vollständige Stakeholder-Aktualisierung
- [ ] Halbjährlich: Templates-Review
- [ ] Halbjährlich: Tabletop-Übung
- [ ] Jährlich: Live-Simulation
- [ ] Jährlich: Notfall-Erreichbarkeitstest
- [ ] Alle 2 Jahre: Externer Audit des Playbook
