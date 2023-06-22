# Author: Sycamore Dennis
# GitHub username: sycamedia
# Date: 5/30/23
# Description: Defines a class called Othello that allows two people to play text-based Othello.
# Also defines the Player class for the game.

class Player:
    """Represents a player with a name and piece color."""

    def __init__(self, player_name, color):
        self._player_name = player_name
        self._color = color

    def get_name(self):
        """Returns player's name."""
        return self._player_name

    def get_color(self):
        """Returns player's piece color."""
        return self._color


class Othello:
    """Represents a game of Othello with a player list, board, and game state.
    Edge: * (star); black piece: X; white piece: O; empty space: . (dot)."""

    def __init__(self):
        self._player_list = []
        self._board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
        ]
        self._game_over = False

    def get_player_list(self):
        """Returns the list of players."""
        return self._player_list

    def get_board(self):
        """Returns the board."""
        return self._board

    def print_board(self):
        """Prints the current board, including the boundaries."""
        for row in self.get_board():
            print(" ".join(row))

    def create_player(self, player_name, color):
        """Creates a Player object with the given name and color (black or white)
        and adds it to the player list."""
        self.get_player_list().append(Player(player_name, color))

    def return_winner(self):
        """Returns information about the winner at the end of a game."""

        winning_color = ""
        winning_name = ""
        black_total = 0
        white_total = 0

        # Count the total black pieces currently on the board:
        for row_index in range(0, 9):
            for col_index in range(0, 9):
                if self._board[row_index][col_index] == "X":
                    black_total += 1

        # Count the total white pieces currently on the board:
        for row_index in range(0, 9):
            for col_index in range(0, 9):
                if self._board[row_index][col_index] == "O":
                    white_total += 1

        # Tie:
        if black_total == white_total:
            return "It's a tie"

        # Black wins:
        elif black_total > white_total:
            winning_color = "black"
            for player in self.get_player_list():
                if player.get_color() == "black":
                    winning_name = player.get_name()

        # White wins:
        elif black_total < white_total:
            winning_color = "white"
            for player in self.get_player_list():
                if player.get_color() == "white":
                    winning_name = player.get_name()

        return f"Winner is {winning_color} player: {winning_name}"

    def return_available_positions(self, color):
        """Returns a list of possible positions for the player with the given color to move on the board.
        Called by play_game() when the proposed move passed to that method is not valid.
        Calls validate_directions() to determine if a potential move is valid for the given color."""

        available_positions = []
        empty_spaces = []

        # Make a list of all the empty spaces:
        for row_index in range(0, 9):
            for col_index in range(0, 9):
                if self._board[row_index][col_index] == ".":
                    empty_spaces.append((row_index, col_index))

        # Check empty spaces for possible moves by calling validate_directions():
        for space in empty_spaces:
            if len(self.validate_directions(color, space)) > 0:
                available_positions.append(space)

        return available_positions

    def validate_directions(self, color, space):
        """Looks at all directions around the given space, and returns a list of directions
        that would make the move valid for the given color. (If the list is empty, the given space cannot be played
        by the given color.)"""

        # Determine the symbols for this player and the other player based on the given color:
        if color == "black":
            played_piece = "X"
            opposing_piece = "O"
        elif color == "white":
            played_piece = "O"
            opposing_piece = "X"

        # Save the coordinates of the given space:
        row = space[0]
        column = space[1]

        valid_directions = []  # Saves the directions that would make the move valid for the given color

        # Up:
        up_row = row - 1
        while self._board[up_row][column] == opposing_piece and self._board[up_row][column] != "*":
            up_row -= 1
            if self._board[up_row][column] == played_piece:
                valid_directions.append("up")

        # Down:
        down_row = row + 1
        while self._board[down_row][column] == opposing_piece and self._board[down_row][column] != "*":
            down_row += 1
            if self._board[down_row][column] == played_piece:
                valid_directions.append("down")

        # Left:
        left_column = column - 1
        while self._board[row][left_column] == opposing_piece and self._board[row][left_column] != "*":
            left_column -= 1
            if self._board[row][left_column] == played_piece:
                valid_directions.append("left")

        # Right:
        right_column = column + 1
        while self._board[row][right_column] == opposing_piece and self._board[row][right_column] != "*":
            right_column += 1
            if self._board[row][right_column] == played_piece:
                valid_directions.append("right")

        # Upper left diagonal:
        up_row = row - 1
        left_column = column - 1
        while self._board[up_row][left_column] == opposing_piece and self._board[up_row][left_column] != "*":
            up_row -= 1
            left_column -= 1
            if self._board[up_row][left_column] == played_piece:
                valid_directions.append("upper left")

        # Upper right diagonal:
        up_row = row - 1
        right_column = column + 1
        while self._board[up_row][right_column] == opposing_piece and self._board[up_row][right_column] != "*":
            up_row -= 1
            right_column += 1
            if self._board[up_row][right_column] == played_piece:
                valid_directions.append("upper right")

        # Lower left diagonal:
        down_row = row + 1
        left_column = column - 1
        while self._board[down_row][left_column] == opposing_piece and self._board[down_row][left_column] != "*":
            down_row += 1
            left_column -= 1
            if self._board[down_row][left_column] == played_piece:
                valid_directions.append("lower left")

        # Lower right diagonal:
        down_row = row + 1
        right_column = column + 1
        while self._board[down_row][right_column] == opposing_piece and self._board[down_row][right_column] != "*":
            down_row += 1
            right_column += 1
            if self._board[down_row][right_column] == played_piece:
                valid_directions.append("lower right")

        return valid_directions

    def check_game_state(self):
        """Checks the number of available moves for both players by calling return_available_positions() for each color,
        and sets the game_over data member to True if both players have run out of moves. Called by make_move()."""
        if len(self.return_available_positions("black")) == 0 and len(self.return_available_positions("white")) == 0:
            self._game_over = True

    def make_move(self, color, piece_position):
        """Puts a piece of the given color at the given position and updates the board accordingly.
        Returns the current board as a 2D list. Called by play_game(). Only valid positions are passed to this method."""

        # Determine the symbols for this player and the other player based on the given color:
        if color == "black":
            played_piece = "X"
            opposing_piece = "O"
        elif color == "white":
            played_piece = "O"
            opposing_piece = "X"

        # Save the coordinates of the given space:
        row = piece_position[0]
        column = piece_position[1]

        # Set the given space to the current player's symbol:
        self._board[row][column] = played_piece

        # For every valid play direction,
        # flip the spaces of the opposite player's symbol to the current player's symbol:
        if "up" in self.validate_directions(color, piece_position):
            up_row = row - 1
            while self._board[up_row][column] == opposing_piece:
                self._board[up_row][column] = played_piece
                up_row -= 1

        if "down" in self.validate_directions(color, piece_position):
            down_row = row + 1
            while self._board[down_row][column] == opposing_piece:
                self._board[down_row][column] = played_piece
                down_row += 1

        if "left" in self.validate_directions(color, piece_position):
            left_column = column - 1
            while self._board[row][left_column] == opposing_piece:
                self._board[row][left_column] = played_piece
                left_column -= 1

        if "right" in self.validate_directions(color, piece_position):
            right_column = column + 1
            while self._board[row][right_column] == opposing_piece:
                self._board[row][right_column] = played_piece
                right_column += 1

        if "upper left" in self.validate_directions(color, piece_position):
            up_row = row - 1
            left_column = column - 1
            while self._board[up_row][left_column] == opposing_piece:
                self._board[up_row][left_column] = played_piece
                up_row -= 1
                left_column += 1

        if "upper right" in self.validate_directions(color, piece_position):
            up_row = row - 1
            right_column = column + 1
            while self._board[up_row][right_column] == opposing_piece:
                self._board[up_row][right_column] = played_piece
                up_row -= 1
                right_column += 1

        if "lower left" in self.validate_directions(color, piece_position):
            down_row = row + 1
            left_column = column - 1
            while self._board[down_row][left_column] == opposing_piece:
                self._board[down_row][left_column] = played_piece
                down_row += 1
                left_column -= 1

        if "lower right" in self.validate_directions(color, piece_position):
            down_row = row + 1
            right_column = column + 1
            while self._board[down_row][right_column] == opposing_piece:
                self._board[down_row][right_column] = played_piece
                down_row += 1
                right_column += 1

        self.check_game_state()  # Check game state after each move
        return self._board

    def play_game(self, player_color, piece_position):
        """Attempts to make a move for the player with the given color at the given position.
        Returns 'Invalid move' and a list of valid moves (if any) if the attempted move is invalid, by calling
        return_available_positions(). Calls return_winner() if the game is over."""

        # If the game has ended, just return winner information:
        if self._game_over:
            print("Game is ended")
            return self.return_winner()

        # Check if the move is out of the board range, and if so, print a list of valid moves:
        if piece_position[0] > 8 or piece_position[0] < 1 or piece_position[1] > 8 or piece_position[1] < 1:
            print("Invalid move. Here are the valid moves:", str(self.return_available_positions(player_color)))
            return "Invalid move"

        # If the given space is empty and has some valid play direction, call make_move() and return:
        if self._board[piece_position[0]][piece_position[1]] == "." and \
                len(self.validate_directions(player_color, piece_position)) > 0:
            self.make_move(player_color, piece_position)
            return

        # Otherwise, the move is invalid; print a list of valid moves:
        else:
            print("Invalid move. Here are the valid moves:", str(self.return_available_positions(player_color)))
            return "Invalid move"
