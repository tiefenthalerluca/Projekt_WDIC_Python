import random
import pygame as pg
from pygame import KEYDOWN
from pygame import constants
from Obstacle import Obstacle
from Player import Player
from constants import *

game_active = True
score = 0 

def game_over():
    global game_active
    game_active = False
    print('You lost! Your score: {}'.format(score))  

def main():
    pg.init()

    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    pg.display.set_caption("GDSC Dino")
    clock = pg.time.Clock()
    pg.mouse.set_visible(True)

    player = Player(screen)
    obstacles = []
    next_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)
    global game_active
    global score  
    while game_active:
        dt = clock.tick(fps) / 1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_active = False
                return
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
