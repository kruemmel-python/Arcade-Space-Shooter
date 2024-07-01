import pygame
import sqlite3
from PIL import Image
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def initialize_pygame():
    pygame.init()

def create_window(window_size):
    return pygame.display.set_mode(window_size)

def set_caption(caption):
    pygame.display.set_caption(caption)

def load_images():
    images = {}
    for i in range(1, 11):
        images[f'player_{i}'] = pygame.image.load(resource_path(f'data/ship_{i}.png'))
        images[f'enemy_{i}'] = pygame.image.load(resource_path(f'data/ship_{i}.png'))
    engine_image = pygame.image.load(resource_path('data/engine_ship.png'))
    heart_image = pygame.image.load(resource_path('data/heart.png'))
    return images, engine_image, heart_image

def scale_images(images):
    scaled_images = {}
    for key, img in images.items():
        scaled_images[key] = pygame.transform.scale(img, (48, 48))
    return scaled_images

def load_sounds():
    pygame.mixer.music.load(resource_path('data/background.mp3'))
    hit_sound = pygame.mixer.Sound(resource_path('data/hit.wav'))
    shot_sound = pygame.mixer.Sound(resource_path('data/shot.wav'))
    death_sound = pygame.mixer.Sound(resource_path('data/death.wav'))
    return hit_sound, shot_sound, death_sound

def set_background_music(volume):
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)

def initialize_database():
    conn = sqlite3.connect(resource_path('data/highscores.db'))
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS highscores (
                    name TEXT, 
                    score INTEGER, 
                    level INTEGER, 
                    time REAL
                )''')
    try:
        c.execute('ALTER TABLE highscores ADD COLUMN time REAL')
    except sqlite3.OperationalError:
        pass
    conn.commit()
    return conn, c

def load_gif_frames(file_path, window_size):
    gif = Image.open(resource_path(file_path))
    frames = []
    for frame in range(0, gif.n_frames):
        gif.seek(frame)
        frame_image = gif.convert('RGBA')
        frame_image = frame_image.resize(window_size, Image.LANCZOS)
        frame_data = frame_image.tobytes()
        frame_surface = pygame.image.fromstring(frame_data, frame_image.size, 'RGBA')
        frames.append(frame_surface)
    return frames
