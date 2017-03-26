from flask import render_template, redirect

from database import db
import targets
import nessie

class ViewPlayer:
	def __init__(self, player, acc):
		self.name = player.name
		self.status = player.status
		self.balance = acc.getBalance(player)
		if(self.balance):
			self.kills = self.balance / player.game.buyIn
			if(player.status == 'Alive'):
				self.kills -= 1
		else:
			self.balance = 0
			self.kills = 0

# player1 = Player('Ahri', 'Alive', 0)
# player2 = Player('Katarina', 'Alive', 2)
# player3 = Player('Kha\'zix', 'Alive', 1)
# player4 = Player('Rengar', 'Slain by Kha\'zix', 0)
# player5 = Player('Talon', 'Slain by Katarina', 0)
# player6 = Player('Zed', 'Slain by Katarina', 0)
# players = [player1, player2, player3, player4, player5, player6]

# players.sort(key=lambda x: x.kills, reverse=True)

def homepage():
	return render_template('index.html')

def leaderboard(code):
	game = targets.Game.query.filter_by(code=code).first_or_404()
	acc = nessie.MasterAccount(game.buyIn)
	players = map(lambda p: ViewPlayer(p, acc), game.players)
	players.sort(key=lambda p: p.balance, reverse=True)
	return render_template('leaderboard.html', players=players, n=len(players), code=code)

def create_show(code):
	if(code is None):
		code = ""
	return render_template('create.html', code=code)

def create_submit(request):
	code = request.form['code']
	if(targets.Game.query.filter_by(code=code).first()):
		return 'choose a different code, that one is taken', 400
	try:
		buyin = float(request.form['buyin'])
	except ValueError:
		return 'buy-in must a number', 400
	db.session.add(targets.Game(code=code, buyIn=buyin, started=False, completed=False))
	db.session.commit()
	return redirect("/leaderboard/" + code, code=302) 
