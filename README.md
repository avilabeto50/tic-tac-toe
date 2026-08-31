# Tic-Tac-Toe Starter — Intro CS Assignment

This is a simple tictactoe simulator that plays a random oponent

**Your assignment:** open `strategy.py` and improve the `choose_move`
function so it implements your own tictactoe strategy.

---

## Files in this repo

| File | What it does | Do you edit it? |
|---|---|---|
| `tictactoe.py` | The game engine — handles the board, moves, and win detection | **No** |
| `strategy.py` | Contains the one function you need to write | **Yes — only this file** |
| `play.py` | Runs a game: your strategy (X) vs. a random opponent (O) | **No** |

> **Rule:** Edit **only** `strategy.py`.  Everything else is done for you.

---

## Getting started

### 1 — Fork this repository

1. Click the **Fork** button at the top-right of this GitHub page.
2. GitHub will create a personal copy of the repo under your account.

### 2 — Clone your fork to your computer

Open a terminal and run (replace `YOUR-USERNAME` with your GitHub username):

```bash
git clone https://github.com/YOUR-USERNAME/tic-tac-toe-starter.git
cd tic-tac-toe-starter
```

### 3 — Run the starter code

```bash
python play.py
```

You should see the board printed after each move, ending with a result.
Right now the program has a dumb strategy. You can implement a better one. 

### 4 — Edit `strategy.py`

Open `strategy.py` in any text editor.  Read the comments, then replace
the starter logic inside `choose_move` with your own strategy

Run `python play.py` as many times as you like to test your changes.

---

## Preliminaries

### The Grid

Every square on the board has a number from **1 to 9**. They are numbered as follows:

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

When it's your turn, you pick one of these numbers to claim that square.

### How `choose_move` Works

You implement your strategy inside `strategy.py`:

```python
def choose_move(game, player):
    ...
    return my_choice   # an integer from 1 to 9
```

The function receives two arguments every time it is called:

| Argument | Type | What it is |
|---|---|---|
| `game` | `TicTacToe` | The current state of the board |
| `player` | `str` | Which mark you are — `'X'` or `'O'` |

It must **return a single integer** — the position number (1–9) you want to play.
That number must come from `game.available_moves()`, which gives you the list of
squares that haven't been taken yet.

### Useful Tools the `game` Object Gives You

| Expression | What you get |
|---|---|
| `game.available_moves()` | A list of open positions, e.g. `[1, 3, 5, 7, 9]` |
| `game.board` | A 10-element list; `game.board[1]` through `game.board[9]` are the squares |
| `game.X` | The string `'X'` |
| `game.O` | The string `'O'` |

A square on `game.board` is either `game.X`, `game.O`, or `' '` (empty).

---

## What to submit

Paste the link to **your fork** on GitHub into the assignment submission
form.  It will look like:

```
https://github.com/YOUR-USERNAME/tic-tac-toe-starter
```

Make sure your latest changes are pushed before the end of class:

```bash
git add strategy.py
git commit -m "My tic-tac-toe strategy"
git push
```