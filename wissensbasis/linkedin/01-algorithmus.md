# LinkedIn Algorithmus: IST-Zustand Mai 2026

---

## Wie der Algorithmus funktioniert

LinkedIn hat im **März 2026** seinen Feed-Algorithmus grundlegend auf fortschrittliche KI-Systeme umgestellt. Der Algorithmus entscheidet, welche Inhalte welchen Nutzern angezeigt werden, und in welcher Reihenfolge.

### Grundprinzip

LinkedIn bewertet jeden Post in mehreren Stufen:

1. **Qualitätsfilter:** Spam, AI Slop und Engagement Bait werden frühzeitig aussortiert
2. **Initiale Verteilung:** Der Post wird einer kleinen Gruppe aus dem Netzwerk des Autors gezeigt
3. **Engagement-Auswertung:** Die Reaktionen dieser Gruppe entscheiden über weitere Reichweite
4. **Erweiterte Verteilung:** Bei starker Performance wird der Post auch an nicht-verbundene Nutzer ausgespielt ("Suggested Posts")
5. **Langfristige Reichweite:** Posts können wochen- bis monatelang im Feed erscheinen, auch ältere Beiträge können noch viral gehen

---

## Was der Algorithmus priorisiert

### Engagement-Signale (absteigend gewichtet)

| Signal | Gewichtung | Hinweis |
|---|---|---|
| Kommentare | Sehr hoch | Qualitätskommentare > kurze Kommentare |
| Reposts / Shares | Hoch | Besonders mit eigenem Kommentar |
| Saves (Speichern) | Hoch | Neu seit September 2025, stark gewichtet |
| Sends (Weiterleiten) | Hoch | Neu seit September 2025, stark gewichtet |
| Reaktionen (Likes etc.) | Mittel | Weniger gewichtet als Kommentare |
| Dwell Time | Hoch | Wie lange ein Nutzer beim Post verweilt |
| Klicks auf "Mehr anzeigen" | Mittel | Zeigt Interesse am Inhalt |

### Content-Faktoren

- **Relevanz für das Netzwerk:** Verbindungen und Follower des Autors haben Priorität
- **Thematische Konsistenz:** Wer konsequent über ein Thema posted, wird als Experte eingestuft
- **Posting-Regelmäßigkeit:** Regelmäßige Poster werden vom Algorithmus bevorzugt
- **Netzwerk-Aktivität des Autors:** Wer aktiv kommentiert und engagiert, hat mehr Reichweite
- **Früh-Engagement:** Die ersten 60 bis 90 Minuten nach Veröffentlichung sind entscheidend

---

## Was der Algorithmus bestraft

### AI Slop & Inauthentic Content (kritisch seit 2026)

LinkedIn erkennt generische KI-Inhalte mit einer Trefferquote von **94%** und reduziert deren Reichweite aktiv. Konkrete Merkmale, die LinkedIn als "AI Slop" klassifiziert:

- Typische ChatGPT-Hooks ("In einer Welt, in der...", "Ich bin überwältigt zu teilen...")
- Übermäßig glatte, strukturierte Texte ohne persönliche Stimme
- Generische Listen ohne spezifische Einblicke
- Vage Formulierungen ohne konkreten Erfahrungsbezug
- Inflationäre Verwendung von Emojis als Aufzählungszeichen

### Engagement Bait

LinkedIn geht aktiv gegen Engagement Bait vor:
- "Tag jemanden, der..." → Reichweite wird reduziert
- "Like wenn du zustimmst" → Gilt als Manipulation
- "Kommentiere X für mehr Infos" → Wird als Spam behandelt

### Automatisierte Kommentare

Kommentare, die von Automatisierungs-Tools stammen, werden in ihrer Sichtbarkeit reduziert (seit August 2025).

**Präzisierung: die drei Eskalationsstufen.** Gyanda Sachdeva, VP of Product bei LinkedIn, hat drei konkrete Maßnahmen benannt. Betroffen sind Kommentare, die über Drittanbieter-Tools, Skripte oder Browser-Plugins **ohne menschliche Kontrolle** gepostet werden:

1. Entfernung aus der Sortierung "Most relevant", also der Standardansicht direkt unter dem Post
2. Mögliche Entfernung aus dem weiteren Kommentar-Netzwerk
3. Bei wiederholtem Posten automatisierter Kommentare niedriger Qualität: **Einschränkung der LinkedIn-Nutzung**

Abgrenzung: Tools zur Unterstützung sind zulässig, Tools, die die menschliche Prüfung vollständig umgehen, nicht.

Quelle im O-Ton mit Belegstatus: `Primaerquellen_Vortraege/01_OMR26_Behrens_LinkedIn.md`, Kasten in Abschnitt B.

### Begriffsklärung: "360 Brew" ist kein LinkedIn-Algorithmus

Der Begriff kursiert international als angeblicher Name der neuen Newsfeed-Architektur. **Der Name existiert so nicht.**

