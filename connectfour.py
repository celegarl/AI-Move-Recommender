ROWS = 6
COLUMNS = 7
PLAYER_PIECE = "X"
AI_PIECE = "O"
EMPTY = " "

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + "   ".join(map(str, range(COLUMNS))))
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("-" * 29)

def is_valid_location(board, col):
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # Check vertical
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    # Check positive diagonal
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    # Check negative diagonal
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLUMNS))