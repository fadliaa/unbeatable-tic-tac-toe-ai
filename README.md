# Unbeatable Tic-Tac-Toe AI (Minimax + Tkinter)

## What It Does

An interactive desktop Tic-Tac-Toe application powered by a **depth-weighted recursive Minimax** search engine, mathematically proven via exhaustive state-space testing to **never lose** from any starting position—whether the human or the AI moves first.

## Tech Stack

- **Language:** Python 3.11+ (zero external dependencies)
- **GUI:** Tkinter (standard library)
- **Algorithm & Testing:** Recursive Depth-Weighted Minimax Search, `unittest`

## Project Structure

```text
├── minimax_engine.py      # Pure game-state logic & depth-weighted Minimax solver
├── gui.py                 # Tkinter desktop UI (clean separation from AI engine)
└── tests/
    └── test_minimax.py    # Exhaustive game-tree verification (human-first & AI-first)
```

## Key Features

- **Optimal Adversarial Search:** Evaluates terminal states using depth-weighted scores (`10 - depth` for AI wins, `depth - 10` for human wins) so the AI chooses the shortest path to victory and blocks all forks.
- **Zero External Dependencies:** Runs entirely on the Python standard library (`tkinter`, `unittest`).
- **Exhaustively Verified:** Automated test suite traverses every reachable human move sequence and asserts **0 human wins**.

## How to Run

```bash
# Run the interactive desktop game
python gui.py

# Run exhaustive unbeatability tests
python -m unittest discover -s tests -v
```

## Team Attribution

Built as an Artificial Intelligence university course project at Alexandria University (Faculty of Computers and Data Science):
- **Minimax Algorithm & GUI:** Abdelrahman Fadlia, Assem, Khaled
- **Core Board & Win-Check Logic:** Abdallah
