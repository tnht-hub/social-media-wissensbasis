# Säule 3: Targeting & Audiences

Targeting hat sich grundlegend verschoben. Die alte Welt feiner Interessen- und Lookalike-Audiences ist durch Signalverlust und AI-Targeting geschwächt worden. Die neue Welt heißt: **breit aussteuern, den Algorithmus über das Creative steuern, erste-Partei-Daten gut pflegen.**

Diese Säule dokumentiert die Audience-Typen, den Broad-Targeting-Trend und die Auswirkungen von Datenschutz und Signalverlust.

---

## Die drei Audience-Typen

| Typ | Was es ist | Funnel-Stufe |
|---|---|---|
| **Cold / Broad** | Menschen ohne vorherigen Kontakt, breit ausgesteuert vom Algorithmus | TOFU |
| **Custom Audiences** | Menschen mit Vorkontakt (Website-Besucher, Kund:innen-Listen, Video-Viewer, Engager) | MOFU / BOFU (Retargeting, siehe Säule 05) |
| **Lookalike Audiences** | Algorithmisch ähnliche Menschen zu einer Seed-Audience (z. B. zu Käufer:innen) | TOFU / MOFU |

---

## Custom Audiences: erste-Partei-Daten als Fundament

Custom Audiences basieren auf eigenen Daten und sind dadurch vom Signalverlust am wenigsten betroffen, sofern sauber getrackt wird:

- **Website-Besucher** (über Pixel / Conversions API)
- **Kund:innen- und Lead-Listen** (CRM-Upload, gehasht)
- **Engagement-Audiences** (Profil-Besucher, Video-Viewer, Formular-Öffner)
- **App-Aktivität**

**Wichtig 2026:** Erste-Partei-Daten sind das wertvollste Asset. Sie speisen Retargeting (Säule 05), sind die beste Seed für Lookalikes und liefern dem Algorithmus saubere Konversions-Signale. Wer Custom Audiences vernachlässigt, verliert den verlässlichsten Targeting-Hebel.

---

## Lookalike Audiences: geschwächt, aber nicht tot

Lookalikes leiden unter degradierter Seed-Daten-Qualität (Signalverlust durch iOS- und Browser-Privacy). Sie funktionieren 2026 aber weiterhin, wenn man sie anpasst:

- **Seed-Qualität schlägt Seed-Größe:** Eine kleine, saubere Liste echter Käufer:innen ist eine bessere Seed als eine große, unscharfe Liste.
- **Mit erste-Partei-Daten neu aufbauen:** Hochwert-Kund:innen, wiederkehrende Käufer:innen oder qualifizierte Leads als Seed nutzen, nicht beliebige Website-Besucher.
- **Rolle hat sich verschoben:** Lookalikes sind heute oft eher ein Test-Werkzeug für neue Märkte oder Creative-Konzepte als der Haupt-Aussteuerungs-Hebel.

---

## Der Broad-Targeting-Trend

Das alte Paradigma (feine Interessen + Lookalikes manuell bauen) ist weitgehend durch AI-Audiences abgelöst worden: Meta Advantage+ Audience, TikTok Smart+. Diese nutzen Verhaltenssignale (Pixel, Conversions API), um vorherzusagen, wer am ehesten konvertiert.

**Wie AI-Audiences arbeiten:** Man kann weiterhin Hinweise geben (Altersbereiche, Orte, Interessen), aber diese sind nur **Startsignale**, keine harten Grenzen. Der Algorithmus beginnt dort und expandiert darüber hinaus, wenn er anderswo besser konvertierende Menschen findet.

**Warum Broad oft gewinnt:** Der Algorithmus arbeitet besser mit aggregierten Mustern als mit schrumpfenden Pools nachverfolgbarer Einzelpersonen. AI-getriebenes Broad-Targeting hat sich verbessert, während granulares User-Level-Targeting degradiert ist.

### Hybrid-Ansatz (Praxis der fortgeschrittenen Accounts 2026)

Die meisten erfahrenen Advertiser fahren weder rein broad noch rein interessenbasiert, sondern eine Mischung:

| Anteil | Verwendung |
|---|---|
| **70–80 %** | Advantage+ / Broad-Targeting-Kampagnen (Prospecting) |
| **10–20 %** | Retargeting (warme Audiences, siehe Säule 05) |
| **5–10 %** | Interessen- oder Lookalike-Seeded-Kampagnen zum Testen neuer Konzepte oder Märkte |

---

## Auswirkungen von Datenschutz und Signalverlust

Der Hintergrund, warum sich Targeting verschoben hat:

- **iOS App Tracking Transparency:** Hat einen großen Teil der Drittanbieter-Daten entfernt, die das alte Targeting fütterten.
- **Browser-Privacy:** Wegfall von Third-Party-Cookies, Tracking-Restriktionen.
- **Folge:** Schlechtere Seed-Daten, ungenauere Attribution, kleinere nachverfolgbare Pools.

### Gegenmaßnahmen

| Maßnahme | Wirkung |
|---|---|
| **Conversions API / serverseitiges Tracking** | Gibt dem Algorithmus wieder verlässliche Signale zurück (siehe Säule 06) |
| **Erste-Partei-Daten aufbauen** | Eigene Kund:innen- und Lead-Listen werden zum wertvollsten Asset |
| **Auf das Creative-Signal setzen** | Wenn Targeting schwächer wird, übernimmt das Creative die Selektion (siehe Säule 04) |
| **Breit aussteuern** | Dem Algorithmus den Suchraum lassen, statt ihn künstlich zu verengen |

**DACH-Hinweis:** In Deutschland und der EU sind DSGVO-konformes Tracking, Consent-Management und transparente Datenverarbeitung Pflicht. Saubere Consent-Banner und korrekt eingebundene Conversions API sind Voraussetzung dafür, dass Custom Audiences und Conversion-Optimierung überhaupt rechtssicher funktionieren.

---

## Checkliste Targeting

- [ ] Conversions API / serverseitiges Tracking eingerichtet (DSGVO-konform)
- [ ] Erste-Partei-Daten gesammelt und als Custom Audiences angelegt
- [ ] Lookalikes mit hochwertiger Seed (echte Käufer:innen) gebaut, nicht mit beliebigen Besuchern
- [ ] Prospecting primär broad / Advantage+ ausgesteuert
- [ ] Hybrid-Verteilung (Broad / Retargeting / Test) festgelegt
- [ ] Audience-Hinweise als Startsignal verstanden, nicht als harte Grenze
- [ ] Creative als primären Steuerungs-Hebel akzeptiert, nicht das Targeting

---

## Verweis

Plattformspezifische Audience-Tools (Advantage+ Setup, TikTok Smart+, LinkedIn Matched Audiences) stehen in den Plattform-Ordnern. Diese Säule liefert die übergreifende Targeting-Logik.
