"""Interactive Tkinter GUI for Unbeatable Tic-Tac-Toe AI.

Original GUI co-developed by Khaled & Abdelrahman Fadlia.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import List

from minimax_engine import AI, EMPTY, HUMAN, check_win, create_board, find_best_move, is_full


class TicTacToeGUI:
    """Desktop 3x3 Tic-Tac-Toe interface against an unbeatable Minimax AI."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Unbeatable Tic-Tac-Toe AI")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8fafc")

        self.board: List[str] = create_board()
        self.current_player: str = HUMAN
        self.buttons: List[tk.Button] = []

        self.status_label = tk.Label(
            self.root,
            text="Your turn (X) — try to beat the AI!",
            font=("Segoe UI", 11, "bold"),
            bg="#f8fafc",
            fg="#0f3d6e",
            pady=8,
        )
        self.status_label.pack()

        grid_frame = tk.Frame(self.root, bg="#f8fafc", padx=12, pady=4)
        grid_frame.pack()
        self._create_board(grid_frame)

        reset_btn = tk.Button(
            self.root,
            text="Restart Game",
            font=("Segoe UI", 10, "bold"),
            bg="#0f3d6e",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            relief="flat",
            padx=14,
            pady=6,
            cursor="hand2",
            command=self.reset_game,
        )
        reset_btn.pack(pady=(6, 12))

    def _create_board(self, parent: tk.Frame) -> None:
        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    parent,
                    text=EMPTY,
                    font=("Segoe UI", 24, "bold"),
                    height=2,
                    width=4,
                    bg="white",
                    fg="#0f172a",
                    relief="solid",
                    bd=1,
                    cursor="hand2",
                    command=lambda r=row, c=col: self.on_click(r, c),
                )
                btn.grid(row=row, column=col, padx=3, pady=3)
                self.buttons.append(btn)

    def on_click(self, row: int, col: int) -> None:
        idx = row * 3 + col
        if self.board[idx] != EMPTY or self.current_player != HUMAN:
            return

        self.board[idx] = HUMAN
        self.buttons[idx].config(text=HUMAN, fg="#0f3d6e")

        if check_win(self.board, HUMAN):
            messagebox.showinfo("Game Over", "Human wins!")
            self.reset_game()
            return
        if is_full(self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
            return

        self.current_player = AI
        self.status_label.config(text="AI (O) is thinking...")
        self.root.update_idletasks()
        self.ai_move()

    def ai_move(self) -> None:
        move = find_best_move(self.board)
        if move is not None:
            self.board[move] = AI
            self.buttons[move].config(text=AI, fg="#b91c1c")

            if check_win(self.board, AI):
                messagebox.showinfo("Game Over", "AI (O) wins!")
                self.reset_game()
                return
            if is_full(self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
                return

        self.current_player = HUMAN
        self.status_label.config(text="Your turn (X)")

    def reset_game(self) -> None:
        self.board = create_board()
        for btn in self.buttons:
            btn.config(text=EMPTY, fg="#0f172a")
        self.current_player = HUMAN
        self.status_label.config(text="Your turn (X) — try to beat the AI!")

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    TicTacToeGUI().run()
