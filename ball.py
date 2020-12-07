import pygame

class Ball(pygame.sprite.Sprite):
	def __init__(self, x, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename).convert_alpha()
		self.rect = self.image.get_rect(center=(x, 0))
		self.speed = speed
		
	def update(self, *args):
		if self.rect.y < args[0] - 20:
			self.rect.y += self.speed
		else:
			self.rect.y = 0