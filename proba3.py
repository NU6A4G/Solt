import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime


class TicTacToe:
    def __init__(self, root, player1, player2):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Initialize variables
        self.current_player = "X"
        self.player_names = {"X": player1, "O": player2}
        self.board = [""] * 9

        # Create labels for player names and current player
        self.player_labels = [
            tk.Label(root, text=f"{player1}'s turn", font=("Helvetica", 12)),
            tk.Label(root, text=f"Current Player: {player1}", font=("Helvetica", 10)),
        ]

        # Create buttons
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(root, text="", font=("Helvetica", 24), width=6, height=3,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i + 1, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def on_button_click(self, row, col):
        if not self.board[row * 3 + col]:
            self.board[row * 3 + col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                winner_name = self.player_names[self.current_player]
                messagebox.showinfo("Tic Tac Toe", f"{winner_name} wins!")
                self.save_winner(winner_name)
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_labels[0].config(text=f"{self.player_names[self.current_player]}'s turn")
                self.player_labels[1].config(text=f"Current Player: {self.player_names[self.current_player]}")

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return True
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i * 3 + j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.player_labels[0].config(text=f"{self.player_names[self.current_player]}'s turn")
        self.player_labels[1].config(text=f"Current Player: {self.player_names[self.current_player]}")

    def save_winner(self, winner_name):
        try:
            with open("winners.txt", "a") as file:
                date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{date_str} - {winner_name}\n")
        except Exception as e:
            print(f"Error saving winner: {e}")


def get_player_names():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    player1 = simpledialog.askstring("Player 1", "Enter Player 1's name:")
    player2 = simpledialog.askstring("Player 2", "Enter Player 2's name:")

    return player1, player2


if __name__ == "__main__":
    player1, player2 = get_player_names()

    root = tk.Tk()
    game = TicTacToe(root, player1, player2)
    root.mainloop()
