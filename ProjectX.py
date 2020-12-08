import pygame as pg 
from ball import Ball
from random import randint

pg.init()
pg.time.set_timer(pg.USEREVENT, 2000)
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

balls_images = ['ball_bear.png','ball_fox.png','ball_panda.png']
balls_surf = [pg.image.load('img/images/'+ path).convert_alpha() for path in balls_images]

def createBall(group):
	indx = randint(0, len(balls_surf)-1)
	x = randint(20, W-20)
	speed = randint(1, 4)

	return Ball(x, speed, balls_surf[indx], group)


balls = pg.sprite.Group()

bg = pg.image.load("img/images/back1.jpg").convert()

speed = 1

createBall(balls)

flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False

		elif event.type == pg.USEREVENT:
			createBall(balls)
	sc.blit(bg, (0, 0))
	balls.draw(sc)
	pg.display.update()
	

	clock.tick(FPS)

	balls.update(H)

	