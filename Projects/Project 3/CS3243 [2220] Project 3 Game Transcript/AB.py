from copy import deepcopy
import sys

# IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
# The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove


class Piece:

    PIECES = {
        "King": "K",
        "Queen": "Q",
        "Rook": "R",
        "Bishop": "B",
        "Knight": "N",
        "Pawn": "P",
        "Attack": "!"
    }

    ASCII_OFFSET = ord('a')

    def __init__(self,
                 piece_type: str,
                 current_position: tuple,
                 player: bool):

        # metadata
        self.piece_type: str = piece_type
        self.symbol: str = self.PIECES[self.piece_type]

        # functional data
        self.current_position: tuple = current_position
        self.player: bool = player

    def possibleplays(self, board) -> list:  # list of (start, stop)

        col, row = self.current_position

        # ===== HELPER FUNCTIONS =====

        def kingplays():
            possibleplays = []
            for col_offset in range(-1, 2):
                for row_offset in range(-1, 2):

                    # ignore current position
                    if row_offset == 0 and col_offset == 0:
                        continue

                    # find valid positions
                    new_col = col + col_offset
                    new_row = row + row_offset
                    new_position = (new_col, new_row)

                    # valid position, unoccupied or can attack
                    if (board.positioninboard(new_position)
                        and (not board.positionoccupied(new_position)
                             or board.pieceatposition_differentplayer(new_position, self.player))):
                        possibleplays.append(new_position)

            return possibleplays

        def queenplays():
            possibleplays = []

            # go left
            for col_offset in range(1, board.columns):

                new_col = col - col_offset
                new_row = row
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go right
            for col_offset in range(1, board.columns):
                new_col = col + col_offset
                new_row = row
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go up
            for row_offset in range(1, board.rows):
                new_col = col
                new_row = row + row_offset
                new_position = (new_col, new_row)

                if row_offset == 0:
                    continue

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go down
            for row_offset in range(1, board.rows):
                new_col = col
                new_row = row - row_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # diagonals have a max bound
            max_offset = max(board.rows, board.columns)

            # go up left
            for diagonal_offset in range(1, max_offset):
                new_col = col - diagonal_offset
                new_row = row + diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go up right
            for diagonal_offset in range(1, max_offset):
                new_col = col + diagonal_offset
                new_row = row + diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go down left
            for diagonal_offset in range(1, max_offset):
                new_col = col - diagonal_offset
                new_row = row - diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go down right
            for diagonal_offset in range(1, max_offset):
                new_col = col + diagonal_offset
                new_row = row - diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            return possibleplays

        def rookplays():
            possibleplays = []

            # go left
            for col_offset in range(1, board.columns):
                new_col = col - col_offset
                new_row = row
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go right
            for col_offset in range(1, board.columns):
                new_col = col + col_offset
                new_row = row
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go up
            for row_offset in range(1, board.rows):
                new_col = col
                new_row = row + row_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go down
            for row_offset in range(1, board.rows):
                new_col = col
                new_row = row - row_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            return possibleplays

        def bishopplays():
            possibleplays = []

            # diagonals have a max bound
            max_offset = max(board.rows, board.columns)

            # go up left
            for diagonal_offset in range(1, max_offset):
                new_col = col - diagonal_offset
                new_row = row + diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go up right
            for diagonal_offset in range(1, max_offset):
                new_col = col + diagonal_offset
                new_row = row + diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go down left
            for diagonal_offset in range(1, max_offset):
                new_col = col - diagonal_offset
                new_row = row - diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            # go down right
            for diagonal_offset in range(1, max_offset):
                new_col = col + diagonal_offset
                new_row = row - diagonal_offset
                new_position = (new_col, new_row)

                # valid position, unoccupied or can attack
                if (board.positioninboard(new_position)
                    and (not board.positionoccupied(new_position)
                         or board.pieceatposition_differentplayer(new_position, self.player))):
                    possibleplays.append(new_position)

                if (board.positioninboard(new_position)
                        and board.positionoccupied(new_position)):
                    break

            return possibleplays

        def knightplays():
            possibleplays = []
            offset_1 = [1, -1]
            offset_2 = [2, -2]

            # col offset by 1, row offset by 2
            for delta_1 in offset_1:
                for delta_2 in offset_2:
                    new_col = col + delta_1
                    new_row = row + delta_2
                    new_position = (new_col, new_row)

                    # valid position, unoccupied or can attack
                    if (board.positioninboard(new_position)
                        and (not board.positionoccupied(new_position)
                             or board.pieceatposition_differentplayer(new_position, self.player))):
                        possibleplays.append(new_position)

            # col offset by 2, row offset by 1
            for delta_1 in offset_1:
                for delta_2 in offset_2:
                    new_col = col + delta_2
                    new_row = row + delta_1
                    new_position = (new_col, new_row)

                    # valid position, unoccupied or can attack
                    if (board.positioninboard(new_position)
                        and (not board.positionoccupied(new_position)
                             or board.pieceatposition_differentplayer(new_position, self.player))):
                        possibleplays.append(new_position)

            return possibleplays

        def pawnplays():

            possibleplays = []

            direction = 1
            if not self.player:  # is MIN player, go in negative direction vertically
                direction *= -1

            # attacks
            for col_offset in (-1, 1):
                new_col = col + col_offset
                new_row = row + direction
                new_position = (new_col, new_row)
                if (board.positioninboard(new_position)
                        and board.pieceatposition_differentplayer(new_position, self.player)):
                    possibleplays.append(new_position)

            # move
            new_col = col
            new_row = row + direction
            new_position = (new_col, new_row)
            if (board.positioninboard(new_position)
                    and not board.positionoccupied(new_position)):
                possibleplays.append(new_position)

            return possibleplays

        if self.piece_type == "King":
            return kingplays()
        elif self.piece_type == "Queen":
            return queenplays()
        elif self.piece_type == "Rook":
            return rookplays()
        elif self.piece_type == "Bishop":
            return bishopplays()
        elif self.piece_type == "Knight":
            return knightplays()
        elif self.piece_type == "Pawn":
            return pawnplays()
        else:
            # pass
            raise RuntimeError(
                "Unidentified piece type calling possibleplays!")

    @staticmethod
    def asciistr_to_xy(ascii_position: str) -> tuple((int, int)):
        assert (len(ascii_position) <= 3)
        col, row = ascii_position[0], ascii_position[1:]
        col, row = int(ord(col) - Piece.ASCII_OFFSET), int(row)
        return (col, row)

    @staticmethod
    def xy_to_asciituple(position: tuple((int, int))) -> str:
        col, row = position
        return (chr(col + Piece.ASCII_OFFSET), row)

    @staticmethod
    def asciituple_to_xy(ascii_position: tuple) -> tuple((int, int)):
        col, row = ascii_position
        col, row = int(ord(col) - Piece.ASCII_OFFSET), int(row)
        return (col, row)

    def position_as_asciituple(self):
        return Piece.xy_to_asciituple(self.current_position)

    def setposition(self, position: tuple):
        self.current_position = position

    def clearposition(self):
        self.current_position = None

    def __repr__(self) -> str:
        if not self.player:
            return "\033[1;33m" + self.symbol + "\033[0;0m"  # red

        return "\033[1;32m" + self.symbol + "\033[0;0m"  # green

    def __str__(self) -> str:
        return self.symbol