- Es gibt eine neue Newsfeed-Architektur mit **Two-Stage-Ranking** (Retrieval, dann Reranking, siehe `08-profil-optimierung.md`). LinkedIn hat sie nie 360 Brew genannt.
- "360 Brew" war ein theoretisches Papier, das zurückgezogen wurde und in seiner Komplexität mit heutigen Mitteln nicht ausrollbar wäre.
- LinkedIn nennt den tatsächlichen Namen bislang nicht.

Wer den Begriff benutzt, signalisiert im Fachgespräch einen veralteten Stand. Gleiches Muster wie bei "Grounding Page" (`08-profil-optimierung.md`).

Herleitung und Beleglage: `Primaerquellen_Vortraege/01_OMR26_Behrens_LinkedIn.md`, Kasten in Abschnitt E.

### Externe Links im Post-Text

Posts mit externen Links im Fließtext erhalten deutlich **weniger organische Reichweite**. LinkedIn priorisiert natives Content. Lösung: Link in den ersten Kommentar posten.

> **Offener Widerspruch.** Britta Behrens vertritt in ihrer OMR-Keynote 2026 die
> Gegenposition: Link in den Beitrag, weil ein Link im ersten Kommentar in der
> Relevanz-Ansicht nicht sichtbar ist. Beide Positionen optimieren auf
> unterschiedliche Zielgrößen (Reichweite des Posts vs. Klick und Nutzen). Nicht
> aufgelöst, eigener Test steht aus. Details in
> `Primaerquellen_Vortraege/04_Abgleich_bestehende_Module.md`, Abschnitt C1.

### Zu niedrige Posting-Qualität

- Copy-Paste aus anderen Plattformen ohne Anpassung
- Schlechte Bildqualität
- Wasserzeichen anderer Plattformen (z.B. TikTok-Wasserzeichen auf Videos)

---

## Suggested Posts & Langzeitreichweite

Seit dem Algorithmus-Update **Februar 2024** werden Posts auch Nutzern angezeigt, die nicht mit dem Autor verbunden sind, durch das "Suggested Posts"-Feature. Inhalte können dadurch **Wochen bis Monate** nach dem Veröffentlichungsdatum noch Reichweite generieren. Das macht LinkedIn zu einer Plattform, auf der Evergreen-Content besonders stark funktioniert.

---

## LinkedIn als AI-Zitierplattform (neu 2026)

LinkedIn belegt **Platz 2** bei AI-Suchantworten: Die Plattform taucht in 11% aller Antworten von ChatGPT Search, Perplexity und Google AI Mode auf. Das bedeutet: Professionell aufbereitete LinkedIn-Inhalte werden zunehmend von KI-Systemen als Quelle herangezogen. Qualitätsinhalt auf LinkedIn hat damit eine Wirkung, die über die Plattform selbst hinausgeht.

**Präzisierung (Juli 2026, Semrush-Studie vom 10.03.2026 im Volltext gegengeprüft):**

- Platz 2 gilt über **alle** Domains, vor Wikipedia, YouTube und allen großen News-Publishern. Basis: 325.000 Prompts (Jan bis Feb 2026), daraus 89.000 zitierte LinkedIn-URLs.
- Je Modell stark unterschiedlich: **ChatGPT Search 14,3 %, Google AI Mode 13,5 %, Perplexity 5,3 %.**
- Der Effekt ist im **B2B- und Professional-Kontext am stärksten**, weil die Mehrheit der Prompts aus Technologie, Business Services, Finanzen und Industrie stammte. Ein eigenes B2B-Ranking weist die Studie nicht aus. Die kursierende Aussage "LinkedIn ist im B2B Platz 1" ist **nicht belegt**.
- Zitiert werden überwiegend Inhalte mit echtem Fachgehalt. **Hohe Engagement-Zahlen und große Followerschaft sind keine Voraussetzung**: Median 15 bis 25 Reaktionen, und Autor:innen unter 500 Followern werden mindestens genauso häufig zitiert wie solche darüber.

Wichtig: Belegt ist **Zitierung zur Laufzeit** über öffentlich sichtbare Inhalte, nicht Training. Volle Faktorenliste in `KI_Sichtbarkeit_Guide/02_Plattform-Matrix.md`, Anwendung in `Primaerquellen_Vortraege/03_Anwendungsregeln.md`, Regeln R3 und R4.

---

## Algorithmus-Unterschied: Profil vs. Unternehmensseite

| Aspekt | Persönliches Profil | Unternehmensseite |
|---|---|---|
| Organische Reichweite | Deutlich höher | Begrenzt |
| Algorithmus-Bevorzugung | Ja, Menschen über Marken | Nein |
| Engagement-Rate | Höher | Niedriger |
| Empfehlung | Hauptkanal für Content | Ergänzend / für Ads |

**Empfehlung:** Persönliche Profile von Mitarbeitenden und Führungskräften als primären Content-Kanal nutzen. Unternehmensseite für Thought Leader Ads und Sponsoring verwenden.
