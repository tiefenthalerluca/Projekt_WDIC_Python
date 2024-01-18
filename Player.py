import pygame as pg
from constants import *
from sound import Sound

class Player:

    def __init__(self, surface: pg.Surface):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.initial_pos = X_OFFSET, surface.get_height() - self.height
        self.images = [pg.image.load('bild1.png'),
                       pg.image.load('bild2.png'),
                       pg.image.load('bild3.png')]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=self.initial_pos)
        self.jumping = False
        self.velocity = 0
        self.sound = Sound()
        self.clock = pg.time.Clock()


    def show(self, surface: pg.Surface):
        surface.blit(self.image, self.rect)

    def update(self, dt):
        self.update_animation(dt)
        self.update_coords(dt)
        self.update_clock()

    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            current_pos = self.rect.topleft
            self.rect = self.image.get_rect(topleft=current_pos)

    def jump(self):
        if self.jumping:
            return
        self.jumping = True
        self.sound.play('jump')
        self.velocity = PLAYER_JUMP_FORCE

    def update_coords(self, dt):
        if self.jumping:
            self.rect.move_ip(0, -dt * self.velocity * PLAYER_JUMP_COEFFICIENT)
            self.velocity = self.velocity + dt * GRAVITY
            if self.rect.y > self.initial_pos[1]:
                self.rect.update(self.initial_pos[0], self.initial_pos[1],
                                 self.width, self.height)
                self.jumping = False

    def update_clock(self):
        self.clock.tick_busy_loop(60)
        dt = self.clock.get_time()
        pg.display.set_caption(f"FPS: {int(self.clock.get_fps())}")
        return dt
