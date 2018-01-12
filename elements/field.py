from elements.ship import Ship
import random

class Field:

	"""A class that represents the game field"""

	def __init__(self, fieldSize):
		self.fieldSize = fieldSize
		self.ships = []		
		self.missiles = []	

	def initField(self):
		self.fields = [pow(2, i) for i in range(pow(self.fieldSize, 2))]

	def printField(self):
		row = 0
		for i in range(self.fieldSize + 1):
			if i > 0 and i < 10:
				print ' {} '.format(i - 1),
			elif i > 9:
				print ' {}'.format(i - 1),
			else:
				print ' ',
		for i, val in enumerate(self.fields):
			if i % self.fieldSize == 0 :
				print
				print row,
				row += 1
			if self.isShipOnArea(val) and self.isMissileOnArea(val) == False:
				print '[o]',
			elif self.isShipOnArea(val) and self.isMissileOnArea(val):
				print '[x]',
			elif self.isShipOnArea(val) == False and self.isMissileOnArea(val):
				print '[-]',
			else:
				print '[ ]',
		print

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
