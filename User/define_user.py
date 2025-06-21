import pygame, time
from pygame.locals import *

class define_User:
	def __init__(self):
		pygame.init()
		Display = pygame.display.get_desktop_sizes()
		self.ScreenWidth = Display[0][0]
		self.ScreenHeight = Display[0][1]

		self.FPS = 60 * 6
		self.affectiveFPS = self.FPS
		self.clock = pygame.time.Clock()
		self.playing = True

User = define_User()
