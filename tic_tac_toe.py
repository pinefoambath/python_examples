import numpy as np

def setup():
    return np.full((3, 3), '.', dtype=str)

def ausgabe(board):
    print("  1 2 3")
    print(" -------")
    for i in range(3):
        print(f"{i+1}|", end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()
    print()


def hatGewonnen(board, player_symbol):
    if np.all(np.diag(board) == player_symbol):
        return True

    if np.all(np.diag(np.fliplr(board)) == player_symbol):
        return True
    return False

# --- Main Game Logic ---

game_board = setup()

current_player = 'X'
winner = None

for turn in range(9):
    ausgabe(game_board)
    print(f"Player '{current_player}', it's your turn.")

    while True:
        try:
            # Get input for row and column, subtracting 1 to match 0-based array indices
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and game_board[row, col] == '.':
                game_board[row, col] = current_player
                break # Exit the input loop if the move is valid
            else:
                print("Invalid move. That spot is taken or out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if hatGewonnen(game_board, current_player):
        winner = current_player
        break # Exit the main game loop 

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# --- End of Game ---
print("\n--- Game Over ---")
ausgabe(game_board)

if winner:
    print(f"Congratulations! Player '{winner}' has won!")
else:
    print("It's a draw!")