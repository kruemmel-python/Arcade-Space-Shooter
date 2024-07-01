import pygame


def draw_stars(window, stars, color):
    for star in stars:
        pygame.draw.rect(window, color, star)


def draw_player(window, player_image, player_rect):
    window.blit(player_image, player_rect)


def draw_engine(window, engine_image, engine_rect):
    window.blit(engine_image, engine_rect)


def draw_bullets(window, bullets, color):
    for bullet in bullets:
        pygame.draw.rect(window, color, bullet)


def draw_enemies(window, enemy_image, enemies):
    for enemy in enemies:
        window.blit(enemy_image, enemy)


def draw_hearts(window, heart_image, hearts, window_size):
    for i in range(hearts):
        window.blit(heart_image, (10 + i * 35, window_size[1] - 40))


def draw_lives(window, font, lives, color, window_size):
    lives_text = font.render(f'Lives: {lives}', True, color)
    window.blit(lives_text, (10, window_size[1] - 80))


def draw_score_and_level(window, font, score, level, color):
    score_text = font.render(f'Score: {score}', True, color)
    level_text = font.render(f'Level: {level}', True, color)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (10, 50))
