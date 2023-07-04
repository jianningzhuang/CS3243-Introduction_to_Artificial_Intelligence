import sys
import random

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
# Piece
#############################################################################


class Piece:
    pass

#############################################################################
# Board
#############################################################################


class Board:
    def __init__(self, rows, cols, grid, pieces):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.pieces = {}
        self.num_pieces = len(pieces)
        self.heuristics = -1
        self.threatening = {}
        self.threatened_by = {}

        for coords, piece in pieces.items():
            self.pieces[coords] = piece

    def count_threats(self, coords, piece):
        piece_row = coords[0]
        piece_col = coords[1]

        if piece == "King":
            if (piece_row > 0 and (piece_row - 1, piece_col) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col)] += 1
            if (piece_col > 0 and (piece_row, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row, piece_col - 1)] += 1
            if (piece_row < self.rows - 1 and (piece_row + 1, piece_col) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col)] += 1
            if (piece_col < self.cols - 1 and (piece_row, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row, piece_col + 1)] += 1
            if (piece_row > 0 and piece_col > 0 and (piece_row - 1, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col - 1)] += 1
            if (piece_row > 0 and piece_col < self.cols - 1 and (piece_row - 1, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col + 1)] += 1
            if (piece_row < self.rows - 1 and piece_col < self.cols - 1 and (piece_row + 1, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col + 1)] += 1
            if (piece_row < self.rows - 1 and piece_col > 0 and (piece_row + 1, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col - 1)] += 1

        elif piece == "Rook":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                if (cur_row - 1, cur_col) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col)] += 1
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                if (cur_row + 1, cur_col) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col)] += 1
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                if (cur_row, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row, cur_col - 1)] += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                if (cur_row, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row, cur_col + 1)] += 1
                cur_col += 1

        elif piece == "Bishop":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                if (cur_row - 1, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col - 1)] += 1
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                if (cur_row + 1, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col - 1)] += 1
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                if (cur_row - 1, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col + 1)] += 1
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                if (cur_row + 1, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col + 1)] += 1
                cur_row += 1
                cur_col += 1

        elif piece == "Queen":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                if (cur_row - 1, cur_col) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col)] += 1
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                if (cur_row + 1, cur_col) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col)] += 1
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                if (cur_row, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row, cur_col - 1)] += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                if (cur_row, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row, cur_col + 1)] += 1
                cur_col += 1

            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                if (cur_row - 1, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col - 1)] += 1
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                if (cur_row + 1, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col - 1)] += 1
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                if (cur_row - 1, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col + 1)] += 1
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                if (cur_row + 1, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col + 1)] += 1
                cur_row += 1
                cur_col += 1

        elif piece == "Knight":
            if (piece_row > 0 and piece_col > 1 and (piece_row - 1, piece_col - 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col - 2) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col - 2)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col - 2)] += 1
            if (piece_row > 1 and piece_col > 0 and (piece_row - 2, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 2, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 2, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row - 2, piece_col - 1)] += 1
            if (piece_row > 1 and piece_col < self.cols - 1 and (piece_row - 2, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 2, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 2, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row - 2, piece_col + 1)] += 1
            if (piece_row > 0 and piece_col < self.cols - 2 and (piece_row - 1, piece_col + 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col + 2) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col + 2)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col + 2)] += 1
            if (piece_row < self.rows - 1 and piece_col < self.cols - 2 and (piece_row + 1, piece_col + 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col + 2) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col + 2)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col + 2)] += 1
            if (piece_row < self.rows - 2 and piece_col < self.cols - 1 and (piece_row + 2, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 2, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 2, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row + 2, piece_col + 1)] += 1
            if (piece_row < self.rows - 2 and piece_col > 0 and (piece_row + 2, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 2, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 2, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row + 2, piece_col - 1)] += 1
            if (piece_row < self.rows - 1 and piece_col > 1 and (piece_row + 1, piece_col - 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col - 2) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col - 2)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col - 2)] += 1

        elif piece == "Ferz":
            if (piece_row > 0 and piece_col > 0 and (piece_row - 1, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col - 1)] += 1
            if (piece_row > 0 and piece_col < self.cols - 1 and (piece_row - 1, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col + 1)] += 1
            if (piece_row < self.rows - 1 and piece_col < self.cols - 1 and (piece_row + 1, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col + 1)] += 1
            if (piece_row < self.rows - 1 and piece_col > 0 and (piece_row + 1, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col - 1)] += 1

        elif piece == "Princess":
            if (piece_row > 0 and piece_col > 1 and (piece_row - 1, piece_col - 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col - 2) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col - 2)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col - 2)] += 1
            if (piece_row > 1 and piece_col > 0 and (piece_row - 2, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 2, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 2, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row - 2, piece_col - 1)] += 1
            if (piece_row > 1 and piece_col < self.cols - 1 and (piece_row - 2, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 2, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 2, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row - 2, piece_col + 1)] += 1
            if (piece_row > 0 and piece_col < self.cols - 2 and (piece_row - 1, piece_col + 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col + 2) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col + 2)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col + 2)] += 1
            if (piece_row < self.rows - 1 and piece_col < self.cols - 2 and (piece_row + 1, piece_col + 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col + 2) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col + 2)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col + 2)] += 1
            if (piece_row < self.rows - 2 and piece_col < self.cols - 1 and (piece_row + 2, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 2, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 2, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row + 2, piece_col + 1)] += 1
            if (piece_row < self.rows - 2 and piece_col > 0 and (piece_row + 2, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 2, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 2, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row + 2, piece_col - 1)] += 1
            if (piece_row < self.rows - 1 and piece_col > 1 and (piece_row + 1, piece_col - 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col - 2) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col - 2)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col - 2)] += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                if (cur_row - 1, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col - 1)] += 1
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                if (cur_row + 1, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col - 1)] += 1
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                if (cur_row - 1, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col + 1)] += 1
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                if (cur_row + 1, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col + 1)] += 1
                cur_row += 1
                cur_col += 1

        elif piece == "Empress":
            if (piece_row > 0 and piece_col > 1 and (piece_row - 1, piece_col - 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col - 2) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col - 2)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col - 2)] += 1
            if (piece_row > 1 and piece_col > 0 and (piece_row - 2, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 2, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 2, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row - 2, piece_col - 1)] += 1
            if (piece_row > 1 and piece_col < self.cols - 1 and (piece_row - 2, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 2, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row - 2, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row - 2, piece_col + 1)] += 1
            if (piece_row > 0 and piece_col < self.cols - 2 and (piece_row - 1, piece_col + 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row - 1, piece_col + 2) not in self.threatened_by:
                    self.threatened_by[(piece_row - 1, piece_col + 2)] = 1
                else:
                    self.threatened_by[(piece_row - 1, piece_col + 2)] += 1
            if (piece_row < self.rows - 1 and piece_col < self.cols - 2 and (piece_row + 1, piece_col + 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col + 2) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col + 2)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col + 2)] += 1
            if (piece_row < self.rows - 2 and piece_col < self.cols - 1 and (piece_row + 2, piece_col + 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 2, piece_col + 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 2, piece_col + 1)] = 1
                else:
                    self.threatened_by[(piece_row + 2, piece_col + 1)] += 1
            if (piece_row < self.rows - 2 and piece_col > 0 and (piece_row + 2, piece_col - 1) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 2, piece_col - 1) not in self.threatened_by:
                    self.threatened_by[(piece_row + 2, piece_col - 1)] = 1
                else:
                    self.threatened_by[(piece_row + 2, piece_col - 1)] += 1
            if (piece_row < self.rows - 1 and piece_col > 1 and (piece_row + 1, piece_col - 2) in self.pieces):
                if coords not in self.threatening:
                    self.threatening[coords] = 1
                else:
                    self.threatening[coords] += 1
                if (piece_row + 1, piece_col - 2) not in self.threatened_by:
                    self.threatened_by[(piece_row + 1, piece_col - 2)] = 1
                else:
                    self.threatened_by[(piece_row + 1, piece_col - 2)] += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                if (cur_row - 1, cur_col) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row - 1, cur_col) not in self.threatened_by:
                        self.threatened_by[(cur_row - 1, cur_col)] = 1
                    else:
                        self.threatened_by[(cur_row - 1, cur_col)] += 1
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                if (cur_row + 1, cur_col) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row + 1, cur_col) not in self.threatened_by:
                        self.threatened_by[(cur_row + 1, cur_col)] = 1
                    else:
                        self.threatened_by[(cur_row + 1, cur_col)] += 1
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                if (cur_row, cur_col - 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row, cur_col - 1) not in self.threatened_by:
                        self.threatened_by[(cur_row, cur_col - 1)] = 1
                    else:
                        self.threatened_by[(cur_row, cur_col - 1)] += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                if (cur_row, cur_col + 1) in self.pieces:
                    if coords not in self.threatening:
                        self.threatening[coords] = 1
                    else:
                        self.threatening[coords] += 1
                    if (cur_row, cur_col + 1) not in self.threatened_by:
                        self.threatened_by[(cur_row, cur_col + 1)] = 1
                    else:
                        self.threatened_by[(cur_row, cur_col + 1)] += 1
                cur_col += 1

    def update_threats(self):
        self.heuristics = 0
        self.threatening = {}
        self.threatened_by = {}
        for coords, piece in self.pieces.items():
            self.count_threats(coords, piece)
        for coords, piece in self.pieces.items():
            if coords in self.threatening:
                self.heuristics += self.threatening[coords]
            if coords in self.threatened_by:
                self.heuristics += self.threatened_by[coords]

    def remove_worst_piece(self):

        worst_piece = None
        worst_value = -1
        for coords, piece in self.pieces.items():
            current_value = 0
            if coords in self.threatening:
                current_value += self.threatening[coords]
            if coords in self.threatened_by:
                current_value += self.threatened_by[coords]
            if worst_piece is None or current_value > worst_value:
                worst_piece = coords
                worst_value = current_value

        # worst_piece = random.choice(list(self.threatened_by.keys()))

        # print("Worst Piece is : " + str(worst_piece))

        self.pieces.pop(worst_piece)
        self.num_pieces = len(self.pieces)

        # print("Pieces Left : " + str(self.num_pieces))


