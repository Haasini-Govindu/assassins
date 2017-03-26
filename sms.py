from twilio import twiml

from targets import Player, Game, generateCode
from database import db


def handleSms(request):
	print(request.form['Body'])
	response = twiml.Response()

	# debug
	if(request.form['Body'] == 'debug'):
		for game in Game.query.all():
			print game.code
			game.printStatus()

	sender = Player.query.filter_by(number=request.form['From']).first()
	if(sender is None):
		sender = Player(number=request.form['From'])
		db.session.add(sender)
	if(not(sender.awaitingResponse is None)):
		return str(sender.awaitingResponse[0](sender.awaitingResponse[1], sender, request, response))
	
	body = request.form['Body'].lower().strip()
	if(body == 'new game'):
		return str(handleNew(sender, response))
	if(body == 'start'):
		return str(handleStart(sender, response))
	if(body.split(' ')[0] == 'join'):
		return str(handleJoin(sender, body, response))
	if(body.split(' ')[0] == 'kill'):
		return str(handleKill(sender, body, response))
	if(body == 'leaderboard'):
		return str(handleLeaderboard(sender, response))
	if(body == 'end game' and sender.game):
		game = sender.game
		for p in game.players:
			p.game = None
		db.session.delete(game)
		db.session.commit()
	return str(handleIdk(response))

def buyIn(_ignore, sender, request, response):
	try:
		val = float(request.form['Body'])
	except ValueError:
		response.message('that\'s not a valid number, try again')
		return response
	sender.awaitingResponse = None
	code = generateCode(5)
	game = Game(code=code, buyIn=val, started=False, completed=False)
	db.session.add(game)
	response.message('new game with code ' + code)
	return handleJoin(sender, 'join ' + code, response)
	

def getName(code, sender, request, response):
	sender.awaitingResponse = None
	game = Game.query.filter_by(code=code).first()
	if(not(game is None)):
		sender.name = request.form['Body']
		sender.game = game
		db.session.commit()
		response.message('you joined the game! we\'ll let you know when it starts')
		return response
	else:
		db.session.commit()

def handleNew(sender, response):
	if(sender.game and not(sender.game.completed)):
		response.message('you\'re already in a game!')
		return response
	sender.awaitingResponse = [buyIn, None]
	db.session.commit()
	response.message('how much for the buy-in?')
	return response

def handleStart(sender, response):
	if(not(sender.game)):
		response.message('you\'re not in a game yet!')
		return response
	game = sender.game
	if(game.started):
		response.message('game is already started')
		return response
	game.start()
	db.session.commit()
	response.message('all players have been notified of the game start')
	return response

def handleJoin(sender, body, response):
	if(sender.game and not(sender.game.completed)):
		response.message('you\'re already in a game!')
		return response
	if(len(body.split(' ')) < 2):
		response.message('please include your game code')
		return response
	game = Game.query.filter_by(code=body.split(' ')[1]).first()
	if(game is None):
		response.message('that\'s not a valid game code')
		return response
	sender.awaitingResponse = [getName, game.code]
	db.session.commit()
	response.message('what\'s your name?')
	return response
	
def handleKill(sender, text, response):
	if(sender.game is None):
		response.message('you\'re not in a game yet!')
		return response
	args = text.split(' ')
	if(len(args) < 2):
		response.message('please include your victim\'s code')
		return response
	if(sender.game.assassinationAttempt(sender, args[1])):
		db.session.commit()
		if(sender.target):
			response.message('successfull kill! your next target is ' + sender.target)
		return response
	response.message('sorry, but that code isn\'t right')
	return response

def handleIdk(response):
	response.message('what?')
	return response

def handleLeaderboard(sender, response):
	if(sender.game is None):
		response.message('you\'re not in a game yet!')
		return response
	response.message(sender.game.leaderboard())
	return response
