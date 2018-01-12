from elements.field import Field
from elements.ship import Ship

myGameField = Field(16)
myGameField.initField()
#myGameField.printField()

ship1 = Ship(4)

myGameField.placeShip(ship1)
