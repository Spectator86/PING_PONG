import pygame as pg
import sys
import random as rand

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

delay = 180

class GameSprite(pg.sprite.Sprite):
    def __init__(self, x, y, file):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

bot = GameSprite(W // 2, 100, "Images/platform.png")
player2 = GameSprite(W // 2, 600, "Images/platform.png")

Ball = GameSprite(W // 2, H // 2, "Images/Ball.png")

speedX = rand.randint(-5, 5)
speedY = rand.randint(-5, 5)

font1 = pg.font.Font(None, 35)

lose1 = font1.render("BOT (TOP) IS LOSER!", True, (255, 255, 255))
lose2 = font1.render("PLAYER (BOTTOM) IS LOSER!", True, (255, 255, 255))

finish = False

limit = 20

delay_end = False
count = 0

while True:
    screen.fill((0, 0, 0))
    bot.draw()
    player2.draw()
    Ball.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN and finish != True:
            if event.key == pg.K_LEFT:
                pressedA2 = True
            elif event.key == pg.K_RIGHT:
                pressedD2 = True
        elif event.type == pg.KEYUP and finish != True:
            if event.key == pg.K_LEFT:
                pressedA2 = False
            elif event.key == pg.K_RIGHT:
                pressedD2 = False
    bot.rect.x = Ball.rect.x - 35
    if pressedA2 == True and player2.rect.x >= 10:
        player2.rect.x -= speed
    elif pressedD2 == True and player2.rect.x + 100 <= W-10:
        player2.rect.x += speed

    if Ball.rect.x + 30 >= W:
        speedX *= -1
        if speedX <= limit and speedX > 0:
            speedX += 1
        if speedX <= limit and speedX < 0:
            speedX -= 1

    elif Ball.rect.x <= 0:
        speedX *= -1
        if speedX <= limit and speedX > 0:
            speedX += 1
        if speedX <= limit and speedX < 0:
            speedX -= 1

    if pg.sprite.collide_rect(bot, Ball) or pg.sprite.collide_rect(player2, Ball):
        speedY *= -1
        #if speedY <= limit and speedX > 0:
            #speedY += 1
        #if speedY <= limit and speedX < 0:
            #speedY -= 1

    
    if count >= delay:
        delay_end = True
    else:
        count += 1
    
    if delay_end:
        Ball.rect.x += speedX
        Ball.rect.y += speedY

    if Ball.rect.y + 30 < 0:
        screen.blit(lose1, (100, H // 2))
        finish = True
    elif Ball.rect.y + 30 > H:
        screen.blit(lose2, (500, H // 2))
        finish = True

    pg.display.update()
    clock.tick(FPS)
