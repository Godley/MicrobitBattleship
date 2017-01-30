def test_ship_length(small_ship):
    assert small_ship.length == 1

def test_move_ship(small_ship):
    small_ship.move(x=1)
    assert small_ship.x == 1
    assert small_ship.y == 0

def test_move_down(small_ship):
    small_ship.move(y=1)
    assert small_ship.y == 1
    assert small_ship.x == 0

def test_is_hit(small_ship):
    assert small_ship.is_hit(x=0, y=0)

def test_is_not_hit(small_ship):
    assert not small_ship.is_hit(x=1, y=0)

def test_is_hit_long_ship(long_ship):
    assert long_ship.is_hit(x=3, y=0)

def test_is_not_hit_long_ship(long_ship):
    assert not long_ship.is_hit(x=3, y=1)

def test_not_sunk(long_ship):
    assert not long_ship.sunk

def test_not_sunk_with_two_hits(long_ship):
    long_ship.hit()
    long_ship.hit(x=1)
    assert not long_ship.sunk

def test_not_sunk_with_three_hits(long_ship):
    long_ship.hit()
    long_ship.hit(x=1)
    long_ship.hit(x=2)
    assert not long_ship.sunk

def test_sunk(long_ship):
    long_ship.hit()
    long_ship.hit(x=1)
    long_ship.hit(x=2)
    long_ship.hit(x=3)
    assert long_ship.sunk

def test_draw(long_ship):
    assert long_ship.draw() == (0, 0, [1, 1, 1, 1], True)

def test_draw_after_hit(long_ship):
    long_ship.hit(x=0, y=0)
    assert long_ship.draw() == (0,0, [2,1,1,1], True)