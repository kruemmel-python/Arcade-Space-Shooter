import pygame
import random
import sys
import time
from game_init import (
    initialize_pygame, create_window, set_caption, load_images, scale_images, 
    load_sounds, set_background_music, initialize_database, load_gif_frames
)
from game_logic import (
    create_star, move_player, shoot_bullet, move_bullets, 
    spawn_enemies, move_enemies, move_stars
)
from game_display import (
    draw_stars, draw_player, draw_engine, draw_bullets, draw_enemies, 
    draw_hearts, draw_lives, draw_score_and_level
)
from highscore_manager import show_highscores, get_player_name, choose_ship, save_highscore

def run_game():
    # Initialize Pygame
    initialize_pygame()

    # Set up display
    window_size = (800, 600)
    window = create_window(window_size)
    set_caption('Shooter Game')

    # Set up colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    # Load and scale images
    images, engine_image, heart_image = load_images()
    images = scale_images(images)

    # Load sounds
    hit_sound, shot_sound, death_sound = load_sounds()

    # Set background music volume
    set_background_music(0.5)

    # Initialize SQLite database
    conn, c = initialize_database()

    # Load GIF frames
    frames = load_gif_frames('data/intro.gif', window_size)

    # Show highscores before starting the game
    show_highscores(frames, window, pygame.font.SysFont(None, 36), yellow, red, blue, white, c)

    # Get player name
    player_name = get_player_name(window, pygame.font.SysFont(None, 36), black, white)

    # Choose player ship
    player_ship_key = choose_ship(window, pygame.font.SysFont(None, 36), black, white, images)
    player_image = images[player_ship_key]

    # Game variables
    running = True
    clock = pygame.time.Clock()
    score = 0
    level = 1
    lives = 3
    hearts = 5
    player_rect = player_image.get_rect(midbottom=(window_size[0] // 2, window_size[1] - 20))
    next_level_score = 50
    gun_speed = 10
    bullet_speed = 7
    enemy_speed = 1
    enemy_spawn_rate = 100
    bullets = []
    enemies = []
    stars = [create_star(window_size) for _ in range(100)]
    last_shot_time = time.time()
    start_time = time.time()

    def update_level():
        nonlocal level, enemy_speed, enemy_spawn_rate, next_level_score, lives
        level += 1
        lives += 1
        if level <= 20:
            enemy_speed += 1
            enemy_spawn_rate = max(10, enemy_spawn_rate - 1)
            next_level_score += 50
        else:
            level = 20

    def return_to_start_screen():
        nonlocal running, start_time, player_name, player_image
        elapsed_time = time.time() - start_time
        save_highscore(c, conn, player_name, score, level, elapsed_time)
        show_highscores(frames, window, pygame.font.SysFont(None, 36), yellow, red, blue, white, c)
        player_name = get_player_name(window, pygame.font.SysFont(None, 36), black, white)
        player_ship_key = choose_ship(window, pygame.font.SysFont(None, 36), black, white, images)
        player_image = images[player_ship_key]
        running = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return_to_start_screen()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return_to_start_screen()

        keys = pygame.key.get_pressed()
        moving = move_player(keys, player_rect, window_size, gun_speed)
        last_shot_time = shoot_bullet(keys, player_rect, bullets, bullet_speed, shot_sound, last_shot_time)
        move_bullets(bullets, bullet_speed)
        spawn_enemies(enemies, images, enemy_spawn_rate, window_size)
        score = move_enemies(enemies, enemy_speed, window_size, score)
        move_stars(stars, window_size)

        bullets_to_remove = []
        enemies_to_remove = []
        for enemy in enemies:
            enemy_rect, enemy_image = enemy
            for bullet in bullets:
                if enemy_rect.colliderect(bullet):
                    enemies_to_remove.append(enemy)
                    bullets_to_remove.append(bullet)
                    score += 1
                    hit_sound.play()

            if enemy_rect.colliderect(player_rect):
                enemies_to_remove.append(enemy)
                hearts -= 1
                death_sound.play()
                if hearts <= 0:
                    lives -= 1
                    hearts = 5
                    if lives <= 0:
                        return_to_start_screen()

        for bullet in bullets_to_remove:
            if bullet in bullets:
                bullets.remove(bullet)
        for enemy in enemies_to_remove:
            if enemy in enemies:
                enemies.remove(enemy)

        if score >= next_level_score:
            update_level()

        window.fill(black)
        draw_stars(window, stars, white)
        draw_player(window, player_image, player_rect)
        if moving:
            engine_rect = engine_image.get_rect(midtop=player_rect.midbottom)
            draw_engine(window, engine_image, engine_rect)
        draw_bullets(window, bullets, white)
        for enemy in enemies:
            enemy_rect, enemy_image = enemy
            window.blit(enemy_image, enemy_rect)
        draw_hearts(window, heart_image, hearts, window_size)
        draw_lives(window, pygame.font.SysFont(None, 36), lives, white, window_size)
        draw_score_and_level(window, pygame.font.SysFont(None, 36), score, level, white)

        pygame.display.flip()
        clock.tick(60)

    conn.close()
    pygame.quit()
    sys.exit()

while True:
    run_game()
