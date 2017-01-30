import pytest
from src.ship import Ship
from src.gameboard import Gameboard
from src.planner import Planner

@pytest.fixture(scope='function')
def small_ship():
    return Ship(length=1)

@pytest.fixture(scope='function')
def long_ship():
    return Ship(length=4)

@pytest.fixture(scope='function')
def board():
    elem = Gameboard()
    yield elem
    elem.ships = []

@pytest.fixture()
def empty_board():
    return [[0 for j in range(5)] for i in range(5)]

@pytest.fixture()
def planner():
    return Planner()