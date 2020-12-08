import pygame as pg 
from ball import Ball
from random import randint

pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()
s_catch = pg.mixer.Sound("sounds/catch.ogg")

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

game_score = 0

telega = pg.image.load("img/images/telega.png").convert_alpha()
t_rect = telega.get_rect(centerx=W//2, bottom = H-5)


score = pg.image.load("img/images/score_fon.png").convert_alpha()
f = pg.font.SysFont("arial", 30)

balls_data = ({'path': 'ball_bear.png', 'score': 100},
			 {'path': 'ball_fox.png', 'score': 150},
			 {'path': 'ball_panda.png', 'score': 200})



balls_surf = [pg.image.load('img/images/'+ data["path"]).convert_alpha() for data in balls_data]

def createBall(group):
	indx = randint(0, len(balls_surf)-1)
	x = randint(20, W-20) 
	speed = randint(1, 4)

	return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)

def collideBalls():
	global game_score
	for ball in balls:
		if t_rect.collidepoint(ball.rect.center):
			s_catch.play()
			game_score += ball.score
			ball.kill()



balls = pg.sprite.Group()

bg = pg.image.load("img/images/back1.jpg").convert()

speed = 10

createBall(balls)


flRunning = True
while flRunning:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			flRunning = False

		elif event.type == pg.USEREVENT:
			createBall(balls)


	keys = pg.key.get_pressed()
	if keys[pg.K_LEFT]:
		t_rect.x -= speed
		if t_rect.x < 0:
			t_rect.x = 0

	elif keys[pg.K_RIGHT]:
		t_rect.x += speed
		if t_rect.x > W - t_rect.width:
			t_rect.x = W - t_rect.width





	collideBalls()
	sc.blit(bg, (0, 0))
	balls.draw(sc)
	sc.blit(score,(0, 0))
	sc_text = f.render(str(game_score), 1, (94, 138, 14))
	sc.blit(sc_text, (20, 10))
	sc.blit(telega, t_rect)

	pg.display.update()
	

	clock.tick(FPS)

	balls.update(H)

	