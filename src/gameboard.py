from src.ship import Ship
from src.exceptions import InvalidPositionError


class Gameboard(object):
    ships = []

    def __init__(self, width=5, height=5):
        self.ship_gen = self.get_ships()
        self.width = width
        self.height = height

    def get_ships(self):
        length = 2
        while length < 5:
            yield Ship(length=length)
            length += 1

    def position_is_valid(self, length, x=0, y=0):
        valid_x = length - 1 + x < self.width and x >= 0
        valid_y = y >= 0 and y <= self.height
        return valid_x and valid_y

    def add_ship(self, x=0, y=0):
        ship = next(self.ship_gen)
        self.ships.append(ship)
        self.move_ship(len(self.ships) - 1, x=x, y=y)

    def move_ship(self, index, x=0, y=0):
        ship = self.ships[index]
        valid_pos = self.position_is_valid(ship.length, x=x, y=y)
        if valid_pos:
            ship.move(x=x, y=y)

        else:
            raise InvalidPositionError()

    def hit(self, x=0, y=0):
        for ship in self.ships:
            ship.hit(x, y)

    def draw(self):
        board = []
        for i in range(self.height):
            row = []
            for i in range(self.width):
                row.append(0)
            board.append(row)
        return board