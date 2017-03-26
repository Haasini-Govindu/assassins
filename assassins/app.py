from flask import Flask, render_template
app = Flask(__name__)

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

@app.route("/")
def homepage():
	return render_template('index.html')

@app.route("/leaderboard")
def leaderboard():
	return render_template('leaderboard.html', test="Testing from app.py", players=players, n=len(players))

if __name__ == "__main__":
	app.run(debug=True)
