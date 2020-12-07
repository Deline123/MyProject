import pygame as pg 

pg.init()


W, H = 800, 600

sc = pg.display.set_mode((W,H), pg.RESIZABLE)
pg.display.set_caption("Моя хернюшка")
pg.display.set_icon(pg.image.load("assassins.ico"))

FPS = 60
clock = pg.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


car_surf = pg.image.load("img/car.png").convert_alpha()
bg_surf = pg.image.load("img/sand.png").convert_alpha()


car_up = car_surf
car_down = pg.transform.flip(car_surf, 0, 1)
car_left = pg.transform.rotate(car_surf, 90)
car_Diag_left = pg.transform.rotate(car_surf, 45)
car_right = pg.transform.rotate(car_surf, -90)
car_Diag_right = pg.transform.rotate(car_surf, -45)


car_rect = car_surf.get_rect(center=(W//2, H//2))


car = car_up
speed = 5


flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False

	bt = pg.key.get_pressed()
	if bt[pg.K_LEFT]:
		car = car_left
		car_rect.x -= speed
		if car_rect.x < 0:
			car_rect.x = 0	


	elif bt[pg.K_RIGHT]:
		car = car_right
		car_rect.x += speed
		if car_rect.x > W - car_rect.height:
			car_rect.x = W - car_rect.height

	elif bt[pg.K_UP]:
		car = car_up
		car_rect.y -= speed
		if car_rect.y < 0:
			car_rect.y = 0

	elif bt[pg.K_DOWN]:
		car = car_down
		car_rect.y += speed
		if car_rect.y > H - car_rect.height:
			car_rect.y = H - car_rect.height		

	sc.blit(bg_surf, (0, 0))
	sc.blit(car, car_rect)
	pg.display.update()
	

	clock.tick(FPS)