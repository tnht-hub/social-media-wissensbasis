# Design: Minimalistische To-do-App auf Obsidian-Basis (SyncTasks-Stil)

**Datum:** 2026-07-06
**Status:** Freigegeben

## Ziel

Ein minimalistisches Aufgaben-System im Stil der App *SyncTasks*, das auf **iPad und Desktop**
sichtbar und editierbar ist und automatisch synchronisiert. Umgesetzt **nicht als eigene App**,
sondern als schlanker **Obsidian-Vault** — dadurch überall bearbeitbar, ohne Hosting/App Store,
und (später) direkt für Claude les- und bearbeitbar, weil alles reines Markdown ist.

## Nicht-Ziele (bewusst weggelassen, YAGNI)

- Kein Fokus-/Pomodoro-Timer
- Keine Ordner-/Projekt-Hierarchie
- Keine wiederkehrenden Aufgaben
- Keine minutengenaue Uhrzeit-Sortierung oder Push-Erinnerungen
- Keine Claude-Anbindung (in dieser Phase)

Alle Punkte sind später ergänzbar, ohne das Grundkonzept zu ändern.

## Architektur & Sync

- **Neuer, eigener Vault `To-dos`**, gespeichert in **iCloud Drive → Obsidian**.
- Auf dem Mac erstellt; auf dem iPad wird derselbe iCloud-Vault geöffnet. iCloud hält beide Geräte synchron.
- Die bestehende Wissensbasis (dieses GitHub-Repo, Git-Sync) bleibt **komplett unberührt** —
  bewusste Trennung von Sync-Welten (iCloud vs. Git), um Konflikte zu vermeiden.
- **Engine:** Community-Plugin **Tasks**.

## Datenmodell

Aufgaben sind einfache Markdown-Checkboxen mit Tasks-Plugin-Metadaten:

```markdown
- [ ] Blogpost schreiben 📅 2026-07-10
- [ ] Content-Kalender planen 📅 2026-07-08 ⏰ 14:00
- [x] Koffer packen ✅ 2026-07-06
- [-] Doch nicht nötig
```

- `📅 JJJJ-MM-TT` = Fälligkeitsdatum
- `✅ JJJJ-MM-TT` = erledigt am (setzt das Plugin automatisch)
- `[x]` = erledigt (durchgestrichen), `[-]` = abgebrochen
- **Uhrzeit:** Das Tasks-Plugin arbeitet datumsgenau. Eine Uhrzeit wird als sichtbarer Text
  (`⏰ 14:00`) mitgeschrieben — informativ, aber ohne minutengenaue Sortierung/Erinnerung.

## Dateien im Vault

- **`Inbox.md`** — Schnellerfassung: neue Gedanken als `- [ ] …` reinwerfen, Datum optional.
- **`Dashboard.md`** — Hauptansicht mit automatischen Tasks-Abfragen (siehe unten).

## Dashboard-Ansichten (Tasks-Abfragen)

`Dashboard.md` bündelt vier Live-Listen. Abgehakt wird per Tap direkt in der Liste;
erledigte Aufgaben verschwinden aus „Heute"/„Demnächst" und erhalten automatisch das `✅`-Datum.

1. **⚠️ Überfällig** — offen, Fälligkeit vor heute
2. **📌 Heute** — offen, heute fällig
3. **🗓️ Demnächst (7 Tage)** — offen, in den nächsten 7 Tagen fällig
4. **📥 Inbox / ohne Datum** — offen, ohne Fälligkeitsdatum

Beispielhafte Abfrage-Logik (Tasks-Syntax):

```tasks
not done
due before today
sort by due
```
(→ Überfällig; die weiteren Blöcke analog mit „due on today", „due after today / before in 7 days",
„no due date".)

## Minimalistischer Look (CSS-Snippet)

Ein CSS-Snippet erzeugt die aufgeräumte SyncTasks-Optik aus den Screenshots:

- Schwarzer Hintergrund, weiße Schrift
- Seitenleisten, Ribbon und Kopfzeilen ausgeblendet → nur die Aufgabenliste
- Großzügige Typografie, viel Weißraum, minimaler Zeilenabstand
- Erledigte Aufgaben dezent ausgegraut/durchgestrichen
- Ziel: „nur meine Aufgaben, sonst nichts"

## Bedienung

- **Erfassen:** In `Inbox.md` tippen; am Desktop optional per Tasks-Dialog „Create Task" (Eingabemaske).
- **Abhaken:** iPad wie Desktop — Checkbox antippen.
- **iPad-Komfort:** `Dashboard.md` als Startnotiz festlegen; optional Homescreen-Icon.

## Umsetzungsschritte (Überblick)

1. Vault `To-dos` in iCloud Drive/Obsidian anlegen (Mac).
2. Obsidian auf iPad installieren, denselben iCloud-Vault öffnen.
3. Community-Plugin **Tasks** installieren & aktivieren.
4. `Inbox.md` und `Dashboard.md` mit den Abfrageblöcken anlegen.
5. CSS-Snippet für den minimalistischen Look aktivieren.

## Erfolgskriterien

- Aufgaben auf iPad und Desktop sichtbar und editierbar; Änderungen syncen über iCloud.
- Dashboard zeigt korrekt Überfällig / Heute / Demnächst / Inbox.
- Abhaken funktioniert per Tap auf beiden Geräten.
- Oberfläche ist minimalistisch schwarz/weiß, ohne störende UI-Elemente.
