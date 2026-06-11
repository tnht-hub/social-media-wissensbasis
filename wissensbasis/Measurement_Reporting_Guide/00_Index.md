# Guideline: Measurement & Reporting für Social Media

**Stand:** Juni 2026
**Scope:** Plattformübergreifend, das übergeordnete KPI- und Reporting-Dach (Phase 5 „Measurement" im Agentur-Prozess). Die plattformeigenen Metriken existieren bereits je Kanal (siehe `instagram/06`, `linkedin/06`, `tiktok/06`, `youtube/06`, `facebook/06`, `x-twitter/06`); dieses Modul liefert das Framework darüber.
**Zielanwender:innen:** Account-Manager:innen, Strategie- und Data-Verantwortliche, Social-Media-Manager:innen, Agentur-Leitung, Kund:innen-seitige Marketing-Verantwortliche

---

## Wichtigster Satz dieser Guideline

> Ein Report ist kein Zahlenfriedhof, sondern eine Antwort auf eine Frage: „Hat das, was wir getan haben, dem Ziel gedient, und was tun wir als Nächstes?" Wenn eine Kennzahl diese Frage nicht beantwortet, gehört sie nicht in den Report.

---

## Inhalt

| Datei | Thema |
|---|---|
| `00_Index.md` | Diese Übersicht, Grundprinzipien, Lebenszyklus |
| `01_KPI-Framework_Funnel.md` | Funnel-Logik (TOFU, MOFU, BOFU), Ziele auf KPIs mappen, North-Star-Metrik, Vanity gegen Actionable |
| `02_Metriken-Definitionen.md` | Saubere Definitionen und Berechnungsformeln, plattformspezifische Besonderheiten |
| `03_Reporting-Templates_und_Rhythmus.md` | Report-Struktur, Frequenz, Stakeholder-gerechtes Reporting, Storytelling mit Daten |
| `04_Benchmarks.md` | Branchen-Benchmarks je Plattform und wie man sie richtig interpretiert |
| `05_Attribution_und_ROI.md` | Attribution-Modelle, ROAS und ROI, UTM-Parameter, Grenzen der Messbarkeit |
| `06_Failure-Modi.md` | Typische Reporting-Fehler und Gegenmittel |
| `07_Quellen.md` | Alle recherchierten Quellen, Methodik-Hinweise, Lebensdauer |

---

## Grundprinzipien

**1. Messung beginnt beim Ziel, nicht bei der Zahl.**
Eine Kennzahl ist nur dann ein KPI, wenn sie auf ein Geschäfts- oder Kampagnenziel einzahlt. Wer zuerst die verfügbaren Dashboard-Zahlen sammelt und dann eine Story darum baut, misst Aktivität, nicht Wirkung. Begründung: Plattformen zeigen Dutzende Metriken an, aber die meisten sind für das jeweilige Ziel irrelevant. Ohne Ziel-Anker wird jeder Report beliebig.

**2. Wenige KPIs schlagen viele.**
Ein guter Report braucht maximal acht bis zehn KPIs, die direkt auf die Ziele einzahlen. Begründung: Aufmerksamkeit ist knapp. Je mehr Zahlen ein Report zeigt, desto weniger Entscheidungen löst er aus. Fokus erzwingt Priorisierung.

**3. Actionable schlägt Vanity.**
Likes, Follower und Impressionen sehen gut aus, sagen aber selten, was als Nächstes zu tun ist. Eine Kennzahl ist erst dann handlungsleitend, wenn sie spezifisch, vergleichbar und mit einer konkreten Handlung verknüpft ist. Begründung: Wenn ein Report mit Follower-Zahlen öffnet, optimiert das Team auf Follower. Öffnet er mit Conversion-Rate, optimiert es auf das Geschäft.

**4. Kontext schlägt absolute Zahl.**
„10.000 Views" bedeutet nichts ohne Vergleich: gegen die Vorperiode, gegen das Ziel, gegen den Benchmark. Begründung: Eine Zahl allein kann nicht gut oder schlecht sein. Erst der Vergleich macht sie interpretierbar und damit reportfähig.

> Eine dokumentierte Reel-Beobachtung stützt das: Erfolg wurde erst durch den Vergleich am Kanal-Median sichtbar, getrennt nach Konto und nach Reichweite gegen Engagement. Ein Reel mit hoher Aufrufzahl, aber nur einer Handvoll Likes belegt, dass Reichweite ohne Engagement ein schwaches Signal ist.

**5. Plattform-Metriken sind nicht vergleichbar, ohne Definition.**
Eine „Engagement-Rate" auf Instagram (Basis: Reach) ist nicht dieselbe wie auf TikTok (Basis: Views) oder LinkedIn (Basis: Impressionen). Begründung: Wer Plattformen direkt nebeneinanderstellt, ohne die Berechnungsbasis offenzulegen, vergleicht Äpfel mit Birnen und erzeugt falsche Schlüsse.

**6. Messbarkeit hat Grenzen, und die gehören in den Report.**
Dark Social, iOS-Tracking-Opt-out und cookieless Tracking machen einen wachsenden Teil der Wirkung unsichtbar. Begründung: Ein Report, der so tut, als sei alles attribuierbar, ist unehrlich. Die Grenzen der Messung offen zu benennen, schützt vor Fehlentscheidungen und schafft Vertrauen.

**7. Reporting ist Kommunikation, nicht Dokumentation.**
Der Report richtet sich nach der Empfängerin: Geschäftsführung will Wirkung und ROI, das operative Team will Detail und Optimierungs-Hebel. Begründung: Dieselben Daten brauchen unterschiedliche Linsen. Ein Report, der für alle gleich aussieht, erreicht niemanden richtig.

---

## Was diese Guideline NICHT abdeckt

- **Plattform-spezifische Metrik-Kataloge** (welche Zahl wo im Dashboard steht): Das steht in den jeweiligen Kanal-Guides (`*/06-analytics-metriken.md`). Hier geht es um das Dach darüber.
- **Paid-Media-Kampagnen-Steuerung im Detail** (Bidding, Audience-Targeting, Creative-Testing): eigene Disziplin. ROAS und Attribution werden hier nur auf Reporting-Ebene behandelt.
- **Web-Analytics-Implementierung** (GA4-Setup, Server-Side-Tracking, Tag-Manager): eigene technische Welt. UTM-Logik wird behandelt, die Tracking-Infrastruktur nicht.
- **Tool-Bedienung im Detail** (wie man in Metricool, Sprout Social oder Looker Studio klickt): Tools werden genannt, nicht als Handbuch erklärt.
- **A/B-Test-Statistik** (Signifikanz, Konfidenzintervalle): eigene Methodik.

---

## Über die Recherche-Basis

Diese Guideline stützt sich auf:
- Aktuelle Benchmark-Reports (Socialinsider, Buffer, Hootsuite, Improvado, Apaya) mit Stand 2026
- KPI- und Funnel-Methodik (Hive Digital, Semrush, Funnel.io, MetricDesk)
- Vanity- gegen Actionable-Metrics-Literatur (Amplitude, Hootsuite, AgencyAnalytics, Neal Schaffer / North-Star-Framework)
- Attribution- und Messbarkeits-Quellen (Improvado, GTech, GA4-Dokumentation, Dark-Social-Recherche 2026)
- Reporting- und Data-Storytelling-Methodik (Sprout Social, AgencyAnalytics, Minto-Pyramiden-Prinzip)
- Deutsche Fachquellen (OMT, Meltwater, Asana, Agorapulse, Skill-Sprinters) zur Spiegelung im DACH-Kontext

Alle Quellen mit URL und Beschreibung in `07_Quellen.md`. Kernaussagen sind durch mindestens drei unabhängige Quellen trianguliert.

---

## Lebenszyklus

| Ebene | Halbwertszeit |
|---|---|
| **Grundprinzipien (00, 01)** | 5 bis 10 Jahre stabil, basieren auf Funnel-Logik und Messlehre |
| **Metriken-Definitionen (02)** | 2 bis 3 Jahre, Plattformen ändern Berechnungsbasen (z.B. Instagram Views seit 2024) |
| **Reporting-Templates (03)** | 3 bis 5 Jahre, Struktur stabil, Tool-Nennungen veralten schneller |
| **Benchmarks (04)** | 6 bis 12 Monate, Engagement-Raten verschieben sich jährlich deutlich |
| **Attribution und Messbarkeit (05)** | 12 bis 18 Monate, Privacy- und Tracking-Landschaft ist in Bewegung |
| **Failure-Modi (06)** | 3 bis 5 Jahre stabil, menschliche Fehler ändern sich langsam |

Jährlicher Review-Termin empfohlen, mit Schwerpunkt auf den Säulen 04 (Benchmarks) und 05 (Attribution).
