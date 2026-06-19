# Prompt-Vorlage: Design-Output (Carousel, Story, Deck, Poster)

Diese Vorlage zerlegt einen funktionierenden Design-Prompt in austauschbare Bausteine. Jeder Block erfüllt eine feste Funktion und lässt sich für jede neue Design-Idee neu befüllen. Ziel ist ein wiederholbares Briefing, das Struktur, Stil und Inhalt sauber voneinander trennt.

---

## Die Vorlage

```
create [FORMAT/SEITENVERHÄLTNIS] [DELIVERABLE] on [THEMA].
[KOMPLEXITÄTS-VORGABE].
pay high attention to design, use [MARKE/FARBSYSTEM].

STYLE: use the attached images as style guides
(dont inherit their theme, only the design is what i was looking at)
+ prompted style: [STIL-BESCHREIBUNG: Gestaltungsmittel,
visuelle Elemente, Format-Kontext]

color palette: [QUELLE]: [FARBNAME #HEX], [FARBNAME #HEX],
[FARBNAME #HEX] als Anker.

[INHALTSPLAN: nummerierte Liste der einzelnen Slides/Seiten/Elemente]
```

---

## Was jeder Baustein leistet

| Baustein | Funktion | Beispielwerte |
|---|---|---|
| **Format/Deliverable** | Legt Container und Maße fest | 4:5 Carousel, 9:16 Story, 16:9 Deck, A4 Poster |
| **Thema** | Der konkrete Inhalt, fachliche Spezifik | „how to create carousels", „3 Trends 2026" |
| **Komplexitäts-Vorgabe** | Steuert Dichte und Textmenge | „as simple as possible", „max 5 words per slide" |
| **Marke/Farbsystem** | Verweist auf ein bestehendes System | Claude-Farben, B&B Corporate Design, Kundenmarke |
| **Style-Referenzen** | Übernimmt die Machart der Bilder, nicht Inhalt oder Stimmung | angehängte Screenshots, Pinterest-Boards |
| **Prompted Style** | Textliche Stilbeschreibung als Ergänzung zu den Bildern | Typografie, 3D-Mockups, Badges, Diagramme |
| **Color Palette** | Explizite Hex-Werte plus Rolle | primary, anchor, accent |
| **Inhaltsplan** | Slide-für-Slide-Gliederung, trennt Struktur von Gestaltung | nummerierte Liste |

### Der entscheidende Trick

Die Trennung von **Design** und **Theme** bei den Style-Referenzen. Die Anweisung lautet, die Machart der Bilder zu übernehmen, nicht deren inhaltliche Aussage oder Stimmung. So lassen sich beliebige Referenzen nutzen, ohne deren Markenwelt zu kopieren.

---

## Ausgefülltes Original (Claude-Carousel)

```
create 4:5 carousel on how to create carousels in claude design.
make it as simple and with as little as possible.
pay high attention to design, use claude colors.

STYLE: use the attached images as style guides
(dont inherit their theme, only the design)
+ prompted style: editorial/informational design slides mixing
bold typography, floating 3d ui mockups, gradient showcases,
pinboard sticky notes, pill badges, and clean infographic diagrams,
all in a social media optimized vertical format.

color palette: claudes brand: warm cream #FAF6F0, coral primary
#D85A30, peach #F0997B, dark #2C2C2A als Anker.

Carousel plan:
1. how to use claude for carousels + showcase (cover)
2. what is claude design and where to use it
3. create moodboard that matches your project
4. creating the carousel with claude design
5. adjust and edit the carousel in the claude design ui
```

---

## Übertragung auf eine andere Idee

```
create 9:16 story series on the 3 biggest social media trends 2026.
keep it bold, max one statement per frame.
pay high attention to design, use B&B corporate design.

STYLE: use the attached images as style guides
(dont inherit their theme, only the design)
+ prompted style: dark editorial frames mixing oversized numerals,
glassmorphism cards, neon accent lines, minimal data charts,
optimized for vertical mobile viewing.

color palette: B&B brand: dark #1A1A18, orange #FF6008,
off-white #F5F2EC als Anker.

Story plan:
1. hook frame with trend count
2. trend 1 with stat
3. trend 2 with stat
4. trend 3 with stat
5. CTA frame
```

---

## Checkliste vor dem Absenden

1. Format und Maße benannt
2. Thema fachlich konkret, nicht generisch
3. Komplexität gesteuert (wie viel Text, wie dicht)
4. Marke oder Farbsystem referenziert
5. Style-Referenzen mit Trennung Design statt Theme
6. Farben als Hex mit Rolle
7. Inhaltsplan Slide für Slide
