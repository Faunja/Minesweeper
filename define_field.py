import copy, random

class define_field:
	def create_field(self):
		self.displayField = []
		for row in range(self.height):
			self.displayField.append([])
			for column in range(self.width):
				self.displayField[row].append(0)
		self.mineField = copy.deepcopy(self.displayField)
		self.mineAmount = int((self.width * self.height) * (random.randint(100, 150) / 1000))
		if self.mineAmount <= 0:
			self.mineAmount = 1

		self.playing = "playing"
		self.firstClick = True
		self.groupSearch = False
		self.flagAmount = self.mineAmount
		self.time = 0

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.create_field()
		self.searchPositions = [[0, 0]]

	def number_tiles(self, position):
		for row in range(-1, 2):
			if position[1] + row < 0 or position[1] + row > self.height - 1:
				continue
			for column in range(-1, 2):
				if position[0] + column < 0 or position[0] + column > self.width - 1:
					continue
				if not row and row == column:
					continue
				if self.mineField[position[1] + row][position[0] + column] != 9:
					self.mineField[position[1] + row][position[0] + column] += 1

	def plant_mines(self, avoidPosition = [-2, -2]):
		avoidPositions = []
		for x in range(-1, 2):
			for y in range(-1, 2):
				avoidPositions.append([avoidPosition[0] + x, avoidPosition[1] + y])
		for mine in range(self.mineAmount):
			plantedMine = False
			while not plantedMine:
				position = [random.randrange(self.width), random.randrange(self.height)]
				if not random.randint(0, self.mineAmount) and position not in avoidPositions:
					self.mineField[position[1]][position[0]] = 9
					self.number_tiles(position)
					avoidPositions.append(position)
					plantedMine = True


	def expose_mines(self):
		for row in range(self.height):
			for column in range(self.width):
				if self.mineField[row][column] == 9:
					self.displayField[row][column] = 1

	def check_field(self):
		for row in range(self.height):
			for column in range(self.width):
				if self.mineField[row][column] != 9 and self.displayField[row][column] == 0:
					return False
		return True

	def get_searchPositions(self, position):
		searchPositions = []
		for y in range(-1, 2):
			if y + position[1] < 0 or y + position[1] > self.height - 1:
				continue
			for x in range(-1, 2):
				if x + position[0] < 0 or x + position[0] > self.width - 1:
					continue
				searchPositions.append([x + position[0], y + position[1]])
		return searchPositions

	def update_displayField(self):
		show = []
		displayField = self.displayField
		middlesearchPosition = self.searchPositions[round(len(self.searchPositions) / 2)]
		if self.firstClick and displayField[middlesearchPosition[1]][middlesearchPosition[0]] != 2:
			self.plant_mines(middlesearchPosition)
			self.firstClick = False
		if not self.firstClick:
			for searchPosition in self.searchPositions:
				if self.mineField[searchPosition[1]][searchPosition[0]] == 0:
					show.append(searchPosition)
				elif self.displayField[searchPosition[1]][searchPosition[0]] != 2:
					displayField[searchPosition[1]][searchPosition[0]] = 1
					if self.mineField[searchPosition[1]][searchPosition[0]] == 9:
						self.expose_mines()
						self.playing = "lost"
		while len(show):
			for tile in copy.deepcopy(show):
				displayField[tile[1]][tile[0]] = 1
				for row in range(-1, 2):
					if tile[1] + row < 0 or tile[1] + row > self.height - 1:
						continue
					for column in range(-1, 2):
						if tile[0] + column < 0 or tile[0] + column > self.width - 1:
							continue
						if displayField[tile[1] + row][tile[0] + column] != 1:
							if self.mineField[tile[1] + row][tile[0] + column] == 0 and [tile[0] + column, tile[1] + row] not in show:
								show.append([tile[0] + column, tile[1] + row])
							else:
								displayField[tile[1] + row][tile[0] + column] = 1
				show.remove(tile)
		if self.check_field():
			self.playing = "won"

Field = define_field(15, 15)