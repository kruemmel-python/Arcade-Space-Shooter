import pygame
import random
import sys
import sqlite3
from PIL import Image

# Initialize Pygame
pygame.init()

# Set up display
WINDOW_SIZE = (800, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Shooter Game')

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Load images
gun_image = pygame.image.load('mnt/data/weapons.png')
enemy_image = pygame.image.load('mnt/data/enemy.png')
player_image = pygame.image.load('mnt/data/ship.png')
engine_image = pygame.image.load('mnt/data/engine_ship.png')
heart_image = pygame.image.load('mnt/data/heart.png')  # Assumed heart image

# Scale images if necessary
gun_image = pygame.transform.scale(gun_image, (64, 64))
enemy_image = pygame.transform.scale(enemy_image, (48, 48))
player_image = pygame.transform.scale(player_image, (48, 48))
engine_image = pygame.transform.scale(engine_image, (48, 48))
heart_image = pygame.transform.scale(heart_image, (30, 30))

# Load sounds
pygame.mixer.music.load('mnt/data/background.mp3')
hit_sound = pygame.mixer.Sound('mnt/data/hit.wav')
shot_sound = pygame.mixer.Sound('mnt/data/shot.wav')
death_sound = pygame.mixer.Sound('mnt/data/death.wav')

# Set background music volume
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Set up game variables
GUN_SPEED = 10
BULLET_SPEED = 7
ENEMY_SPEED = 1
ENEMY_SPAWN_RATE = 100  # Higher values mean slower spawn rate
bullets = []
enemies = []
stars = []

# Set up font
font = pygame.font.SysFont(None, 36)

# Initialize SQLite database
try:
    conn = sqlite3.connect('highscores.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS highscores (name TEXT, score INTEGER, level INTEGER)''')
    conn.commit()
except sqlite3.Error as e:
    print(f"SQLite error: {e}")
    sys.exit()

# Load GIF frames and scale them to window size
gif = Image.open('mnt/data/intro.gif')
frames = []
for frame in range(gif.n_frames):
    gif.seek(frame)
    frame_image = gif.convert('RGBA')
    frame_image = frame_image.resize(WINDOW_SIZE, Image.LANCZOS)  # Scale to window size
    frame_data = frame_image.tobytes()
    frame_surface = pygame.image.fromstring(frame_data, frame_image.size, 'RGBA')
    frames.append(frame_surface)


def show_highscores():
    """Display highscores screen with animated GIF background."""
    intro_active = True
    frame_index = 0
    frame_count = len(frames)
    while intro_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                intro_active = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.blit(frames[frame_index], (0, 0))
        
        c.execute('SELECT * FROM highscores ORDER BY score DESC, level DESC')
        highscores = c.fetchall()
        y_position = 50
        for hs in highscores:
            name_text = font.render(f'Name: {hs[0]}', True, YELLOW)
            score_text = font.render(f'Score: {hs[1]}', True, RED)
            level_text = font.render(f'Level: {hs[2]}', True, BLUE)
            window.blit(name_text, (50, y_position))
            window.blit(score_text, (250, y_position))
            window.blit(level_text, (450, y_position))
            y_position += 40
        
        frame_index = (frame_index + 1) % frame_count
        pygame.display.flip()
        pygame.time.delay(100)  # Adjust delay as needed


def get_player_name():
    """Prompt the player to enter their name."""
    name = ''
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(name) == 3:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif len(name) < 3 and event.unicode.isalpha():
                    name += event.unicode.upper()
        window.fill(BLACK)
        prompt = font.render(f'Enter your name (3 letters): {name}', True, WHITE)
        window.blit(prompt, (50, 50))
        pygame.display.flip()
    return name


def save_highscore(name, score, level):
    """Save the player's highscore to the database."""
    c.execute('INSERT INTO highscores (name, score, level) VALUES (?, ?, ?)', (name, score, level))
    conn.commit()


def update_level():
    """Update the game level, enemy speed, and spawn rate."""
    global level, ENEMY_SPEED, ENEMY_SPAWN_RATE, next_level_score, lives
    level += 1
    lives += 1
    if level <= 20:
        ENEMY_SPEED += 1  # Increase enemy speed
        ENEMY_SPAWN_RATE = max(10, ENEMY_SPAWN_RATE - 1)  # Increase spawn rate
        next_level_score += 50
    else:
        level = 20  # Cap level at 20


def create_star():
    """Create a star at a random position."""
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    star_rect = pygame.Rect(x, y, 2, 2)
    stars.append(star_rect)


# Show highscores before starting the game
show_highscores()

# Get player name
player_name = get_player_name()

# Game variables
running = True
clock = pygame.time.Clock()
score = 0
level = 1
lives = 3
hearts = 5
player_rect = player_image.get_rect(midbottom=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] - 20))
next_level_score = 50

