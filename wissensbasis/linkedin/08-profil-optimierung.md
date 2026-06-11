# LinkedIn Profil-Optimierung: IST-Zustand Juni 2026

Das persönliche Profil ist 2026 nicht mehr nur eine digitale Visitenkarte. Mit der Umstellung von Suche und Feed auf LLM-basiertes Ranking entscheidet das Profil mit darüber, bei welchen Suchanfragen ein Mensch als relevant eingestuft wird, und es wird zunehmend auch außerhalb von LinkedIn von KI-Systemen gelesen. Dieses Dokument fasst zusammen, was belegt ist, was plausible Interpretation ist und was kursierende Halbwahrheiten sind.

---

## Das zweistufige LLM-Ranking (Suche & People Search)

LinkedIn betreibt sein Such- und Empfehlungssystem nach einer zweistufigen Architektur. Das ist durch LinkedIns eigene Forschungspublikationen dokumentiert, nicht nur Marketing-Behauptung.

| Stufe | Funktion |
|---|---|
| 1. Retrieval | Ein embedding-basierter Retriever erzeugt aus Hunderten Millionen Profilen und Inhalten eine Kandidatenmenge |
| 2. Reranking | Ein kompaktes Small Language Model (SLM) bewertet die Top-Kandidaten neu und optimiert gemeinsam auf Relevanz und Engagement |

Wichtig für die Profil-Praxis:

