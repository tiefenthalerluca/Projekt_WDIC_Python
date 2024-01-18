# scoreboard.py
import pygame as pg
from constants import *

class Scoreboard:

    def __init__(self, font_size=36):
        self.score = 0
        self.font = pg.font.Font(None, font_size)

    def increase_score(self, value=1):
        self.score += value

    def reset_score(self):
        self.score = 0

    def show(self, surface: pg.Surface):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        surface.blit(score_text, (10, 10))
