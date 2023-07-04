import sys

# IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
# The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove


class Piece:
    pass


class Knight(Piece):
    pass


class Rook(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass


class Pawn(Piece):
    # New Piece to be implemented
    pass


class Empress(Piece):
    pass


class Ferz(Piece):
    pass


class Princess(Piece):
    pass


class Game:
    pass


class State:
    pass

# Implement your minimax with alpha-beta pruning algorithm here.


def ab():
    pass


#############################################################################
# Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(config):
    handle = open(config, "r")

    def get_par(x): return x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    pieces = {}

    enemy_piece_nums = get_par(handle.readline()).split()
    enemy_num_pieces = 0
    for num in enemy_piece_nums:
        enemy_num_pieces += int(num)

    handle.readline()
    for i in range(enemy_num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = (piece, 'Black')

    own_piece_nums = get_par(handle.readline()).split()
    own_num_pieces = 0
    for num in own_piece_nums:
        own_num_pieces += int(num)

    handle.readline()
    for i in range(own_num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = (piece, 'White')

    return rows, cols, pieces


def add_piece(comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r, c), piece]


def from_chess_coord(ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))


seven_by_seven = {('a', 1): ('Ferz', 'White'), ('a', 5): ('Ferz', 'Black'), ('g', 1): ('Ferz', 'White'), ('g', 5): ('Ferz', 'Black'), ('b', 1): ('Pawn', 'White'), ('b', 5): ('Pawn', 'Black'), ('c', 1): ('Pawn', 'White'), ('c', 5): ('Pawn', 'Black'), ('d', 1): ('Pawn', 'White'), ('d', 5): ('Pawn', 'Black'), ('e', 1): ('Pawn', 'White'), ('e', 5): ('Pawn', 'Black'), ('f', 1): ('Pawn', 'White'), ('f', 5): ('Pawn', 'Black'), ('a', 0): (
    'Knight', 'White'), ('a', 6): ('Knight', 'Black'), ('b', 0): ('Bishop', 'White'), ('b', 6): ('Bishop', 'Black'), ('c', 0): ('Queen', 'White'), ('c', 6): ('Queen', 'Black'), ('d', 0): ('King', 'White'), ('d', 6): ('King', 'Black'), ('e', 0): ('Princess', 'White'), ('e', 6): ('Princess', 'Black'), ('f', 0): ('Empress', 'White'), ('f', 6):  ('Empress', 'Black'), ('g', 0):  ('Rook', 'White'), ('g', 6):  ('Rook', 'Black')}


def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    # OPTIONAL (Since you can hardcode the board): Takes in config.txt
    config = sys.argv[1]
    row, col, pieces = parse(config)
    print(pieces)

    move = (None, None)
    return move  # Format to be returned (('a', 0), ('b', 3))


print(studentAgent(seven_by_seven))
