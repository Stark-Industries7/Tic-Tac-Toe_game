import tkinter as tk
from tkinter import messagebox

# Initialize the board
theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}

# Function to update the button text and board dictionary
def make_move(position):
    global turn
    if theBoard[position] == " ":
        buttons[position].config(text=turn)
        theBoard[position] = turn
        if winGame(theBoard, turn):
            messagebox.showinfo("Game Over", f"{turn} won!")
            reset_board()
        elif " " not in theBoard.values():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        turn = "O" if turn == "X" else "X"
    else:
        messagebox.showwarning("Invalid Move", "This space is already taken.")

# Function to reset the board for a new game
def reset_board():
    global theBoard
    for key in theBoard.keys():
        theBoard[key] = " "
    for button in buttons.values():
        button.config(text="")

# Function to check for a win
def winGame(board, turn):
    # Check rows
    for row in ["top", "mid", "low"]:
        if board[row + "-L"] == board[row + "-M"] == board[row + "-R"] != " ":
            return True

    # Check columns
    for col in ["L", "M", "R"]:
        if board["top-" + col] == board["mid-" + col] == board["low-" + col] != " ":
            return True

    # Check diagonals
    if board["top-L"] == board["mid-M"] == board["low-R"] != " ":
        return True
    if board["top-R"] == board["mid-M"] == board["low-L"] != " ":
        return True

    return False

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the turn
turn = "X"

# Create buttons for each position on the board
buttons = {
    "top-L": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("top-L")),
    "top-M": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("top-M")),
    "top-R": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("top-R")),
    "mid-L": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("mid-L")),
    "mid-M": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("mid-M")),
    "mid-R": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("mid-R")),
    "low-L": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("low-L")),
    "low-M": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("low-M")),
    "low-R": tk.Button(root, text=" ", font="Helvetica 20 bold", height=3, width=6, command=lambda: make_move("low-R")),
}

# Arrange buttons on the grid
buttons["top-L"].grid(row=0, column=0)
buttons["top-M"].grid(row=0, column=1)
buttons["top-R"].grid(row=0, column=2)
buttons["mid-L"].grid(row=1, column=0)
buttons["mid-M"].grid(row=1, column=1)
buttons["mid-R"].grid(row=1, column=2)
buttons["low-L"].grid(row=2, column=0)
buttons["low-M"].grid(row=2, column=1)
buttons["low-R"].grid(row=2, column=2)

# Run the main loop
root.mainloop()
