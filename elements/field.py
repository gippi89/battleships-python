from elements.ship import Ship

class Field:

	"""A class that represents the game field"""

	def __init__(self, fieldSize):
		self.fieldSize = fieldSize

	def initField(self):
		self.fields = [self.createFieldRowForIndex(i, self.fieldSize) for i in range(self.fieldSize)]

	def createFieldRowForIndex(self, index, rowSize):
		rowStartIndex = index * rowSize
		return [self.createFieldValueForField(rowStartIndex + i) for i in range(rowSize)]

	def createFieldValueForField(self, k):
		return pow(2, k)

	def printField(self):
		for i in self.fields:
			for j in i:
				print '[ ]',
			print

	def placeShip(self, ship):
		print 'New ship with size {} has been placed'.format(ship.size)
		print 'Free Areas: {}'.format(self.getFreeAreasForSize(ship.size))

	def getFreeAreasForSize(self, size):
		freeAreas = []
		for i in range(self.fields[-1][-1]):
			if i % size == 0:
				freeAreas.insert(i)
		return freeAreas
