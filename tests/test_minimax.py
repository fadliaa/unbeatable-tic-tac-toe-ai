"""Exhaustive automated tests proving the Minimax AI is mathematically unbeatable."""

from __future__ import annotations

import unittest
from typing import Dict, Tuple

from minimax_engine import (
    AI,
    EMPTY,
    HUMAN,
    available_moves,
    check_win,
    create_board,
    find_best_move,
    is_full,
)


class TestMinimaxUnbeatability(unittest.TestCase):
    """Verify optimal play across every possible human game path."""

    def test_blocks_immediate_human_win(self) -> None:
        board = ["X", "X", " ", "O", " ", " ", " ", " ", " "]
        self.assertEqual(find_best_move(board), 2)

    def test_takes_immediate_winning_move(self) -> None:
        board = ["O", "O", " ", "X", "X", " ", " ", " ", " "]
        self.assertEqual(find_best_move(board), 2)

    def test_exhaustive_ai_never_loses_when_human_starts(self) -> None:
        memo: Dict[Tuple[str, ...], str] = {}

        def explore_human_turn(board: list[str]) -> None:
            key = tuple(board)
            if key in memo:
                return
            if check_win(board, HUMAN):
                self.fail(f"Human won against Minimax AI! Board: {board}")
            if check_win(board, AI) or is_full(board):
                memo[key] = "terminal"
                return

            for human_move in available_moves(board):
                next_board = list(board)
                next_board[human_move] = HUMAN
                if check_win(next_board, HUMAN):
                    self.fail(f"Human found a winning move! Board: {next_board}")
                if is_full(next_board):
                    continue
                ai_move = find_best_move(next_board)
                self.assertIsNotNone(ai_move)
                assert ai_move is not None
                next_board[ai_move] = AI
                explore_human_turn(next_board)

            memo[key] = "checked"

        explore_human_turn(create_board())
        self.assertGreater(len(memo), 100)

    def test_exhaustive_ai_never_loses_when_ai_starts(self) -> None:
        board = create_board()
        first_move = find_best_move(board)
        self.assertEqual(first_move, 4)
        board[first_move] = AI

        memo: set[Tuple[str, ...]] = set()

        def explore(state: list[str]) -> None:
            key = tuple(state)
            if key in memo:
                return
            for human_move in available_moves(state):
                nxt = list(state)
                nxt[human_move] = HUMAN
                self.assertFalse(check_win(nxt, HUMAN), f"Human won: {nxt}")
                if is_full(nxt):
                    continue
                ai_move = find_best_move(nxt)
                assert ai_move is not None
                nxt[ai_move] = AI
                if not check_win(nxt, AI) and not is_full(nxt):
                    explore(nxt)
            memo.add(key)

        explore(board)
        self.assertGreaterEqual(len(memo), 15)


if __name__ == "__main__":
    unittest.main()
