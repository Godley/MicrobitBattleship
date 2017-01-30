from src.gameboard import Gameboard
from src.planner import Planner
from src.exceptions import InvalidPositionError
from microbit import button_a, button_b, radio, display, Image
import time

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

    def play(self):
        self.setup()
        radio.on()
        while True:
            img = self.planner.draw()
            x = 0
            y = 0
            while not a_pressed and b_pressed:
                old = img[y][x]
                a_pressed = button_a.is_pressed()
                b_pressed = button_b.is_pressed()
                if a_pressed and not b_pressed:
                    img[y][x] = old
                    x += 1
                elif b_pressed:
                    img[y][x] = old
                    y += 1
                img[y][x] = 2
                self.draw(img)
            self.transmit_shot(x, y)
            incoming = radio.receive()
            hit = bool(int(incoming[0]))
            win = bool(int(incoming[1]))
            if hit:
                self.planner.hit(x, y)

            else:
                self.planner.miss(x, y)

            if win:
                self.show_win()
                break
            img = self.planner.draw()
            self.draw(img)
            time.sleep(4)
            img = self.board.draw()
            self.draw(img)
            incoming = radio.receive()
            x = int(incoming[0])
            y = int(incoming[1])
            hit, win = self.board.hit(x, y)
            value = str(int(hit)) + str(int(win))
            radio.transmit(value)
            if win:
                self.show_loss()
                break

    def show_win(self):
        display.show(Image.HAPPY)
        time.sleep(2)
        display.scroll("You win!")

    def show_loss(self):
        display.show(Image.SAD)
        time.sleep(2)
        display.scroll("You lose")

    def draw(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    setting = 9
                elif board[i][j] == 2:
                    setting = 4
                else:
                    setting = 0

                display.set_pixel(i, j, setting)