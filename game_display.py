import pygame

def draw_stars(window, stars, color):
    """Zeichnet Sterne auf das Spielfenster."""
    for star in stars:
        pygame.draw.circle(window, color, star['rect'].center, 2)

def draw_player(window, player_image, player_rect):
    """Zeichnet das Spieler-Schiff."""
    window.blit(player_image, player_rect)

def draw_engine(window, engine_image, engine_rect):
    """Zeichnet das Triebwerk des Spieler-Schiffs."""
    window.blit(engine_image, engine_rect)

def draw_bullets(window, bullets, color):
    """Zeichnet die Kugeln."""
    for bullet in bullets:
        pygame.draw.rect(window, color, bullet)

def draw_enemies(window, enemies):
    """Zeichnet die Feinde."""
    for enemy in enemies:
        enemy_rect, enemy_image = enemy
        window.blit(enemy_image, enemy_rect)

def draw_hearts(window, heart_image, hearts, window_size):
    """Zeichnet die Herzen, die die Lebenspunkte darstellen."""
    for i in range(hearts):
        window.blit(heart_image, (10 + i * 35, window_size[1] - 40))

def draw_lives(window, font, lives, color, window_size):
    """Zeichnet die Anzahl der Leben."""
    lives_text = font.render(f'Lives: {lives}', True, color)
    window.blit(lives_text, (10, window_size[1] - 80))

def draw_score_and_level(window, font, score, level, score_color, level_color):
    """Zeichnet den aktuellen Punktestand und das Level."""
    score_text = font.render(f'Score: {score}', True, score_color)
    level_text = font.render(f'Level: {level}', True, level_color)
    window.blit(score_text, (10, 10))
    window.blit(level_text, (10, 50))

def draw_explosions(window, explosions, delta_time):
    """Zeichnet die Explosionen."""
    for explosion in explosions[:]:
        explosion['time'] += delta_time
        frame_index = int(explosion['time'] / 100) % len(explosion['frames'])
        frame = explosion['frames'][frame_index]
        frame_rect = frame.get_rect(center=explosion['position'])
        window.blit(frame, frame_rect)
        if explosion['time'] > len(explosion['frames']) * 100:
            explosions.remove(explosion)

def draw_power_ups(window, power_ups):
    """Zeichnet die Power-Ups."""
    for power_up in power_ups:
        power_up_rect, power_up_image, _ = power_up
        window.blit(power_up_image, power_up_rect)

def draw_active_power_ups(window, font, power_up_effects, window_size):
    """Zeichnet die aktiven Power-Ups und ihre verbleibende Dauer."""
    y_offset = 90
    for power_up, duration in power_up_effects.items():
        if duration > 0:
            minutes, seconds = divmod(duration // 1000, 60)
            duration_text = font.render(f'{power_up.capitalize()}: {int(minutes):02d}:{int(seconds):02d}', True, (255, 255, 255))
            window.blit(duration_text, (10, y_offset))
            y_offset += 40

def draw_boss(window, boss, boss_lives, boss_image):
    """Zeichnet den Boss-Gegner und seine Lebenspunkte."""
    window.blit(boss_image, boss)
    font = pygame.font.SysFont(None, 36)
    boss_lives_text = font.render(f'Boss Lives: {boss_lives}', True, (255, 0, 0))
    window.blit(boss_lives_text, (boss.x, boss.y - 30))
