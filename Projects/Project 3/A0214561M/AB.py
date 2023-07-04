import sys
import math

# IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
# The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove


class Game:
    def __init__(self, my_pieces, enemy_pieces):
        self.my_pieces = my_pieces
        self.enemy_pieces = enemy_pieces
        self.turn = 'White'
        self.depth = 0
        self.max_depth = 3

    def result(self, action):
        old_row, old_col = action[1]
        new_row, new_col = action[2]
        piece = self.my_pieces[(old_row, old_col)]
        new_my_pieces = self.my_pieces.copy()
        new_enemy_pieces = self.enemy_pieces.copy()
        new_my_pieces.pop((old_row, old_col))
        new_my_pieces[(new_row, new_col)] = piece
        if (new_row, new_col) in self.enemy_pieces:
            new_enemy_pieces.pop((new_row, new_col))
        next_state = Game(new_enemy_pieces, new_my_pieces)
        if self.turn == 'White':
            next_state.turn = 'Black'
        else:
            next_state.turn = 'White'
        next_state.depth = self.depth + 1

        return next_state

    def cutoff_test(self):
        return self.depth >= self.max_depth

    def utility(self):
        heuristic_values = {"King": 900, "Queen": 90, "Empress": 80, "Princess": 70,
                            "Rook": 50, "Bishop": 30, "Knight": 30, "Ferz": 20, "Pawn": 10}
        heuristic = 0
        if self.turn == "White":
            for coords, piece in self.my_pieces.items():
                heuristic += heuristic_values[piece[0]]
            for coords, piece in self.enemy_pieces.items():
                heuristic -= heuristic_values[piece[0]]
        else:
            for coords, piece in self.enemy_pieces.items():
                heuristic += heuristic_values[piece[0]]
            for coords, piece in self.my_pieces.items():
                heuristic -= heuristic_values[piece[0]]
        return heuristic

    def is_terminal(self):
        for coords, piece in self.my_pieces.items():
            if piece[0] == "King":
                return False
        return True

    def get_moves(self, coords, piece):

        heuristic_values = {"King": 900, "Queen": 90, "Empress": 80, "Princess": 70,
                            "Rook": 50, "Bishop": 30, "Knight": 30, "Ferz": 20, "Pawn": 10}
        moves = []

        piece_row = coords[0]
        piece_col = coords[1]

        if piece[0] == "Queen":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and (cur_row - 1, cur_col) not in self.my_pieces):
                if (cur_row - 1, cur_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col)][0]], coords, (cur_row - 1, cur_col)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col)))
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and (cur_row + 1, cur_col) not in self.my_pieces):
                if (cur_row + 1, cur_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col)][0]], coords, (cur_row + 1, cur_col)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col)))
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and (cur_row, cur_col - 1) not in self.my_pieces):
                if (cur_row, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row, cur_col - 1)][0]], coords, (cur_row, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row, cur_col - 1)))
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < 6 and (cur_row, cur_col + 1) not in self.my_pieces):
                if (cur_row, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row, cur_col + 1)][0]], coords, (cur_row, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row, cur_col + 1)))
                cur_col += 1

            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and (cur_row - 1, cur_col - 1) not in self.my_pieces):
                if (cur_row - 1, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col - 1)][0]], coords, (cur_row - 1, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col - 1)))
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and cur_col > 0 and (cur_row + 1, cur_col - 1) not in self.my_pieces):
                if (cur_row + 1, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col - 1)][0]], coords, (cur_row + 1, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col - 1)))
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < 6 and (cur_row - 1, cur_col + 1) not in self.my_pieces):
                if (cur_row - 1, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col + 1)][0]], coords, (cur_row - 1, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col + 1)))
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and cur_col < 6 and (cur_row + 1, cur_col + 1) not in self.my_pieces):
                if (cur_row + 1, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col + 1)][0]], coords, (cur_row + 1, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col + 1)))
                cur_row += 1
                cur_col += 1

        elif piece[0] == "Empress":
            if (piece_row > 0 and piece_col > 1 and (piece_row - 1, piece_col - 2) not in self.my_pieces):
                if (piece_row - 1, piece_col - 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col - 2)][0]], coords, (piece_row - 1, piece_col - 2)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col - 2)))
            if (piece_row > 1 and piece_col > 0 and (piece_row - 2, piece_col - 1) not in self.my_pieces):
                if (piece_row - 2, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 2, piece_col - 1)][0]], coords, (piece_row - 2, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row - 2, piece_col - 1)))
            if (piece_row > 1 and piece_col < 6 and (piece_row - 2, piece_col + 1) not in self.my_pieces):
                if (piece_row - 2, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 2, piece_col + 1)][0]], coords, (piece_row - 2, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row - 2, piece_col + 1)))
            if (piece_row > 0 and piece_col < 5 and (piece_row - 1, piece_col + 2) not in self.my_pieces):
                if (piece_row - 1, piece_col + 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col + 2)][0]], coords, (piece_row - 1, piece_col + 2)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col + 2)))
            if (piece_row < 6 and piece_col < 5 and (piece_row + 1, piece_col + 2) not in self.my_pieces):
                if (piece_row + 1, piece_col + 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col + 2)][0]], coords, (piece_row + 1, piece_col + 2)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col + 2)))
            if (piece_row < 5 and piece_col < 6 and (piece_row + 2, piece_col + 1) not in self.my_pieces):
                if (piece_row + 2, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 2, piece_col + 1)][0]], coords, (piece_row + 2, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row + 2, piece_col + 1)))
            if (piece_row < 5 and piece_col > 0 and (piece_row + 2, piece_col - 1) not in self.my_pieces):
                if (piece_row + 2, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 2, piece_col - 1)][0]], coords, (piece_row + 2, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row + 2, piece_col - 1)))
            if (piece_row < 6 and piece_col > 1 and (piece_row + 1, piece_col - 2) not in self.my_pieces):
                if (piece_row + 1, piece_col - 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col - 2)][0]], coords, (piece_row + 1, piece_col - 2)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col - 2)))

            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and (cur_row - 1, cur_col) not in self.my_pieces):
                if (cur_row - 1, cur_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col)][0]], coords, (cur_row - 1, cur_col)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col)))
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and (cur_row + 1, cur_col) not in self.my_pieces):
                if (cur_row + 1, cur_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col)][0]], coords, (cur_row + 1, cur_col)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col)))
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and (cur_row, cur_col - 1) not in self.my_pieces):
                if (cur_row, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row, cur_col - 1)][0]], coords, (cur_row, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row, cur_col - 1)))
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < 6 and (cur_row, cur_col + 1) not in self.my_pieces):
                if (cur_row, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row, cur_col + 1)][0]], coords, (cur_row, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row, cur_col + 1)))
                cur_col += 1

        elif piece[0] == "Princess":
            if (piece_row > 0 and piece_col > 1 and (piece_row - 1, piece_col - 2) not in self.my_pieces):
                if (piece_row - 1, piece_col - 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col - 2)][0]], coords, (piece_row - 1, piece_col - 2)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col - 2)))
            if (piece_row > 1 and piece_col > 0 and (piece_row - 2, piece_col - 1) not in self.my_pieces):
                if (piece_row - 2, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 2, piece_col - 1)][0]], coords, (piece_row - 2, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row - 2, piece_col - 1)))
            if (piece_row > 1 and piece_col < 6 and (piece_row - 2, piece_col + 1) not in self.my_pieces):
                if (piece_row - 2, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 2, piece_col + 1)][0]], coords, (piece_row - 2, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row - 2, piece_col + 1)))
            if (piece_row > 0 and piece_col < 5 and (piece_row - 1, piece_col + 2) not in self.my_pieces):
                if (piece_row - 1, piece_col + 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col + 2)][0]], coords, (piece_row - 1, piece_col + 2)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col + 2)))
            if (piece_row < 6 and piece_col < 5 and (piece_row + 1, piece_col + 2) not in self.my_pieces):
                if (piece_row + 1, piece_col + 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col + 2)][0]], coords, (piece_row + 1, piece_col + 2)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col + 2)))
            if (piece_row < 5 and piece_col < 6 and (piece_row + 2, piece_col + 1) not in self.my_pieces):
                if (piece_row + 2, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 2, piece_col + 1)][0]], coords, (piece_row + 2, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row + 2, piece_col + 1)))
            if (piece_row < 5 and piece_col > 0 and (piece_row + 2, piece_col - 1) not in self.my_pieces):
                if (piece_row + 2, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 2, piece_col - 1)][0]], coords, (piece_row + 2, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row + 2, piece_col - 1)))
            if (piece_row < 6 and piece_col > 1 and (piece_row + 1, piece_col - 2) not in self.my_pieces):
                if (piece_row + 1, piece_col - 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col - 2)][0]], coords, (piece_row + 1, piece_col - 2)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col - 2)))

            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and (cur_row - 1, cur_col - 1) not in self.my_pieces):
                if (cur_row - 1, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col - 1)][0]], coords, (cur_row - 1, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col - 1)))
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and cur_col > 0 and (cur_row + 1, cur_col - 1) not in self.my_pieces):
                if (cur_row + 1, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col - 1)][0]], coords, (cur_row + 1, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col - 1)))
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < 6 and (cur_row - 1, cur_col + 1) not in self.my_pieces):
                if (cur_row - 1, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col + 1)][0]], coords, (cur_row - 1, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col + 1)))
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and cur_col < 6 and (cur_row + 1, cur_col + 1) not in self.my_pieces):
                if (cur_row + 1, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col + 1)][0]], coords, (cur_row + 1, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col + 1)))
                cur_row += 1
                cur_col += 1

        elif piece[0] == "Rook":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and (cur_row - 1, cur_col) not in self.my_pieces):
                if (cur_row - 1, cur_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col)][0]], coords, (cur_row - 1, cur_col)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col)))
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and (cur_row + 1, cur_col) not in self.my_pieces):
                if (cur_row + 1, cur_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col)][0]], coords, (cur_row + 1, cur_col)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col)))
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and (cur_row, cur_col - 1) not in self.my_pieces):
                if (cur_row, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row, cur_col - 1)][0]], coords, (cur_row, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row, cur_col - 1)))
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < 6 and (cur_row, cur_col + 1) not in self.my_pieces):
                if (cur_row, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row, cur_col + 1)][0]], coords, (cur_row, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row, cur_col + 1)))
                cur_col += 1

        elif piece[0] == "Bishop":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and (cur_row - 1, cur_col - 1) not in self.my_pieces):
                if (cur_row - 1, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col - 1)][0]], coords, (cur_row - 1, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col - 1)))
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and cur_col > 0 and (cur_row + 1, cur_col - 1) not in self.my_pieces):
                if (cur_row + 1, cur_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col - 1)][0]], coords, (cur_row + 1, cur_col - 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col - 1)))
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < 6 and (cur_row - 1, cur_col + 1) not in self.my_pieces):
                if (cur_row - 1, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row - 1, cur_col + 1)][0]], coords, (cur_row - 1, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row - 1, cur_col + 1)))
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < 6 and cur_col < 6 and (cur_row + 1, cur_col + 1) not in self.my_pieces):
                if (cur_row + 1, cur_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        cur_row + 1, cur_col + 1)][0]], coords, (cur_row + 1, cur_col + 1)))
                    break
                else:
                    moves.append((0, coords, (cur_row + 1, cur_col + 1)))
                cur_row += 1
                cur_col += 1

        elif piece[0] == "Knight":
            if (piece_row > 0 and piece_col > 1 and (piece_row - 1, piece_col - 2) not in self.my_pieces):
                if (piece_row - 1, piece_col - 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col - 2)][0]], coords, (piece_row - 1, piece_col - 2)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col - 2)))
            if (piece_row > 1 and piece_col > 0 and (piece_row - 2, piece_col - 1) not in self.my_pieces):
                if (piece_row - 2, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 2, piece_col - 1)][0]], coords, (piece_row - 2, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row - 2, piece_col - 1)))
            if (piece_row > 1 and piece_col < 6 and (piece_row - 2, piece_col + 1) not in self.my_pieces):
                if (piece_row - 2, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 2, piece_col + 1)][0]], coords, (piece_row - 2, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row - 2, piece_col + 1)))
            if (piece_row > 0 and piece_col < 5 and (piece_row - 1, piece_col + 2) not in self.my_pieces):
                if (piece_row - 1, piece_col + 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col + 2)][0]], coords, (piece_row - 1, piece_col + 2)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col + 2)))
            if (piece_row < 6 and piece_col < 5 and (piece_row + 1, piece_col + 2) not in self.my_pieces):
                if (piece_row + 1, piece_col + 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col + 2)][0]], coords, (piece_row + 1, piece_col + 2)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col + 2)))
            if (piece_row < 5 and piece_col < 6 and (piece_row + 2, piece_col + 1) not in self.my_pieces):
                if (piece_row + 2, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 2, piece_col + 1)][0]], coords, (piece_row + 2, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row + 2, piece_col + 1)))
            if (piece_row < 5 and piece_col > 0 and (piece_row + 2, piece_col - 1) not in self.my_pieces):
                if (piece_row + 2, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 2, piece_col - 1)][0]], coords, (piece_row + 2, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row + 2, piece_col - 1)))
            if (piece_row < 6 and piece_col > 1 and (piece_row + 1, piece_col - 2) not in self.my_pieces):
                if (piece_row + 1, piece_col - 2) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col - 2)][0]], coords, (piece_row + 1, piece_col - 2)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col - 2)))

        elif piece[0] == "Ferz":
            if (piece_row > 0 and piece_col > 0 and (piece_row - 1, piece_col - 1) not in self.my_pieces):
                if (piece_row - 1, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col - 1)][0]], coords, (piece_row - 1, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col - 1)))
            if (piece_row > 0 and piece_col < 6 and (piece_row - 1, piece_col + 1) not in self.my_pieces):
                if (piece_row - 1, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col + 1)][0]], coords, (piece_row - 1, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col + 1)))
            if (piece_row < 6 and piece_col < 6 and (piece_row + 1, piece_col + 1) not in self.my_pieces):
                if (piece_row + 1, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col + 1)][0]], coords, (piece_row + 1, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col + 1)))
            if (piece_row < 6 and piece_col > 0 and (piece_row + 1, piece_col - 1) not in self.my_pieces):
                if (piece_row + 1, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col - 1)][0]], coords, (piece_row + 1, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col - 1)))

        elif piece[0] == "Pawn":
            if piece[1] == "White":
                if (piece_row < 6 and (piece_row + 1, piece_col) not in self.my_pieces and (piece_row + 1, piece_col) not in self.enemy_pieces):
                    moves.append((0, coords, (piece_row + 1, piece_col)))
                if (piece_row < 6 and piece_col < 6 and (piece_row + 1, piece_col + 1) in self.enemy_pieces):
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col + 1)][0]], coords, (piece_row + 1, piece_col + 1)))
                if (piece_row < 6 and piece_col > 0 and (piece_row + 1, piece_col - 1) in self.enemy_pieces):
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col - 1)][0]], coords, (piece_row + 1, piece_col - 1)))
            else:
                if (piece_row > 0 and (piece_row - 1, piece_col) not in self.my_pieces and (piece_row - 1, piece_col) not in self.enemy_pieces):
                    moves.append((0, coords, (piece_row - 1, piece_col)))
                if (piece_row > 0 and piece_col > 0 and (piece_row - 1, piece_col - 1) in self.enemy_pieces):
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col - 1)][0]], coords, (piece_row - 1, piece_col - 1)))
                if (piece_row > 0 and piece_col < 6 and (piece_row - 1, piece_col + 1) in self.enemy_pieces):
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col + 1)][0]], coords, (piece_row - 1, piece_col + 1)))

        elif piece[0] == "King":
            if (piece_row > 0 and (piece_row - 1, piece_col) not in self.my_pieces):
                if (piece_row - 1, piece_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col)][0]], coords, (piece_row - 1, piece_col)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col)))
            if (piece_col > 0 and (piece_row, piece_col - 1) not in self.my_pieces):
                if (piece_row, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row, piece_col - 1)][0]], coords, (piece_row - 1, piece_col)))
                else:
                    moves.append((0, coords, (piece_row, piece_col - 1)))
            if (piece_row < 6 and (piece_row + 1, piece_col) not in self.my_pieces):
                if (piece_row + 1, piece_col) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col)][0]], coords, (piece_row + 1, piece_col)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col)))
            if (piece_col < 6 and (piece_row, piece_col + 1) not in self.my_pieces):
                if (piece_row, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row, piece_col + 1)][0]], coords, (piece_row, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row, piece_col + 1)))
            if (piece_row > 0 and piece_col > 0 and (piece_row - 1, piece_col - 1) not in self.my_pieces):
                if (piece_row - 1, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col - 1)][0]], coords, (piece_row - 1, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col - 1)))
            if (piece_row > 0 and piece_col < 6 and (piece_row - 1, piece_col + 1) not in self.my_pieces):
                if (piece_row - 1, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row - 1, piece_col + 1)][0]], coords, (piece_row - 1, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row - 1, piece_col + 1)))
            if (piece_row < 6 and piece_col < 6 and (piece_row + 1, piece_col + 1) not in self.my_pieces):
                if (piece_row + 1, piece_col + 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col + 1)][0]], coords, (piece_row + 1, piece_col + 1)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col + 1)))
            if (piece_row < 6 and piece_col > 0 and (piece_row + 1, piece_col - 1) not in self.my_pieces):
                if (piece_row + 1, piece_col - 1) in self.enemy_pieces:
                    moves.append((heuristic_values[self.enemy_pieces[(
                        piece_row + 1, piece_col - 1)][0]], coords, (piece_row + 1, piece_col - 1)))
                else:
                    moves.append((0, coords, (piece_row + 1, piece_col - 1)))

        return moves

    def actions(self):
        moves = []
        for coords, piece in self.my_pieces.items():
            moves_for_piece = self.get_moves(coords, piece)
            moves.extend(moves_for_piece)
        return sorted(moves)  # order actions based on value of piece taken


