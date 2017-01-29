import pytest
from src.ship import Ship
from src.gameboard import Gameboard

@pytest.fixture()
def small_ship():
    return Ship(length=1)

@pytest.fixture()
def long_ship():
    return Ship(length=4)

@pytest.fixture()
def board():
    return Gameboard()