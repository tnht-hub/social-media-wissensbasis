# Säule 9 — Rechtliches

**Disclaimer vorab:** Diese Säule liefert **Awareness**, keine Rechtsberatung. Für konkrete Rechtsfragen ist Fachanwalt:innen-Beratung erforderlich. Im Zweifel: Anwält:in fragen, lieber einmal zu viel.

Diese Säule dokumentiert die wichtigsten rechtlichen Aspekte für Visual Production in Deutschland/EU.

---

## Vier rechtliche Hauptbereiche

| Bereich | Was es betrifft |
|---|---|
| **EU AI Act** | KI-generierte Inhalte — Kennzeichnung, Urheberrecht |
| **GEMA / Musik-Lizenzen** | Musik in Social-Media-Videos |
| **BFSG (Barrierefreiheit)** | Untertitel, Alt-Texte für Webseiten und Online-Inhalte |
| **DSGVO + Recht am eigenen Bild** | Personen in Bildern/Videos |

Jeder Bereich hat eigene Pflichten, eigene Fristen, eigene Bußgelder.

---

## 1. EU AI Act — KI-generierte Inhalte

Der EU AI Act bringt **ab August 2026** verbindliche Kennzeichnungspflicht für KI-generierte Inhalte.

### Was muss gekennzeichnet werden

> **Texte, Bilder, Videos und Audio**, die durch generative KI-Systeme erstellt oder verändert wurden, müssen klar gekennzeichnet werden — wenn der Inhalt geeignet ist, Menschen über seinen Ursprung zu täuschen oder den Eindruck einer menschlichen Kommunikation zu erwecken.

### Was das konkret bedeutet

| Use Case | Pflicht |
|---|---|
| **Vollständig KI-generiertes Bild** in Marketing | Kennzeichnung Pflicht |
| **KI-generierter Video-Clip** in Reel | Kennzeichnung Pflicht |
| **Echte Person + KI-Background (Hybrid)** | Kennzeichnung empfohlen, da Compositing manipulativ wirken kann |
| **KI-Voice-Over** | Kennzeichnung Pflicht |
| **KI-Bearbeitung eines Fotos (Filter, Beautify)** | Grauzone — bei substanzieller Veränderung Kennzeichnung |
| **KI als reines Hilfsmittel** (z.B. Hintergrund-Removal) | Meistens keine Kennzeichnung nötig |

### Wie wird gekennzeichnet

Die Kennzeichnung muss erfüllen:

1. **Für Menschen verständlich:** Sichtbarer Hinweis wie "KI-generiert" oder Wasserzeichen
2. **Für Maschinen lesbar:** Technische Metadaten in den Dateien (XML, IPTC, EXIF)

**Praktisch:** Ein kleiner Schriftzug „KI-generiert" oder „AI-generated" in der Caption oder im Bild. Plus Metadaten beim Export.

### Bußgelder

- Bis zu **35 Millionen Euro** oder **7 % des weltweiten Konzernumsatzes** (höherer Betrag).

### Urheberrecht von KI-Bildern

Wichtig zu verstehen:

> **KI-generierte Bilder sind in Deutschland und der EU grundsätzlich NICHT urheberrechtlich geschützt.**

Das bedeutet:
- Eure KI-Bilder können von anderen verwendet werden (oder zumindest nicht über Urheberrecht geschützt)
- Nur bei **„massivem Eingriff"** (extreme Detail-Steuerung, manueller Nach-Edit) ist Schutz möglich
- Bei reiner Text-zu-Bild-Generierung kein Schutz

**Konsequenz:** Wenn ihr KI-Bilder als Brand-Asset etablieren wollt, müsst ihr sie über andere Mechanismen schützen (Marken-Anmeldung, sichtbare Brand-Elemente).

### Praktische Empfehlungen

- **Kennzeichnungs-Pflicht ab August 2026 einhalten:** Auch wenn ihr bisher nichts gekennzeichnet habt — ab Sommer 2026 ist es Pflicht
- **Tool-Lizenzen prüfen:** Welche Tools erlauben kommerzielle Nutzung? (siehe Säule 03 — fast alle Pro-Tools tun das)
- **Bei Werbe-Kampagnen mit KI-generierten Personen:** Besondere Vorsicht — kann als irreführende Werbung gewertet werden

---

## 2. GEMA / Musik-Lizenzen

