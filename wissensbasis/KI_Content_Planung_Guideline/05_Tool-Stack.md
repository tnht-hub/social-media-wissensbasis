# Säule 5 — Tool-Stack-Empfehlung

Auf Basis der Recherche (Zapier, Buffer, Piktochart, HubSpot) — minimal-viables Setup ohne Tool-Inflation.

---

## Kern-Stack (Empfehlung)

| Funktion | Tool-Optionen | Kosten/Monat | Warum |
|---|---|---|---|
| **Brainstorming + Captions** | Claude Pro / ChatGPT Plus / Gemini Advanced | ~20 € | Hauptarbeitspferd. Claude besser für Nuance, GPT besser für Bulk, Gemini stark in Google-Workspace-Integration. |
| **Content-Schedule** | Buffer / Later / Metricool | 15–25 € | CSV-Import aus KI-Output, Multi-Plattform |
| **Video-Repurposing** | Opus Clip / Submagic | 20 € | Lange Videos zu Shorts/Reels/TikToks |
| **Design / Visual-Templates** | Canva Pro / Figma | 13 € | Schnelle visuelle Varianten, CI-Templates |
| **Persistente Wissensbasis** | Notion + Notion AI / Obsidian | 10 € | Brand-Brief, Performance-Daten, Prompt-Bibliothek |

**Gesamt: ca. 80–100 € pro Monat** für ein voll funktionsfähiges Setup. Skalierbar für Team-Erweiterung.

---

## Detail-Empfehlungen pro Funktion

### Brainstorming + Captions

| Tool | Stärken | Schwächen |
|---|---|---|
| **Claude (Anthropic)** | Bessere Sprachnuance, weniger generischer Output. Projekte halten Kontext zwischen Sessions. Lange Outputs ohne Qualitätsverlust. | Kleinere Plug-in-Welt als ChatGPT |
| **ChatGPT (OpenAI)** | Schneller für Bulk-Output. Custom GPTs für teamweite Standardisierung. Größere Plug-in-Welt. | Output etwas generischer in der Voreinstellung |
| **Gemini (Google)** | Stark integriert in Google Workspace. Echtzeit-Internet-Suche. Gut für Faktenchecks. | Stilistisch oft glatter, weniger Voice-Variation |

**Pragmatischer Ansatz:** Ein Tool als Haupt-Werkzeug + ein Zweittool für spezifische Stärken (z.B. Claude für Strategie, ChatGPT für Bulk-Varianten).

### Content-Schedule

| Tool | Beste für |
|---|---|
| **Buffer** | Kleinere bis mittlere Teams. CSV-Import sauber. Approval-Workflow eingebaut. |
| **Later** | Visuelle Plattformen (IG, Pinterest, TikTok). Bessere Vorschau-Funktion. |
| **Metricool** | Reporting-fokus. Gut für Agenturen mit Performance-Reports. |

**Nicht empfohlen für kleine Setups:** Hootsuite — überdimensioniert, hohe Lernkurve, viele Features die ihr nicht braucht.

### Video-Repurposing

| Tool | Beste für |
|---|---|
| **Opus Clip** | Lange Talking-Heads / Interviews zu Shorts. KI wählt beste Momente. |
| **Submagic** | Auto-Captions, Highlight-Effekte für TikTok/Reels. |
| **Repurpose.io** | Cross-Posting + Text-zu-Video. Mehr Automation. |

**Bei eigener Produktion:** Manuelle Schnitte in CapCut, Premiere oder DaVinci reichen für die Anfangsphase. Spezialtools erst bei regelmäßiger längerer Produktion.

### Design / Visual-Templates

| Tool | Beste für |
|---|---|
| **Canva Pro** | Schnelle Carousels, Brand Kit, Magic Design für Varianten. |
| **Figma** | Custom-Templates, Design-System-Konsistenz, Team-Collaboration. |
| **Adobe Express** | Wenn ihr eh Adobe-Stack nutzt. |

### Persistente Wissensbasis

| Tool | Beste für |
|---|---|
| **Notion + Notion AI** | Brand-Brief, Performance-Daten, Prompt-Bibliothek, Versionierung. Team-Collaboration. |
| **Obsidian** | Lokal-first, datenschutz-sensibel, Markdown-nativ. Eher Solo. |
| **Confluence** | Wenn ihr eh Atlassian-Stack nutzt. Enterprise-Setup. |

---

## Bewusst NICHT empfohlen

