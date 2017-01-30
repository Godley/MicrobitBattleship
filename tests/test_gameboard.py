import pytest
from src.exceptions import InvalidPositionError

def test_get_ships(board):
    ships = board.get_ships()
    nxtship = next(ships)
    assert nxtship.length == 2

def test_get_max_ships(board):
    ships = board.get_ships()
    for i in range(3):
        next(ships)
    with pytest.raises(StopIteration):
        next(ships)

def test_ship_lengths(board):
    ships = board.get_ships()
    for i in range(2,5):
        nxtship = next(ships)
        assert nxtship.length == i

def test_add_ship(board):
    board.add_ship(x=1, y=3)
    assert board.ships[0].position() == (1, 3)

def test_invalid_pos(board):
    length = 2
    assert not board.position_is_valid(length, x=4)

def test_add_ship_invalid_pos(board):
    with pytest.raises(InvalidPositionError):
        board.add_ship(x=4)

def test_move_ship_invalid_pos(board):
    board.add_ship()
    with pytest.raises(InvalidPositionError):
        board.move_ship(0, x=5)

def test_draw(board):
    result = board.draw()
    assert result == [[0 for j in range(5)] for i in range(5)]

def test_draw_with_ship(board):
    board.add_ship()
    result = board.draw()
    exp = [[0 for j in range(5)] for i in range(5)]
    exp[0][0] = 1
    exp[0][1] = 1
    assert result == exp

def test_draw_with_hit_ship(board):
    board.add_ship()
    board.hit(x=0, y=0)
    result = board.draw()
    exp = [[0 for j in range(5)] for i in range(5)]
    exp[0][0] = 2
    exp[0][1] = 1
    assert result == exp