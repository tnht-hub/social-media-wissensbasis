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

Die Logik (Skill) wird mit dem Plugin verteilt. Die Daten (Module) werden zur Laufzeit über die Roh-Adresse von GitHub gelesen.

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

### 3. Basis-Adresse

Die Basis-Adresse ist bereits fest eingetragen auf:
`https://raw.githubusercontent.com/tnht-hub/social-media-wissensbasis/main/wissensbasis/`

Sie steht in `wissensbasis/index.json` (Feld `basis_url`) und in `skills/socialmedia-agentur/SKILL.md`. Bei einem späteren Repo-Umzug an diesen beiden Stellen anpassen.

### 4. Plugin im Team hinzufügen

Jede Person fügt einmalig den Marketplace hinzu und installiert das Plugin. In Claude Code oder Cowork:

```
/plugin marketplace add tnht-hub/social-media-wissensbasis
/plugin install social-media-wissensbasis
```

Ab dann steht der Skill `socialmedia-agentur` zur Verfügung und liest die Module zentral aus dem Repository.

## Laufende Pflege

Die Pflege betrifft nur die Inhalte unter `wissensbasis/`. Logik und Manifeste bleiben in der Regel unberührt.

1. Das betreffende Modul unter `wissensbasis/` bearbeiten.
2. Die `**Stand:**`-Angabe im Kopf des Moduls beziehungsweise der Index-/README-Datei des Moduls auf den neuen Monat setzen.
3. Den Index neu erzeugen, damit Titel und Stand stimmen:

   ```
   python3 werkzeuge/index_erzeugen.py
   ```

4. Änderungen committen und pushen. Über die Roh-Adresse stehen sie sofort allen zur Verfügung. Eine kurze CDN-Pufferung von wenigen Minuten ist normal.

Ändert sich die Logik des Skills, die Versionsnummer in `.claude-plugin/plugin.json` erhöhen und das Team das Plugin aktualisieren lassen.

## Schnell veraltende Teile

Besonders zu beobachten sind Plattform-Algorithmen, Features und rechtliche Angaben. Ein monatlicher Review ist sinnvoll. Eine automatische Erinnerung lässt sich als geplante Aufgabe einrichten oder als zeitgesteuerte GitHub-Action, die zum Monatsersten ein Issue zur Aktualisierung anlegt.

## Hinweise

Das Repository enthält bewusst keine Mandanten- oder internen B&B-Daten. Die zuvor eingebetteten Wettbewerbs- und Kundenbezüge wurden anonymisiert, die Originale liegen getrennt im internen B&B-Ordner. Vor jeder Veröffentlichung neuer Module ist zu prüfen, dass kein vertrauliches Material in die öffentliche Wissensbasis gelangt.
