import tkinter as tk
from tkinter import messagebox

# Initialize the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
# Function to check if the game is over
def check_game_over():
    # Check for a win
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return "win"
# Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"
# Function to handle a player's turn
def take_turn(position, button):
    global current_player

    # Prevent action if the position is already filled
    if board[position] != "-":
        return

    # Mark the board with the current player's move
    board[position] = current_player
    button.config(text=current_player, state="disabled")

    # Check if the game is over after the move
    game_result = check_game_over()
    if game_result == "win":
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
    elif game_result == "tie":
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
    else:
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Function to reset the game board
def reset_game():
    global board, current_player
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    current_player = "X"
    for i in range(9):
        buttons[i].config(text="-", state="normal")
# Create the main window using tkinter
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the current player
current_player = "X"

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="-", width=10, height=3,
                       command=lambda i=i: take_turn(i, buttons[i]))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)
# Start the GUI main loop
root.mainloop()