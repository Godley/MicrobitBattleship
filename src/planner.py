class Planner(object):
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.board = [[0 for i in range(self.width)] for j in range(self.height)]

    def miss(self, x=0, y=0):
        self.board[y][x] = 2

    def hit(self, x=0, y=0):
        self.board[y][x] = 1

    def draw(self):
        return self.board