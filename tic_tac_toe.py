# Determine if someone has won a game of tic-tac-toe.
#
# Points of interest:
#
# - How to represent the game
# - Should the solution work for arbitrary game sizes?
# - Dont Repeat Yourself
# - Testing, TDD
# - How to optimise


def is_win(game):
    # rows
    for axis_x in range(0, 3):
        # row
        if game[axis_x][0] == game[axis_x][1] == game[axis_x][2]:
            return True
        # col
        if game[0][axis_x] == game[1][axis_x] == game[2][axis_x]:
            return True

        # diagonal
        if game[0][0] == game[1][1] == game[2][2]:
            return True
        if game[0][2] == game[1][1] == game[2][0]:
            return True

    return False

assert is_win(
    [
        ['x', 'o', 'o'], 
        ['x', 'o', 'x'], 
        ['x', 'x', 'x']
    ]
) == True                 
assert is_win(
    [
        ['x', 'o', 'o'], 
        ['x', 'o', 'x'], 
        ['o', 'x', 'x']
    ]
) == False
