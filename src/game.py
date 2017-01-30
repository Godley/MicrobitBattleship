from src.player import Player

class Game(Player):
    def play(self):
        self.setup()
        self.play()

if __name__ == '__main__':
    game = Game()
    game.play()