class Board:

    def __init__(self, rows: int, columns: int):

        # metadata
        self.rows: int = rows
        self.columns: int = columns

        # attacks
        self.attacks_grid: list(list(int)) = [
            [0 for x in range(self.columns)] for y in range(self.rows)]

        # pieces, (x,y) -> piece
        self.max_pieces: dict = dict()
        self.min_pieces: dict = dict()

        # king
        self.max_king: Piece = None
        self.min_king: Piece = None

        # flags
        self.terminal = False

    # ===== INTERNAL METHODS =====

    def reset_attacks_grid(self):
        self.attacks_grid: list(list(int)) = [
            [0 for x in range(self.columns)] for y in range(self.rows)]

    # ===== FUNCTIONAL EXTERNAL METHODS =====

    def positioninboard(self, position: tuple) -> bool:
        col, row = position
        return (col < self.columns and col >= 0) and (row < self.rows and row >= 0)

    def positionoccupied(self, position: tuple) -> bool:
        max_piece = self.max_pieces.get(position)
        min_piece = self.min_pieces.get(position)
        return not ((max_piece is None) and (min_piece is None))

    def pieceatposition_differentplayer(self, position: tuple, maximisingplayer: bool) -> bool:

        # assumes position is within bounds of board
        # if no piece, returns true
        max_piece = self.max_pieces.get(position)
        min_piece = self.min_pieces.get(position)
        if max_piece is not None:
            return not maximisingplayer
        elif min_piece is not None:
            return maximisingplayer
        else:
            return True  # by default, since no piece in position

    def setpiece(self, position: tuple, piece: Piece, is_king: bool, maximisingplayer: bool):
        if maximisingplayer:
            self.max_pieces[position] = piece
            if is_king:
                self.max_king = piece
        else:
            self.min_pieces[position] = piece
            if is_king:
                self.min_king = piece

    # ===== GAME EXTERNAL METHODS =====

    def getpossiblemoves(self, maximisingplayer: bool) -> list:
        possibleplays = []

        if maximisingplayer:
            pieces = self.max_pieces
        else:
            pieces = self.min_pieces

        for position, piece in pieces.items():
            piece: Piece = piece
            for new_position in piece.possibleplays(self):
                possibleplays.append((position, new_position))
        return possibleplays

    def applyplay(self, play: tuple, maximisingplayer: bool):

        start, end = play
        self.reset_attacks_grid()
        copy_board = deepcopy(self)

        if maximisingplayer:

            # move starting player
            max_piece = copy_board.max_pieces.pop(start)
            copy_board.max_pieces[end] = max_piece

            # remove ending opponent, if applicable
            if copy_board.min_pieces.get(end) is not None:
                copy_board.min_pieces.pop(end)

        else:

            # move starting player
            min_piece = copy_board.min_pieces.pop(start)
            copy_board.min_pieces[end] = min_piece

            # remove ending opponent, if applicable
            if copy_board.max_pieces.get(end) is not None:
                copy_board.max_pieces.pop(end)

        return copy_board  # copy

    def isterminal(self, maximisingplayer: bool) -> bool:

        # initialize
        attacked = False
        if maximisingplayer:
            attacking_pieces = self.min_pieces
            king = self.max_king
        else:
            attacking_pieces = self.max_pieces
            king = self.min_king

        # see if king is attacked
        for position, piece in attacking_pieces.items():
            for new_position in piece.possibleplays(self):
                if king.current_position == new_position:
                    attacked = True
                    break

        if not attacked:
            return False  # early exit if not attacked

        # get all prospective attacks, break when all possible king moves are attacked
        possible_kingmoves = set(king.possibleplays(self))
        for position, piece in attacking_pieces:
            piece: Piece = piece
            for new_position in piece.possibleplays(self):
                for look_ahead_position in self.applyplay(position, new_position).possibleplays():

                    # if clash, remove
                    if look_ahead_position in possible_kingmoves:
                        possible_kingmoves.pop(look_ahead_position)

                    # no more moves?
                    if len(possible_kingmoves) == 0:
                        self.terminal = True
                        return True

        return False

    def evaluate(self, depth: int, maximisingplayer: bool) -> float:

        def heuristic_by_piece_type():
            PIECES_VALUE = {
                "King": 0,
                "Queen": 9,
                "Rook": 5,
                "Bishop": 3,
                "Knight": 3,
                "Pawn": 1
            }
            if maximisingplayer:
                pieces = self.max_pieces
            else:
                pieces = self.min_pieces

            value = 0
            for _, piece in pieces.items():
                value += PIECES_VALUE[piece.piece_type]
            return value

        def heuristic_by_num_pieces():
            if maximisingplayer:
                return len(self.max_pieces)
            return len(self.min_pieces)

        def winlossdraw():
            assert (depth == 50 or self.terminal)
            if depth == 50:
                return 0
            else:
                win = 1
                if maximisingplayer:
                    win *= -1  # maximising player faced with terminal state
                return win

        if self.terminal or depth == 50:
            return winlossdraw()

        return heuristic_by_piece_type()


