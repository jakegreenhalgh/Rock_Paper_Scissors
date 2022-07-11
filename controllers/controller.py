from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player
from models.players import *

@app.route('/')
def index():
    return render_template('index.html', title = 'Player 1 enter')

@app.route('/', methods=['POST'])
def player1chooses():
    player1_name = request.form["name"]
    player1_choice = request.form["choice"]
    player1 = Player(name = player1_name, choice = player1_choice)
    return redirect ('/<player1_choice>/')

@app.route('/<player1_choice>/', methods = ["POST"])
def player2_choice():
    return render_template('player2_choose.html', title='Player 2 enter')

@app.route('/<player1_choice>/', methods=['POST'])
def player2chooses():
    player2_name = request.form["name"]
    player2_choice = request.form["choice"]
    player2 = Player(name = player2_name, choice = player2_choice)
    redirect ('/player1_choice/player2_choice/')

@app.route('/<player1_choice>/<player2_choice>/')
def return_results():
    return render_template('results_page.html', player1 = player1, player2 = player2)

@app.route('/<player1_choice>/<player2_choice>/')
def results():
    game1 = Game(player1 = player1, player2 = player2)
    game_result = game1.play_r_p_s()






