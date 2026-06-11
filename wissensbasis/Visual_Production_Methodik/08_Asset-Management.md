# Säule 8 — Asset-Management

Eine Visual-Production-Pipeline produziert Tausende von Dateien: Raw-Footage, KI-Generierungen, Edits, Exports, Music-Tracks, Reference-Images, LoRA-Files. Ohne System wird das innerhalb von 6 Monaten unbenutzbar.

Diese Säule dokumentiert, wie ihr eure Assets organisiert, benennt, versioniert und archiviert.

---

## Drei Asset-Management-Ebenen

| Ebene | Was es leistet |
|---|---|
| **Storage** | Wo liegen die Dateien? |
| **Naming** | Wie sind sie benannt? |
| **Versionierung** | Wie verfolgt man Iterationen? |

Plus quer dazu:
- **Rechte / Lizenzen:** Wem gehört was?
- **Archiv:** Wie lange aufbewahren? Wann löschen?

---

## Storage: Wo liegen die Dateien?

### Empfohlene Storage-Hierarchie

```
[BRAND-NAME]/
├── 00_Brand-Foundation/
│   ├── Visual-Identity-Manual/
│   ├── Logos/
│   ├── Schriften/
│   ├── Farbpaletten/
│   └── LUTs/
│
├── 01_Reference-Library/
│   ├── Reference-Images/
│   ├── Character-Sheets/
│   ├── Prompt-Bibliothek/
│   └── LoRA-Files/
│
├── 02_Projects/
│   ├── 2026-05_Projekt-X/
│   │   ├── 01_Briefing/
│   │   ├── 02_Pre-Production/
│   │   ├── 03_Raw-Assets/
│   │   ├── 04_Edits/
│   │   ├── 05_Exports/
│   │   └── 06_Final/
│   ├── 2026-06_Projekt-Y/
│   │   └── ...
│   └── 2026-07_Projekt-Z/
│       └── ...
│
├── 03_Music-and-SFX-Library/
│   ├── Music-tracks/
│   ├── SFX/
│   └── Voice-Overs/
│
├── 04_Templates/
│   ├── Edit-Templates/
│   ├── Storyboard-Templates/
│   └── Briefing-Templates/
│
└── 05_Archive/
    └── (abgeschlossene Projekte > 12 Monate)
```

### Tool-Empfehlungen für Storage

| Use Case | Tool | Pricing |
|---|---|---|
| **Team-Drive (Standard)** | Google Drive / Dropbox / OneDrive | $10–20/User/mo |
| **Großvolumen-Video** | Frame.io (Adobe) | $15+/mo |
| **Versionierung** | Frame.io + Git LFS für Code-Assets | Frame.io / GitHub LFS |
| **Lokales NAS (große Teams)** | Synology / QNAP | Einmalig $500+ |
| **Brand-Asset-Management Profi** | Bynder / Brandfolder / Frontify | $200+/mo |

**Empfehlung für 2–5-Personen-Teams:** Google Drive mit klarer Ordnerstruktur (oder Dropbox). Frame.io wenn Video-Review-Workflows kritisch sind.

---

## Naming: Wie sind sie benannt?

Konsistente Naming-Conventions sind das wichtigste Asset-Management-Tool. Ohne sie wird Suche und Wiederfindung in 12 Monaten unmöglich.

### Naming-Schema

```
[Datum]_[Brand]_[Projekt]_[Asset-Typ]_[Beschreibung]_[Version].[ext]

Beispiele:
2026-05-29_BrandX_KampagneA_Reel_Aylin-Cut3_v04.mp4
2026-05-29_BrandX_KampagneA_KI-Image_Cover-Hero_v02.png
2026-05-29_BrandX_KampagneA_LoRA_Aylin-Character_v01.safetensors
```

### Naming-Regeln

| Regel | Warum |
|---|---|
| **Datum vor Asset-Name** | Sortierung automatisch chronologisch |
| **Format YYYY-MM-DD** | Funktioniert in jeder Sortierung |
| **Keine Leerzeichen** | Underscore statt Leerzeichen — vermeidet Probleme bei Skripten/URLs |
| **Keine Sonderzeichen** | Keine ö, ä, ü, é etc. — manche Systeme stolpern |
| **Lower-Camel oder kebab-case** | Konsistent halten |
| **Version-Nummer am Ende** | v01, v02, v03 — niemals „final", „FINAL", „FINAL-FINAL" |

### Anti-Patterns

