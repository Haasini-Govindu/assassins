from flask import render_template
class Player:
	def __init__(self, name, status, kills):
		self.name = name
		self.status = status
		self.kills = kills

player1 = Player('Ahri', 'Alive', 0)
player2 = Player('Katarina', 'Alive', 2)
player3 = Player('Kha\'zix', 'Alive', 1)
player4 = Player('Rengar', 'Slain by Kha\'zix', 0)
player5 = Player('Talon', 'Slain by Katarina', 0)
player6 = Player('Zed', 'Slain by Katarina', 0)
players = [player1, player2, player3, player4, player5, player6]

players.sort(key=lambda x: x.kills, reverse=True)

def homepage():
	return render_template('index.html')

def leaderboard():
	return render_template('leaderboard.html', players=players, n=len(players))
