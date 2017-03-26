from flask import Flask, render_template, request, redirect, url_for, abort, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route("/")
def home():
	return render_template('index.html')
	
def message():
	return render_template('message.html', message=session['message']

if __name__ == '__main__':
app.run()