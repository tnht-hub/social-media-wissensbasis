# X (Twitter) Algorithmus: IST-Zustand Mai 2026

---

## Die zwei Haupt-Feeds

| Feed | Logik | Sortierung |
|---|---|---|
| **For You** | Algorithmus-basiert; zeigt Content von Accounts denen man nicht folgt | KI-Rankings (Grok AI) |
| **Following** | Nur gefolgten Accounts | Seit Dez 2025: KI-sortiert nach Relevanz; Nutzer können auf zeitliche Sortierung zurückschalten |

Seit **Dezember 2025** wird auch der Following-Feed durch Grok AI nach vorhergesagter Relevanz und Engagement-Wahrscheinlichkeit sortiert, nicht mehr rein chronologisch. Nutzer können manuell zur zeitlichen Ansicht wechseln.

---

## Grok AI als Algorithmus-Kern

Seit **Oktober 2025** wird der Algorithmus vollständig durch **xAI's Grok** betrieben. Die KI:
- Bewertet Content-Qualität und Engagement-Wahrscheinlichkeit
- Sortiert Both Feeds dynamisch
- Erkennt Bots und inauthentic engagement (Bot Purge April 2026: 208 Bots/Minute entfernt)
- Nutzer können seit September 2025 den Feed durch direkte Grok-Anfragen anpassen ("Zeig mir mehr von X")

---

## Offengelegte Gewichte des Phoenix-Algorithmus (August 2026)

X hat im August 2026 Teile seines Feed-Algorithmus offengelegt und die positiven und negativen Signale benannt. Eine Auswertung des Quellcodes durch Business Insider ergibt folgende Punktwerte. Sie ersetzen die qualitative Einschätzung im Abschnitt darunter, wo sie ihr widersprechen.

| Aktion | Punktwert | Verhältnis zum Like |
|---|---|---|
| **Share per kopierter Post-URL** | rund 20 | rund 40 mal ein Like |
| **Reply** | rund 5 | 10 mal ein Like |
| **Quote** | rund 5 | 10 mal ein Like |
| **Share per interner DM** | rund 5 | 10 mal ein Like |
| **Follow** | rund 4 | 8 mal ein Like |
| **Repost** | rund 1 | 2 mal ein Like |
| **Like** | 0,5 | Referenzwert, eines der schwächsten Positivsignale |

**Kernaussage.** Der Phoenix-Algorithmus optimiert vorrangig auf Weiterleitung, nicht auf Likes. Aus den Punktwerten und den weiteren Faktoren (wem jemand folgt, Aktualität und weitere) bildet X pro Post und Nutzer eine Rangzahl, die über die Feed-Position entscheidet.

**Folge für die Kanalarbeit.** Zielgröße ist der geteilte Post, nicht der gelikte. Inhalte, die jemand aus eigenem Antrieb weiterschickt oder außerhalb der Plattform verlinkt, gewinnen ein Vielfaches gegenüber Inhalten, die nur Zustimmung erzeugen. Ein Like ist als Erfolgsindikator nahezu wertlos.

**Belegqualität.** Drittauswertung des offengelegten Quellcodes, kein von X veröffentlichtes Zahlenwerk. Die Punktwerte sind gerundet. Beim nächsten Pflegelauf gegen die X-Quelle auf GitHub gegenprüfen.

> **Quelle:** Business Insider, aufbereitet von SocialMediaToday am 17. August 2026: https://www.socialmediatoday.com/news/x-algorithm-insights-highlight-key-posting-strategies/828094/

---

## Transparenz und Shadowbanning (August 2026)

X hat am 13. August 2026 seine Code-Darstellung auf GitHub erweitert und zeigt dort genauer, wie die Reichweite einzelner Posts zustande kommt. Zusätzlich testet X einen vereinfachten Weg, mit dem Nutzer prüfen können, ob ein einzelner Post eingeschränkt oder shadowbanned wurde.

**Nutzen für die Praxis.** Bei unerklärlichem Reichweiteneinbruch lässt sich erstmals plattformseitig prüfen, ob eine Einschränkung vorliegt, statt auf Vermutungen auszuweichen. Das gehört in die Diagnose vor jeder Krisenreaktion.

> **Quelle:** SocialMediaToday, 13. August 2026: https://www.socialmediatoday.com/news/x-shares-new-insights-into-transparency-and-shadowbanning/827858/