# Initial stars
for _ in range(100):
    create_star()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_highscore(player_name, score, level)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                save_highscore(player_name, score, level)
                running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move player in all directions
    moving = False
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-GUN_SPEED, 0)
        moving = True
    if keys[pygame.K_RIGHT] and player_rect.right < WINDOW_SIZE[0]:
        player_rect.move_ip(GUN_SPEED, 0)
        moving = True
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.move_ip(0, -GUN_SPEED)
        moving = True
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_SIZE[1]:
        player_rect.move_ip(0, GUN_SPEED)
        moving = True

    # Shoot bullet
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit the number of bullets on screen
            bullet_rect = pygame.Rect(player_rect.centerx - 5, player_rect.top - 10, 10, 20)
            bullets.append(bullet_rect)
            shot_sound.play()  # Play shooting sound

    # Move bullets
    for bullet in bullets[:]:
        bullet.move_ip(0, -BULLET_SPEED)
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, ENEMY_SPAWN_RATE) == 1:
        enemy_rect = enemy_image.get_rect(topleft=(random.randint(0, WINDOW_SIZE[0] - enemy_image.get_width()), 0))
        enemies.append(enemy_rect)

    # Move enemies
    for enemy in enemies[:]:
        enemy.move_ip(0, ENEMY_SPEED)
        if enemy.top > WINDOW_SIZE[1]:
            enemies.remove(enemy)
            score -= 1  # Penalty for missed enemy

    # Move stars
    for star in stars[:]:
        star.move_ip(0, -1)
        if star.bottom < 0:
            stars.remove(star)
            create_star()

    # Check for collisions
    bullets_to_remove = []
    enemies_to_remove = []
    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                enemies_to_remove.append(enemy)
                bullets_to_remove.append(bullet)
                score += 1  # Increase score for hitting an enemy
                hit_sound.play()  # Play hit sound

        if enemy.colliderect(player_rect):
            enemies_to_remove.append(enemy)
            hearts -= 1
            death_sound.play()  # Play death sound
            if hearts <= 0:
                lives -= 1
                hearts = 5
                if lives <= 0:
                    save_highscore(player_name, score, level)
                    running = False  # End game if no lives left

    # Remove collided bullets and enemies
    for bullet in bullets_to_remove:
        if bullet in bullets:
            bullets.remove(bullet)
    for enemy in enemies_to_remove:
        if enemy in enemies:
            enemies.remove(enemy)

    # Update level
    if score >= next_level_score:
        update_level()

    # Clear screen
    window.fill(BLACK)

    # Draw stars
    for star in stars:
        pygame.draw.rect(window, WHITE, star)

    # Draw player
    window.blit(player_image, player_rect)

    # Draw engine if moving
    if moving:
        engine_rect = engine_image.get_rect(midtop=player_rect.midbottom)
        window.blit(engine_image, engine_rect)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, bullet)

    # Draw enemies
    for enemy in enemies:
        window.blit(enemy_image, enemy)

    # Draw hearts
    for i in range(hearts):
        window.blit(heart_image, (10 + i * 35, WINDOW_SIZE[1] - 40))

    # Draw lives
    lives_text = font.render(f'Lives: {lives}', True, WHITE)
    window.blit(lives_text, (10, WINDOW_SIZE[1] - 80))

    # Draw score and level
    score_text = font.render(f'Score: {score}', True, WHITE)
    level_text = font.render(f'Level: {level}', True, WHITE)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (10, 50))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Close the SQLite connection
conn.close()

# Quit Pygame
pygame.quit()
sys.exit()