- Das **Mitgliedsprofil wird zusammengefasst und als Kontext bzw. Embedding** in das Ranking eingespeist. Es ist damit faktisch der Ankerpunkt, von dem aus Relevanz berechnet wird.
- Belegt ist das vor allem für **AI Job Search und AI People Search** sowie für das Feed-Retrieval. Die Verallgemeinerung „so wird man überall kategorisiert" ist eine zulässige Richtung, aber keine wörtliche Aussage der Quellen.
- Konsequenz: Ein Profil, das sich nicht klar einordnen lässt („Ich helfe Unternehmen, erfolgreicher zu werden"), liefert dem Modell keine trennscharfen Signale und landet in keiner klaren Kategorie.

---

## KI-Systeme lesen das Profil mit

Profile wirken über LinkedIn hinaus. Wie in `01-algorithmus.md` dokumentiert, belegt LinkedIn Platz 2 bei AI-Suchantworten und taucht in rund 11 % aller Antworten von ChatGPT Search, Perplexity und Google AI Mode auf.

Einordnung mit der nötigen Schärfe:

- KI-Systeme greifen auf **öffentlich sichtbare** LinkedIn-Inhalte zu, nicht auf das vollständige, eingeloggte Profil. LinkedIn ist weitgehend login-geschützt und blockt generische Crawler.
- Sowohl ganze Posts als auch einzelne Profile werden zitiert. Profile dienen KI-Systemen unter anderem zur Verifikation von Autoren und Expertise.
- Praktischer Selbsttest: den eigenen Namen in ChatGPT oder Perplexity eingeben und prüfen, welche Expertise zugeschrieben wird und ob das mit der gewünschten Positionierung übereinstimmt.

---

## Die Skills-Sektion: belegter Hebel

Die Skills-Sektion ist der am besten dokumentierte Profil-Hebel.

- LinkedIn extrahiert Skills **per LLM** aus dem gesamten Profilinhalt (Headline, About, Erfahrung) und speist sie in den **LinkedIn Skills Graph** ein. Dieser Graph treibt Job-Matching, Recruiter-Suche und Feed-Ranking.
- Laut LinkedIn-Daten erhalten Mitglieder mit mindestens einem gepflegten Skill **bis zu 2x mehr Profilaufrufe und Kontaktanfragen** sowie **bis zu 4x mehr Nachrichten**.
- Recruiter-Suche und Filter greifen auf Skills direkt zu. Präzise, spezifische Skills schlagen generische.

Praxis: Statt „Marketing" lieber „B2B-Sichtbarkeit für Mittelstandsunternehmen mit 100 bis 500 Mitarbeitern". Das klingt enger, trifft aber genau die Zielgruppe und liefert dem Ranking-System ein klares Signal.

---

## Die Featured-Sektion: Showcase, kein Such-Signal

Häufige Fehlannahme: Die Featured-Sektion beeinflusse Suche oder KI-Kategorisierung. Das ist so nicht gedeckt.

- LinkedIns eigene Hilfe stellt klar: Inhalte der Featured-Sektion sind **nicht über Suchmaschinen auffindbar** („not discoverable through search engines").
- Es gibt **keinen Beleg**, dass die Featured-Sektion in die LLM-Kategorisierung einfließt.
- Funktion der Sektion: kuratiertes Schaufenster für Arbeitsproben, das Profilbesucher überzeugt. Sie wirkt auf Menschen, nicht auf den Such-Index.

Fazit: Featured pflegen, ja, aber als Conversion- und Vertrauenselement für Besucher, nicht als Ranking-Hebel.

---

## Begriffsklärung: „Grounding Page"

Der Begriff „Grounding Page" kursiert in LinkedIn-Beiträgen als angebliche neue LinkedIn-Bewertung des Profils. Das ist terminologisch falsch.

- „Grounding Page" ist **kein LinkedIn-Begriff**. Es ist ein eigener Standard des SEO-Experten Hanns Kronenberg (groundingpage.com, aktuell v1.6).
- Gemeint ist damit etwas anderes: eine **dedizierte, faktenbasierte HTML-Seite auf der eigenen Website** mit maschinenlesbaren Daten, die KI-Systemen eine zitierbare Wahrheitsquelle über eine Entität liefert.
- Das zugrunde liegende Konzept „Grounding" (KI-Antworten in Quelldaten verankern) ist real und sinnvoll. Der Etikettenname „Grounding Page" auf ein LinkedIn-Profil zu kleben, vermischt jedoch zwei verschiedene Dinge.

Merke: Wer von „dein LinkedIn-Profil ist jetzt eine Grounding Page" spricht, nutzt einen fremden Marketing-Begriff, keine offizielle LinkedIn-Funktion.

---

## Konkrete Handlungsempfehlungen

| Element | Empfehlung |
|---|---|
| Headline & About | Konkrete Positionierung statt Floskeln. Branche, Zielgruppe und Leistung benennen |
| Skills | Spezifische, präzise Skills pflegen. Generische Begriffe vermeiden |
| Featured | Als Vertrauens-Schaufenster für Besucher pflegen, nicht als Ranking-Hoffnung |
| Selbsttest | Eigenen Namen regelmäßig in ChatGPT/Perplexity eingeben und zugeschriebene Expertise prüfen |
| Konsistenz | Profil und Posting-Themen aufeinander abstimmen, damit das Modell eine klare Kategorie erkennt |

---

## Quick-Check: Was stimmt, was nicht

| Aussage | Status |
|---|---|
| LinkedIn nutzt ein zweistufiges LLM-Ranking | Belegt (LinkedIn-Forschung) |
| Das Profil ist Ankerpunkt für Relevanz | Im Kern belegt, Verallgemeinerung ist Interpretation |
| ChatGPT/Perplexity nutzen LinkedIn als Quelle | Belegt, aber nur öffentliche Inhalte |
| Skills beeinflussen Auffindbarkeit & Kategorisierung | Belegt (Skills Graph, LLM-Extraktion) |
| Featured-Sektion treibt Such-/LLM-Kategorisierung | Nicht belegt, teils widerlegt |
| „Grounding Page" ist eine LinkedIn-Profilbewertung | Falsch (fremder Standard, andere Bedeutung) |

---

## Quellen & Einordnung

Belegte Fakten:

- Semantic Search At LinkedIn, arXiv 2602.07309 (Februar 2026): zweistufige Architektur aus embedding-basiertem Retrieval und SLM-Reranking; Profil als Kontext im Ranking.
  https://arxiv.org/abs/2602.07309
- Large Scale Retrieval for the LinkedIn Feed using Causal Language Models, arXiv 2510.14223 (Oktober 2025): LLaMA-3-Dual-Encoder für Mitglieds- und Content-Embeddings.
  https://arxiv.org/html/2510.14223v1
- Introducing Semantic Capability in LinkedIn's Content Search Engine, arXiv 2412.20366 (Dezember 2024).
  https://arxiv.org/html/2412.20366v1
- LinkedIn Engineering, Extracting skills to fuel the Skills Graph (2023): LLM-basierte Skill-Extraktion.
  https://engineering.linkedin.com/blog/2023/extracting-skills-from-content-to-fuel-the-linkedin-skills-graph
- LinkedIn Talent Blog, Why It's Important to List Skills on Your LinkedIn Profile: Mitglieder mit mindestens einem Skill erhalten bis zu 2x mehr Profilaufrufe und Kontaktanfragen sowie bis zu 4x mehr Nachrichten.
  https://www.linkedin.com/business/talent/blog/talent-acquisition/skills-on-linkedin-profile
- LinkedIn Help, Featured Section FAQs: Featured-Inhalte sind nicht über die Suche auffindbar.
  https://www.linkedin.com/help/linkedin/answer/a552452/featured-section-on-your-profile-faqs

Begriffsklärung:

- Grounding Page Standard von Hanns Kronenberg (kein LinkedIn-Begriff).
  https://groundingpage.com/

Interner Bezug:

- AI-Zitierhäufigkeit von LinkedIn: siehe `01-algorithmus.md`, Abschnitt „LinkedIn als AI-Zitierplattform".
