from elements.field import Field
from elements.ship import Ship
from elements.missile import Missile

myGameField = Field(16)
myGameField.initField()

ship1 = Ship(3)
#ship2 = Ship(4)
#ship3 = Ship(5)
#ship4 = Ship(6)

myGameField.placeShip(ship1)
#myGameField.placeShip(ship2)
#myGameField.placeShip(ship3)
#myGameField.placeShip(ship4)

myGameField.printField()

while(myGameField.hasRemainingShips()):
	x = int(raw_input("Bitte X eingeben"))
	y = int(raw_input("Bitte Y eingeben"))

	missile = Missile(x,y)
	hit = myGameField.placeMissile(missile)

	if hit == True:
		print "Juhu getroffen"
	else:
		print "Leider nicht getroffen"

	myGameField.printField()

print 'Gewonnen!'
