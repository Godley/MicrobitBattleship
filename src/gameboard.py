from src.ship import Ship
from src.exceptions import InvalidPositionError
import copy


class Gameboard(object):

    def __init__(self, width=5, height=5):
        self.ships = []
        self.ship_gen = self.get_ships()
        self.width = width
        self.height = height
        self.board = [[0 for i in range(self.width)] for j in range(self.height)]

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

    def move_ship(self, index=-1, x=0, y=0):
        ship = self.ships[index]
        valid_pos = self.position_is_valid(ship.length, x=x, y=y)
        if valid_pos:
            ship.move(x=x, y=y)

        else:
            raise InvalidPositionError()

    def rotate_ship(self, index=-1):
        ship = self.ships[index]
        ship.rotate()

    def hit(self, x=0, y=0):
        hit = False
        ships_sunk = []
        for ship in self.ships:
            hit, sunk = ship.hit(x, y)
            if sunk:
                ships_sunk.append(sunk)
            if hit:
                break
        lost = len(ships_sunk) == 3
        return hit, lost

    def update(self):
        for ship in self.ships:
            x, y, hits, horizontal = ship.draw()
            if horizontal:
                row = copy.deepcopy(self.board[y])
                prefix = row[:x]
                postfix = row[x+ship.length:]
                new_row = []
                new_row.extend(prefix)
                new_row.extend(hits)
                new_row.extend(postfix)
                self.board[x] = new_row
            else:
                column = [elem[x] for elem in self.board]
                prefix = column[:y]
                postfix = column[y+ship.length:]
                new_col = []
                new_col.extend(prefix)
                new_col.extend(hits)
                new_col.extend(postfix)
                for i in range(len(self.board)):
                    self.board[i][x] = new_col[i]

    def draw(self):
        return self.board