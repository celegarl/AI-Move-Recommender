from connectfour import (
    create_board, print_board, is_valid_location, get_next_open_row,
    drop_piece, winning_move, is_draw, ROWS, COLUMNS,
    PLAYER_PIECE, AI_PIECE
)
from ai import get_best_move

from tutor import explain_move

def main():
    board = create_board()
    game_over = False
    turn = 0  # 0 = Human, 1 = AI

    print("Welcome to Connect Four!")
    print("You are X. The AI is O.")
    print_board(board)

    while not game_over:
        if turn == 0:
            # Human move
            suggested_col = get_best_move(board, depth=3, piece=PLAYER_PIECE, opponent=AI_PIECE)
            suggestion_reason = explain_move(board, suggested_col, PLAYER_PIECE, AI_PIECE)
            print(f"Tutor Suggestion: You should consider column {suggested_col}.")
            print(f"Reason: {suggestion_reason}")
            
            col = input(f"Your move (0-{COLUMNS - 1}): ")
            if not col.isdigit() or not (0 <= int(col) < COLUMNS):
                print("Invalid input. Try again!")
                continue
            col = int(col)
        else:
            # AI move
            print("AI is thinking...")
            col = get_best_move(board, depth=4)
            print(f"AI selects column {col}")
            explanation = explain_move(board, col, AI_PIECE, PLAYER_PIECE)
            print(f"Explanation: {explanation}")

            

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            piece = PLAYER_PIECE if turn == 0 else AI_PIECE
            drop_piece(board, row, col, piece)

            print_board(board) 

        if winning_move(board, piece):
            winner = "You" if turn == 0 else "AI"
            print(f"{winner} ({piece}) WINS!")
            game_over = True
        elif is_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            turn ^= 1
    else:
        print("Column full. Try a different one.")

if __name__ == "__main__":
    main()