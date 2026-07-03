# Säule 7: Präzise Pixel-Safe-Zones für Bewegtbild

**Stand:** Juli 2026

Diese Säule ergänzt `03_Plattform-Masse_und_Safe-Zones.md` um konkrete Pixel-Werte für vertikales Bewegtbild. Wo Säule 3 die Mechanik prosaisch beschreibt, liefert diese Datei die Zahlen, die direkt in ein Overlay oder eine Vorlage übernommen werden können. Alle Werte beziehen sich auf die Standard-Canvas **1080 x 1920 px (9:16)**. Die Angaben sind der Rand, den du vom jeweiligen Bildrand **freihalten** solltest.

## Grundregel

> Produziere jedes vertikale Format in 1080 x 1920. Motiv, Text, Logo und Call-to-Action gehören in die zentrale Safe Zone. Die Ränder gehören der Plattform-UI.

## TikTok

Schwerste UI, das größte Risiko liegt rechts und unten.

| Rand | Freihalten | UI dort |
|---|---|---|
| Oben | 130 px | „Für dich" / „Folge ich"-Tabs, Suche |
| Unten | 484 px | Caption, Sound, Account-Name, CTA-Button |
| Links | 44 px | Edge-Cropping auf schmalen Geräten |
| Rechts | 140 px | Profilbild, Like, Kommentar, Teilen, Speichern |

**Zentrale Safe Zone:** rund 896 x 1306 px. Berührt Text oder ein Gesicht das rechte Drittel, ist es gefährdet.

## Instagram Reels und Stories

| Rand | Freihalten | UI dort |
|---|---|---|
| Oben | 220 px | Account-Name, Follow-Button |
| Unten | 420 px | Caption, Like/Kommentar/Share, Audio-Attribution |
| Links | 60 px | Rand und Caption-Bereich |
| Rechts | 120 px | Action-Button-Stack |

**Zentrale Safe Zone:** rund 900 x 1280 px. Reels und Stories teilen sich die UI-Logik. Untertitel höher setzen, weil unten die Caption aufklappt.

## YouTube Shorts

| Rand | Freihalten | UI dort |
|---|---|---|
| Oben | 288 px | Such- und Menü-Icons |
| Unten | 672 px | Kanal-Info, Titel, Sound |
| Links | 48 px | Rand |
| Rechts | 192 px | Action-Buttons |

**Zentrale Safe Zone:** rund 840 x 960 px. Der untere Rand wächst bei Dynamic Island oder aufgeklappter Beschreibung. Kritische Elemente mindestens 100 px über der unteren Linie halten.

## Master-Zone für Cross-Posting

Wer ein Video ohne Anpassung auf TikTok, Reels und Shorts ausspielt, plant für den engsten gemeinsamen Crop. TikTok ist unten und rechts der Engpass, Shorts oben.

| Rand | Freihalten |
|---|---|
| Oben | 290 px |
| Unten | 500 px |
| Links | 60 px |
| Rechts | 200 px |

**Sichere Kernfläche:** rund 820 x 1130 px, mittig bis leicht nach oben ausgerichtet.

## Bezugswerte Bild-Formate

Ergänzend die wichtigsten Standbild-Maße, damit diese Datei allein für die Produktion ausreicht. Details und Quellen in Säule 3.

| Plattform und Platz | Maße (px) | Verhältnis |
|---|---|---|
| Instagram Feed (Grid-sicher) | 1080 x 1440 | 3:4 |
| Instagram Feed (hoch) | 1080 x 1350 | 4:5 |
| Feed quadratisch (universell) | 1080 x 1080 | 1:1 |
| Story / Reel / TikTok / Short | 1080 x 1920 | 9:16 |
| Link-Vorschau (OG, FB, LinkedIn) | 1200 x 630 | 1.91:1 |
| YouTube Thumbnail | 1280 x 720 | 16:9 |
| Pinterest Pin | 1000 x 1500 | 2:3 |

## Umsetzung

Vor dem Export mit einem Safe-Zone-Overlay gegenprüfen. Für After Effects existiert ein Overlay- und Skript-Kit, das diese Zonen als gesperrten Guide-Layer in die aktive Comp legt und automatisch auf die Comp-Größe skaliert. Bandbreiten und Endgeräte beachten: Notch und Dynamic Island verschieben die untere Grenze, im Zweifel den größeren Wert wählen.

Werte veralten schneller als der Rest dieser Guideline. Bei Unsicherheit gegen die Quellen in `06_Quellen.md` prüfen.
