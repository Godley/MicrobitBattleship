def test_shot_miss(planner, empty_board):
    planner.miss(x=0, y=0)
    result = planner.draw()
    board = empty_board
    board[0][0] = 2
    assert result == board

def test_shot_hit(planner, empty_board):
    planner.hit(x=0, y=0)
    result = planner.draw()
    board = empty_board
    board[0][0] = 1
    assert result == board