---

## Ranking-Signale, qualitative Einordnung (Stand Mai 2026)

Diese Tabelle stammt aus dem Stand vor der Offenlegung im August 2026. Wo sie den Punktwerten oben widerspricht, gelten die Punktwerte. Sie bleibt hier, weil sie Signale abdeckt, die in der Offenlegung nicht mit Punktwerten belegt sind, etwa Bookmarks und Watch Time.

| Signal | Gewichtung | Details |
|---|---|---|
| **Replies** | Sehr hoch | Starkes Engagement-Signal, echte Konversation. Laut Offenlegung August 2026 rund 5 Punkte, deutlich unter dem URL-Share |
| **Retweets / Quotes** | Hoch | Redistribution und Kommentierung. Laut Offenlegung August 2026 unterscheiden sich beide stark: Quote rund 5 Punkte, reiner Repost rund 1 Punkt |
| **Bookmarks** | Hoch | Privates Speichern = echter Mehrwert |
| **Likes** | Gering | Seit Juni 2024 privat. Laut Offenlegung August 2026 nur 0,5 Punkte, damit schwächer als hier ursprünglich eingeschätzt |
| **Link Clicks** | Mittel | Click-Through auf externe Links |
| **Impressions / Views** | Gering | Nur Basis-Signal, nicht direkt gewichtet |
| **Watch Time (Video)** | Hoch für Videos | Analog zu anderen Plattformen |
| **Follows nach dem Post** | Mittel | Content überzeugt zum Folgen |

**Wichtig:** X bewertet Engagement von **Premium-Nutzern** stärker als von kostenlosen Nutzern (seit Oktober 2024).

---

## Original Content vs. Aggregator-Accounts

Seit **April/Mai 2026** stärkt X gezielt **original Content Creator** gegenüber Accounts, die primär fremde Inhalte reposten:
- Mehr algorithmische Sichtbarkeit für Original-Posts
- Ziel: Bessere Datenqualität für AI-Projekte (Grok Training)
- Aggregator-Accounts erhalten weniger Reichweite bei gleicher Engagement-Rate

---

## Custom Timelines (seit April 2026)

Nutzer können aus **75 themenbasierten Timelines** wählen, kuratierte Feeds zu den wichtigsten Diskussionsthemen der Plattform. X Premium-Vorteil, aber themenbasierte Feeds sind auch für Nicht-Premium sichtbar.

---

## Topic Snooze (global seit April 2026)

Nutzer können bestimmte Themen im "For You"-Feed vorübergehend stummschalten. Ermöglicht bessere Kontrolle über den Feed-Content, besonders nach viralen, unerwünschten News-Zyklen.

---

## Community Notes

Seit Mai 2025: **1 Million Contributor weltweit**.

Wichtige Updates:
- **Februar 2026:** Kollaborative Community Notes für englische Posts (Mehrere Nutzer arbeiten zusammen an einer Note)
- **Januar 2026:** Experimentelle KI-Contributor testen Community Note-Erstellung
- **Juli 2025:** AI Note Writers helfen Nutzern bei der Erstellung von Community Notes
- **Mai 2025:** Gleichgewichtung von Upvotes und Downvotes, reduziert Manipulationspotenzial

---

## Inauthentic Behavior & Moderation

- **April 2026:** Bot Purge, 208 Bots pro Minute entfernt (nach Angabe von X Head of Product)
- **November 2025:** VPN-Erkennung, Profile, die VPNs zur Verschleierung ihres Standorts nutzen, werden bald markiert
- **September 2024:** Blocking-Änderung, Posts von öffentlichen Accounts sind weiterhin für blockierte Nutzer sichtbar (nur DM-Versand wird geblockt)

---

## Posting-Einschränkungen für kostenlose Nutzer (Mai 2026)

Neue **Posting-Limits für Nicht-Premium-Nutzer** wurden eingeführt, um Spam und Bot-Aktivität zu reduzieren. Das Limit macht es wirtschaftlich unrentabel, die Plattform für Spam-Zwecke zu nutzen.

---

## Plattform-Kontext: Polarisierung

**Harvard-Studie April 2026:** Dokumentierter signifikanter Anstieg polarisierender und politisch kontroverser Inhalte auf X seit der Musk-Übernahme (2022). Relevant für Brand-Safety-Entscheidungen.
