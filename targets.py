# targets.py
# Python Script for handling the game data

from random import shuffle

class Player:
	def __init__(self, name, number):
		self.name = name
		self.number = number # refers to phone number
		self.status = 'Alive'
		self.target = None		
		
	def __str__(self):
# 		return "%s - %s" %(self.name, self.status)
		return "%s" %(self.name)
		
	def setTarget(self, target):
		self.target = target
		
	def getName(self):
		return self.name
	
	def getTarget(self):
		return self.target
		
player1 = Player('Ahri', '+18002221222')
player2 = Player('Katarina', '+18002221222')
player3 = Player('Kha\'zix', '+18002221222')
player4 = Player('Rengar', '+18002221222')
player5 = Player('Talon', '+18002221222')
player6 = Player('Zed', '+18002221222')

players = [player1, player2, player3, player4, player5, player6]

shuffle(players)

for n in range(0, len(players)-1):
	players[n].target = players[n+1]
players[len(players)-1].target = players[0]

for n in range(0, len(players)):
	print str(players[n]) + ' is targeting ' + str(players[n].target)