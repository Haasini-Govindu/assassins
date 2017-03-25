# targets.py
# Python Script for handling the game data

from random import shuffle, randint
from nessie import MasterAccount

def generateCode(n):
	string = ''
	for i in range(0, n):
		r = randint(0, 9)
		string += str(r)
	return string

class Player:
	def __init__(self, name, number):
		self.name = name
		self.number = number # refers to phone number
		self.status = 'Alive'
		self.target = None
		self.secretCode = None
		self._id = None
		
	def __str__(self):
		return "%s - %s" %(self.name, self.status)
		
	def setTarget(self, target):
		self.target = target
		
	def setSecretCode(self, secretCode):
		self.secretCode = secretCode
		
	def set_id(self, _id):
		self._id = _id
		
	def setStatus(self, newStatus):
		self.status = newStatus
		
	def getName(self):
		return "%s" %(self.name)
	
	def getTarget(self):
		return self.target

	def get_id(self):
		return self._id
		
	def getNumber(self):
		return "%s" %self.number

class Game:
	def __init__(self, buyIn):
		self.players = []
		self.buyIn = buyIn

	def addPlayer(self, p):
		self.players.append(p)

	def assassinate(self, idx):
# 		print self.players[idx].getTarget().getName() + ' has been slain by ' + self.players[idx].getName() + '!'
# 		print '% has been slain by %!' %(victim.getName(), assassin.getName())
		self.players[idx].getTarget().setStatus('Slain by ' + self.players[idx].getName())
		self.players[idx].target = self.players[idx].getTarget().target
		self.players[idx].target = None
		
	def findPlayer(self, number):
		n = 0
		for p in self.players:
			if (str(p.getNumber()) == str(number)):
				return n
			n += 1
		
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

	def startGame(self):
		acc = MasterAccount()
		shuffle(self.players)

		for n in range(0, len(self.players)-1):
			self.players[n].setSecretCode(generateCode(6))
			self.players[n].set_id(acc.createAccount(self.players[n].getName()))
			self.players[n].setTarget(self.players[n+1])
# 			print str(self.players[n].getName()) + ' is targeting ' + str(self.players[n].getTarget())
		
		self.players[len(self.players)-1].setSecretCode(generateCode(6))
		self.players[len(self.players)-1].set_id(acc.createAccount(self.players[len(self.players)-1].getName()))
		self.players[len(self.players)-1].setTarget(self.players[0])
# 		print str(self.players[len(self.players)-1].getName()) + ' is targeting ' + str(self.players[len(self.players)-1].getTarget())
	
g = Game(5)
g.addPlayer(Player('Ahri', '+18001111111'))
g.addPlayer(Player('Katarina', '+18002221222'))
g.addPlayer(Player('Kha\'zix', '+18003333333'))
g.addPlayer(Player('Rengar', '+18004444444'))
g.addPlayer(Player('Talon', '+18005555555'))
g.addPlayer(Player('Zed', '+18006666666'))
g.printGameStatus()
g.startGame()

idx = g.findPlayer('+18002221222')

g.assassinate(idx)
# assassinate(players[4], players[4].getTarget())
g.printGameStatus()