| Fehler | Beispiel | Korrektur |
|---|---|---|
| **„Final" im Namen** | `Reel-FINAL.mp4` | Version-Nummer: `v04` |
| **Leerzeichen** | `Reel Aylin v3.mp4` | Underscore: `Reel_Aylin_v03.mp4` |
| **Inkonsistent** | Manchmal `2026-05-29`, manchmal `29.05.2026` | Immer YYYY-MM-DD |
| **Unverständlich** | `IMG_4837.jpg` | Beschreibend: `2026-05-29_Brand_Cover-Hero_v01.jpg` |
| **Versionen überschreiben** | Datei wird einfach überschrieben | Jede Iteration neue Version |

---

## Versionierung

### Iterations-Schema

Eine **Iteration** entspricht einer Veränderung, die später ggf. wieder gebraucht wird.

```
v01 — Erster Entwurf
v02 — Nach Feedback Runde 1
v03 — Nach Feedback Runde 2
v04 — Nach Approval (oft als final markiert)
```

### Approval-Versionen

Wenn ihr Kund:innen-Approval habt:

```
v04 — Approved by [Name] on [Datum]
```

Im Dateinamen oder in einem begleitenden Metadaten-File.

### Source-Files vs. Exports

```
[Project]/
├── 04_Edits/
│   ├── Project.drp                    [Source-File DaVinci]
│   ├── 2026-05-29_Reel_v01.mp4        [Export v01]
│   ├── 2026-05-29_Reel_v02.mp4        [Export v02]
│   └── 2026-05-29_Reel_v03.mp4        [Export v03]
└── 05_Exports/
    └── 2026-05-29_Reel_v03_Final/
        ├── Instagram-Reel.mp4
        ├── TikTok.mp4
        └── LinkedIn.mp4
```

Source-Files (`.drp`, `.prproj`) sind wichtig für spätere Re-Edits. **Niemals nur Exports behalten ohne Source-Files.**

---

## Metadaten

Dateien können selbst Metadaten enthalten:

### EXIF / IPTC für Bilder
- Aufnahme-Datum
- Kamera / Tool
- GPS (bei echten Aufnahmen)
- Copyright-Notiz
- Beschreibung

**Tools:** Adobe Bridge, Lightroom für Batch-Metadaten-Bearbeitung.

### XMP für Video
- Tags
- Kommentare
- Color-Space-Information

### Custom-Metadaten in DAM-Systemen
Brand-Asset-Management-Tools (Bynder, Brandfolder) erlauben benutzerdefinierte Metadaten:
- Kampagne
- Zielgruppe
- Approval-Status
- Verwendungs-Lizenz

---

## Archive: Wann was löschen?

### Empfohlene Aufbewahrungs-Hierarchie

| Asset-Typ | Aufbewahrung |
|---|---|
| **Source-Files (.drp, .prproj)** | Mindestens 3 Jahre, idealerweise unbefristet |
| **Final Exports** | Dauerhaft (für Portfolio + Wiederverwendung) |
| **Raw-Footage / Rohaufnahmen** | 2 Jahre, dann selektiv archivieren |
| **KI-Zwischen-Generierungen** | 6 Monate, dann löschen |
| **Edit-Iterationen (v01, v02)** | Bis Final-Approval, dann ältere löschen |
| **Reference-Images** | Dauerhaft (für Pattern-Wiedererkennung) |

### Archiv-Strategie

**Hot Storage (aktiv genutzt):** Schneller Zugriff, höhere Kosten — Google Drive / Dropbox.

**Cold Storage (Archiv):** Langsamer, günstiger — AWS Glacier, Backblaze B2, externe Festplatten.

Faustregel: Projekte älter als **12 Monate** ins Cold Storage. Aktive Projekte im Hot Storage.

### DSGVO-Konformität

**Wichtig:** Wenn Assets personenbezogene Daten enthalten (Fotos echter Personen, Voice-Aufnahmen):

- **Speicherort:** EU-konform (kein US-Storage ohne SCC / DPF)
- **Aufbewahrungs-Frist:** Mindestens so lange wie der Nutzungsvertrag mit der Person erlaubt
- **Recht auf Löschung:** Bei Anfrage der Person müssen Daten gelöscht werden können

Mehr in Säule 09 (Rechtliches).

---

## Rechte-Management (mit Säule 09 verzahnt)

Pro Asset solltet ihr wissen:

| Frage | Tracking |
|---|---|
| **Wer hat es erstellt?** | Metadaten oder Begleitdokument |
| **Welche Lizenz / welche Rechte?** | Lizenz-Dokumentation oder Vertrag |
| **Für welche Verwendung erlaubt?** | Lizenz-Spezifika |
| **Bis wann?** | Vertragsdauer |