def generate_ch_coord_move(move):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    old_row, old_col = move[1]
    new_row, new_col = move[2]

    return [(alphabet[old_col], old_row), (alphabet[new_col], new_row)]

# Implement your minimax with alpha-beta pruning algorithm here.


def ab(game):
    value, move = max_value(game, -math.inf, math.inf)
    return generate_ch_coord_move(move)


def max_value(game, alpha, beta):
    if game.cutoff_test():
        return game.utility(), None
    if game.is_terminal():  # no more king
        return game.utility(), None
    actions = game.actions()
    # if len(actions) == 0:  # draw
    #    return 0, None
    v = -math.inf
    move = None
    for action in actions:
        next_state = game.result(action)
        v2, a2 = min_value(next_state, alpha, beta)
        if v2 > v:
            v = v2
            move = action
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move


def min_value(game, alpha, beta):
    if game.cutoff_test():
        return game.utility(), None
    if game.is_terminal():  # no more king
        return game.utility(), None
    actions = game.actions()
    # if len(actions) == 0:  # draw
    #    return 0, None
    v = math.inf
    move = None
    for action in actions:
        next_state = game.result(action)
        v2, a2 = max_value(next_state, alpha, beta)
        if v2 < v:
            v = v2
            move = action
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move

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
    return [(ch_coord[0], int(ch_coord[1:])), piece]


