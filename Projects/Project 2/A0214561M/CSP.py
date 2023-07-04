import sys

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
    def __init__(self, rows, cols, grid, num_pieces):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.unassigned_pieces = {'King': num_pieces[0], 'Queen': num_pieces[1],
                                  'Bishop': num_pieces[2], 'Rook': num_pieces[3], 'Knight': num_pieces[4], 'Ferz': num_pieces[5], 'Princess': num_pieces[6], 'Empress': num_pieces[7]}
        self.total_num_pieces = sum(num_pieces)
        self.consistent_domains = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != -1:
                    self.consistent_domains.add((i, j))

    def mark_threats(self, coords, piece):

        threats = []

        piece_row = coords[0]
        piece_col = coords[1]

        if piece == "King":
            if (piece_row > 0 and self.grid[piece_row - 1][piece_col] != -1):
                threats.append((piece_row - 1, piece_col))
            if (piece_col > 0 and self.grid[piece_row][piece_col - 1] != -1):
                threats.append((piece_row, piece_col - 1))
            if (piece_row < self.rows - 1 and self.grid[piece_row + 1][piece_col] != -1):
                threats.append((piece_row + 1, piece_col))
            if (piece_col < self.cols - 1 and self.grid[piece_row][piece_col + 1] != -1):
                threats.append((piece_row, piece_col + 1))
            if (piece_row > 0 and piece_col > 0 and self.grid[piece_row - 1][piece_col - 1] != -1):
                threats.append((piece_row - 1, piece_col - 1))
            if (piece_row > 0 and piece_col < self.cols - 1 and self.grid[piece_row - 1][piece_col + 1] != -1):
                threats.append((piece_row - 1, piece_col + 1))
            if (piece_row < self.rows - 1 and piece_col < self.cols - 1 and self.grid[piece_row + 1][piece_col + 1] != -1):
                threats.append((piece_row + 1, piece_col + 1))
            if (piece_row < self.rows - 1 and piece_col > 0 and self.grid[piece_row + 1][piece_col - 1] != -1):
                threats.append((piece_row + 1, piece_col - 1))

        elif piece == "Rook":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                threats.append((cur_row - 1, cur_col))
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                threats.append((cur_row + 1, cur_col))
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                threats.append((cur_row, cur_col - 1))
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                threats.append((cur_row, cur_col + 1))
                cur_col += 1

        elif piece == "Bishop":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                threats.append((cur_row - 1, cur_col - 1))
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                threats.append((cur_row + 1, cur_col - 1))
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                threats.append((cur_row - 1, cur_col + 1))
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                threats.append((cur_row + 1, cur_col + 1))
                cur_row += 1
                cur_col += 1

        elif piece == "Queen":
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                threats.append((cur_row - 1, cur_col))
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                threats.append((cur_row + 1, cur_col))
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                threats.append((cur_row, cur_col - 1))
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                threats.append((cur_row, cur_col + 1))
                cur_col += 1

            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                threats.append((cur_row - 1, cur_col - 1))
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                threats.append((cur_row + 1, cur_col - 1))
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                threats.append((cur_row - 1, cur_col + 1))
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                threats.append((cur_row + 1, cur_col + 1))
                cur_row += 1
                cur_col += 1

        elif piece == "Knight":
            if (piece_row > 0 and piece_col > 1 and self.grid[piece_row - 1][piece_col - 2] != -1):
                threats.append((piece_row - 1, piece_col - 2))
            if (piece_row > 1 and piece_col > 0 and self.grid[piece_row - 2][piece_col - 1] != -1):
                threats.append((piece_row - 2, piece_col - 1))
            if (piece_row > 1 and piece_col < self.cols - 1 and self.grid[piece_row - 2][piece_col + 1] != -1):
                threats.append((piece_row - 2, piece_col + 1))
            if (piece_row > 0 and piece_col < self.cols - 2 and self.grid[piece_row - 1][piece_col + 2] != -1):
                threats.append((piece_row - 1, piece_col + 2))
            if (piece_row < self.rows - 1 and piece_col < self.cols - 2 and self.grid[piece_row + 1][piece_col + 2] != 1):
                threats.append((piece_row + 1, piece_col + 2))
            if (piece_row < self.rows - 2 and piece_col < self.cols - 1 and self.grid[piece_row + 2][piece_col + 1] != -1):
                threats.append((piece_row + 2, piece_col + 1))
            if (piece_row < self.rows - 2 and piece_col > 0 and self.grid[piece_row + 2][piece_col - 1] != -1):
                threats.append((piece_row + 2, piece_col - 1))
            if (piece_row < self.rows - 1 and piece_col > 1 and self.grid[piece_row + 1][piece_col - 2] != -1):
                threats.append((piece_row + 1, piece_col - 2))

        elif piece == "Ferz":
            if (piece_row > 0 and piece_col > 0 and self.grid[piece_row - 1][piece_col - 1] != -1):
                threats.append((piece_row - 1, piece_col - 1))
            if (piece_row > 0 and piece_col < self.cols - 1 and self.grid[piece_row - 1][piece_col + 1] != -1):
                threats.append((piece_row - 1, piece_col + 1))
            if (piece_row < self.rows - 1 and piece_col < self.cols - 1 and self.grid[piece_row + 1][piece_col + 1] != -1):
                threats.append((piece_row + 1, piece_col + 1))
            if (piece_row < self.rows - 1 and piece_col > 0 and self.grid[piece_row + 1][piece_col - 1] != -1):
                threats.append((piece_row + 1, piece_col - 1))

        elif piece == "Princess":
            if (piece_row > 0 and piece_col > 1 and self.grid[piece_row - 1][piece_col - 2] != -1):
                threats.append((piece_row - 1, piece_col - 2))
            if (piece_row > 1 and piece_col > 0 and self.grid[piece_row - 2][piece_col - 1] != -1):
                threats.append((piece_row - 2, piece_col - 1))
            if (piece_row > 1 and piece_col < self.cols - 1 and self.grid[piece_row - 2][piece_col + 1] != -1):
                threats.append((piece_row - 2, piece_col + 1))
            if (piece_row > 0 and piece_col < self.cols - 2 and self.grid[piece_row - 1][piece_col + 2] != -1):
                threats.append((piece_row - 1, piece_col + 2))
            if (piece_row < self.rows - 1 and piece_col < self.cols - 2 and self.grid[piece_row + 1][piece_col + 2] != 1):
                threats.append((piece_row + 1, piece_col + 2))
            if (piece_row < self.rows - 2 and piece_col < self.cols - 1 and self.grid[piece_row + 2][piece_col + 1] != -1):
                threats.append((piece_row + 2, piece_col + 1))
            if (piece_row < self.rows - 2 and piece_col > 0 and self.grid[piece_row + 2][piece_col - 1] != -1):
                threats.append((piece_row + 2, piece_col - 1))
            if (piece_row < self.rows - 1 and piece_col > 1 and self.grid[piece_row + 1][piece_col - 2] != -1):
                threats.append((piece_row + 1, piece_col - 2))
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                threats.append((cur_row - 1, cur_col - 1))
                cur_row -= 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                threats.append((cur_row + 1, cur_col - 1))
                cur_row += 1
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                threats.append((cur_row - 1, cur_col + 1))
                cur_row -= 1
                cur_col += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                threats.append((cur_row + 1, cur_col + 1))
                cur_row += 1
                cur_col += 1

        elif piece == "Empress":
            if (piece_row > 0 and piece_col > 1 and self.grid[piece_row - 1][piece_col - 2] != -1):
                threats.append((piece_row - 1, piece_col - 2))
            if (piece_row > 1 and piece_col > 0 and self.grid[piece_row - 2][piece_col - 1] != -1):
                threats.append((piece_row - 2, piece_col - 1))
            if (piece_row > 1 and piece_col < self.cols - 1 and self.grid[piece_row - 2][piece_col + 1] != -1):
                threats.append((piece_row - 2, piece_col + 1))
            if (piece_row > 0 and piece_col < self.cols - 2 and self.grid[piece_row - 1][piece_col + 2] != -1):
                threats.append((piece_row - 1, piece_col + 2))
            if (piece_row < self.rows - 1 and piece_col < self.cols - 2 and self.grid[piece_row + 1][piece_col + 2] != 1):
                threats.append((piece_row + 1, piece_col + 2))
            if (piece_row < self.rows - 2 and piece_col < self.cols - 1 and self.grid[piece_row + 2][piece_col + 1] != -1):
                threats.append((piece_row + 2, piece_col + 1))
            if (piece_row < self.rows - 2 and piece_col > 0 and self.grid[piece_row + 2][piece_col - 1] != -1):
                threats.append((piece_row + 2, piece_col - 1))
            if (piece_row < self.rows - 1 and piece_col > 1 and self.grid[piece_row + 1][piece_col - 2] != -1):
                threats.append((piece_row + 1, piece_col - 2))
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                threats.append((cur_row - 1, cur_col))
                cur_row -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                threats.append((cur_row + 1, cur_col))
                cur_row += 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                threats.append((cur_row, cur_col - 1))
                cur_col -= 1
            cur_row = piece_row
            cur_col = piece_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                threats.append((cur_row, cur_col + 1))
                cur_col += 1

        return threats

    # MRV tied, go with Degree Heuristic?

    def select_unassigned_variable(self, assignment):
        if self.unassigned_pieces['Queen'] != 0:
            return 'Queen'
        if self.unassigned_pieces['Princess'] != 0:
            return 'Princess'
        if self.unassigned_pieces['Empress'] != 0:
            return 'Empress'
        if self.unassigned_pieces['Ferz'] != 0:
            return 'Ferz'
        if self.unassigned_pieces['Rook'] != 0:
            return 'Rook'
        if self.unassigned_pieces['Bishop'] != 0:
            return 'Bishop'
        if self.unassigned_pieces['Knight'] != 0:
            return 'Knight'
        if self.unassigned_pieces['King'] != 0:
            return 'King'

    def order_domain_values(self, piece, assignment):
        least_constraining_order = []
        for coords in self.consistent_domains:
            threats = self.mark_threats(coords, piece)
            new_threats = []
            for threat in threats:
                if threat in self.consistent_domains:
                    new_threats.append(threat)
            least_constraining_order.append(
                (len(new_threats), coords, threats, new_threats))
        least_constraining_order.sort()
        return least_constraining_order

    def inference(self, coords, new_threats):
        self.consistent_domains.remove(coords)
        for threat in new_threats:
            self.consistent_domains.remove(threat)
        if len(self.consistent_domains) == 0 and sum(self.unassigned_pieces.values()) != 0:
            return False
        return True