# Implement your minimax with alpha-beta pruning algorithm here.
def ab():
    pass


# returns starting position of piece to next position
def alphabeta(board: Board, depth: int, alpha, beta, maximisingplayer: bool) -> tuple:

    CUTOFF = 5

    if depth == CUTOFF or board.isterminal(maximisingplayer):
        eval, move = board.evaluate(depth, maximisingplayer), None
        print("depth is", depth, " player 1:",
              maximisingplayer, " eval:", eval)
        return eval, move

    bestplay = None

    possibleplays = board.getpossiblemoves(maximisingplayer)

    # ===== MAX PLAYER =====
    if maximisingplayer:  # == 1
        value = -1
        for play in possibleplays:
            childstate = board.applyplay(play, maximisingplayer)

            # if better than current value, record
            downstreamvalue, _ = alphabeta(
                childstate, depth + 1, alpha, beta, not maximisingplayer)
            if downstreamvalue > value:
                value = downstreamvalue
                bestplay = play

            alpha = max(alpha, value)  # record max so far for every child

            # prune
            if value >= beta:
                break  # beta cutoff, since value propagated up larger than seen so far, min player won't play

    # ===== MIN PLAYER =====
    else:
        value = 2**32
        for play in possibleplays:
            childstate = board.applyplay(play, maximisingplayer)

            # if better than current value, record
            downstreamvalue, _ = alphabeta(
                childstate, depth + 1, alpha, beta, not maximisingplayer)
            if downstreamvalue < value:
                value = downstreamvalue
                bestplay = play

            beta = min(beta, value)  # record max so far for every child

            # prune
            if value <= alpha:
                break  # alpha cutoff, since value propagated up smaller than seen so far, max player won't play

    return value, bestplay


