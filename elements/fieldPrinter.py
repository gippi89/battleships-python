class FieldPrinter:

	"""A class that is able to print a game field to the console"""

	def __init__(self, field):
		self.field = field

	def printFieldWithShips(self):                                                              
		self.printField(True)

	def printFieldWithoutShips(self):
		self.printField(False)

	def printField(self, withShips):
		row = 0
		for i in range(self.field.fieldSize + 1):                                        
			if i > 0 and i < 10:                                               
				print(' {} '.format(i - 1),)
			elif i > 9:                                                        
				print(' {}'.format(i - 1),)                                
			else:
				print ('  ',)

		for i, val in enumerate(self.field.fields):                                      
			if i % self.field.fieldSize == 0 :
				print                                                      
				if row < 10:                                               
					print('{} '.format(row),)                           
				else:                                                      
					print(row,)                                         
				row += 1                                                   
			if self.field.isShipOnArea(val) and self.field.isMissileOnArea(val) == False and withShips == True:
				print('[o]',)                                               
			elif self.field.isShipOnArea(val) and self.field.isMissileOnArea(val):         
				print('[x]',)                                               
			elif self.field.isShipOnArea(val) == False and self.field.isMissileOnArea(val):
				print('[-]',)                                               
			else:                                                              
				print('[ ]',)                                               
		print

