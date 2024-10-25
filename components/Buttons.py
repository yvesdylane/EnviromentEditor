import pygame

#button class
class Button():
	def __init__(self,x, y, image, scale):
		self.width = image.get_width()
		self.height = image.get_height()
		self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def update(self, change_h):
		self.rect.topleft = (self.rect.topleft[0], self.rect.topleft[1] + change_h)

	def draw(self, surface):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

class Layer():
	def __init__(self, x, y, image_list, scale, number):
		self.width = image_list[0].get_width()
		self.height = image_list[0].get_height()
		self.clicked = False
		self.image_list = image_list
		self.image = pygame.transform.scale(image_list[0], (int(self.width * scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.scale = scale
		self.x = x
		self.y = y
		self.active = False
		self.number = number


	def update(self):
		if self.active:
			self.image = pygame.transform.scale(self.image_list[1], (int(self.width * self.scale), int(self.height * self.scale)))
			self.rect = self.image.get_rect()
			self.rect.topleft = (self.x, self.y)
		else:
			self.image = pygame.transform.scale(self.image_list[0], (int(self.width * self.scale), int(self.height * self.scale)))
			self.rect = self.image.get_rect()
			self.rect.topleft = (self.x, self.y)

	def check_click(self, pos):
		return self.rect.collidepoint(pos)

	def draw(self, surface):
		action = False

		# get mouse position
		pos = pygame.mouse.get_pos()

		# check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		# draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action