| Tool-Kategorie | Warum nicht |
|---|---|
| **Hootsuite (für kleine Setups)** | Überdimensioniert. Hohe Lernkurve. Viele Features nicht genutzt. |
| **Jasper / Copy.ai** | Überschneidet zu sehr mit ChatGPT/Claude — zusätzliche Kosten ohne Mehrwert |
| **Vollautomatisierungs-Tools** (z.B. auto-post.io) | Risiko bei regulierten Branchen / sensiblen Themen |
| **AI-Influencer-Tools** (z.B. HeyGen Avatar) | Zielgruppen erkennen AI-Avatare → Authentizitäts-Verlust |
| **Tools mit Lock-in-Risiko** | Wenn Brand-Brief / Content-Pläne nicht als Standard-Format (.md, .csv) exportierbar sind |

---

## Skalierungs-Stufen

### Stufe 1 — Startphase (Monat 1–3)
Nur Kern-Stack. Manuell schedulen. Performance-Daten manuell sammeln.

### Stufe 2 — Etablierungsphase (Monat 4–12)
+ Zapier / Make für einfache Automations (z.B. „neue Post-Idee in Notion → Slack-Notification an Team")
+ Eigene Prompt-Bibliothek in der Wissensbasis strukturieren

### Stufe 3 — Skalierungsphase (Jahr 2+)
+ Custom GPT / Claude-Projekt für teamweite Standardisierung
+ Performance-Dashboard (Google Looker Studio kostenlos)
+ Wenn Video-Produktion stark steigt: Pro-Editing-Suite (Premiere, DaVinci)

### Stufe 4 — Vollautomatisierung (Jahr 3+)
Nur falls nötig. Make / n8n für Multi-Tool-Workflows. Aber: **Human-in-the-Loop bleibt Pflicht** — besonders bei sensiblen Branchen.

---

## Kosten-Vergleich nach Use-Case

### Solo-Creator (1 Person, 2 Plattformen)
- Claude Pro 20 € + Buffer Essentials 15 € + Canva Pro 13 € = **48 € / Monat**

### Kleines Marketing-Team (3–5 Personen, 3–4 Plattformen)
- Claude Pro / ChatGPT Plus + Buffer + Canva + Notion AI = **80–100 € / Monat** (+ Team-Lizenzen)

### Agentur mit mehreren Kund:innen
- ChatGPT Team / Claude Enterprise + Buffer / Later + Canva for Teams + Notion Business + Opus Clip = **300–600 € / Monat** je nach Größe

### Großunternehmen / Konzern
- Eigene KI-Infrastruktur (z.B. Azure OpenAI, AWS Bedrock) + Sprinklr / Hootsuite Enterprise + Adobe Stack + spezifische Compliance-Tools = **5.000+ € / Monat**

---

## Zukunfts-Vorbehalt

Das Tool-Ökosystem 2026 wird in 3–5 Jahren komplett anders aussehen. Die Empfehlungen oben sind Stand Mai 2026. **Jährlicher Tool-Audit** sollte fester Bestandteil der Content-Steuerung sein — nicht öfter, sonst wird Setup-Zeit zur Kostenfalle.

**Was wahrscheinlich gleich bleibt:**
- LLM als Brainstorming-Tool
- Schedule-Tool für Multi-Plattform
- Persistente Wissensbasis

**Was sich wahrscheinlich ändert:**
- Konkrete Anbieter und Marktführer
- Preise (eher steigend, mit AI-Premium-Aufschlägen)
- Integration mit Plattform-APIs (Meta, ByteDance Restriktionen werden enger)
- Compliance-Anforderungen (EU AI Act, branchenspezifische Vorgaben)
- Verschmelzung von Schedule + AI in einem Tool

---

## Tool-Auswahl-Kriterien

Wenn ihr einen Tool-Wechsel überlegt, prüft:

1. **Export-Fähigkeit:** Kann ich meine Daten als Standard-Format (.md, .csv, .json) rausziehen?
2. **API-Verfügbarkeit:** Lässt sich das Tool in mein bestehendes Setup integrieren?
3. **Team-Skalierung:** Funktioniert die Lizenz-Logik, wenn das Team wächst?
4. **Datenschutz:** Wo werden die Daten gespeichert? DSGVO-konform?
5. **Lebenszyklus-Stabilität:** Wie alt ist das Tool? Wer steht dahinter? Risiko, dass es in 18 Monaten eingestellt wird?

Punkte 1 und 5 werden oft unterschätzt — und sind die teuersten Wechsel-Kosten, wenn sie schiefgehen.
