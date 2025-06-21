import pygame
from pygame.locals import *
from User.define_user import User
from define_field import Field

class define_Display:
	def __init__(self):
		self.fullscreen = False
		self.displayDifference = 4 / 5
		self.DisplayWidth = round(User.ScreenWidth * self.displayDifference)
		self.DisplayHeight = round(User.ScreenHeight * self.displayDifference)
		if self.DisplayWidth <= self.DisplayHeight:
			self.DisplayOffset = [0, self.DisplayHeight - self.DisplayWidth]
		elif self.DisplayWidth > self.DisplayHeight:
			self.DisplayOffset = [self.DisplayWidth - self.DisplayHeight, 0]

		self.tabSize = int((self.DisplayHeight - self.DisplayOffset[1]) / 9)
		self.tileSize = int((self.DisplayHeight - self.DisplayOffset[1] - self.tabSize) / Field.height)
		if self.tileSize * Field.width > self.DisplayWidth:
			self.tileSize = int((self.DisplayWidth - self.DisplayOffset[1] - self.tabSize) / Field.width)
		self.tileOffset = [round((self.DisplayWidth - self.tileSize * Field.width) / 2), round((self.DisplayHeight - self.tileSize * Field.height - self.tabSize) / 2)]
		self.displayStats = False

		self.update_display(self.DisplayWidth, self.DisplayHeight, self.fullscreen)

	def update_display(self, DisplayWidth, DisplayHeight, fullscreen):
		if fullscreen == False:
			User.Display = pygame.display.set_mode((DisplayWidth, DisplayHeight), pygame.RESIZABLE)
		else:
			User.Display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		User.font = pygame.font.SysFont("impact", int(self.tileSize / 2))
		User.tabFont = pygame.font.SysFont("impact", int(self.tabSize / 2))

	def change_displaySize(self, width, height):
		self.DisplayWidth = width
		self.DisplayHeight = height
		if self.DisplayWidth < self.DisplayHeight:
			self.DisplayOffset = [0, self.DisplayHeight - self.DisplayWidth]
		elif self.DisplayWidth > self.DisplayHeight:
			self.DisplayOffset = [self.DisplayWidth - self.DisplayHeight, 0]

		self.tabSize = int((self.DisplayHeight - self.DisplayOffset[1]) / 9)
		self.tileSize = int((self.DisplayHeight - self.DisplayOffset[1] - self.tabSize) / Field.height)
		if self.tileSize * Field.width > self.DisplayWidth:
			self.tileSize = int((self.DisplayWidth - self.DisplayOffset[1] - self.tabSize) / Field.width)
		self.tileOffset = [round((self.DisplayWidth - self.tileSize * Field.width) / 2), round((self.DisplayHeight - self.tileSize * Field.height - self.tabSize) / 2)]

		self.update_display(self.DisplayWidth, self.DisplayHeight, self.fullscreen)
	
	def toggle_fullscreen(self):
		self.fullscreen = not self.fullscreen
		if self.fullscreen:
			self.change_displaySize(User.ScreenWidth, User.ScreenHeight)
		else:
			self.change_displaySize(round(User.ScreenWidth * self.displayDifference), round(User.ScreenHeight * self.displayDifference))

Display = define_Display()