# Arcade-Space-Shooter

![intro](https://github.com/kruemmel-python/Arcade-Space-Shooter/assets/169469747/b321f938-ead7-43b7-bab6-35d9d78cd50e)


Ein spannendes Shooter-Spiel mit Pygame, in dem du feindliche Schiffe abschießen und dein eigenes Raumschiff steuern musst, um Punkte zu sammeln und Level aufzusteigen. Das Spiel speichert Highscores in einer SQLite-Datenbank.

## Inhalt

- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Spielsteuerung](#spielsteuerung)
- [Highscore-Anzeige](#highscore-anzeige)
- [Datenbank](#datenbank)
- [Credits](#credits)
- [Lizenz](#lizenz)

## Features

- Spielersteuerung eines Raumschiffs mit Tastatur
- Schießen von Kugeln zur Zerstörung von Feinden
- Gegnerische Schiffe erscheinen mit zunehmender Schwierigkeit
- Animation von Sternen im Hintergrund
- Speicherung von Highscores in einer SQLite-Datenbank
- Hintergrundmusik und Soundeffekte
- Anzeige der Highscores mit animiertem GIF-Hintergrund

## Installation

1. **Python installieren**: Stelle sicher, dass Python 3.12 oder neuer installiert ist. Lade Python von der [offiziellen Webseite](https://www.python.org/downloads/) herunter und installiere es.

2. **Abhängigkeiten installieren**: Installiere die benötigten Python-Bibliotheken mit `pip`.

    ```bash
    pip install pygame pillow
    ```

3. **Projektdateien**: Stelle sicher, dass du die folgenden Dateien in deinem Projektverzeichnis hast:
    - `main.py` (das Hauptspielskript)
    - `mnt/data/weapons.png` (Bild der Waffe)
    - `mnt/data/enemy.png` (Bild des Gegners)
    - `mnt/data/ship.png` (Bild des Spielerschiffs)
    - `mnt/data/engine_ship.png` (Bild des Triebwerks)
    - `mnt/data/heart.png` (Bild des Herzens)
    - `mnt/data/background.mp3` (Hintergrundmusik)
    - `mnt/data/hit.wav` (Soundeffekt für Treffer)
    - `mnt/data/shot.wav` (Soundeffekt für Schüsse)
    - `mnt/data/death.wav` (Soundeffekt für Tod)
    - `mnt/data/intro.gif` (animierter Hintergrund für Highscore-Anzeige)

## Verwendung

Starte das Spiel mit folgendem Befehl:

```bash
python main.py
```

## Spielsteuerung

- **Pfeiltasten**: Bewege das Raumschiff nach links, rechts, oben oder unten.
- **Leertaste**: Schieße Kugeln ab.
- **Escape**: Beende das Spiel.

## Highscore-Anzeige

Nach dem Start des Spiels wird zunächst die Highscore-Anzeige gezeigt. Drücke die `Enter`-Taste, um zum Spiel zu gelangen.

## Datenbank

Die Highscores werden in einer SQLite-Datenbank (`highscores.db`) gespeichert. Die Datenbank enthält eine Tabelle `highscores` mit den folgenden Spalten:

- `name` (TEXT): Der Name des Spielers.
- `score` (INTEGER): Der erzielte Punktestand.
- `level` (INTEGER): Das erreichte Level.

## Credits

- **Programmierer**: Ralf Krümmel
- **Bibliotheken**: [Pygame](https://www.pygame.org/), [Pillow](https://python-pillow.org/)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.
