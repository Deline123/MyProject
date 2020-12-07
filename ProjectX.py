import pygame as pg 
from ball import Ball

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

W, H = 1000, 570

sc = pg.display.set_mode((W,H))
pg.display.set_caption("Моя хернюшка")
pg.display.set_icon(pg.image.load("assassins.ico"))

clock = pg.time.Clock()
FPS = 60

bg = pg.image.load("img/bg.png")

speed = 1
b1 = Ball(W//2, speed, "img/ball.png")



flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False
	sc.blit(bg, (0, 0))
	sc.blit(b1.image, b1.rect)
	pg.display.update()
	

	clock.tick(FPS)

	b1.update(H)

	