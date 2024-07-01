import sqlite3
import pygame
import sys

def show_highscores(frames, window, font, yellow, red, blue, white, c):
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

        c.execute('SELECT * FROM highscores ORDER BY score DESC, level DESC, time ASC')
        highscores = c.fetchall()
        y = 50
        for hs in highscores:
            name_text = font.render(f'Name: {hs[0]}', True, yellow)
            score_text = font.render(f'Score: {hs[1]}', True, red)
            level_text = font.render(f'Level: {hs[2]}', True, blue)
            minutes, seconds = divmod(hs[3], 60)
            time_text = font.render(f'Time: {int(minutes):02d}:{int(seconds):02d}', True, white)
            window.blit(name_text, (50, y))
            window.blit(score_text, (250, y))
            window.blit(level_text, (450, y))
            window.blit(time_text, (650, y))
            y += 40

        frame_index = (frame_index + 1) % frame_count
        pygame.display.flip()
        pygame.time.delay(100)

def get_player_name(window, font, black, white):
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
        window.fill(black)
        prompt = font.render('Enter your name (3 letters): ' + name, True, white)
        window.blit(prompt, (50, 50))
        pygame.display.flip()
    return name

def choose_ship(window, font, black, white, images):
    selected_ship = 0
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_LEFT:
                    selected_ship = (selected_ship - 1) % 10
                elif event.key == pygame.K_RIGHT:
                    selected_ship = (selected_ship + 1) % 10
        window.fill(black)
        prompt = font.render('Choose your ship: ', True, white)
        window.blit(prompt, (50, 50))
        ship_image = images[f'player_{selected_ship + 1}']
        window.blit(ship_image, (400, 300))
        pygame.display.flip()
    return f'player_{selected_ship + 1}'

def save_highscore(c, conn, name, score, level, time):
    c.execute('INSERT INTO highscores (name, score, level, time) VALUES (?, ?, ?, ?)', (name, score, level, time))
    conn.commit()
