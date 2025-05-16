import math
import random
import copy
from connectfour import ROWS, COLUMNS, EMPTY, PLAYER_PIECE, AI_PIECE, winning_move, is_valid_location, get_next_open_row, drop_piece

def evaluate(board, piece):
    score = 0
    opponent_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    center_array = [row[COLUMNS // 2] for row in board]
    center_count = center_array.count(piece)
    score += center_count * 3

    for row in board:
        for c in range(COLUMNS - 3):
            window = row[c:c + 4]
            score += evaluate_window(window, piece)

    for c in range(COLUMNS):
        col_array = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            window = col_array[r:r + 4]
            score += evaluate_window(window, piece)

    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            window = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 5

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 80

    return score

def get_valid_locations(board):
    return [col for col in range(COLUMNS) if is_valid_location(board, col)]

def simulate_move(board, col, piece):
    new_board = copy.deepcopy(board)
    row = get_next_open_row(new_board, col)
    if row is not None:
        drop_piece(new_board, row, col, piece)
    return new_board

def is_terminal_node(board, player, opponent):
    return winning_move(board, player) or winning_move(board, opponent) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer, player, opponent):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board, player, opponent)

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, player):
                return (None, 1000000000)
            elif winning_move(board, opponent):
                return (None, -1000000000)
            else:
                return (None, 0)
        else:
            return (None, evaluate(board, player))

    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            new_board = simulate_move(board, col, player)
            new_score = minimax(new_board, depth - 1, alpha, beta, False, player, opponent)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_col, value
    else:
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            new_board = simulate_move(board, col, opponent)
            new_score = minimax(new_board, depth - 1, alpha, beta, True, player, opponent)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_col, value

def get_best_move(board, depth=4, piece=AI_PIECE, opponent=PLAYER_PIECE):
    col, _ = minimax(board, depth, -math.inf, math.inf, True, piece, opponent)
    return col