#############################################################################
# State
#############################################################################


class State:
    pass


def initial_state(rows, cols, grid, pieces):
    board = Board(rows, cols, grid, pieces)
    random_piece = random.choice(list(board.pieces.keys()))
    board.pieces.pop(random_piece)
    board.num_pieces = len(board.pieces)
    board.update_threats()
    return board


def is_goal(board):
    return board.heuristics == 0


def generate_goal_state(board):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    goal_state = {}
    for coords, piece in board.pieces.items():
        goal_state[(alphabet[coords[1]], coords[0])] = piece
    return goal_state


#############################################################################
# Implement Search Algorithm
#############################################################################


def search(rows, cols, grid, pieces, k):

    min_remaining = int(k)

    current = None
    while current is None or not is_goal(current):

        current = initial_state(rows, cols, grid, pieces)
        while True:
            current_value = current.heuristics
            current.remove_worst_piece()
            current.update_threats()
            successor_value = current.heuristics

            if is_goal(current):
                break
            if successor_value >= current_value:
                break
            if current.num_pieces <= min_remaining:
                break

    return generate_goal_state(current)


#############################################################################
# Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
def parse(testcase):
    handle = open(testcase, "r")

    def get_par(x): return x.split(":")[1]
    rows = int(get_par(handle.readline()))
    cols = int(get_par(handle.readline()))
    grid = [[0 for j in range(cols)] for i in range(rows)]
    k = 0
    pieces = {}

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()

    k = handle.readline().split(":")[1]  # Read in value of k

    piece_nums = get_par(handle.readline()).split()
    num_pieces = 0
    for num in piece_nums:
        num_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        pieces[coords] = piece

    return rows, cols, grid, pieces, k


def add_piece(comma_seperated):
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r, c), piece]

# Returns row and col index in integers respectively


def from_chess_coord(ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces (String): King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}


def run_local():
    testcase = sys.argv[1]  # Do not remove. This is your input testfile.
    rows, cols, grid, pieces, k = parse(testcase)
    goalstate = search(rows, cols, grid, pieces, k)
    return goalstate  # Format to be returned


# print(run_local())
