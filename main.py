import random
import pygame as pg
from pygame import KEYDOWN
from pygame import constants
from Obstacle import Obstacle
from Player import Player
from constants import *

game_active = False
score = 0 

def game_over():
    global game_active
    game_active = False
    print('You lost! Your score: {}'.format(score))  

def main_menu(screen):
    font = pg.font.Font(None, 36)
    play_button = pg.Rect(50, 200, 200, 50)
    close_button = pg.Rect(50, 300, 200, 50)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return True
                elif close_button.collidepoint(event.pos):
                    pg.quit()
                    quit()

        screen.fill(BG_RGB)
        pg.draw.rect(screen, (0, 255, 0), play_button)
        pg.draw.rect(screen, (255, 0, 0), close_button)

        play_text = font.render("Play", True, (255, 255, 255))
        close_text = font.render("Close", True, (255, 255, 255))

        screen.blit(play_text, (play_button.x + 50, play_button.y + 15))
        screen.blit(close_text, (close_button.x + 50, close_button.y + 15))

        pg.display.flip()

def main():
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("GDSC Dino")
    clock = pg.time.Clock()
    pg.mouse.set_visible(True)

    global game_active
    global score  

    while True:
        if not game_active:
            game_active = main_menu(screen)
            if not game_active:
                return

        player = Player(screen)
        obstacles = []
        next_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)

        while game_active:
            dt = clock.tick(fps) / 1000.0

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    game_active = False
                if event.type == KEYDOWN:
                    if event.key == constants.K_SPACE:
                        player.jump()

            next_spawn -= dt
            if next_spawn <= 0:
                obstacles.append(Obstacle(screen))
                next_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)

            screen.fill(BG_RGB)
            player.show(screen)
            player.update_coords(dt)

            for obstacle in obstacles:
                if obstacle.rect.right <= 0:
                    obstacles.remove(obstacle)
                    score += 1  
                obstacle.update_coords(dt)
                obstacle.show(screen)

            if player.rect.collidelist([obstacle.rect for obstacle in obstacles]) != -1:
                game_over()

            pg.display.update()

if __name__ == "__main__":
    main()
    pg.quit()
