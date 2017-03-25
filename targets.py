# targets.py
# Python Script for handling the game data

class Player:
	def __init__(self, name, number, status):
		self.name = name
		self.number = number # refers to phone number
		self.status = 1
		self.target = None		
		
	def setTarget(self, target):
		self.target = target
		
player1 = Player('Ahri', '+18002221222')
player2 = Player('Katarina', '+18002221222')
player3 = Player('Kha\'zix', '+18002221222')
player4 = Player('Rengar', '+18002221222')
player5 = Player('Talon', '+18002221222')
player6 = Player('Zed', '+18002221222')

players = [player1, player2, player3, player4, player5, player6]