def parse_gameboard_and_play(gameboard: dict, visualize=False):

    # create board
    board = Board(5, 5)

    for position, playerpiece in gameboard.items():
        position = Piece.asciituple_to_xy(position)
        piece_type, player = playerpiece
        maximisingplayer = (player == "White")
        piece = Piece(piece_type, position, maximisingplayer)
        is_king = piece_type == "King"
        board.setpiece(position, piece, is_king, maximisingplayer)

    if visualize:
        print(board)

    # get move
    eval, move = alphabeta(board, 0, -2**32, 2**32, True)

    # convert move to desired format
    start, end = move
    move = (Piece.xy_to_asciituple(start), Piece.xy_to_asciituple(end))
    return move


def parse(file_path: str):

    # read file piped in
    with open(file_path) as f:
        lines = f.readlines()

    # ===== game board =====
    rows = int(lines[0][5:])
    columns = int(lines[1][5:])

    board = dict()

    # ===== enemy pieces =====
    line_index = 2
    # read number of pieces
    line = lines[line_index]
    num_enemy_pieces = line.split(":")[1].split(" ")
    num_enemy_pieces = sum(map(int, num_enemy_pieces))
    line_index += 2

    # read in positions of pieces and add to board
    for i in range(num_enemy_pieces):

        # read in piece
        line = lines[line_index].strip("[]\n\r")
        piece_type, ascii_position = line.split(",")
        position = Piece.xy_to_asciituple(Piece.asciistr_to_xy(ascii_position))
        board[position] = (piece_type, "Black")

        # next iteration
        line_index += 1

    # ===== friendly pieces =====
    line = lines[line_index]
    num_friendly_pieces = line.split(":")[1].strip("\n").split(" ")
    num_friendly_pieces = sum(map(int, num_friendly_pieces))
    line_index += 2
    for i in range(num_friendly_pieces):

        # read in piece
        line = lines[line_index].strip("[]\n\r")
        piece_type, ascii_position = line.split(",")
        position = Piece.xy_to_asciituple(Piece.asciistr_to_xy(ascii_position))
        board[position] = (piece_type, "White")

        # next iteration
        line_index += 1

    return board


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


def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type

    move = parse_gameboard_and_play(gameboard)
    return move  # Format to be returned (('a', 0), ('b', 3))
