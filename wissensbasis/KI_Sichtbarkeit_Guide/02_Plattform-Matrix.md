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
| LinkedIn | Mittel | ChatGPT, Perplexity, Google AI (Zitierung) | Stark (siehe linkedin-Ordner) |

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

- LinkedIn belegt Platz 2 bei AI-Suchantworten und taucht in rund 11 % der Antworten von ChatGPT Search, Perplexity und Google AI Mode auf (Stand der LinkedIn-DB). **Glaubwürdig.**
- Anders als die übrigen Plattformen ist hier das Profil selbst ranking- und zitierrelevant, weil LinkedIn personensuche-zentriert ist.
