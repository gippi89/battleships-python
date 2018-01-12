from elements.field import Field
from elements.ship import Ship

myGameField = Field(8)
myGameField.initField()

ship1 = Ship(3)
ship2 = Ship(4)
ship3 = Ship(5)
ship4 = Ship(6)

myGameField.placeShip(ship1)
myGameField.placeShip(ship2)
myGameField.placeShip(ship3)
myGameField.placeShip(ship4)

myGameField.printField()
