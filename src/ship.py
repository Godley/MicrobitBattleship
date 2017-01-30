class Ship(object):
    def __init__(self, length):
        self.x = 0
        self.y = 0
        self.length = length
        self.sunk = False
        self.hits = [1 for i in range(self.length)]

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def is_hit(self, x=0, y=0):
        width_true = x >= self.x and x <= self.x + self.length - 1
        height_true = y == self.y
        return width_true and height_true

    def position(self):
        return self.x, self.y

    def hit(self, x=0, y=0):
        if self.is_hit(x, y):
            idx = x - self.x
            self.hits[idx] = 2
        if (sum(self.hits) / 2) >= self.length:
            self.sunk = True

    def draw(self):
        return self.position(), self.hits