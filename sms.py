from twilio import twiml

# import targets
from targets import Player, Game, generateCode

# codes to games
games = {}

# players to games
players = {}

awaitingResponse = {}

def handleSms(request):
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
		return str(handleNew(request.form['From'], response))
	if(body == 'start'):
		return str(handleStart(request.form['From'], response))
	if(body.split(' ')[0] == 'join'):
		return str(handleJoin(request.form['From'], body, response))
	if(body.split(' ')[0] == 'kill'):
		return str(handleKill(request.form['From'], body, response))
	if(body == 'leaderboard'):
		return str(handleLeaderboard(request.form['From'], response))
	return str(handleIdk(response))

def buyIn(request, response):
	try:
		val = float(request.form['Body'])
	except ValueError:
		awaitingResponse[request.form['From']] = buyIn
		response.message('that\'s not a valid number, try again')
		return response
	code = generateCode(5)
	games[code] = Game(val)
	response.message('new game with code ' + code)
	return handleJoin(request.form['From'], 'join ' + code, response)
	

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
		return response
	awaitingResponse[sender] = buyIn
	response.message('how much for the buy-in?')
	return response

def handleStart(sender, response):
	if(not(sender in players)):
		response.message('you\'re not in a game yet!')
		return response
	players[sender].start()
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
	if(not(sender in players)):
		response.message('you\'re not in a game yet!')
		return response
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
		response.message('you\'re not in a game yet!')
		return response
	response.message(players[sender].leaderboard())
	return response
