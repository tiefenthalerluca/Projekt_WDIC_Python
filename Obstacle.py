import random
import pygame as pg
from constants import *

class Obstacle:

    def __init__(self, surface: pg.Surface, speed):
        self.width = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.height = random.randint(MIN_HEIGHT, MAX_HEIGHT)
        self.rect = pg.Rect(surface.get_width(), surface.get_height() -
                                 self.height, self.width,
                                 self.height)
        self.jumping = False
        self.velocity = 0
        self.color = random.choice(COLORS)
        self.speed = speed  # Set the obstacle speed based on the selected level

    def show(self, surface: pg.Surface):
        pg.draw.rect(surface, self.color, self.rect)

    def update_coords(self, dt):
        self.rect.move_ip(-self.speed * dt, 0)
