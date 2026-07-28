# 05 Failure-Modi

**Stand:** Juli 2026

Typische Fehlinterpretationen **genau dieser beiden Quellen**. Nicht allgemeine
Social-Media-Fehler, dafür gibt es die Failure-Modi der Fachmodule.

Diese Datei ist die Gegenprobe zum Anspruch "nichts wird missinterpretiert". Sie
listet auf, was mit hoher Wahrscheinlichkeit falsch laufen wird, wenn jemand in
sechs Monaten nur die Zusammenfassung liest.

---

## FM-1 – "Der LinkedIn-Algorithmus heißt 360 Brew"

**Der Fehler:** Den Begriff als Namen der Newsfeed-Architektur verwenden.

**Warum er passiert:** Der Begriff hat sich international verbreitet und klingt
nach Insiderwissen. Behrens selbst hat nach eigener Aussage zur Verbreitung
beigetragen `[B 16:53]`.

**Richtig:** Es gibt eine neue Newsfeed-Architektur mit Two-Stage-Ranking.
LinkedIn hat sie nie 360 Brew genannt. 360 Brew war ein theoretisches,
zurückgezogenes Papier, das in seiner Komplexität nicht ausrollbar wäre
`[B 18:18]`, `[B 18:59]`.

**Kosten des Fehlers:** Im Fachgespräch sofort als veralteter Stand erkennbar.

**Gegenmittel:** Regel R11.

---

## FM-2 – "LinkedIn trainiert die LLMs, also müssen wir dort posten"

**Der Fehler:** Zitierung zur Laufzeit und Training in einen Topf werfen.

**Warum er passiert:** Behrens verwendet beide Begriffe im selben Satz:
"Wissensdatenbank und Trainingsquelle für LMs" `[B 9:29]`. Wer nur diesen Satz
mitnimmt, hat beides vermischt.

**Richtig:**

| | Was belegt ist |
|---|---|
| **Zitierung zur Laufzeit** | Belegt. Semrush misst rund 11 Prozent Zitieranteil im Schnitt über ChatGPT Search, Google AI Mode und Perplexity. Betrifft **öffentlich sichtbare** Inhalte |
| **Training** | Nicht durch diese Quelle belegt. LinkedIn ist weitgehend login-geschützt und blockt generische Crawler, siehe `linkedin/08-profil-optimierung.md` |

**Kosten des Fehlers:** Eine im Kundengespräch angreifbare Aussage. Ein
informierter Gegenüber zerlegt sie in einem Satz.

**Gegenmittel:** Regel R4 mit der dort formulierten Präzisierung.
`KI_Sichtbarkeit_Guide/01_Grundlagen.md` behandelt die Unterscheidung
grundsätzlich.

---

## FM-3 – "Behrens sagt, Reichweite ist egal"

**Der Fehler:** Aus "Impact-Plattform, keine virale Plattform" `[B 14:14]` eine
Reichweitenfeindlichkeit machen.

**Warum er passiert:** Der Satz ist zitierfähig und wird ohne den Folgesatz
weitergegeben.

**Richtig:** Behrens sagt im selben Abschnitt ausdrücklich, man sei natürlich an
guter Reichweite im relevanten Netzwerk interessiert `[B 14:14]`. Ihre These ist
nicht "Reichweite ist egal", sondern **"Reichweite ist kein Ziel, sondern eine
Messgröße"** `[B 15:30]`.

**Kosten des Fehlers:** Ein Kunde, der Reichweite braucht, fühlt sich nicht
verstanden, und die Beratung verliert Anschluss.

**Gegenmittel:** Regel R1, Abschnitt "Grenze der Regel".

---

## FM-4 – "Ein Corporate-Influencer-Programm bringt 50.000 Euro"

**Der Fehler:** Behrens' Beispielrechnung als ROI oder als belastbaren
Wirtschaftlichkeitsnachweis verwenden.

**Warum er passiert:** Die Zahl ist konkret, klingt seriös und löst genau das
Problem, das man im Pitch hat.

**Richtig:** Es ist eine **Werbeäquivalenz-Rechnung**, kein ROI. Sie

- setzt organische Impressionen mit gekauften gleich,
- ignoriert die Personalkosten des Programms vollständig,
- unterstellt einen TKP, der stark schwankt,
- wird von Behrens selbst als "tief gestapelt" gekennzeichnet `[B 23:08]`.

**Kosten des Fehlers:** Ein CFO rechnet die Personalkosten dagegen und die ganze
Argumentation kippt. Schlimmer: Das Programm wird an einer Zahl gemessen, die es
nie liefern sollte.

**Gegenmittel:** Regel R6. Als Größenordnung im Gespräch verwenden, im Angebot
nur mit ausgewiesener Methodik, und immer zusammen mit den drei anderen
Impact-Faktoren.

---

## FM-5 – "Der LinkedIn-CEO hat auf der OMR gesagt..."

**Der Fehler:** Aneesh Raman für den CEO von LinkedIn halten.

**Warum er passiert:** Der YouTube-Titel lautet "LinkedIn CEOO über Arbeiten und
Künstliche Intelligenz". "CEOO" wird als Tippfehler gelesen.

**Richtig:** CEOO steht für **Chief Economic Opportunity Officer** `[R 14:01]`.
CEO von LinkedIn ist Ryan Roslansky, Ramans Co-Autor `[R 0:30]`.

**Kosten des Fehlers:** Falsche Attribution in einer Kundenpräsentation.
Peinlich und leicht nachprüfbar.

**Zusatz:** Auch inhaltlich ist die Zuschreibung falsch. Raman spricht
durchgehend als Buchautor und Arbeitsmarkt-Beobachter, nicht als
Produktverantwortlicher. Er sagt kein Wort zum LinkedIn-Algorithmus.

