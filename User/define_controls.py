import pygame

class define_Controls:
	def __init__(self):
		self.quitGame = pygame.K_ESCAPE
		self.fullscreen = [pygame.K_F11, pygame.K_f]

		self.changedisplayStats = [pygame.K_F3, pygame.K_q]
		self.restartGame = [pygame.K_r]
		self.togglegroupSearch = [pygame.K_LCTRL]
		
		self.keypressed = []

Controls = define_Controls()
