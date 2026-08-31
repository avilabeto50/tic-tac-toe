# tictactoe.py — the game engine.
# You do NOT need to edit this file.
#
# A quick note on "self":
#   When you see "self" inside a class, it just means "this particular
#   game object".  If you create two games at once, each one has its
#   own board, its own winner-check, etc.  "self" is Python's way of
#   saying "the one I'm currently talking about."


class TicTacToe:
    """
    A simple Tic-Tac-Toe game you can use in your own programs.

    Basic usage
    -----------
        game = TicTacToe()   # create a new game
        game.print_board()   # see the board
        game.make_move(5, game.X)   # X plays position 5
        winner = game.check_winner()

    Board layout
    ------------
    Positions are numbered 1-9, just like a phone keypad:

        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9
    """

    def __init__(self):
        """
        Set up a brand-new game.

        __init__ is called automatically when you write TicTacToe().
        Think of it as the "set everything up" step.
        """

        # The two player markers.  Use game.X and game.O in your code
        # instead of typing the strings 'X' and 'O' by hand — fewer typos!
        self.X = 'X'
        self.O = 'O'

        # We use a 10-element list so that position numbers match
        # list indexes directly:
        #
        #   board[1] is position 1, board[2] is position 2, ..., board[9] is position 9
        #
        # board[0] is never used — it's just a placeholder so the
        # numbering works out without any off-by-one math.
        #
        # An empty cell stores its own position number (as a string)
        # so the board prints nicely.
        self.board = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        #              ^
        #         placeholder at index 0 — never touched

    # ------------------------------------------------------------------
    # print_board  ·  show the current state of the board
    # ------------------------------------------------------------------

    def print_board(self):
        """
        Print the 3-by-3 grid to the screen.

        Empty squares show their position number so you always know
        which number to play.

        Example output (fresh game):

            1 | 2 | 3
            ---------
            4 | 5 | 6
            ---------
            7 | 8 | 9
        """

        # The board has three rows of three squares each.
        # Rows start at index 1, 4, and 7 in self.board.
        print()
        print(' ', self.board[1], '|', self.board[2], '|', self.board[3])
        print('  ---------')
        print(' ', self.board[4], '|', self.board[5], '|', self.board[6])
        print('  ---------')
        print(' ', self.board[7], '|', self.board[8], '|', self.board[9])
        print()

    # ------------------------------------------------------------------
    # available_moves  ·  which positions are still open?
    # ------------------------------------------------------------------

    def available_moves(self):
        """
        Return a list of position numbers (1-9) that have not been
        played yet.

        Example:
            moves = game.available_moves()
            # might return [1, 3, 5, 7, 9] mid-game
        """

        open_positions = []

        # Check every position from 1 to 9.
        for position in range(1, 10):
            # A cell is empty when it still holds its position number
            # (stored as a string, e.g. '5').
            if self.board[position] == str(position):
                open_positions.append(position)

        return open_positions

    # ------------------------------------------------------------------
    # make_move  ·  place a mark on the board
    # ------------------------------------------------------------------

    def make_move(self, position, player):
        """
        Place player's mark at the given position.

        Parameters
        ----------
        position : int
            A number from 1 to 9.
        player : str
            Either game.X or game.O.

        Raises
        ------
        ValueError
            If the position is out of range or already taken.

        Example
        -------
            game.make_move(5, game.X)   # X plays the center
        """

        # Make sure the position is a number we know about.
        if position < 1 or position > 9:
            raise ValueError(
                "Oops!  Position must be between 1 and 9.  "
                "You passed: " + str(position)
            )

        # Make sure that square isn't already taken.
        if self.board[position] != str(position):
            raise ValueError(
                "Oops!  Position " + str(position) + " is already taken.  "
                "Available moves are: " + str(self.available_moves())
            )

        # Everything looks good — place the mark.
        self.board[position] = player

    # ------------------------------------------------------------------
    # check_winner  ·  has someone won, or is the game a draw?
    # ------------------------------------------------------------------

    def check_winner(self):
        """
        Check whether the game is over.

        Returns
        -------
        str or None
            game.X   — X has won
            game.O   — O has won
            'Draw'   — all squares are filled, no winner
            None     — the game is still going
        """

        # All eight ways to win: three rows, three columns, two diagonals.
        winning_combinations = [
            [1, 2, 3],  # top row
            [4, 5, 6],  # middle row
            [7, 8, 9],  # bottom row
            [1, 4, 7],  # left column
            [2, 5, 8],  # middle column
            [3, 6, 9],  # right column
            [1, 5, 9],  # diagonal top-left to bottom-right
            [3, 5, 7],  # diagonal top-right to bottom-left
        ]

        # Check each winning combination.
        for combo in winning_combinations:
            a = combo[0]
            b = combo[1]
            c = combo[2]

            # All three squares match and belong to a player (not a number).
            if self.board[a] == self.board[b] == self.board[c]:
                if self.board[a] == self.X or self.board[a] == self.O:
                    return self.board[a]  # return the winning player's marker

        # No winner yet.  Is the board full?
        if len(self.available_moves()) == 0:
            return 'Draw'

        # Still moves left and no winner — game is ongoing.
        return None

    # ------------------------------------------------------------------
    # reset  ·  start a new game without creating a new object
    # ------------------------------------------------------------------

    def reset(self):
        """
        Clear the board so you can play again with the same game object.

        Example
        -------
            game.reset()
            game.print_board()   # fresh empty board
        """

        # Put every position back to its starting number string.
        for position in range(1, 10):
            self.board[position] = str(position)
