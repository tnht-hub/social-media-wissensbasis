# Social-Media-Wissensbasis (B&B)

Dieses Repository bündelt zwei Dinge an einem Ort: die gepflegte Social-Media-Wissensbasis von B&B und den Orchestrator-Skill `socialmedia-agentur`, der darauf zugreift. Es ist zugleich ein installierbares Plugin und die zentrale Datenquelle.

Der Grundgedanke: Eine Person pflegt die Inhalte in diesem Repository, alle anderen installieren einmal das Plugin und greifen über den Skill zu. Inhaltsänderungen stehen sofort allen zur Verfügung, ohne dass jemand etwas neu installieren muss. So entfällt das Problem lokal veralteter Kopien.

## Aufbau

```
social-media-wissensbasis/
├── .claude-plugin/
│   ├── plugin.json          Plugin-Manifest
│   └── marketplace.json     Marketplace-Eintrag fuer die Team-Installation
├── skills/
│   └── socialmedia-agentur/ der Orchestrator-Skill (Logik)
├── wissensbasis/
│   ├── index.json           Verzeichnis aller Module mit Stand
│   └── <alle Module>        Plattform- und Methodik-Wissen als Markdown
├── werkzeuge/
│   └── index_erzeugen.py    erzeugt index.json nach Aenderungen neu
└── README.md
```

Mit dem Plugin wird zuverlässig nur die `SKILL.md` des Orchestrators verteilt. Alles andere wird zur Laufzeit über die Roh-Adresse von GitHub gelesen: die Module unter `wissensbasis/` und seit Version 1.5.1 auch die drei skill-internen Dateien `persona-modul-karte.md`, `briefing-fragebogen.md` und `rats-modus.md`. Hintergrund: Der Org-Plugin-Upload liefert pro Skill nur die `SKILL.md` aus und lässt die übrigen Dateien im Skill-Ordner fallen, deshalb werden sie aus dem Repo nachgeladen.

## Einmalige Einrichtung

### 1. Öffentliches Repository anlegen

Auf GitHub ein neues, öffentliches Repository erstellen. Der Name ist frei wählbar, etwa `social-media-wissensbasis`.

### 2. Inhalt hochladen

Den gesamten Inhalt dieses Ordners in das Repository laden, entweder über die Weboberfläche (Upload) oder per Git:

```
git init
git add .
git commit -m "Wissensbasis und Skill"
git branch -M main
git remote add origin https://github.com/tnht-hub/social-media-wissensbasis.git
git push -u origin main
```

### 3. Basis-Adressen

Es sind zwei feste Roh-Adressen eingetragen:

- Module: `https://raw.githubusercontent.com/tnht-hub/social-media-wissensbasis/main/wissensbasis/` (in `wissensbasis/index.json` im Feld `basis_url` und in der `SKILL.md` als `RAW_BASIS_URL`)
- Skill-interne Dateien: `https://raw.githubusercontent.com/tnht-hub/social-media-wissensbasis/main/skills/socialmedia-agentur/` (in der `SKILL.md` als `RAW_SKILL_URL`)

Wichtig: Der Skill funktioniert nur, solange dieses Repository öffentlich und unter dem Pfad `tnht-hub/social-media-wissensbasis`, Branch `main`, erreichbar bleibt. Wird das Repository umbenannt, der Eigentümer gewechselt, der Branch geändert oder das Repo auf privat gestellt, fehlen zur Laufzeit nicht nur die Module, sondern auch Briefing-Fragebogen, Persona-Karte und Rats-Modus, und der Skill degradiert ohne Vorwarnung. Bei einem solchen Umzug beide Adressen anpassen, also `RAW_BASIS_URL` und `RAW_SKILL_URL` in der `SKILL.md` sowie `basis_url` in `wissensbasis/index.json`, und das Plugin neu verteilen.

### 4. Plugin im Team hinzufügen

In Claude Code über die Marketplace-Befehle:

```
/plugin marketplace add tnht-hub/social-media-wissensbasis
/plugin install social-media-wissensbasis
```

In Cowork gibt es diese Befehle nicht. Dort verteilt ein Owner das Plugin über Organization settings > Plugins per ZIP-Upload. Beim Bauen des ZIP den gesamten Repo-Inhalt einpacken, ohne `.git` und `.DS_Store`. Auch wenn das ZIP alle Dateien enthält, installiert dieser Weg pro Skill nur die `SKILL.md`. Die übrigen Skill-Dateien kommen deshalb zur Laufzeit über `RAW_SKILL_URL` aus dem Repo, siehe oben.

Ab dann steht der Skill `socialmedia-agentur` zur Verfügung und liest Module und skill-interne Dateien zentral aus dem Repository.

## Laufende Pflege

Die laufende Pflege betrifft die Inhalte unter `wissensbasis/` sowie die drei skill-internen Dateien unter `skills/socialmedia-agentur/` (`persona-modul-karte.md`, `briefing-fragebogen.md`, `rats-modus.md`). Die `SKILL.md` und die Manifeste bleiben in der Regel unberührt.

1. Das betreffende Modul unter `wissensbasis/` bearbeiten.
2. Die `**Stand:**`-Angabe im Kopf des Moduls beziehungsweise der Index-/README-Datei des Moduls auf den neuen Monat setzen.
3. Den Index neu erzeugen, damit Titel und Stand stimmen:

   ```
   python3 werkzeuge/index_erzeugen.py
   ```

4. Änderungen committen und pushen. Über die Roh-Adresse stehen sie sofort allen zur Verfügung. Eine kurze CDN-Pufferung von wenigen Minuten ist normal.

Änderungen an den drei skill-internen Dateien wirken wie Modul-Änderungen sofort über die Roh-Adresse, ein erneuter Upload ist dafür nicht nötig, nur committen und pushen.

Nur wenn sich die `SKILL.md` selbst ändert, muss das Plugin neu verteilt werden: Versionsnummer in `.claude-plugin/plugin.json` und `marketplace.json` erhöhen, neues ZIP hochladen, und das Team aktualisiert das Plugin und startet die App neu, damit die neue Fassung geladen wird.

## Schnell veraltende Teile

Besonders zu beobachten sind Plattform-Algorithmen, Features und rechtliche Angaben. Ein monatlicher Review ist sinnvoll. Eine automatische Erinnerung lässt sich als geplante Aufgabe einrichten oder als zeitgesteuerte GitHub-Action, die zum Monatsersten ein Issue zur Aktualisierung anlegt.

## Hinweise

Das Repository enthält bewusst keine Mandanten- oder internen B&B-Daten. Die zuvor eingebetteten Wettbewerbs- und Kundenbezüge wurden anonymisiert, die Originale liegen getrennt im internen B&B-Ordner. Vor jeder Veröffentlichung neuer Module ist zu prüfen, dass kein vertrauliches Material in die öffentliche Wissensbasis gelangt.
