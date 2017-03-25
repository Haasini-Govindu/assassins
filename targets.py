# targets.py
# Python Script for handling the game data

from random import shuffle, randint

class Player:
	def __init__(self, name, number):
		self.name = name
		self.number = number # refers to phone number
		self.status = 'Alive'
		self.target = None
		self.secretCode = None	
		
	def __str__(self):
		return "%s - %s" %(self.name, self.status)
		
	def setTarget(self, target):
		self.target = target
		
	def setSecretCode(self, secretCode):
		self.secretCode = secretCode
		
	def getName(self):
		return "%s" %(self.name)
	
	def getTarget(self):
		return "%s" %(self.target)

class Game:
	def __init__(self):
		self.players = []

	def addPlayer(self, p):
		self.players.append(p)

	def assassinate(self, assassin, victim):
		print str(victim.getName()) + ' has been slain by ' + str(assassin.getName()) + '!'
		victim.status = 'Slain by ' + str(assassin.getName())
		assassin.target = victim.target
		victim.target = None
		
# player1 = Player('Ahri', '+18002221222')
# player2 = Player('Katarina', '+18002221222')
# player3 = Player('Kha\'zix', '+18002221222')
# player4 = Player('Rengar', '+18002221222')
# player5 = Player('Talon', '+18002221222')
# player6 = Player('Zed', '+18002221222')
# 
# players = [player1, player2, player3, player4, player5, player6]

	def printGameStatus(self):
		print '----------'
		for p in self.players:
			print p
		print '----------'

	def generateCode(self, n):
		string = ''
		for i in range(0, n):
			r = randint(0, 9)
			string += str(r)
		return string

	def startGame(self):
		shuffle(self.players)

		for n in range(0, len(self.players)-1):
			self.players[n].setSecretCode(generateCode(6))
			self.players[n].setTarget(self.players[n+1])
			print str(self.players[n].getName()) + ' is targeting ' + str(self.players[n].getTarget())

		self.players[len(self.players)-1].setTarget(self.players[0])
		print str(self.players[len(self.players)-1].getName()) + ' is targeting ' + str(self.players[len(self.players)-1].getTarget())
	
	
# assassinate(players[2], players[2].getTarget())
# assassinate(players[4], players[4].getTarget())
# printGameStatus()