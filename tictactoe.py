"""
Tic Tac Toe Player
"""
import copy
import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount, Ocount = 0, 0
    for row in board:
        for cell in row:
            if cell == X:
                Xcount += 1
            elif cell == O:
                Ocount += 1
    if Xcount > Ocount:
        return O
    elif not terminal(board) and Xcount == Ocount:
        return X
    return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    x = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                moves.add((x, y))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError('Game Over')
    elif action not in actions(board):
        raise Exception("Invalid action")
    else:
        play = player(board)
        nextBoard = copy.deepcopy(board)
        (x, y) = action
        nextBoard[x][y] = play
    return nextBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRows(board) == X or checkColumns(board) == X or checkDiagonals(board) == X:
        return X
    elif checkRows(board) == O or checkColumns(board) == O or checkDiagonals(board) == O:
        return O
    return None


def checkRows(board):
    for row in board:
        if (len(set(row))) == 1:
            return row[0]
    return 0


def checkColumns(board):
    if len(set([board[i][0] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][1] for i in range(len(board))])) == 1:
        return board[0][1]
    if len(set([board[i][2] for i in range(len(board))])) == 1:
        return board[0][2]
    return 0


def checkDiagonals(board):
    if (len(set([board[i][i] for i in range(len(board))]))) == 1:
        return board[0][0]
    if (len(set([board[i][len(board) - i - 1] for i in range(len(board))]))) == 1:
        return board[0][len(board) - 1]
    return 0


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    # if board is empty return random starting position
    if board == [[EMPTY] * 3] * 3:
        return (random.randint(0, len(board) - 1), random.randint(0, len(board) - 1))

    if p == X:
        v = float("-inf")
        move = None
        for action in actions(board):
            min = minValue(result(board, action))
            if min > v:
                v = min
                move = action
    elif p == O:
        v = float("inf")
        move = None
        for action in actions(board):
            max = maxValue(result(board, action))
            if max < v:
                v = max
                move = action
    return move


def minValue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v
