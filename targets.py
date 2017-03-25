# targets.py
# Python Script for handling the game data

from random import shuffle, randint

import outgoing

class Game:
	def __init__(self):
		self.players = []
		self.started = False

	def findPlayer(self, number):
		ll = filter(lambda player: player.number == number, self.players)
		if(len(ll) == 1):
			return ll[0]
		return None
	
	def addPlayer(self, player):
		self.players.append(player)
	
	def printStatus(self):
		print '----------'
		for p in self.players:
			print p
		print '----------'
	
	def start(self):
		shuffle(self.players)
		for n in range(0, len(self.players)):
			self.players[n].setSecretCode(generateCode(6))
			self.players[n].setTarget(self.players[(n + 1) % len(self.players)])
			print str(self.players[n].getName()) + ' is targeting ' + str(self.players[n].getTarget())
			outgoing.start(self.players[n])
	
	def leaderboard(self):
		ret = ''
		for player in self.players:
			ret += str(player) + '\n'
		return ret
	
	def assassinationAttempt(self, assassin, code):
		if(assassin.target.secretCode != code):
			return False
		self.assassinate(assassin, assassin.target)
		return True
	
	def assassinate(self, assassin, victim):
		print str(victim.getName()) + ' has been slain by ' + str(assassin.getName()) + '!'
		victim.status = 'Slain by ' + str(assassin.getName())
		assassin.target = victim.target
		victim.target = None
		outgoing.killed(victim)
		if(len(filter(lambda player: player.status == 'Alive', self.players)) == 1):
			for player in self.players:
				outgoing.gameover(player, assassin)
			# end game
	

class Player:
	def __init__(self, name, number):
		self.name = name
		self.number = number # refers to phone number
		self.status = 'Alive'
		self.target = None
		self.secretCode = None
		
	def __str__(self):
		return "%s - %s" %(self.name, self.status)
# 		return "%s" %(self.name)
		
	def setTarget(self, target):
		self.target = target
		
	def setSecretCode(self, secretCode):
		self.secretCode = secretCode
		
	def getName(self):
		return "%s" %(self.name)
	
	def getTarget(self):
		return "%s" %(self.target.name)
		
# player1 = Player('Ahri', '+18002221222')
# player2 = Player('Katarina', '+18002221222')
# player3 = Player('Kha\'zix', '+18002221222')
# player4 = Player('Rengar', '+18002221222')
# player5 = Player('Talon', '+18002221222')
# player6 = Player('Zed', '+18002221222')

# players = [player1, player2, player3, player4, player5, player6]

def generateCode(n):
	string = ''
	for i in range(0, n):
		r = randint(0, 9)
		string += str(r)
	return string

def go():
	assassinate(players[2], players[2].getTarget())
	assassinate(players[4], players[4].getTarget())

	printGameStatus()
