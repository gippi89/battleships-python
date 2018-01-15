from elements.ship import Ship
from elements.fieldPrinter import FieldPrinter
import random

class Field:

	"""A class that represents the game field"""

	def __init__(self, fieldSize):
		self.fieldSize = fieldSize
		self.ships = []		
		self.missiles = []	

	def initField(self):
		self.fields = [pow(2, i) for i in range(pow(self.fieldSize, 2))]
		self.fieldPrinter = FieldPrinter(self)

	def printField(self):
		self.fieldPrinter.printField()

	def placeShip(self, ship):		
		while True:	
			areaToTry = self.getRandomShipAreaForSize(ship.size)
			if (self.isShipOnArea(areaToTry) == False):
				self.ships.append(areaToTry)
				return

	def placeMissile(self, missile):
		missileHit = 1 << missile.x << missile.y * self.fieldSize
		self.missiles.append(missileHit)
		return self.isShipOnArea(missileHit)

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

	def hasRemainingShips(self):
		allShips = 0
		allMissiles = 0
		for ship in self.ships:
			allShips = allShips | ship
		for missile in self.missiles:
			allMissiles = allMissiles | missile
		return (allShips & allMissiles) != allShips

	def isShipOnArea(self, area):
		for ship in self.ships:
			if ship & area > 0:
				return True
		return False

	def isMissileOnArea(self, area):
		for missile in self.missiles:
			if missile & area > 0:
				return True
		return False
