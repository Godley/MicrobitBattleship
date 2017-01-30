from src.gameboard import Gameboard
from src.planner import Planner
from src.exceptions import InvalidPositionError
from enum import Enum
from microbit import button_a, button_b

class Player(object):
    def __init__(self, width=5, height=5):
        self.planner = Planner(width, height)
        self.board = Gameboard(width, height)

    def setup(self):
        while True:
            try:
                self.board.add_ship()
                x = 0
                y = 0
                doublepress = False
                while not doublepress:
                    a_was_pressed = button_a.was_pressed()
                    b_was_pressed = button_b.was_pressed()
                    a_pressed = button_a.is_pressed()
                    b_pressed = button_b.is_pressed()
                    if a_pressed and b_pressed:
                        self.board.rotate_ship()
                        if a_was_pressed and b_was_pressed:
                           doublepress = True
                    elif a_pressed:
                        x += 1
                        try:
                            self.board.move_ship(x=x, y=y)
                        except InvalidPositionError:
                            x = 0
                            self.board.move_ship(x=x, y=y)
                    elif b_pressed:
                        y += 1
                        try:
                            self.board.move_ship(x=x, y=y)
                        except InvalidPositionError:
                            y = 0
                            self.board.move_ship(x=x, y=y)

            except StopIteration:
                break

    def turn(self):
        pass


    def shot(self, x=0, y=0):
        hit, sunk = self.board.hit(x, y)
        return hit, sunk