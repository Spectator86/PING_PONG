import pygame as pg
import sys

W,H = 1000, 700

pg.init()
screen = pg.display.set_mode((W,H))
pg.display.set_caption("PING PONG")

clock = pg.time.Clock()
FPS = 60

pressedA1 = False
pressedD1 = False

pressedA2 = False
pressedD2 = False

speed = 15

class Block(pg.sprite.Sprite):
    def __init__(self, x, y, file):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, file):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load(file).convert_alpha(), (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

player1 = Block(W // 2, 600, "Images/platform.png")
player2 = Block(W // 2, 100, "Images/platform.png")

Ball = Block(W // 2, H // 2, "Images/Ball.png")

while True:
    screen.fill((0, 0, 0))
    player1.draw()
    player2.draw()
    Ball.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                pressedA1 = True
            elif event.key == pg.K_d:
                pressedD1 = True
            if event.key == pg.K_LEFT:
                pressedA2 = True
            elif event.key == pg.K_RIGHT:
                pressedD2 = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_a:
                pressedA1 = False
            elif event.key == pg.K_d:
                pressedD1 = False
            if event.key == pg.K_LEFT:
                pressedA2 = False
            elif event.key == pg.K_RIGHT:
                pressedD2 = False
    if pressedA1 == True and player1.rect.x >= 10:
        player1.rect.x -= speed
    elif pressedD1 == True and player1.rect.x + 100 <= 990:
        player1.rect.x += speed
    if pressedA2 == True and player2.rect.x >= 10:
        player2.rect.x -= speed
    elif pressedD2 == True and player2.rect.x + 100 <= 990:
        player2.rect.x += speed

    pg.display.update()
    clock.tick(FPS)
