import pygame
from pygame.locals import *
from User.define_user import User
from User.define_controls import Controls
from define_field import Field
from Display.define_display import Display

def udpate_FieldsearchPosition():
	mouseX, mouseY = pygame.mouse.get_pos()
	xPosition = int((mouseX - Display.tileOffset[0]) / Display.tileSize)
	yPosition = int((mouseY - Display.tileOffset[1] - Display.tabSize) / Display.tileSize)
	if xPosition < 0 or xPosition > Field.width - 1 or yPosition < 0 or yPosition > Field.height - 1:
		return
	if Field.groupSearch:
		Field.searchPositions = Field.get_searchPositions([xPosition, yPosition])
	else:
		Field.searchPositions = [[xPosition, yPosition]]

def event_handler():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and Field.playing == "playing":
			if event.button == 1:
				Field.update_displayField()
			if event.button == 3:
				displayField = Field.displayField
				flagPosition = Field.searchPositions[round(len(Field.searchPositions) / 2)]
				if not displayField[flagPosition[1]][flagPosition[0]] and Field.flagAmount != 0:
					displayField[flagPosition[1]][flagPosition[0]] = 2
					Field.flagAmount -= 1
				elif displayField[flagPosition[1]][flagPosition[0]] != 1:
					displayField[flagPosition[1]][flagPosition[0]] = 0
					Field.flagAmount += 1

		if event.type == pygame.KEYDOWN:
			if event.key == Controls.quitGame:
				User.playing = False
			
			if event.key in Controls.restartGame:
				Field.create_field()
			if event.key in Controls.togglegroupSearch:
				Field.groupSearch = True

			if event.key in Controls.changedisplayStats:
				Display.displayStats = 1 - Display.displayStats
			if event.key in Controls.fullscreen:
				Display.toggle_fullscreen()
		
		if event.type == pygame.KEYUP:
			if event.key in Controls.togglegroupSearch:
				Field.groupSearch = False

		if event.type == pygame.VIDEORESIZE:
			width, height = event.size
			Display.change_displaySize(width, height)
		if event.type == pygame.QUIT:
			User.playing = False
	
	udpate_FieldsearchPosition()
	Field.time += 1 / User.affectiveFPS
