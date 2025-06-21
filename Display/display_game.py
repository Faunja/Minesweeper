import pygame
from pygame.locals import *
from User.define_user import User
from Display.define_display import Display
from define_field import Field

def stat_text(text, position, color = (255, 255, 255)):
	text = User.font.render(text, True, color)
	width, height = text.get_size()
	User.Display.blit(text, (position[0] * width, position[1] * height))

def display_stats():
	if User.affectiveFPS < 40:
		stat_text("FPS: "+str(int(User.affectiveFPS)), [0, 0], (255, 60, 60))
		return
	stat_text("FPS: "+str(int(User.affectiveFPS)), [0, 0], (60, 255, 60))

def mine_text(number, position, color = (0, 0, 0)):
	text = User.font.render(str(number), True, color)
	width, height = text.get_size()
	printPosition = (position[0] - .5 * width, position[1] - .5 * height)
	User.Display.blit(text, printPosition)

def display_tile(tile, mineTile, tileSize, xPosition, yPosition, color):
	if tile == 1:
		if mineTile != 0:
			if mineTile == 9:
				pygame.draw.rect(User.Display,  (255 - color, 30 - color, 30 - color), (xPosition, yPosition, tileSize, tileSize))
			else:
				pygame.draw.rect(User.Display,  (180 - color, 165 - color, 75 - color), (xPosition, yPosition, tileSize, tileSize))
				mine_text(mineTile, [xPosition + int(tileSize / 2), yPosition + int(tileSize / 2)], (30 - color, 30 - color, 0))
		else:
			pygame.draw.rect(User.Display,  (195 - color, 180 - color, 90 - color), (xPosition, yPosition, tileSize, tileSize))
	elif tile == 2:
		pygame.draw.rect(User.Display,  (30 - color, 30 - color, 30 - color), (xPosition, yPosition, tileSize, tileSize))
	else:
		pygame.draw.rect(User.Display,  (30 - color, 30 - color, 255 - color), (xPosition, yPosition, tileSize, tileSize))

def display_field():
	tileSize = Display.tileSize
	offset = (Display.tileOffset[0], Display.tileOffset[1] + Display.tabSize)
	displayField = Field.displayField
	mineField = Field.mineField
	searchPositions = Field.searchPositions
	for y in range(Field.height):
		yPosition = y * tileSize + offset[1]
		for x in range(Field.width):
			xPosition = x * tileSize + offset[0]
			color = int(x % 2 == y % 2) * 3
			if [x, y] in searchPositions:
				if mineField[y][x] or not displayField[y][x]:
					color = int([x, y] in searchPositions) * 5
			display_tile(displayField[y][x], mineField[y][x], tileSize, xPosition, yPosition, color)

def tab_text(text, position, color = (255, 255, 255)):
	text = User.tabFont.render(text, True, color)
	width, height = text.get_size()
	printPosition = (position[0] - .5 * width, position[1] - .5 * height)
	User.Display.blit(text, printPosition)

def display_tab():
	if Field.playing == "playing":
		tab_text("Searching", (Display.DisplayWidth / 2, Display.DisplayOffset[1] + Display.tileOffset[1] + int(Display.tabSize / 2)))
		offset = int(Display.tileSize * Field.width / 4 + Display.tileSize / 4)
		tab_text(str(Field.flagAmount), (Display.DisplayWidth / 2 - offset, Display.DisplayOffset[1] + Display.tileOffset[1] + int(Display.tabSize / 2)))
		displayTime = str(int(Field.time % 60))
		if Field.time >= 60:
			if Field.time % 60 < 10:
				displayTime = str(int(Field.time / 60))+":0"+displayTime
			else:
				displayTime = str(int(Field.time / 60))+":"+displayTime
		tab_text(str(displayTime), (Display.DisplayWidth / 2 + offset, Display.DisplayOffset[1] + Display.tileOffset[1] + int(Display.tabSize / 2)))
	if Field.playing == "won":
		tab_text("You Win!", (Display.DisplayWidth / 2, Display.DisplayOffset[1] + Display.tileOffset[1] + int(Display.tabSize / 2)), (60, 255, 60))
	if Field.playing == "lost":
		tab_text("You Lose!", (Display.DisplayWidth / 2, Display.DisplayOffset[1] + Display.tileOffset[1] + int(Display.tabSize / 2)), (255, 60, 60))

def display_game():
	pygame.draw.rect(User.Display, (0, 0, 0), (0, 0, Display.DisplayWidth, Display.DisplayHeight))
	display_tab()
	display_field()
	if Display.displayStats:
		display_stats()
