# 02 Plattform-Matrix: KI-Sichtbarkeit im Vergleich

Reihenfolge nach KI-Relevanz. Jede Plattform mit Beleglage. Konfidenz-Labels: dokumentiert (Primär- oder offizielle Quelle), glaubwürdig (seriöse Dritte), spekulativ.

---

## Überblick

| Plattform | KI-Sichtbarkeit | Speist welche KI | Profil als Hebel |
|---|---|---|---|
| YouTube | Sehr hoch | Google AI/Gemini (Zitierung + Training), ChatGPT, Perplexity | Schwach (content-zentriert) |
| X/Twitter | Hoch, aber konzentriert auf Grok | Grok (Training + Echtzeit), Perplexity (Zitierung) | Schwach |
| Instagram | Mittel | Meta AI (Training), Google-Index seit Juli 2025 | Mittel (Such-SEO) |
| Facebook | Mittel bis niedrig | Meta AI (Training), Google-Index seit Juli 2025 | Sehr schwach |
| TikTok | Sehr niedrig | Google-Index, sonst kaum | Sehr schwach |
| LinkedIn | Hoch (Platz 2 aller Domains), Schwerpunkt B2B | ChatGPT, Perplexity, Google AI (Zitierung) | Stark (siehe linkedin-Ordner) |

---

## YouTube

YouTube ist die mit Abstand stärkste KI-Quelle unter den Social-Plattformen.

- YouTube ist die meistzitierte Domain in Google AI Overviews. BrightEdge nennt rund 29,5 % Zitieranteil (Datenzeitraum Mai 2024 bis September 2025), Ahrefs für Juni 2026 rund 20,9 %. Beide sind Anbieter-Studien, aber sie zeigen konsistent dieselbe Dominanz. **Glaubwürdig.**
- Google nutzt einen Teil der YouTube-Videos, um eigene KI-Modelle (Gemini, Veo) zu trainieren. **Dokumentiert** (CNBC, mit offizieller Google-Bestätigung).
- Für Drittanbieter-Training gibt es ein Opt-in-Setting, das standardmäßig aus ist. **Dokumentiert** (YouTube Help).
- Perplexity zitiert sichtbar Transkript-Ausschnitte. **Glaubwürdig.**

Mechanik: Transkripte und Metadaten liefern KI sauberen, zitierfähigen Text. Details in der Datei `youtube/08-kanal-seo-und-ki-sichtbarkeit.md`.

---

## X/Twitter

X hat einen Sonderweg über die plattformeigene KI Grok.

- Der Empfehlungsalgorithmus läuft über Grok. Elon Musk kündigte den Umbau im Oktober 2025 an, der Kern-Algorithmus wurde am 20. Januar 2026 quelloffen gestellt. **Dokumentiert** (TechCrunch, GitHub xai-org).
- Öffentliche X-Daten (Posts, Metadaten, öffentliche Profile) trainieren Grok, mit Echtzeit-Zugriff auf den öffentlichen Stream. Eigene Grok-Konversationen werden laut xAI standardmäßig nicht genutzt, nur per Opt-in. **Dokumentiert** (xAI Legal FAQ).
- Für andere Modelle (ChatGPT, Gemini, Claude) gibt es keine belegte X-Trainingnutzung. Perplexity zitiert X bei aktuellen Themen. **Teils spekulativ, teils glaubwürdig.**
- X blockt per robots.txt breit, lässt vor allem Google und Bing zu. **Dokumentiert.**

Konsequenz: Auf X zahlt KI-Sichtbarkeit vor allem auf Grok ein, weniger auf das übrige KI-Ökosystem.

---

## Instagram

- Die Instagram-Suche ist keyword-basiert; Name-Feld und Bio sind durchsuchbar. **Glaubwürdig** (von Adam Mosseri bestätigt, Gewichtungen nicht offengelegt).
- Seit dem 10. Juli 2025 werden öffentliche Inhalte von Profi-Accounts durch Google indexiert. **Dokumentiert** (Instagram-Ankündigung).
- Meta AI nutzt öffentliche Instagram-Inhalte (Fotos, Posts, Captions, Kommentare) zum Training. **Dokumentiert** (Meta Transparency Center).
- Keine belegte Nutzung durch ChatGPT oder Perplexity. Kurzvideo (Reels) wird laut Ahrefs selten direkt zitiert. **Glaubwürdig.**

