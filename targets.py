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
		return "%s - %s" %(self.name, self.status)
# 		return "%s" %(self.name)
		
	def setTarget(self, target):
		self.target = target
		
	def getName(self):
		return "%s" %(self.name)
	
	def getTarget(self):
		return self.target
		
def assassinate(assassin, victim):
	print str(victim.getName()) + ' has been slain by ' + str(assassin.getName()) + '!'
	victim.status = 'Slain by ' + str(assassin.getName())
	assassin.target = victim.target
	victim.target = None
		
player1 = Player('Ahri', '+18002221222')
player2 = Player('Katarina', '+18002221222')
player3 = Player('Kha\'zix', '+18002221222')
player4 = Player('Rengar', '+18002221222')
player5 = Player('Talon', '+18002221222')
player6 = Player('Zed', '+18002221222')

players = [player1, player2, player3, player4, player5, player6]

def printGameStatus():
	print '----------'
	for p in players:
		print p
	print '----------'

shuffle(players)

for n in range(0, len(players)-1):
	players[n].target = players[n+1]
players[len(players)-1].target = players[0]

for n in range(0, len(players)):
	print str(players[n].getName()) + ' is targeting ' + str(players[n].target.getName())
	
assassinate(players[2], players[2].target)
assassinate(players[4], players[4].target)
		
printGameStatus()