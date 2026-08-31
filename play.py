# play.py — run a full Tic-Tac-Toe game to test your strategy.
#
# You do NOT need to edit this file.
# Just run:  python play.py
#
# Your strategy (in strategy.py) plays as X.
# The opponent plays as O and picks a random legal move.

import random

from tictactoe import TicTacToe
from strategy import choose_move


def opponent_move(game):
    """
    The built-in opponent: picks a random open position.

    This is intentionally simple so your strategy has a
    fighting chance even with a basic implementation.
    """

    # Get all positions that haven't been played yet.
    open_squares = game.available_moves()

    # Pick one at random.
    chosen = random.choice(open_squares)

    return chosen


def run_game():
    """
    Play one full game from start to finish.

    Prints the board after every move and announces the result.
    """

    # Create a fresh game.
    game = TicTacToe()

    print("===========================================")
    print("  TIC-TAC-TOE  --  Your Strategy vs. Random")
    print("===========================================")
    print("  You are X.  Opponent is O.")
    print("  X always goes first.")

    # Show the starting board so players know the layout.
    print("\nStarting board (numbers show available positions):")
    game.print_board()

    # X always goes first, so we alternate: X, O, X, O, ...
    # A full game has at most 9 moves.
    move_number = 1

    while move_number <= 9:

        # ---- X's turn (your strategy) ----
        if move_number % 2 == 1:
            current_player = game.X
            print("--- Move", move_number, ": X's turn (your strategy) ---")

            # Ask your choose_move function where to play.
            position = choose_move(game, current_player)
            print("Your strategy chose position:", position)

        # ---- O's turn (random opponent) ----
        else:
            current_player = game.O
            print("--- Move", move_number, ": O's turn (random opponent) ---")

            # The built-in opponent picks randomly.
            position = opponent_move(game)
            print("Opponent chose position:", position)

        # Place the mark on the board.
        game.make_move(position, current_player)

        # Show the updated board.
        game.print_board()

        # Check whether someone has won or the board is full.
        result = game.check_winner()

        if result == game.X:
            print("===========================================")
            print("  *** X wins!  Your strategy won the game.")
            print("===========================================")
            return

        if result == game.O:
            print("===========================================")
            print("  O wins.  Better luck next time!")
            print("===========================================")
            return

        if result == 'Draw':
            print("===========================================")
            print("  It's a draw!  Nobody wins.")
            print("===========================================")
            return

        # No winner yet — move on to the next turn.
        move_number = move_number + 1


# This block runs only when you execute "python play.py" directly.
# It won't run if another file imports play.py.
if __name__ == '__main__':
    run_game()
