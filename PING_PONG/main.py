import pygame as pg
import sys

W,H = 1000, 700

pg.init()
screen = pg.display.set_mode((W,H))
pg.display.set_caption("PING PONG")

clock = pg.time.Clock()
FPS = 30

class Sprite(pg.sprite.Sprite):
    def init(self, x, y, w, h, file):
        super.init()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    pg.display.update()
    clock.tick(FPS)