Musik in Social-Media-Videos ist **rechtlich komplex** und wird oft unterschätzt.

### Grundregel: Privat vs. Kommerziell

| Nutzung | Lizenz-Bedarf |
|---|---|
| **Privater Nutzer / persönlicher Account** | Synchronisations-Recht ist über Plattform-Lizenz mit GEMA abgedeckt |
| **Unternehmen / Freelance / Selbstständige (kommerziell)** | **Separate Lizenz erforderlich** |

**Wichtig:** Wenn euer Account ein Business-Account ist oder ihr für ein Unternehmen postet, gilt **kommerzielle Nutzung** — auch wenn der Post nicht direkt werblich ist.

### GEMA-Lizenz auf Instagram, TikTok, Facebook

Die GEMA hat mit den Plattformen **keine Synchronisations-Rechte** für UGC-Plattformen vereinbart, was kommerzielle Nutzung betrifft. Konkret:

- **Privatpersonen** dürfen Musik aus dem Plattform-Catalog frei nutzen
- **Unternehmen** müssen eigene Lizenzen für kommerzielle Werbung haben
- Die Plattform-Catalog-Musik darf **nicht ohne Weiteres** für Werbe-Zwecke verwendet werden

### Konkrete Konsequenzen

| Use Case | Was erlaubt ist |
|---|---|
| **Mein Privat-Account postet ein Tanzvideo zu Top-100-Hit** | OK über Plattform-Lizenz |
| **Brand-Account postet Reel zu Top-100-Hit, kommerziell** | **Nicht erlaubt** — Lizenz fehlt |
| **Brand-Account postet Reel zu Plattform-Business-Library-Track** | OK |
| **Brand-Account postet Reel zu lizenzierter Premium-Library (Epidemic, Artlist)** | OK |
| **Werbe-Anzeige mit lizenziertem Musik-Track** | OK, wenn die Lizenz Werbung abdeckt |

### Praktische Empfehlung für Brand-Accounts

**Niemals:**
- Trending Sounds, die nicht in der Business-Library der Plattform sind
- GEMA-pflichtige Musik ohne separate Lizenz

**Stattdessen:**
- **Business-Library** der Plattform nutzen (Meta Sound Collection, TikTok Commercial Music)
- **Premium-Library** wie **Epidemic Sound, Artlist, Soundstripe** (siehe Säule 06)
- **Eigene KI-generierte Musik** (Suno, Udio) — aber Rechtslage hier noch in Klärung

### Risiken bei Verstoß

- Take-Down der Inhalte
- Account-Sperrung
- Schadensersatz-Forderungen
- Bei systematischer Verletzung: rechtliche Schritte

---

## 3. BFSG — Barrierefreiheitsstärkungsgesetz

Das BFSG ist seit **28. Juni 2025** in Kraft. Es macht Barrierefreiheit für digitale Produkte und Dienstleistungen verbindlich.

### Wer ist betroffen

Das BFSG gilt für:
- **E-Commerce-Anbieter** (alle, die Produkte oder Dienstleistungen B2C online anbieten)
- **Größere Webseiten** mit digitalem Verkauf
- **Banken / Versicherungen / Telekommunikation**
- **Öffentliche Stellen** (waren schon vorher unter BITV)

**Ausnahmen:** Kleinstunternehmen unter 10 Mitarbeiter:innen und Jahresumsatz unter 2 Mio €.

### Was für Visual Content konkret gilt

| Asset-Typ | Pflicht |
|---|---|
| **Videos mit gesprochenem Inhalt** | **Untertitel Pflicht** |
| **Live-Audio** (Webinare, Live-Streams) | Untertitel Pflicht |
| **Bilder auf Webseiten** | **Alt-Texte Pflicht** |
| **Bilder in Social Media (eigene Webseite)** | Alt-Texte Pflicht |
| **Videos auf eigener Webseite** | Untertitel + Audio-Beschreibungen |

**Wichtig:** Soziale Medien wie Instagram/TikTok haben eigene Accessibility-Tools (Auto-Captions auf TikTok), die bei der Pflicht-Erfüllung helfen. Aber die rechtliche Verantwortung liegt beim Inhaltsanbieter.

### Konkrete Vorgaben für Untertitel

