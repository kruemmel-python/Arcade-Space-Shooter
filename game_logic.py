import random
import pygame
import time

def create_star(window_size):
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    return pygame.Rect(x, y, 2, 2)

def move_player(keys, player_rect, window_size, gun_speed):
    moving = False
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-gun_speed, 0)
        moving = True
    if keys[pygame.K_RIGHT] and player_rect.right < window_size[0]:
        player_rect.move_ip(gun_speed, 0)
        moving = True
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.move_ip(0, -gun_speed)
        moving = True
    if keys[pygame.K_DOWN] and player_rect.bottom < window_size[1]:
        player_rect.move_ip(0, gun_speed)
        moving = True
    return moving

def shoot_bullet(keys, player_rect, bullets, bullet_speed, shot_sound, last_shot_time):
    current_time = time.time()
    if keys[pygame.K_SPACE] and (current_time - last_shot_time) > 0.001:
        if len(bullets) < 5:
            bullet_rect = pygame.Rect(player_rect.centerx - 5, player_rect.top - 10, 10, 20)
            bullets.append(bullet_rect)
            shot_sound.play()
            last_shot_time = current_time
    return last_shot_time

def move_bullets(bullets, bullet_speed):
    for bullet in bullets[:]:
        bullet.move_ip(0, -bullet_speed)
        if bullet.bottom < 0:
            bullets.remove(bullet)

def spawn_enemies(enemies, images, enemy_spawn_rate, window_size):
    if random.randint(1, enemy_spawn_rate) == 1:
        enemy_index = random.randint(1, 10)
        enemy_image = images[f'enemy_{enemy_index}']
        enemy_rect = enemy_image.get_rect(topleft=(random.randint(0, window_size[0] - enemy_image.get_width()), 0))
        enemies.append((enemy_rect, enemy_image))

def move_enemies(enemies, enemy_speed, window_size, score):
    for enemy in enemies[:]:
        enemy_rect, enemy_image = enemy
        enemy_rect.move_ip(0, enemy_speed)
        if enemy_rect.top > window_size[1]:
            enemies.remove(enemy)
            score -= 1  # Penalty for missed enemy
    return score

def move_stars(stars, window_size):
    for star in stars[:]:
        star.move_ip(0, -1)
        if star.bottom < 0:
            stars.remove(star)
            stars.append(create_star(window_size))