---

## Facebook

- Öffentliche Posts von Business-/Creator-Accounts werden seit dem 10. Juli 2025 von Google indexiert. **Dokumentiert.**
- Meta AI trainiert seit Juni 2024 auf öffentlichen Facebook-Inhalten (in der EU zeitweise pausiert). **Dokumentiert** (Meta-Blog, TechCrunch).
- Externe KI-Systeme haben keinen belegten Zugang; Facebook ist login-geschützt, es gibt keine bekannten Lizenzdeals. **Dokumentiert.**
- Auffällig: Ahrefs listet Facebook für Juni 2026 relativ weit oben unter zitierten Domains (rund 11,6 %). Das dürfte an den seit Juli 2025 indexierten öffentlichen Inhalten liegen. **Glaubwürdig, mit Vorsicht zu lesen.**

Reichweite organisch läuft ohnehin über Reels und Gruppen, nicht über das Profil als Entität.

---

## TikTok

- TikTok ist in KI-Antworten fast unsichtbar. Ahrefs ordnet Kurzvideo (TikTok, Reels) als selten direkt zitiert ein. **Glaubwürdig.**
- Google indexiert TikTok-Videos seit Februar 2024. **Dokumentiert.**
- Keine belegte Einbindung in ChatGPT oder Perplexity. **Spekulativ bis unbelegt.**
- Der For-You-Algorithmus ist rein content- und engagement-getrieben, nicht profil-bewusst.

Konsequenz: KI-Sichtbarkeit ist auf TikTok derzeit kein lohnender Hebel.

---

## LinkedIn

LinkedIn ist im Detail im eigenen Ordner behandelt (`linkedin/01-algorithmus.md` und `linkedin/08-profil-optimierung.md`).

- LinkedIn belegt **Platz 2** aller zitierten Domains in KI-Antworten, mit rund **11 %** Zitieranteil im Schnitt, vor Wikipedia, YouTube und allen großen News-Publishern. Grundlage: Semrush-Studie vom 10. März 2026, 325.000 Prompts über ChatGPT Search, Google AI Mode und Perplexity im Zeitraum Januar bis Februar 2026, daraus 89.000 zitierte LinkedIn-URLs, ausgewertet in Zusammenarbeit mit LinkedIn. **Glaubwürdig** (Anbieter-Studie).
- Aufschlüsselung je Modell: **ChatGPT Search 14,3 %, Google AI Mode 13,5 %, Perplexity 5,3 %.** Der Unterschied ist groß genug, um bei der Priorisierung zu zählen. **Glaubwürdig.**
- Die Mehrheit der ausgewerteten Prompts stammte aus Technologie, Business Services, Finanzen und Industrie. Der Effekt ist damit im **B2B- und Professional-Kontext am stärksten**. Ein eigenes B2B-Ranking weist die Studie **nicht** aus. Die verbreitete Aussage "LinkedIn ist im B2B Platz 1" geht über die Quelle hinaus. **Glaubwürdig** für den Schwerpunkt, **spekulativ** für Platz 1.
- **Semantische Ähnlichkeit 0,57 bis 0,60** zwischen KI-Antwort und zitiertem LinkedIn-Inhalt, höher als Reddit (0,53 bis 0,54) und Quora (0,435). KI-Systeme paraphrasieren LinkedIn also weniger stark, die eigene Formulierung landet fast wörtlich in der Antwort. **Glaubwürdig.**
- Urheber je Modell: Perplexity zitiert zu 59 % **Company Pages**, ChatGPT Search und Google AI Mode zu je 59 % **Einzelpersonen**. Wer beide Systeme bedienen will, braucht beides. **Glaubwürdig.**
- Anders als die übrigen Plattformen ist hier das Profil selbst ranking- und zitierrelevant, weil LinkedIn personensuche-zentriert ist.

