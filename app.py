from sys import exit
import os
from elements.field import Field
from elements.ship import Ship
from elements.missile import Missile

FIELD_SIZE = 16
ships = [Ship(2), Ship(2), Ship(2), Ship(3), Ship(3), Ship(4), Ship(4), Ship(8), Ship(8), Ship(12)]

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')

def playRound(player, enemie):
	cls()
	print enemie.name
	enemie.printFieldWithoutShips()
	print
	print player.name
	player.printFieldWithShips()
	
	x = int(raw_input('{} Bitte X eingeben '.format(player.name)))
	y = int(raw_input('{} Bitte Y eingeben '.format(player.name)))
	
	missile = Missile(x,y)
	hit = enemie.placeMissile(missile)

	if hit == True:
		print "Juhu getroffen"
	else:
		print "Leider nicht getroffen"

	if enemie.hasRemainingShips() == False:
		print '{} hat gewonnen!'.format(player.name)
		raw_input("Beenden")
		exit()
	raw_input("Weiter")
	cls()

def createPlayer(name):
	player = Field(FIELD_SIZE, name)
	player.initField()
	for ship in ships:
		player.placeShip(ship)
	return player

myGameFieldPlayer1 = createPlayer("Spieler 1")
myGameFieldPlayer2 = createPlayer("Spieler 2")

while(myGameFieldPlayer1.hasRemainingShips() and myGameFieldPlayer2.hasRemainingShips()):	
	playRound(myGameFieldPlayer1, myGameFieldPlayer2)
	playRound(myGameFieldPlayer2, myGameFieldPlayer1)	
