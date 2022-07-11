class Game:
    def __init__(self, _player1, _player2):
        self.player1 = _player1
        self.player2 = _player2
    
    def play_r_p_s(self):
        player1_win = True
        if self.player1.choice == "rock":
            if self.player2.choice == "scissors":
                player1_win = True
            else:
                player1_win = False
        elif self.player1.choice == "paper":
            if self.player2.choice == "rock":
                player1_win = True
            else:
                player1_win = False
        elif self.player1.choice == "scissors":
            if self.player2.choice == "paper":
                player1_win = True
            else:
                player1_win = False
        elif self.player1.choice == self.player2.choice:
            player1_win = None
        return player1_win