### Wichtige Abgrenzung: Zitierung, nicht Training

Belegt ist ausschließlich **Zitierung zur Laufzeit** über öffentlich sichtbare Inhalte. Für **Training** durch externe Modelle gibt es keinen Beleg, und LinkedIn ist weitgehend login-geschützt und blockt generische Crawler. Die Formulierung "LinkedIn trainiert die LLMs" ist verbreitet, aber nicht gedeckt. Grundlagen dazu in `01_Grundlagen.md`.

### Praktischer Hebel

Was im Semrush-Datensatz zitiert wurde, ist ungewöhnlich klar messbar:

| Faktor | Befund |
|---|---|
| Format | Artikel 50 bis 66 % der Zitate, Feed-Posts 15 bis 28 % |
| Länge | Artikel 500 bis 2.000 Wörter, Posts 50 bis 299 Wörter |
| Originalität | rund 95 % Originale, Reshares nur 5 % |
| Intention | 54 bis 64 % vermitteln Wissen oder Rat |
| Frequenz der Autor:innen | rund 75 % posten über 5 Mal in vier Wochen |
| Followerzahl | knapp die Hälfte über 2.000. Unter 500 Follower werden mindestens genauso häufig zitiert wie über 500 |
| Engagement | Median 15 bis 25 Reaktionen, höchstens 1 Kommentar |

Konsequenz: **Frequenz und Substanz schlagen Reichweite und Followerzahl.** Zitierung ist kein Beliebtheitswettbewerb. Ausführlich in `Primaerquellen_Vortraege/03_Anwendungsregeln.md`, Regeln R3 und R4.

Siehe auch: `Primaerquellen_Vortraege/01_OMR26_Behrens_LinkedIn.md`, Abschnitt C. Britta Behrens bezeichnet diesen Punkt in ihrer OMR-Keynote 2026 als wichtigste Kernbotschaft.

---

## Kontext: KI-Assistenten-Markt (State of AI 2026)

Kontextdatenpunkt, keine plattform-spezifische Aussage. Er ordnet ein, welche KI-Systeme Sichtbarkeit überhaupt lohnend machen.

- Die Nutzung generativer KI-Apps hat sich binnen zwölf Monaten mehr als verdoppelt: rund 36 Milliarden Stunden im ersten Halbjahr 2026 gegenüber 17 Milliarden im Vorjahreszeitraum. **Glaubwürdig** (Anbieter-Studie).
- ChatGPT bleibt Marktführer (über 1 Milliarde monatlich aktive Nutzer, rund 215 Minuten pro Nutzer und Monat), fiel im März 2026 aber erstmals unter 50 Prozent plattformübergreifenden Reichweitenanteil (True Audience). Gemini und Claude wachsen am schnellsten, Claude-Reichweite plus 452 Prozent im Jahresvergleich.
- ChatGPT, Gemini und DeepSeek vereinen zusammen fast 90 Prozent der Nutzungszeit (Q1 2026). Die Nutzung ist stark konzentriert, aber nicht mehr Winner-takes-all: viele Menschen wählen je Aufgabe (ChatGPT allgemein, Claude für Research und Coding, Gemini im Google-Ökosystem).
- KI wird zum Discovery Layer: KI-getriebener Traffic auf Shopping-Websites steigt in allen großen Kategorien. Wer in den Antworten der Systeme nicht auftaucht, verliert Aufmerksamkeit, bevor SEO, Paid oder Social greifen.

Konsequenz für die KI-Sichtbarkeit: Aufwand auf die reichweitenstärksten Assistenten konzentrieren (ChatGPT, Gemini, Claude, dazu Perplexity als Zitier-Engine), statt ihn auf Randsysteme zu verteilen.

Quelle: Sensor Tower, State of AI 2026, via onlinemarketing.de vom 22. Juni 2026 (https://onlinemarketing.de/cases/state-of-ai-studie-2026-sensor-tower).
