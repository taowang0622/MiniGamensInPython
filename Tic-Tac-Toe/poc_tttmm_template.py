"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor

# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def max_result(results):
    """
    :param results: [(score1, (row1, col1)), (score2, (row2, col2))......]
    :return: maxScore, (row, col)
    """
    max_score = results[0][0]
    row, col = results[0][1]
    for result in results:
        if result[0] > max_score:
            max_score = result[0]
            row, col = result[1]
    return max_score, (row, col)

def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    result = board.check_win()
    if result != None:
        return SCORES[result], (-1, -1)
    empty_squares = board.get_empty_squares() # return a list containing tuples representing squares
    scores = []
    for square in empty_squares: # square is a tuple (row, col)
        new_board = board.clone()
        new_board.move(square[0], square[1], player)
        score, (row, col) = mm_move(new_board, provided.switch_player(player))
        if score == SCORES[player]:
            return score, square  # disruptive statement
        else:
            scores.append((score * SCORES[player], square))
    score, (row, col) = max_result(scores)
    return score * SCORES[player], (row, col)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

# board = provided.TTTBoard(3, False)
# board.move(0, 0, provided.PLAYERO)
# board.move(0, 1, provided.PLAYERX)
# board.move(1, 0, provided.PLAYERO)
# board.move(1, 1, provided.PLAYERX)
# board.move(2, 0, provided.PLAYERX)
# board.move(2, 1, provided.PLAYERO)
# board.move(2, 2, provided.PLAYERX)
# score, (row, col) = mm_move(board, provided.PLAYERX)