import pygame as pg 

pg.init()


W, H = 600, 400

sc = pg.display.set_mode((W,H), pg.RESIZABLE)
pg.display.set_caption("Моя хернюшка")
pg.display.set_icon(pg.image.load("assassins.ico"))


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60
clock = pg.time.Clock()

ground = H-70
jump_force = 20
move = jump_force + 1

hero = pg.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx=(W//2))
rect.bottom = ground



flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_SPACE and ground == rect.bottom:
				move = -jump_force
			


	if move <= jump_force:
		if rect.bottom + move < ground:
			rect.bottom += move
			if move < jump_force:
				move += 1
		else:
			rect.bottom = ground
			move = jump_force + 1

	sc.fill(WHITE)
	sc.blit(hero, rect)
	pg.display.update()
		
	


	

	clock.tick(FPS)