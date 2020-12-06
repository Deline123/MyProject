import pygame as pg 

pg.init()


W, H = 600, 400
sc = pg.display.set_mode((W,H), pg.RESIZABLE)
pg.display.set_caption("Моя хернюшка")
pg.display.set_icon(pg.image.load("assassins.ico"))
clock = pg.time.Clock()



FPS = 60


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (255, 0, 0)
RED = (255, 0, 0)


x = W // 2
y = H // 2
speed = 5

move = 0


flLeft = flRight = False

#Цикл

flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False

		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_LEFT and event.mod == pg.KMOD_LCTRL:
				move = -speed
			elif event.key == pg.K_RIGHT and event.mod == pg.KMOD_LCTRL:
				move = speed
		elif event.type == pg.KEYUP:
			if event.key in [pg.K_LEFT, pg.K_RIGHT]:
				move = 0
	x += move

#Считывание клавиш
	# keys = pg.key.get_pressed()

	# if keys[pg.K_LEFT]:
	# 	x -= speed
	# elif keys[pg.K_RIGHT]:
	# 	x += speed

	sc.fill(WHITE)
	pg.draw.rect(sc, BLUE, (x, y, 10, 20))
	pg.display.update()
			

	clock.tick(FPS)