from src.player import Player

class Game(object):
    def __init__(self, width=5, height=5):
        self.player1 = Player(width=width, height=height)
        self.player2 = Player(width=width, height=height)

    def play(self):
        pass
