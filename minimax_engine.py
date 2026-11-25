"""Core game state and depth-weighted Minimax AI engine for Tic-Tac-Toe.

Original algorithm co-developed by Abdelrahman Fadlia & Assem; game logic by Abdallah.
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

Board = List[str]

WIN_COMBOS: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)

HUMAN = "X"
AI = "O"
EMPTY = " "


def create_board() -> Board:
    """Return a fresh 3x3 board represented as a 9-element list."""
    return [EMPTY] * 9


def _validate_board(board: Sequence[str]) -> None:
    if len(board) != 9:
        raise ValueError(f"Tic-Tac-Toe board must contain exactly 9 cells, got {len(board)}.")


def check_win(board: Sequence[str], player: str) -> bool:
    """Return True if `player` has three in a row on `board`."""
    _validate_board(board)
    return any(board[a] == board[b] == board[c] == player for a, b, c in WIN_COMBOS)


def is_full(board: Sequence[str]) -> bool:
    """Return True if no empty cells remain on `board`."""
    _validate_board(board)
    return all(cell != EMPTY for cell in board)


def available_moves(board: Sequence[str]) -> List[int]:
    """Return indices of all currently unoccupied squares."""
    _validate_board(board)
    return [idx for idx, cell in enumerate(board) if cell == EMPTY]


def minimax(
    board: Board,
    is_maximizing: bool,
    depth: int = 0,
    ai_player: str = AI,
    human_player: str = HUMAN,
) -> int:
    """Evaluate board state using depth-weighted Minimax search.

    Depth weighting ensures the AI prefers faster wins and delays unavoidable losses.
    """
    if check_win(board, ai_player):
        return 10 - depth
    if check_win(board, human_player):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -100
        for move in available_moves(board):
            board[move] = ai_player
            score = minimax(board, False, depth + 1, ai_player, human_player)
            board[move] = EMPTY
            if score > best_score:
                best_score = score
        return best_score

    best_score = 100
    for move in available_moves(board):
        board[move] = human_player
        score = minimax(board, True, depth + 1, ai_player, human_player)
        board[move] = EMPTY
        if score < best_score:
            best_score = score
    return best_score


def find_best_move(
    board: Sequence[str],
    ai_player: str = AI,
    human_player: str = HUMAN,
) -> Optional[int]:
    """Compute the mathematically optimal next move for `ai_player`."""
    moves = available_moves(board)
    if not moves:
        return None
    # Fast optimal opening: take center if opening on an empty board
    if len(moves) == 9:
        return 4

    working = list(board)
    best_score = -100
    best_move: Optional[int] = None

    for move in moves:
        working[move] = ai_player
        score = minimax(working, False, 0, ai_player, human_player)
        working[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
