import tkinter as tk
from tkinter import messagebox

# Constants
PLAYER = "X"
AI = "O"

# Initialize empty board
board = [[" " for _ in range(3)] for _ in range(3)]

# Check for a winner
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check for a draw
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, PLAYER):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best
    else:
        best = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = PLAYER
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best

# Get best move for AI
def best_move():
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Button click handler
def on_click(i, j):
    if board[i][j] == " " and not check_winner(board, PLAYER) and not check_winner(board, AI):
        board[i][j] = PLAYER
        buttons[i][j].config(text=PLAYER, state="disabled")
        if check_winner(board, PLAYER):
            messagebox.showinfo("Game Over", "You win!")
            disable_all_buttons()
            return
        elif is_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            return

        move = best_move()
        if move:
            board[move[0]][move[1]] = AI
            buttons[move[0]][move[1]].config(text=AI, state="disabled")
            if check_winner(board, AI):
                messagebox.showinfo("Game Over", "AI wins!")
                disable_all_buttons()

# Disable all buttons
def disable_all_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state="disabled")

# Create GUI
root = tk.Tk()
root.title("Tic-Tac-Toe with AI")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
