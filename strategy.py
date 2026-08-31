# strategy.py
# ============================================================
# This is the ONLY file you need to edit.
# ============================================================
#
# Your job: fill in the choose_move function below so that
# it picks a smart position instead of always picking the
# first available one.
#
# You do NOT need to touch tictactoe.py or play.py.
# Run your strategy any time with:  python play.py


def choose_move(game, player):
    """
    Decide which position to play next.

    Parameters
    ----------
    game : TicTacToe
        The current game object.

        Useful things you can do with it:
            game.available_moves()  →  list of open positions, e.g. [1, 3, 7]
            game.board              →  the full 10-element board list
                                       (board[1] through board[9] are the squares)
            game.X                  →  the string 'X'
            game.O                  →  the string 'O'

    player : str
        Who you are — either game.X or game.O.

    Returns
    -------
    int
        The position number (1-9) you want to play.
        It must be one of the numbers in game.available_moves().
    """

    # ---------------------------------------------------------------
    # Starter behavior: always pick the first open square. (this is a dumb strategy, don't use it)
    # ---------------------------------------------------------------
    # remember YOU are X. X goes first. 
    
    # Step 1: find out which moves are still available.
    open_squares = game.available_moves()

    # Step 2: for now, just take the first one on the list.
    my_choice = open_squares[0]

    # Step 3: return the position number you chose.
    return my_choice

    # ---------------------------------------------------------------
    # Ideas to try (don't peek until you've thought about it!):
    #
    #   - Can you pick a random position instead of always the first?
    #     Hint: look up the "random" module.
    #
    #   - What if you always grab the center (position 5) when it's free?
    #
    #   - Can you check if you are one move away from winning and
    #     take that move?
    #
    #   - Can you check if your opponent is one move away from winning
    #     and block them?
    # ---------------------------------------------------------------
