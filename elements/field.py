from elements.ship import Ship
import random

class Field:

	"""A class that represents the game field"""

	def __init__(self, fieldSize):
		self.fieldSize = fieldSize
		self.ships = []		

	def initField(self):
		self.fields = [pow(2, i) for i in range(pow(self.fieldSize, 2))]

	def printField(self):
		for i, val in enumerate(self.fields):
			if i % self.fieldSize == 0 and i > 0:
				print
			if self.isShipOnArea(val):
				print '[x]',
			else:
				print '[ ]',
		print

	def placeShip(self, ship):		
		while True:	
			areaToTry = self.getRandomShipAreaForSize(ship.size)
			if (self.isShipOnArea(areaToTry) == False):
				self.ships.append(areaToTry)
				print "Ship has been placed to {}".format(str(bin(areaToTry))[2:])
				return

	def getRandomShipAreaForSize(self, size):

                if random.randint(0, 10) % 2 == 0:
			# Horizontal
			areaToTry = 1 << random.randint(0, self.fieldSize - size) << (self.fieldSize * random.randint(0, self.fieldSize - 1))
			for i in range(size - 1):
				areaToTry = areaToTry | areaToTry << 1
                else:
			#Vertical
                        areaToTry = 1 << random.randint(0, pow(self.fieldSize, 2) - (size * self.fieldSize))
                        for i in range(size - 1):
                                areaToTry = areaToTry | areaToTry << self.fieldSize
		return areaToTry

	def isShipOnArea(self, area):
		for ship in self.ships:
			if ship & area > 0:
				return True
		return False
