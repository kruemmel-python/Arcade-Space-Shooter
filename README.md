# Arcade Space Shooter
![intro](https://github.com/kruemmel-python/Arcade-Space-Shooter/assets/169469747/b321f938-ead7-43b7-bab6-35d9d78cd50e)
Willkommen zum Arcade Space Shooter! Dies ist ein klassisches Weltraum-Shooter-Spiel, bei dem Sie durch den Weltraum fliegen, Gegner abschießen und Punkte sammeln. Das Spiel bietet verschiedene Schiffstypen zur Auswahl und zufällig erscheinende Gegner.

## Inhaltsverzeichnis

- [Features](#features)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Steuerung](#steuerung)
- [Screenshots](#screenshots)
- [Technologien](#technologien)
- [Mitwirkende](#mitwirkende)
- [Lizenz](#lizenz)

## Features

- Auswahl aus 10 verschiedenen Spieler-Schiffen
- Zufällig erscheinende Gegner
- Highscore-System mit Speicherung der Spielername, Punkte, Level und Spielzeit
- Hintergrundmusik und Soundeffekte
- Animierter Sternenhintergrund

## Installation

### Voraussetzungen

- Python 3.12
- Pygame
- Pillow
- SQLite3

### Schritt-für-Schritt-Anleitung

1. **Projekt klonen**

   ```sh
   git clone https://github.com/kruemmel-python/Arcade-Space-Shooter.git
   cd Arcade-Space-Shooter
   ```

2. **Virtuelle Umgebung erstellen**

   ```sh
   python -m venv venv
   source venv/bin/activate  # Für Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**

   ```sh
   pip install -r requirements.txt
   ```

4. **Spiel starten**

   ```sh
   python main.py
   ```

## Verwendung

### Hauptmenü

Nach dem Start des Spiels sehen Sie das Hauptmenü mit den folgenden Optionen:

- Highscores: Zeigt die besten Spieler an
- Spiel starten: Beginnen Sie ein neues Spiel
- Beenden: Beenden Sie das Spiel

### Spielername und Schiffsauswahl

1. Geben Sie Ihren Spielernamen (3 Buchstaben) ein.
2. Wählen Sie Ihr Schiff mit den Pfeiltasten links und rechts aus und drücken Sie `Enter`, um das Spiel zu starten.

## Steuerung

- **Pfeiltasten**: Bewegung des Schiffs
- **Leertaste**: Schießen
- **ESC**: Zurück zum Hauptmenü

## Screenshots

![Hauptmenü](screenshots/main_menu.png)
*Hauptmenü des Spiels*

![Schiffsauswahl](screenshots/ship_selection.png)
*Auswahl des Spielerschiffs*

![Spiel](screenshots/game.png)
*Spielbildschirm*

## Technologien

- [Pygame](https://www.pygame.org/): Bibliothek für die Spieleentwicklung
- [Pillow](https://python-pillow.org/): Bildverarbeitungsbibliothek
- [SQLite3](https://www.sqlite.org/index.html): Leichtgewichtige SQL-Datenbank

## Mitwirkende

- [kruemmel-python](https://github.com/kruemmel-python)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.


