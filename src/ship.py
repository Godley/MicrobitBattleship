class Ship(object):
    def __init__(self, length):
        self.x = 0
        self.y = 0
        self.length = length
        self.sunk = False
        self.hits = [1 for i in range(self.length)]
        self.horizontal = True

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def is_hit(self, x=0, y=0):
        in_width = x == self.x
        in_height = y == self.y
        if self.horizontal:
            in_width = x >= self.x and x <= self.x + self.length - 1
        else:
            in_height = y >= self.y and y <= self.y + self.length - 1
        return in_width and in_height

    def position(self):
        return self.x, self.y

    def hit(self, x=0, y=0):
        is_hit = self.is_hit(x, y)
        if is_hit:
            idx = x - self.x
            self.hits[idx] = 2
        if (sum(self.hits) / 2) >= self.length:
            self.sunk = True
        return is_hit, self.sunk

    def rotate(self):
        self.horizontal = False

    def draw(self):
        x, y = self.position()
        return x, y, self.hits, self.horizontal