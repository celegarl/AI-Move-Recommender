from connectfour import drop_piece, get_next_open_row, is_valid_location, winning_move, ROWS, COLUMNS, EMPTY
import copy

def move_blocks_opponent(board, col, opponent_piece):
    if not is_valid_location(board, col):
        return False
    temp_board = copy.deepcopy(board)
    row = get_next_open_row(temp_board, col)
    drop_piece(temp_board, row, col, opponent_piece)
    return winning_move(temp_board, opponent_piece)

def explain_move(board, col, ai_piece, player_piece):
    if move_blocks_opponent(board, col, player_piece):
        return "This move blocks your opponent from winning."
    if col == COLUMNS // 2:
        return "This move controls the center column."
    return "This move builds toward a potential connect-four."
