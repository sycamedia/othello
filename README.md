# othello
Othello game project from CS-162: Intro to Computer Science II at Oregon State University. 

### Rules
- Starting with black, players take turns placing pieces with the goal of capturing the other player's pieces.
- A capture is accomplished when a player places a piece next to an opponent's piece, forming a line (horizontal, vertical or diagonal) with the current player's piece at each end. The opponent's pieces in between are all flipped to the current player's color (this can occur in multiple directions at once.)
- If a player can't make a move, their turn passes to the next player. The game ends when there are no more moves for either player. The winner will have the most pieces on the board. 

### Board
For this text-based game, the 8x8 board is represented with symbols: X for black, O for white, '.' for empty space, and * for the board boundary.

### Playing the Game
This version of Othello is played by calling functions in the Python console:
1. Create an Othello object. 
2. Add two Players with the create_player method.
3. Take turns making a move with the play_game method. 
