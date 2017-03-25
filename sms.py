from twilio import twiml
from flask import Flask, request

# import targets
from targets import Player, Game, generateCode


app = Flask(__name__)

# codes to games
games = {}

# players to games
players = {}

awaitingResponse = {}

@app.route("/", methods=['GET', 'POST'])
def root():
	print(request.form['Body'])
	response = twiml.Response()

	# debug
	if(request.form['Body'] == 'debug'):
		for key in games.keys():
			print key
			games[key].printStatus()


	if(request.form['From'] in awaitingResponse):
		return str(awaitingResponse.pop(request.form['From'])(request, response))
	body = request.form['Body'].lower().strip()
	if(body == 'new game'):
		code = handleNew(request.form['From'], response)
		if code:
			return str(handleJoin(request.form['From'], 'join ' + code, response))
		return str(response)
	if(body == 'start'):
		return str(handleStart(request.form['From'], response))
	if(body.split(' ')[0] == 'join'):
		return str(handleJoin(request.form['From'], body, response))
	if(body.split(' ')[0] == 'kill'):
		return str(handleKill(request.form['From'], body, response))
	if(body == 'leaderboard'):
		return str(handleLeaderboard(request.form['From'], response))
	return str(handleIdk(response))

def getName(code):
	if code in games:
		def go(request, response):
			games[code].addPlayer(Player(request.form['Body'], request.form['From']))
			players[request.form['From']] = games[code]
			response.message('you joined the game! we\'ll let you know when it starts')
			return response
		return go

def handleNew(sender, response):
	if(sender in players):
		response.message('you\'re already in a game!')
		return None
	code = generateCode(5)
	games[code] = Game()
	response.message('new game with code ' + code)
	return code

def handleStart(sender, response):
	if(not(sender in players)):
		reponse.message('you\'re not in a game yet!')
		return response
	game = players[sender]
	game.start()
	response.message('all players have been notified of the game start')
	return response

def handleJoin(sender, body, response):
	if(sender in players):
		response.message('you\'re already in a game!')
		return response
	if(len(body.split(' ')) < 2):
		response.message('please include your game code')
		return response
	if(not(body.split(' ')[1] in games)):
		response.message('that\'s not a valid game code')
		return response
	awaitingResponse[sender] = getName(body.split(' ')[1])
	response.message('what\'s your name?')
	return response
	
def handleKill(sender, text, response):
	game = players[sender]
	args = text.split(' ')
	if(len(args) < 2):
		response.message('please include your victim\'s code')
		return response
	player = game.findPlayer(sender);
	if(not(player)):
		response.message('you\'re not even playing dumbass')
		return response
	if(game.assassinationAttempt(player, args[1])):
		if(player.target):
			response.message('successfull kill! your next target is ' + player.getTarget())
		return response
	response.message('sorry, but that code isn\'t right')
	return response

def handleIdk(response):
	response.message('what?')
	return response

def handleLeaderboard(sender, response):
	if(not(sender in players)):
		reponse.message('you\'re not in a game yet!')
		return response
	game = players[sender]
	response.message(game.leaderboard())
	return response


# placeholder functions
# ingame = False

# def inGame(sender):
# 	return ingame

# def joinGame(sender, name):
# 	global ingame
# 	ingame = True

# def getTarget(sender):
# 	return 'charlie'

# def kill(sender, code):
# 	return code == 'yes'