def from_chess_coord(ch_coord):
    return (ch_coord[1], ord(ch_coord[0]) - 97)


def initialise_board(rows, cols, pieces):
    my_pieces = {}
    enemy_pieces = {}
    board = [[0 for j in range(cols)] for i in range(rows)]
    for ch_coord, piece in pieces.items():
        r, c = from_chess_coord(ch_coord)
        if piece[1] == 'White':
            my_pieces[(r, c)] = piece
        else:
            enemy_pieces[(r, c)] = piece
        board[r][c] = piece
    return my_pieces, enemy_pieces, board


def initialise_from_gameboard(gameboard):
    my_pieces = {}
    enemy_pieces = {}
    board = [[0 for j in range(7)] for i in range(7)]
    for ch_coord, piece in gameboard.items():
        r, c = from_chess_coord(ch_coord)
        if piece[1] == 'White':
            my_pieces[(r, c)] = piece
        else:
            enemy_pieces[(r, c)] = piece
        board[r][c] = piece
    return my_pieces, enemy_pieces, board


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

minichess = {('a', 1): ('Ferz', 'White'), ('a', 5): ('Ferz', 'Black'), ('g', 1): ('Ferz', 'White'), ('g', 5): ('Ferz', 'Black'), ('b', 1): ('Pawn', 'White'), ('b', 5): ('Pawn', 'Black'), ('c', 1): ('Pawn', 'White'), ('c', 5): ('Pawn', 'Black'), ('d', 1): ('Pawn', 'White'), ('d', 5): ('Pawn', 'Black'), ('e', 1): ('Pawn', 'White'), ('e', 5): ('Pawn', 'Black'), ('f', 1): ('Pawn', 'White'), ('f', 5): ('Pawn', 'Black'), ('a', 0): (
    'Knight', 'White'), ('a', 6): ('Knight', 'Black'), ('b', 0): ('Bishop', 'White'), ('b', 6): ('Bishop', 'Black'), ('c', 0): ('Queen', 'White'), ('c', 6): ('Queen', 'Black'), ('d', 0): ('King', 'White'), ('d', 6): ('King', 'Black'), ('e', 0): ('Princess', 'White'), ('e', 6): ('Princess', 'Black'), ('f', 0): ('Empress', 'White'), ('f', 6):  ('Empress', 'Black'), ('g', 0):  ('Rook', 'White'), ('g', 6):  ('Rook', 'Black')}


def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    # OPTIONAL (Since you can hardcode the board): Takes in config.txt
    # config = sys.argv[1]
    # rows, cols, pieces = parse(config)
    # my_pieces, enemy_pieces, board = initialise_board(rows, cols, pieces)
    my_pieces, enemy_pieces, board = initialise_from_gameboard(gameboard)
    game = Game(my_pieces, enemy_pieces)
    move = ab(game)
    return move  # Format to be returned (('a', 0), ('b', 3))


# print(studentAgent(minichess))
