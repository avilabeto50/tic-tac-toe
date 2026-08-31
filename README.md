# Tic-Tac-Toe Starter — Intro CS Assignment

Tic-Tac-Toe is a two-player game played on a 3×3 grid.
Players take turns marking squares; the first to get three in a row
(across, down, or diagonally) wins.

**Your assignment:** open `strategy.py` and improve the `choose_move`
function so it plays smarter than picking the very first available square.

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
Right now your strategy always picks the first available square, so it
won't win very often — that's your job to fix!

### 4 — Edit `strategy.py`

Open `strategy.py` in any text editor.  Read the comments, then replace
the starter logic inside `choose_move` with something smarter.

Run `python play.py` as many times as you like to test your changes.

---

## What to submit

Paste the link to **your fork** on GitHub into the assignment submission
form.  It will look like:

```
https://github.com/YOUR-USERNAME/tic-tac-toe-starter
```

Make sure your latest changes are pushed before the deadline:

```bash
git add strategy.py
git commit -m "My tic-tac-toe strategy"
git push
```

---

## Hints and stretch goals

These are optional ideas to make your strategy stronger.
Think through each one before reading the next — every hint is a
real technique used in game-playing programs!

- **Pick the center first.** Position 5 is in the middle of the board.
  Why might that be a good opening move?

- **Take a corner.** Positions 1, 3, 7, and 9 are the corners.
  What advantage might a corner give you?

- **Look for a winning move.** Before you pick any square, can you check
  whether playing one particular square would give you three in a row
  right now?  If so, take it!

- **Block your opponent.** If your opponent is one move away from
  winning, can you spot that and play there first to stop them?

- **Combine both checks.** What should happen if you can both win *and*
  block on the same turn?  Which one matters more?

- **Count how often you win.** Play 100 games in a loop and count the
  wins, losses, and draws.  Does your strategy improve as you add
  more ideas?

Good luck — have fun!