**Bei KI-generierten Assets:**
- Welches Tool / Welcher Workflow?
- Welche Lizenz hatte der Generator? (Kommerzielle Nutzung erlaubt?)
- Wann gemäß EU AI Act gekennzeichnet?

---

## Asset-Tracking-Dokument

Für jedes Projekt ein einfaches Tracking-Sheet:

```markdown
# Asset-Tracker [Projekt]

## Übersicht
- Projekt-Name:
- Status: [in_progress / approved / archived]
- Erstellt: [Datum]
- Final: [Datum]

## Assets

### Asset 1: Cover-Hero
- Datei: 2026-05-29_BrandX_KampagneA_Cover-Hero_v04.png
- Tool: Midjourney V7
- Prompt: [siehe Prompt-Bibliothek]
- Lizenz: Midjourney Pro (kommerziell OK)
- Reference: 2026-05-28_Reference_v01.jpg
- Approved by: [Name] on [Datum]

### Asset 2: Reel-Cut 1
- Datei: 2026-05-29_BrandX_KampagneA_Reel_Cut1_v03.mp4
- Tool: Premiere + Veo 3.1 Background
- Source: 2026-05-29_BrandX_KampagneA_Reel-Master.prproj
- Approved by: [Name] on [Datum]

## Verwendung
- Wo veröffentlicht: [Instagram / TikTok / etc.]
- Wann: [Datum]
- Performance-Daten: [Link]
```

---

## Tools für Asset-Management

### Für 2–5-Personen-Teams (empfohlen)

| Funktion | Tool | Pricing |
|---|---|---|
| **Storage** | Google Drive / Dropbox | $10–20/User/mo |
| **Project-Tracking** | Notion / ClickUp / Asana | $8–20/User/mo |
| **Video-Review** | Frame.io | $15+/mo |
| **Photo-Library** | Adobe Lightroom CC | $10/mo (oder Adobe CC) |
| **Approval-Workflow** | Notion + Frame.io | inklusive |

**Gesamt:** ca. $50–80/mo pro Person.

### Für größere Teams / Agenturen

Brand-Asset-Management-Tools (DAM):
- **Bynder** — Mid-tier, gute Brand-Funktionen
- **Brandfolder** — Enterprise, sehr mächtig
- **Frontify** — Brand-fokussiert, integriert mit Adobe

Diese sind in der Regel ab $200+/mo und überdimensioniert für In-House-Teams.

---

## Häufige Asset-Management-Fehler

| Fehler | Konsequenz |
|---|---|
| **Keine Naming-Convention** | In 6 Monaten findet niemand mehr was |
| **Source-Files vergessen** | Re-Edit nicht mehr möglich |
| **Final-Final-FINAL-Versionen** | Niemand weiß welche aktuell |
| **DSGVO-Verstoß bei Personen-Fotos** | Bußgelder, rechtliche Konsequenzen |
| **Keine Lizenz-Dokumentation** | Verwendungs-Recht später nicht nachweisbar |
| **Cold Storage zu früh** | Aktive Wiederverwendung erschwert |
| **Cold Storage zu spät** | Hot Storage explodiert in Kosten |
| **Backup vergessen** | Datenverlust bei Hardware-Ausfall |

---

## Asset-Management-Checkliste

### Setup (einmalig)
- [ ] Storage-Hierarchie definiert
- [ ] Naming-Convention schriftlich fixiert
- [ ] Tool-Stack ausgewählt und eingerichtet
- [ ] Backup-Strategie definiert
- [ ] DSGVO-konformer Storage geprüft

### Pro Projekt
- [ ] Projektordner nach Standard-Struktur angelegt
- [ ] Asset-Tracker-Dokument erstellt
- [ ] Lizenz-Status jedes Assets dokumentiert
- [ ] Approval-Stufen klar

### Bei Abschluss eines Projekts
- [ ] Final-Exports im richtigen Ordner
- [ ] Source-Files gesichert
- [ ] Reference-Library erweitert
- [ ] Performance-Daten verlinkt

### Quartalsweise
- [ ] Hot Storage aufgeräumt
- [ ] Alte Projekte ins Cold Storage
- [ ] Backup-Integrität geprüft

### Jährlich
- [ ] Asset-Library kuratiert (was wird noch gebraucht?)
- [ ] DSGVO-Aufbewahrungs-Pflichten geprüft
- [ ] Lizenz-Verträge gegengecheckt (laufen welche aus?)
