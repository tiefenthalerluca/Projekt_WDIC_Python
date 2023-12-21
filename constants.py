import pygame as pg

# constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREENRECT = pg.rect.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
fps = 120
BG_RGB = [255, 255, 255]
SPAWN_MIN = 1
SPAWN_MAX = 5

# Player constants
PLAYER_JUMP_FORCE = 10
PLAYER_JUMP_COEFFICIENT = 50
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 100
X_OFFSET = 50
PLAYER_COLOR = (0, 0, 255)
GRAVITY = -10

# Obstacle constants
COLORS = [(0, 255, 0), (255, 0, 0)]
MIN_WIDTH = 50
MAX_WIDTH = 100
MIN_HEIGHT = 50
MAX_HEIGHT = 100
MIN_SPEED = 400
MAX_SPEED = 400
