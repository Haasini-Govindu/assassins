# targets.py
# Python Script for handling the game data

from random import shuffle, randint
from nessie import MasterAccount

from database import db

import outgoing

def generateCode(n):
	string = ''
	for i in range(0, n):
		r = randint(0, 9)
		string += str(r)
	return string

class Game(db.Model):
	code = db.Column(db.String(5), primary_key=True)
	players = db.relationship('Player', backref='game', lazy='dynamic')
	buyIn = db.Column(db.Float)
	started = db.Column(db.Boolean)
	completed = db.Column(db.Boolean)
	
	# def __init__(self, buyIn):
	# 	self.acc = MasterAccount(self.buyIn)

	# convert to strings before comparison?
	def findPlayer(self, number):
		ll = filter(lambda player: player.number == number, self.players)
		if(len(ll) == 1):
			return ll[0]
		return None
	
	def addPlayer(self, player):
		self.players.append(player)
	
	def printStatus(self):
		acc = MasterAccount(self.buyIn)
		print '----------'
		for p in self.players:
			print p.string() + ' ' + str(acc.getBalance(p.bankId))
		print '----------'
	
	def start(self):
		players = self.players.all()
		shuffle(players)
		acc = MasterAccount(self.buyIn)
		for n in range(0, len(players)):
			players[n].status = 'Alive'
			players[n].secretCode = generateCode(6)
			players[n].bankId = acc.createAccount(players[n].name)
			players[n].target = players[(n + 1) % len(players)]
			print players[n].name + ' is targeting ' + players[n].target.name
			outgoing.start(players[n])
		self.started = True
	
	def leaderboard(self):
		acc = MasterAccount(self.buyIn)
		ret = ''
		for player in self.players:
			ret += player.string() + ': $' + str(acc.getBalance(player.bankId)) + '\n'
		return ret
	
	def assassinationAttempt(self, assassin, code):
		if(not(assassin.target) or assassin.target.secretCode != code):
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
		victim = assassin.target
		print victim.name + ' has been slain by ' + assassin.name + '!'
		victim.status = 'Slain by ' + assassin.name
		victim.target = None
		acc = MasterAccount(self.buyIn)
		acc.transfer(victim.bankId, assassin)
		outgoing.killed(victim, acc.getBalance(victim.bankId))
		if(len(filter(lambda player: player.status == 'Alive', self.players)) == 1):
			money = acc.getBalance(assassin.bankId)
			for player in self.players:
				outgoing.gameover(player, assassin, money)
			assassin.target = None
			self.completed = True
		else:
			assassin.target = victim.target
	

class Player(db.Model):
	name = db.Column(db.String)
	number = db.Column(db.String(12), primary_key=True)
	status = db.Column(db.String)
	target_number = db.Column(db.String(12), db.ForeignKey('player.number'))
	target = db.relationship("Player", remote_side=[number], join_depth=2, post_update=True)
	secretCode = db.Column(db.String)
	bankId = db.Column(db.String)
	awaitingResponse = db.Column(db.PickleType)
	game_code = db.Column(db.String(5), db.ForeignKey('game.code'))
	
	def string(self):
		return "%s - %s" %(self.name, self.status)
