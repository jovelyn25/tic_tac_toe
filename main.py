import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow

root = tk.Tk()
root.title("Tic Tac Toe")
root.config(bg="#1e1e2f")

# Fullscreen-like window
root.geometry("400x500")

current_player = "X"
board = [" " for _ in range(9)]
buttons = []
score_X = 0
score_O = 0

# Load images
x_img = ImageTk.PhotoImage(Image.open("x.png").resize((80, 80)))
o_img = ImageTk.PhotoImage(Image.open("o.png").resize((80, 80)))
blank_img = ImageTk.PhotoImage(Image.new("RGBA", (80, 80), (0, 0, 0, 0)))

# ------------------ Win & Draw Check ------------------
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diags
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return combo
    return None

def check_draw():
    return all(space != " " for space in board)

# ------------------ Game Actions ------------------
def on_click(index):
    global current_player, score_X, score_O

    if board[index] != " ":
        return

    board[index] = current_player
    buttons[index].config(image=x_img if current_player == "X" else o_img, state="disabled")

    winning_combo = check_win(current_player)
    if winning_combo:
        highlight_win(winning_combo)
        if current_player == "X":
            score_X += 1
        else:
            score_O += 1
        update_score()
        root.after(1000, lambda: messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!"))
        root.after(1500, reset_board)
        return

    if check_draw():
        root.after(500, lambda: messagebox.showinfo("Game Over", "It's a draw!"))
        root.after(1000, reset_board)
        return

    current_player = "O" if current_player == "X" else "X"
    turn_label.config(text=f"Player {current_player}'s Turn")

def highlight_win(combo):
    for i in combo:
        buttons[i].config(bg="#4CAF50")

def reset_board():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    turn_label.config(text="Player X's Turn")
    for btn in buttons:
        btn.config(image=blank_img, state="normal", bg="#3b3b58")

def reset_score():
    global score_X, score_O
    score_X = 0
    score_O = 0
    update_score()
    reset_board()

def update_score():
    score_label.config(text=f"Score  X: {score_X}  |  O: {score_O}")

# ------------------ UI Layout ------------------
turn_label = tk.Label(root, text="Player X's Turn", font=("Helvetica", 18, "bold"),
                      fg="#f5f5f5", bg="#1e1e2f")
turn_label.grid(row=0, column=0, columnspan=3, pady=10)

score_label = tk.Label(root, text=f"Score  X: {score_X}  |  O: {score_O}",
                       font=("Helvetica", 15), fg="#cccccc", bg="#1e1e2f")
score_label.grid(row=1, column=0, columnspan=3, pady=5)

for i in range(9):
    btn = tk.Button(root, image=blank_img, bg="#3b3b58", activebackground="#57577a",
                    relief="flat", command=lambda i=i: on_click(i))
    btn.grid(row=(i//3)+2, column=i%3, padx=5, pady=5)
    buttons.append(btn)

reset_board_btn = tk.Button(root, text="Reset Board", font=("Helvetica", 13),
                            bg="#f39c12", fg="black", command=reset_board)
reset_board_btn.grid(row=5, column=0, pady=10)

reset_score_btn = tk.Button(root, text="Reset Score", font=("Helvetica", 13),
                            bg="#e74c3c", fg="black", command=reset_score)
reset_score_btn.grid(row=5, column=2, pady=10)

root.mainloop()
