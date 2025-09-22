"""
# --- KEY LEARNINGS FOR THIS PROGRAM ---

This is a practical exercise in modeling a real-world system (a game) 
with a NumPy matrix and using NumPy's functions to analyze the 
system's state. 

### 1. Modeling a System with a Matrix
- **Concept:** Matrixes represent 2D spaces.
- **In this code:** The `setup()` function creates a 3x3 NumPy array. This 
  matrix is the game board.

### 2. Addressing Matrix Elements with Indices
- **Concept:** To access any element, we need its address: a row and column 
  index.
- **In this code:** The main game loop takes the player's 1-based input 
  (e.g., row "1") and immediately converts it to a 0-based index 
  (`row = int(input(...)) - 1`). It then uses this to place a mark on the 
  board: `game_board[row, col] = current_player`. 

### 3. Efficient Analysis with NumPy Functions
- **Concept:** The primary advantage of NumPy is its set of fast, high-level 
  functions that simplify complex operations on arrays.
- **In this code:** The `hatGewonnen` function is the best example of this. 
  Instead of writing complex `if` statements and loops to check the diagonals, 
  we use NumPy commands:
    - `np.diag(board)`: Instantly extracts the main diagonal.
    - `np.fliplr(board)`: flips the board so we can use `np.diag` 
      again to get the other diagonal.
    - `np.all(...)`: Checks if all elements in the diagonal are the same in a 
      single, fast operation.
  This highlights the "NumPy way" of thinking: solve problems by applying 
  functions to whole arrays, not by looping through them manually.
"""

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