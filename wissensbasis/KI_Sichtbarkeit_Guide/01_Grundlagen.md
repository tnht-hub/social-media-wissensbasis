# 01 Grundlagen: Zitierung, Training, Zugang

Drei Unterscheidungen entscheiden darüber, ob eine Aussage zur KI-Sichtbarkeit stimmt oder Unsinn ist. Wer sie kennt, durchschaut die meisten Marketing-Behauptungen zum Thema sofort.

---

## 1. Zitierung (Retrieval) ist nicht Training

Das ist die wichtigste Unterscheidung.

- **Zitierung / Retrieval:** Ein KI-System ruft zur Laufzeit aktuelle Inhalte ab und zeigt sie als Quelle in der Antwort an. Beispiele: Google AI Overviews, ChatGPT Search, Perplexity. Hier zählt, ob ein Inhalt jetzt auffindbar und zitierfähig ist.
- **Training:** Ein Inhalt fließt einmalig in die Modellgewichte ein. Das wirkt diffus, ist nicht quellengenau nachweisbar und liegt hinter einem Wissensstichtag.

Praktische Konsequenz: Für Sichtbarkeit heute ist Zitierung der relevante Hebel, nicht Training. Wer sagt „ChatGPT wurde auf meinem Post trainiert", meint meist etwas Unprüfbares. Wer sagt „Perplexity zitiert meinen Post", meint etwas Beobachtbares.

---

## 2. Login-geschützt ist nicht öffentlich-indexierbar

KI-Systeme und Suchmaschinen erreichen nur, was öffentlich zugänglich ist.

- **Login-Wall:** Inhalte hinter Anmeldung (große Teile von LinkedIn, Instagram, Facebook) sind für externe Crawler grundsätzlich nicht erreichbar.
- **Öffentlich-indexierbar:** Seit dem 10. Juli 2025 lassen Meta-Plattformen öffentliche Inhalte von Profi-/Business-Accounts durch Google und andere Suchmaschinen indexieren. Das ist die Voraussetzung dafür, dass solche Inhalte überhaupt in KI-Antworten auftauchen können.

Konsequenz: „KI liest mein Profil aus" gilt immer nur für den öffentlichen, indexierbaren Teil, nicht für das vollständige eingeloggte Profil.

---

## 3. robots.txt und Crawler-Politik

Ob ein KI-Crawler zugreifen darf, regelt unter anderem die robots.txt der Plattform.

- Die etablierten KI-Crawler (GPTBot von OpenAI, PerplexityBot, ClaudeBot) geben an, robots.txt zu respektieren. Es gibt dokumentierte Ausnahmen und Vorwürfe, etwa gegen Perplexity wegen verdeckter Crawler.
- Plattformen blocken unterschiedlich stark. X blockt per robots.txt breit und lässt vor allem Google und Bing zu. ByteDance/TikToks Crawler (Bytespider) gilt als aggressiv und nicht zuverlässig regelkonform.
- Eigene KI der Plattform ist ein Sonderfall: Meta AI nutzt Meta-Daten direkt, Grok nutzt X-Daten direkt. Das umgeht die Crawler-Frage komplett, weil es kein externer Zugriff ist.

---

## Merksatz

Bevor man eine Sichtbarkeits-Behauptung glaubt, drei Fragen stellen: Geht es um Zitierung oder Training? Ist der Inhalt öffentlich oder login-geschützt? Und darf der jeweilige Crawler überhaupt zugreifen? Erst diese drei Filter trennen belegbare Aussagen von Marketing-Geräusch.