- **Maximale Länge:** 37 Zeichen pro Zeile, max 2 Zeilen
- **Anzeigedauer:** 1–6 Sek pro Untertitel
- **Position:** Untertitel sollten nicht relevanten Bild-Inhalt verdecken
- **Sprache:** Klare, vollständige Sätze
- **Sprecher-Kennzeichnung:** Bei mehreren Sprechern Position oder Farbe wechseln

### Konkrete Vorgaben für Alt-Texte

- **Maximale Länge:** 125 Zeichen (Screenreader-Standard)
- **Beschreibung:** Was zeigt das Bild konkret? Nicht „Schönes Bild" sondern „Person mit Helm vor Windkraftanlage"
- **Wichtige Texte im Bild:** Im Alt-Text wiedergeben
- **Bei dekorativen Bildern:** Leerer Alt-Text (`alt=""`)

### WCAG 2.1 Level AA

Der konkrete Standard, der erfüllt werden muss, ist **WCAG 2.1 Level AA** — das international anerkannte Web-Accessibility-Standard.

Wichtigste Aspekte für Visual Content:
- Kontrast-Verhältnis (Text auf Bild: mindestens 4.5:1)
- Untertitel (1.2.2)
- Alt-Texte (1.1.1)
- Audio-Beschreibung für reine Audio-/Video-Inhalte (1.2.3)

### Bußgelder

- Bis zu **100.000 Euro** für Verstöße

### Praktische Empfehlung

- **Alle Videos mit gesprochenem Inhalt brauchen Untertitel** — auch wenn nicht auf eigener Webseite. Best Practice.
- **Auto-Captions als Start, dann manuell prüfen** — Auto-Captions sind oft fehlerhaft
- **Alt-Texte bei allen Social-Media-Posts** — selbst wenn Plattform es nicht erzwingt, kostet wenig und ist gute Praxis
- **Kontrast prüfen** — Text auf Bild muss lesbar sein

---

## 4. DSGVO + Recht am eigenen Bild

Bei Visual Content mit echten Personen greift sowohl DSGVO als auch das deutsche Recht am eigenen Bild.

### Recht am eigenen Bild (KUG / KUG § 22)

> **Bildnisse dürfen nur mit Einwilligung des Abgebildeten verbreitet oder öffentlich zur Schau gestellt werden.**

Das heißt: Bevor ihr ein Bild oder Video einer Person veröffentlicht, braucht ihr **deren Einwilligung**.

### Ausnahmen (§ 23 KUG)

Keine Einwilligung nötig für:
- Bildnisse der Zeitgeschichte (Prominente bei öffentlichen Ereignissen)
- Bilder, in denen Personen nur Beiwerk sind
- Bilder von Versammlungen / Aufzügen
- Bildnisse, die im Interesse der Kunst dienen

**ABER:** Diese Ausnahmen gelten **nicht für Werbung**. Für Werbe-Zwecke ist immer Einwilligung Pflicht.

### Einwilligungs-Form

- **Schriftlich** ist Best Practice (rechtlich sicher)
- Mündliche Einwilligung möglich, aber schwer nachweisbar
- **Klar formuliert:** Welche Bilder, welche Nutzung, welche Dauer, welcher Kanal
- **Widerrufbar:** Personen können Einwilligung widerrufen (mit Wirkung für die Zukunft)

### Modell-Verträge

Bei professionellen Aufnahmen:

```markdown
# Modell-Vereinbarung [PROJEKT]

## Identifikation
- Name:
- Geburtsdatum:
- Adresse:

## Aufnahme-Detail
- Datum:
- Ort:
- Foto / Video?
- Anzahl Aufnahmen:

## Verwendung
- Erlaubte Plattformen: [Instagram / TikTok / etc.]
- Erlaubte Zwecke: [Awareness / Recruiting / Werbung / etc.]
- Erlaubte Bearbeitungen: [Crop / Color-Grade / KI-Background-Replacement / etc.]
- Geografischer Geltungsbereich:
- Zeitraum:

## Honorar
- Honorar / Buyout:
- Zusatz-Vergütung bei zusätzlichen Verwendungen:

## Sonstiges
- Datenschutz-Hinweise (DSGVO)
- Widerrufs-Belehrung
- Aufbewahrungs-Fristen

Unterschrift Modell: ___________
Unterschrift Auftraggeber: ___________
Datum:
```

### DSGVO bei Personen-Fotos

Personenbezogene Daten in Visual Content fallen unter DSGVO:

