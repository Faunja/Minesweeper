# minesweeper.py
# By Kayden Campbell
# Copyright 2024
# Licensed under the terms of the GPL 3
# If pygame is not installed: sudo apt install python3-pygame
# To run: python3 ./minesweeper.py
import pygame, random, os
pygame.init()
DISPLAYSURF = pygame.display.get_desktop_sizes()
SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAYSURF[0]
SCREEN_HEIGHT = SCREEN_HEIGHT*3/4
cell_size = round(SCREEN_HEIGHT//16)
SCREEN_HEIGHT = SCREEN_HEIGHT//cell_size*cell_size+cell_size
screen = pygame.display.set_mode((SCREEN_HEIGHT - cell_size, SCREEN_HEIGHT))
grid_height = round((SCREEN_HEIGHT-cell_size)/cell_size)
grid = []
TOTAL_MINES = 0
def set_grid():
	global TOTAL_MINES
	if len(grid) != 0:
		grid.clear()
		TOTAL_MINES = 0
	for row in range(grid_height):
		grid.append([])
		for col in range(grid_height):
			minechance = random.randint(1, 10)
			if minechance == 1:
				grid[row].append(2)
				TOTAL_MINES += 1
			else:
				grid[row].append(1)
	while TOTAL_MINES < 24 or TOTAL_MINES > 40:
		if TOTAL_MINES < 32:
			for row in range(grid_height):
				for col in range(grid_height):
					minechance = random.randint(1, 10)
					if minechance == 1 and grid[row][col] == 1:
						grid[row][col] = 2
						TOTAL_MINES += 1
		else:
			for row in range(grid_height):
				for col in range(grid_height):
					minechance = random.randint(1, 10)
					if minechance != 1 and grid[row][col] == 2:
						grid[row][col] = 1
						TOTAL_MINES -= 1
def draw_grid(ended, TIME, control):
	flags = TOTAL_MINES
	hexed = 0
	for row in range(grid_height):
		hexed = 1 - hexed
		for col in range(grid_height):
			x = col * cell_size
			y = row * cell_size + cell_size
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_x = mouse_x//cell_size*cell_size
			mouse_y = mouse_y//cell_size*cell_size
			rect = pygame.Rect(x, y, cell_size, cell_size)
			flag = pygame.Rect(x+cell_size/7, y+cell_size/7, cell_size*(3/4), cell_size*(3/4))
			if grid[row][col] == 10:
				if hexed == 1:
					pygame.draw.rect(screen, (130, 130, 130), rect)
				else:
					pygame.draw.rect(screen, (105, 105, 105), rect)
			elif grid[row][col] == 11:
				if control == True:
					if mouse_x == x and mouse_y == y and ended == 0:
						pygame.draw.rect(screen, (80, 5, 0), rect)
					else:
						if hexed == 1:
							pygame.draw.rect(screen, (130, 55, 0), rect)
						else:
							pygame.draw.rect(screen, (105, 30, 0), rect)
				else:
					if hexed == 1:
						pygame.draw.rect(screen, (130, 55, 0), rect)
					else:
						pygame.draw.rect(screen, (105, 30, 0), rect)
				mines = 0
				for minirow in range(3):
					for minicol in range(3):
						minix, miniy = col-1+minicol, row-1+minirow
						if 0 <= minix < grid_height and 0 <= miniy < grid_height:
							if grid[miniy][minix] == 2 or grid[miniy][minix] == 12 or grid[miniy][minix] == 22:
								mines += 1
				font = pygame.font.Font('freesansbold.ttf', cell_size)
				text = font.render(str(mines), True, (0,0,0))
				textRect = text.get_rect()
				textRect.center = (x+cell_size/2, y+cell_size/2)
				screen.blit(text, textRect)
			elif grid[row][col] == 12:
				pygame.draw.rect(screen, (255, 0, 0), rect)
			else:
				if mouse_x == x and mouse_y == y and ended == 0:
					pygame.draw.rect(screen, (0, 55, 0), rect)
				else:
					if hexed == 1:
						pygame.draw.rect(screen, (0, 105, 0), rect)
					else:
						pygame.draw.rect(screen, (0, 80, 0), rect)
				if grid[row][col] == 21 or grid[row][col] == 22:
					pygame.draw.rect(screen, (155, 0, 0), flag)
					flags -= 1
			hexed = 1 - hexed
	font = pygame.font.Font('freesansbold.ttf', cell_size)
	text = font.render(str(flags)+" Flags", True, (255, 255, 255))
	textRect = text.get_rect()
	textRect.center = (cell_size*3, cell_size/2)
	screen.blit(text, textRect)
	if TIME<10 or TIME%60<10:
		if round(TIME/60)<10:
			text = font.render("0"+str(round(TIME/60))+":0"+str(TIME%60), True, (255, 255, 255))
		else:
			text = font.render(str(round(TIME/60))+":0"+str(TIME%60), True, (255, 255, 255))
	else:
		if round(TIME/60)<10:
			text = font.render("0"+str(round(TIME/60))+":"+str(TIME%60), True, (255, 255, 255))
		else:
			text = font.render(str(round(TIME/60))+":"+str(TIME%60), True, (255, 255, 255))
	textRect = text.get_rect()
	textRect.center = (cell_size*14, cell_size/2)
	screen.blit(text, textRect)
	if ended != 0:
		font = pygame.font.Font('freesansbold.ttf', cell_size*2)
		if ended == 1:
			text = font.render('You Win!', True, (0, 255, 0), (0, 0, 0))
			textRect = text.get_rect()
		else:
			text = font.render('You Lose!', True, (255, 0, 0), (0, 0, 0))
			textRect = text.get_rect()
		textRect.center = ((SCREEN_HEIGHT-cell_size)/2, SCREEN_HEIGHT/2)
		screen.blit(text, textRect)
def update_grid():
	for sweep in range(grid_height*grid_height):
		for row in range(grid_height):
			for col in range(grid_height):
				if grid[row][col] == 1:
					for minirow in range(3):
						for minicol in range(3):
							if 0 <= col-1+minicol < grid_height and 0 <= row-1+minirow < grid_height:
								if grid[row-1+minirow][col-1+minicol] == 10:
									grid[row][col] = 11
				if grid[row][col] == 11:
					cleared = 0
					offscreen = 0
					for minirow in range(3):
						for minicol in range(3):
							minix, miniy = col-1+minicol, row-1+minirow
							if 0 <= minix < grid_height and 0 <= miniy < grid_height:
								if grid[miniy][minix] == 1 or grid[miniy][minix] == 10 or grid[miniy][minix] == 11 or grid[miniy][minix] == 21:
									cleared += 1
							else:
								offscreen += 1
					if cleared+offscreen == 9:
						grid[row][col] = 10
def mine_grid():
	for row in range(grid_height):
		for col in range(grid_height):
			if grid[row][col] == 2 or grid[row][col] == 22:
				grid[row][col] = 12
def main():
	FPS = 24
	clock = pygame.time.Clock()
	run = True
	ended = 0
	TIME = 0
	first_click = True
	control = False
	reset = False
	set_grid()
	while run:
		clock.tick(FPS)
		if reset == True:
			ended = 0
			TIME = 0
			first_click = True
			reset = False
			set_grid()
		if ended == 0:
			TIME += 1
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run = False
				if event.key == pygame.K_LCTRL:
					control = True
				if event.key == pygame.K_r:
					reset = True
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LCTRL:
					control = False
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					col = x // cell_size
					row = (y - cell_size) // cell_size
					if 0 <= col < grid_height and 0 <= row < grid_height and ended == 0:
						if control == False:
							if grid[row][col] < 10 or grid[row][col] > 20:
								if event.button == 1 and grid[row][col] < 10:
									grid[row][col] += 10
									if first_click == True:
										if grid[row][col] == 12:
											grid[row][col] = 11
											newrow = random.randint(0, 15)
											newcol = random.randint(0, 15)
											while grid[newrow][newcol] == 2 or newrow == row and newcol == col:
												newrow = random.randint(0, 15)
												newcol = random.randint(0, 15)
											grid[newrow][newcol] = 2
										update_grid()
										first_click = False
									else:
										if grid[row][col] == 12:
											mine_grid()
											ended = 2
										else:
											update_grid()
											unmined = 0
											for minerow in range(grid_height):
												for minecol in range(grid_height):
													if grid[minerow][minecol] == 1 or grid[minerow][minecol] == 21:
														unmined += 1
											if unmined == 0:
												ended = 1
								elif event.button == 3:
									flags = 0
									for flagrow in range(grid_height):
										for flagcol in range(grid_height):
											if grid[flagrow][flagcol] == 2:
												flags += 1
											elif grid[flagrow][flagcol] == 21:
												flags -= 1
									if grid[row][col] > 20:
										grid[row][col] -= 20
									elif grid[row][col] < 20 and flags > 0:
										grid[row][col] += 20
						else:
							if event.button == 1:
								for minix in range(3):
									for miniy in range(3):
										minicol = col - 1 + minix
										minirow = row - 1 + miniy
										if 0 <= minicol < grid_height and 0 <= minirow < grid_height and ended == 0:
											if grid[minirow][minicol] < 10:
												grid[minirow][minicol] += 10
												if grid[minirow][minicol] == 12:
													mine_grid()
													ended = 2
												else:
													update_grid()
													unmined = 0
													for minerow in range(grid_height):
														for minecol in range(grid_height):
															if grid[minerow][minecol] == 1 or grid[minerow][minecol] == 21:
																unmined += 1
													if unmined == 0:
														ended = 1
		screen.fill((0,0,0))
		draw_grid(ended, round(TIME/FPS), control)
		pygame.display.update()
	pygame.quit()
main()
