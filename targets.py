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

import outgoing

class Game:
	def __init__(self, buyIn):
		self.players = []
		self.buyIn = buyIn
		self.acc = MasterAccount(self.buyIn)
		self.started = False

	# convert to strings before comparison?
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
			print str(p) + ' ' + str(self.acc.getBalance(p.get_id()))
		print '----------'
	
	def start(self):
		shuffle(self.players)
		for n in range(0, len(self.players)):
			self.players[n].setSecretCode(generateCode(6))
			self.players[n].set_id(self.acc.createAccount(self.players[n].getName()))
			self.players[n].setTarget(self.players[(n + 1) % len(self.players)])
			print str(self.players[n].getName()) + ' is targeting ' + str(self.players[n].getTarget())
			outgoing.start(self.players[n])
		self.started = True
	
	def leaderboard(self):
		ret = ''
		for player in self.players:
			ret += str(player) + ': $' + str(self.acc.getBalance(player.get_id())) + '\n'
		return ret
	
	def assassinationAttempt(self, assassin, code):
		if(not(assassin.getTarget()) or assassin.getTarget().secretCode != code):
			return False
		self.assassinate(assassin)
		return True

	# unused in christopher's code
# 	def assassinate_by_index(self, idx):
# # 		print self.players[idx].getTarget().getName() + ' has been slain by ' + self.players[idx].getName() + '!'
# # 		print '% has been slain by %!' %(victim.getName(), assassin.getName())
# 		self.players[idx].getTarget().setStatus('Slain by ' + self.players[idx].getName())
# 		victim = self.players[idx].getTarget()
# 		self.players[idx].target = self.players[idx].getTarget().target
# 		victim.target = None
# 		self.acc.transfer(victim.get_id(), self.players[idx])

	
	def assassinate(self, assassin):
		victim = assassin.getTarget()
		print str(victim.getName()) + ' has been slain by ' + str(assassin.getName()) + '!'
		victim.setStatus('Slain by ' + assassin.getName())
		victim.target = None
		self.acc.transfer(victim.get_id(), assassin)
		outgoing.killed(victim, self.acc.getBalance(victim.get_id()))
		if(len(filter(lambda player: player.status == 'Alive', self.players)) == 1):
			money = self.acc.getBalance(assassin.get_id())
			for player in self.players:
				outgoing.gameover(player, assassin, money)
			assassin.target = None
			# end game
		else:
			assassin.target = victim.target
	

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

# g = Game(5)
# g.addPlayer(Player('Ahri', '+18001111111'))
# g.addPlayer(Player('Katarina', '+18002221222'))
# g.addPlayer(Player('Kha\'zix', '+18003333333'))
# g.addPlayer(Player('Rengar', '+18004444444'))
# g.addPlayer(Player('Talon', '+18005555555'))
# g.addPlayer(Player('Zed', '+18006666666'))
# # g.printGameStatus()
# g.startGame()

# idx = g.findPlayer('+18002221222')

# g.assassinate(idx)
# # assassinate(players[4], players[4].getTarget())
# g.printGameStatus()
# g.printBalances()
