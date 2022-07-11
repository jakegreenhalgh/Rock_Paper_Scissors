import random
from models.player import Player

class Game():    
    def play_r_p_s(player1, player2):
        player1_win = None
        if player1.choice == 'rock':
            if player2.choice == 'scissors':
                player1_win = True
            else:
                player1_win = False
        elif player1.choice == 'paper':
            if player2.choice == 'rock':
                player1_win = True
            else:
                player1_win = False
        elif player1.choice == 'scissors':
            if player2.choice == 'paper':
                player1_win = True
            else:
                player1_win = False
        if player1.choice == player2.choice:
            return None
        return player1_win
    
    def play_comp():
        return (Player('Computer', random.choice(['rock', 'paper', 'scissors'])))

    
    def get_results(player1, player2):
        if Game.play_r_p_s(player1, player2) == True:
            results = f"{player1.name} wins"
        elif Game.play_r_p_s(player1, player2) == False:
            results = f"{player2.name} wins"
        else:
            results = f"{player1.name} and {player2.name} have tied"
        return results
