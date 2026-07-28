# Säule 3: Freigabe-Workflows

Diese Säule ist der Kern des Moduls. Sie beantwortet: **In welcher Reihenfolge, in welcher Frist, und was gilt bei Schweigen?**

---

## Die zwei Freigabeebenen

Der wichtigste Hebel im gesamten Modul. Er entscheidet über den Abstimmungsaufwand um den Faktor drei und mehr.

| Ebene | Was freigegeben wird | Aufwand |
|---|---|---|
| **Planfreigabe** | Der Monatsplan: Themen, Formate, Termine. Vor der Produktion | einmal pro Monat |
| **Assetfreigabe** | Das fertige Einzel-Asset. Nach der Produktion | pro Asset |

### Die drei Modelle

| Modell | Ablauf | Aufwand | Geeignet für |
|---|---|---|---|
| **Nur Planfreigabe** | Plan wird freigegeben, Assets gehen ohne weitere Freigabe live | niedrig | eingespielte Zusammenarbeit, unkritische Branchen, hohes Vertrauen |
| **Plan plus Assetfreigabe** | Beide Ebenen | hoch | Standard bei neuen Mandaten, regulierte Branchen, hohe Markensensibilität |
| **Nur Assetfreigabe** | Kein Plan, jedes Asset einzeln | **höchster Aufwand, schlechtestes Ergebnis** | nie empfehlen |

**Warum "nur Assetfreigabe" das schlechteste Modell ist:** Ohne Planfreigabe wird bei jedem Asset über die Richtung diskutiert, nicht über die Ausführung. Die Grundsatzdiskussion findet dann zwölfmal statt statt einmal. Und wenn ein Asset abgelehnt wird, ist die Produktion bereits bezahlt.

**Der Übergang, den man anstreben sollte:** Neue Mandate starten mit "Plan plus Asset". Nach drei bis vier funktionierenden Zyklen Vorschlag, für definierte Formate auf reine Planfreigabe umzustellen. Das ist ein Vertrauensbeweis und senkt beiderseits den Aufwand.

---

## Fristen

**Belegstatus: Konvention.** Die Werte unten sind Vorschläge zur Vereinbarung, keine Branchenstandards, auf die man sich berufen kann. Siehe Hinweis in `00_Index.md`.

| Freigabeart | Vorgeschlagene Frist | Begründung |
|---|---|---|
| Monatsplan | 5 Werktage | genug Zeit für interne Rücksprache, ohne den Produktionsstart zu verschieben |
| Einzel-Asset, Standard | 2 bis 3 Werktage | Produktion ist fertig, es geht nur um Ja oder Anmerkung |
| Einzel-Asset, tagesaktuell | 4 bis 24 Stunden | siehe `Aktuelle_Themen_und_Newsjacking/03_Schnellbewertung_und_Reaktion.md` |
| Reaktion auf Community-Anfrage mit Rückfragebedarf | siehe SLA | `Community_Management_Playbook/04` |
| Krisenreaktion | sofort | `Krisenkommunikation_Playbook/03_Response-Timeline.md` |
| Rohmaterial-Lieferung durch Kunden | bis zum 20. des Vormonats | damit der Folgemonat produziert werden kann |

### Der Zeitpuffer, der eingeplant werden muss

Ein Monatsplan, der am 25. freigegeben werden soll, muss am 18. rausgehen: 5 Werktage Frist plus Puffer für eine Korrekturschleife. Wer am 24. verschickt, plant den Verzug ein.

**Rückwärtsrechnung für einen Monatsstart am 1.:**

| Tag | Was passiert |
|---|---|
| 10. des Vormonats | Rohmaterial-Anforderung an Kunden |
| 15. bis 18. | Planentwurf durch Agentur |
| 18. | Plan an Kunden zur Freigabe |
| bis 25. | Freigabefrist, 5 Werktage |
| 20. | Deadline Rohmaterial-Lieferung |
| 25. bis 31. | Produktion |
| 28. bis 31. | Assetfreigaben, gestaffelt |
| 1. | Start |

Das ist eng. Bei monatlicher Produktion ohne Vorlauf ist Verzug der Normalfall, nicht die Ausnahme.

**Der Ausweg ist Vorlauf, nicht Beschleunigung.** Ziel sollte sein, einen Monat Vorsprung aufzubauen: Im Juli wird September produziert. Das entspannt jede Freigabe und ermöglicht Batching, was laut `Kalkulation_und_Angebot/01_Aufwandsrichtwerte.md` 20 bis 40 Prozent Stückaufwand spart. Der Aufbau dieses Vorsprungs kostet einmalig einen Doppelmonat.

---

## Die Schweigefrist

**Regel:** Erfolgt bis Fristablauf keine Rückmeldung, gilt der Vorschlag als freigegeben.

**Warum sie nötig ist:** Ohne Folge ist eine Frist eine Bitte. Der Monatsplan verschiebt sich in den Folgemonat, die Stunden sind verbraucht, das Honorar einmal gezahlt.

**Wie sie formuliert wird:** Freundlich und im Voraus, nicht als Drohung im Konfliktfall.

> "Sofern wir bis zum [Datum] keine Rückmeldung erhalten, gehen wir von Ihrer Freigabe aus und starten die Produktion. Damit halten wir den Zeitplan, auch wenn bei Ihnen einmal etwas dazwischenkommt."

Der zweite Satz ist wichtig. Er macht aus einer Regel eine Serviceleistung, ohne den Inhalt zu ändern.