#############################################################################
# State
#############################################################################


class State:
    pass


def complete_assignment(board, assignment):
    num_assigned = 0
    for piece, coords_list in assignment.items():
        num_assigned += len(coords_list)
    return num_assigned == board.total_num_pieces


def consistent_assignment(board, assignment, threats):
    for piece, coords_list in assignment.items():
        for coords in coords_list:
            if coords in threats:
                return False
    return True


def backtrack(board, assignment):
    if complete_assignment(board, assignment):
        return assignment
    piece = board.select_unassigned_variable(assignment)
    # print(piece)
    for num_threats, coords, threats, new_threats in board.order_domain_values(piece, assignment):
        # print(coords)
        if consistent_assignment(board, assignment, threats):
            assignment[piece].append(coords)
            board.unassigned_pieces[piece] -= 1
            if board.inference(coords, new_threats) != False:
                result = backtrack(board, assignment)
                if result != False:
                    return result
                board.consistent_domains.add(coords)
                for threat in new_threats:
                    board.consistent_domains.add(threat)
            else:
                board.consistent_domains.add(coords)
                for threat in new_threats:
                    board.consistent_domains.add(threat)

            assignment[piece].remove(coords)
            board.unassigned_pieces[piece] += 1
    return False


def generate_goal_state(assignment):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    goal_state = {}
    for piece, coords_list in assignment.items():
        for coords in coords_list:
            goal_state[(alphabet[coords[1]], coords[0])] = piece
    return goal_state


#############################################################################
# Implement Search Algorithm
#############################################################################


def search(rows, cols, grid, num_pieces):

    board = Board(rows, cols, grid, num_pieces)

    valid_assignment = backtrack(
        board, {'King': [], 'Queen': [], 'Bishop': [], 'Rook': [], 'Knight': [], 'Ferz': [], 'Princess': [], 'Empress': []})

    # print(valid_assignment)
    if valid_assignment != False:
        return generate_goal_state(valid_assignment)


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

    num_obstacles = int(get_par(handle.readline()))
    if num_obstacles > 0:
        for ch_coord in get_par(handle.readline()).split():  # Init obstacles
            r, c = from_chess_coord(ch_coord)
            grid[r][c] = -1
    else:
        handle.readline()

    piece_nums = get_par(handle.readline()).split()
    # List in the order of King, Queen, Bishop, Rook, Knight
    num_pieces = [int(x) for x in piece_nums]

    return rows, cols, grid, num_pieces


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


def run_CSP():
    testcase = sys.argv[1]  # Do not remove. This is your input testfile.
    rows, cols, grid, num_pieces = parse(testcase)
    goalstate = search(rows, cols, grid, num_pieces)
    return goalstate  # Format to be returned


# print(run_CSP())