- **Rechtmäßigkeit der Verarbeitung:** Einwilligung oder berechtigtes Interesse
- **Aufbewahrungs-Frist:** Nur so lange wie nötig
- **Auskunfts-Recht:** Personen können Auskunft verlangen, welche Bilder von ihnen verarbeitet werden
- **Löschungs-Recht:** Personen können Löschung verlangen

### KI-generierte Personen — Spezial-Fall

KI-generierte Personen, die **realen Personen ähneln**, sind problematisch:

- **Persönlichkeits-Recht** kann verletzt sein
- **Recht am eigenen Bild** kann analog gelten
- **Irreführung** der Audience möglich (EU AI Act)

**Empfehlung:** KI-generierte Personen sollten klar **nicht erkennbar** als echte Person sein. Bei Zweifeln: Anwält:in fragen.

### Mitarbeitende in Visual Content

Wenn ihr eigene Mitarbeitende in Visual Content zeigt:

- **Arbeitsvertrag** allein reicht meistens **nicht** für Werbung
- **Separate Modell-Vereinbarung** für jeden Werbe-Einsatz
- **Bei Ausscheiden:** Bilder müssen ggf. nicht mehr verwendet werden

---

## Rechtliche Trigger — wann Anwalt:in einbeziehen

Sofortige Rechtsberatung empfohlen bei:

- **KI-generierte Person ähnelt realer Person**
- **Modell verweigert nachträglich Einwilligung**
- **Musik-Nutzung in Werbung ohne klare Lizenz**
- **Krise: ein Inhalt löst rechtliche Forderungen aus**
- **Internationale Verwendung** (andere Länder haben andere Regeln)
- **Behörden-Anfrage** zu Inhalten (z.B. Datenschutz-Behörde)
- **Branchen-Regulatorik** unklar (Gesundheit, Finanzen, Politik)
- **Mitarbeiter:in ist Bildgegenstand und hat sich verändert (Ausscheiden, etc.)**

---

## Compliance-Checkliste pro Projekt

### KI-Inhalte
- [ ] EU AI Act: Wird der KI-Anteil gekennzeichnet?
- [ ] Tool-Lizenz erlaubt kommerzielle Nutzung?
- [ ] Wenn KI-Person: ähnelt sie keiner realen Person?

### Musik
- [ ] Lizenz für kommerzielle Nutzung vorhanden?
- [ ] Plattform-Business-Library oder Premium-Library?
- [ ] Bei Werbung: Lizenz deckt Werbe-Zwecke ab?

### Barrierefreiheit
- [ ] Untertitel bei allen Videos mit gesprochenem Inhalt
- [ ] Alt-Texte bei allen Bildern
- [ ] Kontrast (4.5:1) bei Text auf Bild

### Personen-Aufnahmen
- [ ] Einwilligung schriftlich vorliegend
- [ ] Modell-Vereinbarung gegengezeichnet
- [ ] Verwendungs-Zweck klar dokumentiert
- [ ] Aufbewahrungs-Frist DSGVO-konform

---

## Spezifisches Risiko: Öffentlicher Sektor

Für Marken im öffentlichen Sektor (Behörden, Ministerien, Public Health, NGOs):

- **Erhöhte Sorgfaltspflicht** bei allen rechtlichen Aspekten
- **Politische Sensibilität:** Werbung darf nicht parteiisch wirken
- **Informationsfreiheits-Gesetze:** Erhöhte Transparenz-Pflichten
- **BITV (vor BFSG):** Öffentliche Stellen sind schon länger zu Barrierefreiheit verpflichtet
- **Vergaberecht:** Bei Agentur-Beauftragungen — eigene Komplexität

Für öffentliche Aufträge: **Spezialisierte Vergabe-Anwält:innen** einbeziehen.

---

## Zusammenfassung: Die 5 wichtigsten Punkte

1. **EU AI Act ab August 2026:** Kennzeichnung Pflicht. Bußgeld bis 35 Mio €.
2. **GEMA für Brand-Accounts:** Niemals trending Sounds ohne Business-Library. Nur Premium-Library oder Plattform-Business-Catalog.
3. **BFSG seit 2025:** Untertitel + Alt-Texte Pflicht für viele Use Cases. Bußgeld bis 100k €.
4. **Recht am eigenen Bild:** Bei jedem Personen-Visual Einwilligung schriftlich.
5. **KI-Personen ≠ reale Personen:** Niemals so generieren, dass es Persönlichkeitsrechte verletzt.