**Wichtige Einschränkung:** Eine Schweigefrist muss vereinbart sein, um zu gelten. Ob und wie sie im Einzelfall vertragsrechtlich trägt, ist eine juristische Frage und in dieser Wissensbasis ausdrücklich nicht abgedeckt, siehe `Recht_Compliance_DE/00_Index.md`, wo Agenturverträge als eigenes Rechtsgebiet ausgeklammert sind. Was hier steht, ist Prozesslogik.

**Wo die Schweigefrist nicht angewendet werden sollte:**

- Bei rechtlich oder fachlich prüfungsbedürftigen Inhalten
- Bei Aussagen über Dritte oder Wettbewerber
- Bei allem, was Personen zeigt, deren Einwilligung nicht dokumentiert ist
- Bei tagesaktuellen Themen mit Reputationsrisiko, siehe `Aktuelle_Themen_und_Newsjacking/04_Ton_und_Tabu-Zonen.md`

Bei diesen Kategorien gilt: keine Freigabe bedeutet keine Veröffentlichung. Das gehört ausdrücklich in die Vereinbarung, sonst entsteht ein Widerspruch.

---

## Was eine Korrekturschleife ist

Marktstandard: 2 Schleifen inklusive, danach 200 bis 500 € pro Runde (chaerry, Juni 2026). Diese Zahl ist nur belastbar, wenn definiert ist, was zählt.

**Brauchbare Definition:**

> Eine Korrekturschleife ist **eine gebündelte, abgeschlossene Rückmeldung aller beteiligten Personen**, übermittelt in einem Vorgang innerhalb der vereinbarten Frist.

**Was daraus folgt:**

| Fall | Zählt als |
|---|---|
| Eine Mail mit allen Anmerkungen aller Beteiligten | eine Schleife |
| Drei Mails von drei Personen am selben Tag | eine Schleife, wenn innerhalb der Frist |
| Nachträgliche Anmerkung nach begonnener Umsetzung | neue Schleife |
| Widersprüchliche Anmerkungen mehrerer Personen | eine Schleife, aber Rückfrage zur Klärung ist keine neue |
| Änderung, die auf einer Änderung der Vorgabe beruht | keine Schleife, sondern Scope-Änderung |

**Die letzte Zeile ist die wichtigste.** Wenn der Kunde nach der Produktion die Zielgruppe oder Kernaussage ändert, ist das keine Korrektur, sondern ein neuer Auftrag. Diese Unterscheidung muss man aussprechen können, ohne dass es kleinlich wirkt. Formulierung, die funktioniert:

> "Das können wir gerne so machen. Weil sich damit die Grundaussage ändert, ist es keine Korrektur der bestehenden Version, sondern eine neue. Ich schicke Ihnen dazu kurz den Zusatzaufwand, dann können Sie entscheiden."

---

## Der Freigabekanal

**Regel: ein Ort für Feedback, nicht drei.**

| Kanal | Geeignet | Problem |
|---|---|---|
| Planungstool mit Kommentarfunktion | ja, ideal | Kunde muss es nutzen wollen |
| Ein Mail-Thread pro Monatsplan | ja, praktikabel | zerfällt bei mehreren Beteiligten |
| Geteiltes Dokument mit Kommentaren | ja | Versionierung muss klar sein |
| Chat und Messenger | nur für Terminfragen | Feedback geht verloren, keine Nachvollziehbarkeit |
| Telefon | nur zur Klärung | muss danach schriftlich festgehalten werden |

**Praxisregel:** Was mündlich entschieden wurde, gilt erst, wenn es schriftlich bestätigt ist. Nicht aus Misstrauen, sondern weil sich Erinnerungen unterscheiden.

**Zur DM- und Messenger-Nutzung mit Kunden:** Rechtlich relevant, wenn dabei personenbezogene Daten oder Marketinginhalte fließen. Siehe `Recht_Compliance_DE/08_Messenger_und_DM_Marketing.md`.

---

## Freigabe bei Paid

Eigene Logik, weil hier Geld unmittelbar fließt.

| Was | Freigabe nötig? |
|---|---|
| Kampagnenstart mit vereinbartem Budget | ja, einmalig |
| Creative-Varianten innerhalb der freigegebenen Aussage | nein, wenn Delegationsstufe vereinbart |
| Budgetverschiebung zwischen Ad-Sets innerhalb der Gesamtsumme | nein, wenn vereinbart |
| Budgeterhöhung | ja, immer |
| Neue Zielgruppe oder neuer Kanal | ja |
| Pausieren einer unterperformenden Kampagne | nein, das ist Optimierung |

**Wichtig, gegen die Lernphasen-Logik:** Wer jede Optimierung freigeben lässt, verzögert Eingriffe und verletzt die Steuerungslogik aus `Paid_Performance_Methodik/06_Optimierung_und_Metriken.md`. Dort steht auch die Gegenwarnung: Zu frühes Eingreifen setzt die Lernphase zurück. Beides zusammen bedeutet: Die Agentur braucht Handlungsfreiheit **und** die Disziplin, sie nicht aus Nervosität zu nutzen.

Das gehört als Erwartung ins Onboarding: In den ersten Tagen einer Kampagne passiert bewusst nichts, und das ist kein Stillstand.

---

## Verweise

- Rollen hinter den Freigaben: `02_Rollen_und_Verantwortung.md`
- Betriebsrhythmus und Termine: `04_Betriebsrhythmus.md`
- Wenn Fristen reißen: `05_Eskalation_und_Konflikt.md`
- Korrekturschleifen im Angebot: `Kalkulation_und_Angebot/04_Scoping_und_Annahmen.md`
- Content-Workflow inhaltlich: `KI_Content_Planung_Guideline/04_Operativer-Workflow.md`
- Tagesaktuelle Themen mit verkürzter Frist: `Aktuelle_Themen_und_Newsjacking/03_Schnellbewertung_und_Reaktion.md`