---

## FM-6 – "Raman hat gesagt, wie der LinkedIn-Algorithmus funktioniert"

**Der Fehler:** Den Vortrag als Quelle für Feed, Ranking oder Reichweite
heranziehen, weil der Sprecher von LinkedIn kommt.

**Warum er passiert:** LinkedIn-Rolle plus OMR-Bühne plus 24 Minuten Redezeit
erzeugen die Erwartung, dass Plattformwissen dabei ist.

**Richtig:** Kein einziges Wort zu Feed, Ranking, Reichweite oder
Content-Distribution. Siehe Abschnitt "Was der Vortrag nicht sagt" in
`02_OMR26_Raman_FutureOfWork.md`.

---

## FM-7 – "Die 70-Prozent-Zahl ist eine Studie"

**Der Fehler:** "70 Prozent der Skills verändern sich bis 2030" als neutralen
Marktbefund zitieren.

**Warum er passiert:** Raman nennt sie den wichtigsten Datenpunkt des Buchs
`[R 12:50]`. Das klingt nach Evidenz.

**Richtig:** Es ist eine **LinkedIn-eigene Auswertung**, im Gespräch ohne
Quellenangabe genannt. Dasselbe gilt für "doppelt so viele Jobs" `[R 16:09]` und
den Founder- und Creator-Anstieg `[R 17:13]`.

**Gegenmittel:** Immer mit "laut LinkedIn" attribuieren. Gegenprüfung steht als
offener Punkt O5 in `04_Abgleich_bestehende_Module.md`.

---

## FM-8 – "KI beim Schreiben schadet"

**Der Fehler:** Aus der AI-Slop-Kritik beider Sprecher ein Verbot von KI im
Content-Prozess ableiten.

**Warum er passiert:** Beide Vorträge kritisieren KI-Output deutlich, und die
Kritik ist der einprägsamste Teil.

**Richtig:** Beide kritisieren zwei spezifische Dinge:

1. **Unbeaufsichtigte Automatisierung**, die menschliche Prüfung vollständig
   umgeht `[B 7:01]`
2. **Generischen Output**, der wie jeder andere klingt `[R 7:05]`

Beide sind ausdrücklich KI-positiv. Raman nutzt KI stündlich `[R 3:44]`.
Behrens' Positivbeispiel automatisiert viel, schreibt Content aber selbst
`[B 11:39]`.

**Kosten des Fehlers:** Eine Beratungshaltung, die Kunden 2026 nicht mehr
abnehmen, und ein internes Verbot, das Bucket 2 aus Ramans Modell blockiert.

---

## FM-9 – "Zwei Quellen sagen dasselbe, also ist es belegt"

**Der Fehler:** Die Übereinstimmung von Behrens und Raman beim Thema AI Slop als
Evidenz behandeln.

**Warum er passiert:** Zwei unabhängige Sprecher, gleiche Diagnose. Das fühlt
sich wie Bestätigung an.

**Richtig:** Beide äußern eine **Meinung**, keine Messung. Die Übereinstimmung
zeigt, dass die Einschätzung im Feld verbreitet ist, nicht dass sie zutrifft. Die
einzige harte Zahl zu AI-Slop-Erkennung steht nicht in den Keynotes, sondern in
`linkedin/01-algorithmus.md` (94 Prozent Trefferquote).

**Gegenmittel:** Belegstatus in `01_` und `02_` prüfen, bevor eine Aussage als
belegt weitergegeben wird.

---

## FM-10 – "Man braucht 2.000 Follower, um zitiert zu werden"

**Der Fehler:** Behrens' Satz "75 % der Leute hatten ab 2000 Follower aufwärts"
`[B 10:53]` als Schwellenwert weitergeben.

**Warum er passiert:** Die Zahl ist konkret, klingt nach Studienergebnis und
passt in jede Kundenpräsentation.

**Richtig:** Behrens verwechselt zwei Werte aus derselben Studie.

| Was sie sagt | Was die Studie sagt |
|---|---|
| 75 % hatten ab 2.000 Follower | 75 % sind **Vielposter** (über 5 Posts in vier Wochen). **Knapp die Hälfte** hat über 2.000 Follower |

Die Studie geht sogar in die andere Richtung: Personen mit unter 500 Followern
werden mindestens genauso häufig zitiert wie solche mit über 500.

**Ihre Schlussfolgerung bleibt richtig.** Frequenz und Substanz schlagen
Followerzahl. Die Studie stützt das stärker, als Behrens es selbst formuliert.
Nur die Zahl ist falsch zugeordnet.

**Kosten des Fehlers:** Ein Kunde mit 400 Followern glaubt, KI-Sichtbarkeit sei
für ihn unerreichbar. Das Gegenteil ist belegt.

**Gegenmittel:** Regel R3. Nie "2.000 Follower" als Schwelle nennen.

---

## FM-11 – Das Modul wird als Zusammenfassung gelesen

**Der Fehler:** Nur `03_Anwendungsregeln.md` lesen und die Regeln als Fakten
zitieren.

**Warum er passiert:** Das ist der bestimmungsgemäße Normalbetrieb, und er
funktioniert. Bis jemand eine Regel öffentlich behauptet.

**Richtig:** Ebene 3 ist für **Entscheidungen** gebaut, nicht für **Behauptungen**.
Wer eine Regel nach außen vertritt, prüft vorher den Belegstatus in Ebene 2. Der
Herkunftsstempel macht das zu einem Schritt.

**Faustregel:** Intern entscheiden aus Ebene 3. Extern behaupten erst nach Ebene 2.
