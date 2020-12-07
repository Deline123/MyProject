import pygame as pg 

pg.init()

FPS = 60


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



W, H = 600, 400
sc = pg.display.set_mode((W,H), pg.RESIZABLE)
pg.display.set_caption("Моя хернюшка")
pg.display.set_icon(pg.image.load("assassins.ico"))
clock = pg.time.Clock()


surf = pg.Surface((W, 200))
bita = pg.Surface((50, 10))


surf.fill(BLUE)
bita.fill(RED)

bx, by = 0, 150
x, y = 0, 0


# x = W // 2
# y = H // 2
# speed = 5

# move = 0


# flLeft = flRight = False

#Цикл

# flStartDraw = False
# sp = ep = None
# sc.fill(WHITE)
# pg.display.update()


flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False
			
	surf.fill(BLUE)
	surf.blit(bita, (bx, by))
	if bx < W:
		bx += 5
	else:
		bx = 0

	if y < H:
		y += 1
	else:
		y = 0


	sc.fill(WHITE)
	sc.blit(surf, (x, y))
	pg.display.update()




		# elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
		# 	flStartDraw = True
		# 	sp = event.pos
		# elif event.type == pg.MOUSEMOTION:
		# 	if flStartDraw:
		# 		pos = event.pos

		# 		width = pos[0] - sp[0]
		# 		height = pos[1] - sp[1]

		# 		sc.fill(WHITE)
		# 		pg.draw.rect(sc, RED, (sp[0],sp[1], width, height))
		# 		pg.display.update()
		# elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
		# 	flStartDraw = False









#считывание клавиш с CTRL
	# 	elif event.type == pg.KEYDOWN:
	# 		if event.key == pg.K_LEFT and event.mod == pg.KMOD_LCTRL:
	# 			move = -speed
	# 		elif event.key == pg.K_RIGHT and event.mod == pg.KMOD_LCTRL:
	# 			move = speed
	# 	elif event.type == pg.KEYUP:
	# 		if event.key in [pg.K_LEFT, pg.K_RIGHT]:
	# 			move = 0
	# x += move

#Считывание клавиш
	# keys = pg.key.get_pressed()

	# if keys[pg.K_LEFT]:
	# 	x -= speed
	# elif keys[pg.K_RIGHT]:
	# 	x += speed


#Отрисовка
	# sc.fill(WHITE)
	# pg.draw.rect(sc, BLUE, (x, y, 10, 20))
	# pg.display.update()
			

	clock.tick(FPS)