from elements.ship import Ship
from elements.fieldPrinter import FieldPrinter
import random

class Field:

	"""A class that represents the game field"""

	def __init__(self, fieldSize, name):
		self.fieldSize = fieldSize
		self.name = name
		self.ships = 0		
		self.missiles = 0	

	def initField(self):
		self.fields = [pow(2, i) for i in range(pow(self.fieldSize, 2))]
		self.fieldPrinter = FieldPrinter(self)

	def printFieldWithShips(self):
		self.fieldPrinter.printFieldWithShips()

	def printFieldWithoutShips(self):
		self.fieldPrinter.printFieldWithoutShips()

	def placeShip(self, ship):		
		while True:	
			areaToTry = self.getRandomShipAreaForSize(ship.size)
			if (self.isShipOnArea(areaToTry) == False):
				self.ships = self.ships | areaToTry
				return

	def placeMissile(self, missile):
		missileHit = 1 << missile.x << missile.y * self.fieldSize
		self.missiles = self.missiles | missileHit
		return self.isShipOnArea(missileHit)

	def getRandomShipAreaForSize(self, size):
                if random.randint(0, 10) % 2 == 0:
			return self.getHorizontalRandomShipAreaForSize(size)
                else:
			return self.getVerticalRandomShipAreaForSize(size)
	
	def getHorizontalRandomShipAreaForSize(self, size):
		areaToTry = 1 << random.randint(0, self.fieldSize - size) << (self.fieldSize * random.randint(0, self.fieldSize - 1))
		for i in range(size - 1):
			areaToTry = areaToTry | areaToTry << 1
		return areaToTry

	def getVerticalRandomShipAreaForSize(self, size):
		areaToTry = 1 << random.randint(0, pow(self.fieldSize, 2) - (size * self.fieldSize))
		for i in range(size - 1):
			areaToTry = areaToTry | areaToTry << self.fieldSize
		return areaToTry

	def hasRemainingShips(self):
		return (self.ships & self.missiles) != self.ships

	def isShipOnArea(self, area):
		return self.ships & area > 0

	def isMissileOnArea(self, area):
		return self.missiles & area > 0 
