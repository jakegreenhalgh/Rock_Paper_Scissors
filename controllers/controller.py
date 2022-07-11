from crypt import methods
from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player

@app.route('/play')
def play():
    return render_template('player1_choose.html', title = 'Player 1 enter')

@app.route('/play', methods=['POST'])
def player1chooses(choice):
    global player1
    player1_name = request.form["Name"]
    player1_choice = choice
    player1 = Player(player1_name, player1_choice)
    return render_template("player2_choose.html", choice=player1_choice, title='Player 2 enter')

# @app.route('/<choice>')
# def player2_choice():
#     return render_template('player2_choose.html', )

@app.route('/<choice>', methods=['POST'])
def player2chooses(choice, choice2):
    global player2
    player2_name = request.form["Name"]
    player2_choice = choice2
    player2 = Player(player2_name, player2_choice)
    return render_template('results_page.html', player1 = player1, player2 = player2, results = Game.get_results(player1, player2))

# @app.route('/<choice>/<choice2>')
# def return_results():
#     return render_template('results_page.html', player1 = player1, player2 = player2, results = results)


@app.route('/computer')
def computer_page():
    return render_template('computer.html', title='Player enter')

@app.route('/computer/<choice>', methods=['POST'])
def play_computer(choice):
    global player
    player_name = request.form["Name"]
    player_choice = choice
    player = Player(player_name, player_choice)
    return render_template('results_page.html', player1 = player, player2 = Game.play_comp(), results = Game.get_results(player, Game.play_comp()))







