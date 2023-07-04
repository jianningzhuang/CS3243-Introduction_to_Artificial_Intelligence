import sys

# Helper functions to aid in your implementation. Can edit/remove
#############################################################################
######## Piece
#############################################################################
class Piece:
    pass

#############################################################################
######## Board
#############################################################################
class Board:
    def __init__(self, rows, cols, grid, enemy_pieces, own_pieces, goals):
        self.rows = rows
        self.cols = cols
        self.grid = grid
        self.action_costs = grid
        self.enemy_pieces = enemy_pieces
        self.my_king = own_pieces[0][1]
        self.goals = goals

    def mark_threats(self, enemy):
        enemy_type = enemy[0]
        enemy_row = enemy[1][0]
        enemy_col = enemy[1][1]
        
        if enemy_type == "King":
            if (enemy_row > 0 and self.grid[enemy_row - 1][enemy_col] != -1):
                self.grid[enemy_row - 1][enemy_col] = -2
            if (enemy_col > 0 and self.grid[enemy_row][enemy_col - 1] != -1):
                self.grid[enemy_row][enemy_col - 1] = -2
            if (enemy_row < self.rows - 1 and self.grid[enemy_row + 1][enemy_col] != -1):
                self.grid[enemy_row + 1][enemy_col] = -2
            if (enemy_col < self.cols - 1 and self.grid[enemy_row][enemy_col + 1] != -1):
                self.grid[enemy_row][enemy_col + 1] = -2
            if (enemy_row > 0 and enemy_col > 0 and self.grid[enemy_row - 1][enemy_col - 1] != -1):
                self.grid[enemy_row - 1][enemy_col - 1] = -2
            if (enemy_row > 0 and enemy_col < self.cols - 1 and self.grid[enemy_row - 1][enemy_col + 1] != -1):
                self.grid[enemy_row - 1][enemy_col + 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col < self.cols - 1 and self.grid[enemy_row + 1][enemy_col + 1] != -1):
                self.grid[enemy_row + 1][enemy_col + 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col > 0 and self.grid[enemy_row + 1][enemy_col - 1] != -1):
                self.grid[enemy_row + 1][enemy_col - 1] = -2
            
        elif enemy_type == "Rook":
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                self.grid[cur_row - 1][cur_col] = -2
                cur_row -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                self.grid[cur_row + 1][cur_col] = -2
                cur_row += 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                self.grid[cur_row][cur_col - 1] = -2
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                self.grid[cur_row][cur_col + 1] = -2
                cur_col += 1
                
        elif enemy_type == "Bishop":
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                self.grid[cur_row - 1][cur_col - 1] = -2
                cur_row -= 1
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                self.grid[cur_row + 1][cur_col - 1] = -2
                cur_row += 1
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                self.grid[cur_row - 1][cur_col + 1] = -2
                cur_row -= 1
                cur_col += 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                self.grid[cur_row + 1][cur_col + 1] = -2
                cur_row += 1
                cur_col += 1
                
        elif enemy_type == "Queen":
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                self.grid[cur_row - 1][cur_col] = -2
                cur_row -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                self.grid[cur_row + 1][cur_col] = -2
                cur_row += 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                self.grid[cur_row][cur_col - 1] = -2
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                self.grid[cur_row][cur_col + 1] = -2
                cur_col += 1
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                self.grid[cur_row - 1][cur_col - 1] = -2
                cur_row -= 1
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                self.grid[cur_row + 1][cur_col - 1] = -2
                cur_row += 1
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                self.grid[cur_row - 1][cur_col + 1] = -2
                cur_row -= 1
                cur_col += 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                self.grid[cur_row + 1][cur_col + 1] = -2
                cur_row += 1
                cur_col += 1
                
        elif enemy_type == "Knight":
            if (enemy_row > 0 and enemy_col > 1 and self.grid[enemy_row - 1][enemy_col - 2] != -1):
                self.grid[enemy_row - 1][enemy_col - 2] = -2
            if (enemy_row > 1 and enemy_col > 0 and self.grid[enemy_row - 2][enemy_col - 1] != -1):
                self.grid[enemy_row - 2][enemy_col - 1] = -2
            if (enemy_row > 1 and enemy_col < self.cols - 1 and self.grid[enemy_row - 2][enemy_col + 1] != -1):
                self.grid[enemy_row - 2][enemy_col + 1] = -2
            if (enemy_row > 0 and enemy_col < self.cols - 2 and self.grid[enemy_row - 1][enemy_col + 2] != -1):
                self.grid[enemy_row - 1][enemy_col + 2] = -2
            if (enemy_row < self.rows - 1 and enemy_col < self.cols - 2 and self.grid[enemy_row + 1][enemy_col + 2] != -1):
                self.grid[enemy_row + 1][enemy_col + 2] = -2
            if (enemy_row < self.rows - 2 and enemy_col < self.cols - 1 and self.grid[enemy_row + 2][enemy_col + 1] != -1):
                self.grid[enemy_row + 2][enemy_col + 1] = -2
            if (enemy_row < self.rows - 2 and enemy_col > 0 and self.grid[enemy_row + 2][enemy_col - 1] != -1):
                self.grid[enemy_row + 2][enemy_col - 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col > 1 and self.grid[enemy_row + 1][enemy_col - 2] != -1):
                self.grid[enemy_row + 1][enemy_col - 2] = -2
                
        elif enemy_type == "Ferz":
            if (enemy_row > 0 and enemy_col > 0 and self.grid[enemy_row - 1][enemy_col - 1] != -1):
                self.grid[enemy_row - 1][enemy_col - 1] = -2
            if (enemy_row > 0 and enemy_col < self.cols - 1 and self.grid[enemy_row - 1][enemy_col + 1] != -1):
                self.grid[enemy_row - 1][enemy_col + 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col < self.cols - 1 and self.grid[enemy_row + 1][enemy_col + 1] != -1):
                self.grid[enemy_row + 1][enemy_col + 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col > 0 and self.grid[enemy_row + 1][enemy_col - 1] != -1):
                self.grid[enemy_row + 1][enemy_col - 1] = -2
                
        elif enemy_type == "Princess":
            if (enemy_row > 0 and enemy_col > 1 and self.grid[enemy_row - 1][enemy_col - 2] != -1):
                self.grid[enemy_row - 1][enemy_col - 2] = -2
            if (enemy_row > 1 and enemy_col > 0 and self.grid[enemy_row - 2][enemy_col - 1] != -1):
                self.grid[enemy_row - 2][enemy_col - 1] = -2
            if (enemy_row > 1 and enemy_col < self.cols - 1 and self.grid[enemy_row - 2][enemy_col + 1] != -1):
                self.grid[enemy_row - 2][enemy_col + 1] = -2
            if (enemy_row > 0 and enemy_col < self.cols - 2 and self.grid[enemy_row - 1][enemy_col + 2] != -1):
                self.grid[enemy_row - 1][enemy_col + 2] = -2
            if (enemy_row < self.rows - 1 and enemy_col < self.cols - 2 and self.grid[enemy_row + 1][enemy_col + 2] != -1):
                self.grid[enemy_row + 1][enemy_col + 2] = -2
            if (enemy_row < self.rows - 2 and enemy_col < self.cols - 1 and self.grid[enemy_row + 2][enemy_col + 1] != -1):
                self.grid[enemy_row + 2][enemy_col + 1] = -2
            if (enemy_row < self.rows - 2 and enemy_col > 0 and self.grid[enemy_row + 2][enemy_col - 1] != -1):
                self.grid[enemy_row + 2][enemy_col - 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col > 1 and self.grid[enemy_row + 1][enemy_col - 2] != -1):
                self.grid[enemy_row + 1][enemy_col - 2] = -2
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1):
                self.grid[cur_row - 1][cur_col - 1] = -2
                cur_row -= 1
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1):
                self.grid[cur_row + 1][cur_col - 1] = -2
                cur_row += 1
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1):
                self.grid[cur_row - 1][cur_col + 1] = -2
                cur_row -= 1
                cur_col += 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1):
                self.grid[cur_row + 1][cur_col + 1] = -2
                cur_row += 1
                cur_col += 1
            
        elif enemy_type == "Empress":
            if (enemy_row > 0 and enemy_col > 1 and self.grid[enemy_row - 1][enemy_col - 2] != -1):
                self.grid[enemy_row - 1][enemy_col - 2] = -2
            if (enemy_row > 1 and enemy_col > 0 and self.grid[enemy_row - 2][enemy_col - 1] != -1):
                self.grid[enemy_row - 2][enemy_col - 1] = -2
            if (enemy_row > 1 and enemy_col < self.cols - 1 and self.grid[enemy_row - 2][enemy_col + 1] != -1):
                self.grid[enemy_row - 2][enemy_col + 1] = -2
            if (enemy_row > 0 and enemy_col < self.cols - 2 and self.grid[enemy_row - 1][enemy_col + 2] != -1):
                self.grid[enemy_row - 1][enemy_col + 2] = -2
            if (enemy_row < self.rows - 1 and enemy_col < self.cols - 2 and self.grid[enemy_row + 1][enemy_col + 2] != -1):
                self.grid[enemy_row + 1][enemy_col + 2] = -2
            if (enemy_row < self.rows - 2 and enemy_col < self.cols - 1 and self.grid[enemy_row + 2][enemy_col + 1] != -1):
                self.grid[enemy_row + 2][enemy_col + 1] = -2
            if (enemy_row < self.rows - 2 and enemy_col > 0 and self.grid[enemy_row + 2][enemy_col - 1] != -1):
                self.grid[enemy_row + 2][enemy_col - 1] = -2
            if (enemy_row < self.rows - 1 and enemy_col > 1 and self.grid[enemy_row + 1][enemy_col - 2] != -1):
                self.grid[enemy_row + 1][enemy_col - 2] = -2
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1):
                self.grid[cur_row - 1][cur_col] = -2
                cur_row -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1):
                self.grid[cur_row + 1][cur_col] = -2
                cur_row += 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1):
                self.grid[cur_row][cur_col - 1] = -2
                cur_col -= 1
            cur_row = enemy_row
            cur_col = enemy_col
            while (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1):
                self.grid[cur_row][cur_col + 1] = -2
                cur_col += 1


    def set_board(self):
        self.grid[self.my_king[0]][self.my_king[1]] = -1
        for enemy in self.enemy_pieces:
            self.grid[enemy[1][0]][enemy[1][1]] = -1
        for enemy in self.enemy_pieces:
            self.mark_threats(enemy)

    def actions(self, current):
        valid_moves = []
        cur_row = current[0]
        cur_col = current[1]
        if (cur_row > 0 and self.grid[cur_row - 1][cur_col] != -1 and self.grid[cur_row - 1][cur_col] != -2):
            valid_moves.append((-1, 0))
        if (cur_col > 0 and self.grid[cur_row][cur_col - 1] != -1 and self.grid[cur_row][cur_col - 1] != -2):
            valid_moves.append((0, -1))
        if (cur_row < self.rows - 1 and self.grid[cur_row + 1][cur_col] != -1 and self.grid[cur_row + 1][cur_col] != -2):
            valid_moves.append((1, 0))
        if (cur_col < self.cols - 1 and self.grid[cur_row][cur_col + 1] != -1 and self.grid[cur_row][cur_col + 1] != -2):
            valid_moves.append((0, 1))
        if (cur_row > 0 and cur_col > 0 and self.grid[cur_row - 1][cur_col - 1] != -1 and self.grid[cur_row - 1][cur_col - 1] != -2):
            valid_moves.append((-1, -1))
        if (cur_row > 0 and cur_col < self.cols - 1 and self.grid[cur_row - 1][cur_col + 1] != -1 and self.grid[cur_row - 1][cur_col + 1] != -2):
            valid_moves.append((-1, 1))
        if (cur_row < self.rows - 1 and cur_col < self.cols - 1 and self.grid[cur_row + 1][cur_col + 1] != -1 and self.grid[cur_row + 1][cur_col + 1] != -2):
            valid_moves.append((1, 1))
        if (cur_row < self.rows - 1 and cur_col > 0 and self.grid[cur_row + 1][cur_col - 1] != -1 and self.grid[cur_row + 1][cur_col - 1] != -2):
            valid_moves.append((1, -1))
        return valid_moves

    def move_king(self, current, valid_move):
        cur_row = current[0]
        cur_col = current[1]
        self.my_king = (cur_row + valid_move[0], cur_col + valid_move[1])
        return self.my_king
                

#############################################################################
######## State
#############################################################################
class State:
    pass

class Node:
    def __init__(self, state, parent, action_cost):
        self.state = state
        self.parent = parent
        if parent != None:
            self.path_cost = parent.path_cost + action_cost
        else:
            self.path_cost = 0

    def get_path(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        moves = []
        current = self
        while current.parent != None:
            moves.insert(0, [(alphabet[current.parent.state[1]], current.parent.state[0]), (alphabet[current.state[1]], current.state[0])])
            current = current.parent
        return moves

                    
#############################################################################
######## Implement Search Algorithm
#############################################################################
def search(rows, cols, grid, enemy_pieces, own_pieces, goals):
    
    board = Board(rows, cols, grid, enemy_pieces, own_pieces, goals)
    board.set_board()
    
    frontier = []
    reached = {}

    my_king = own_pieces[0][1]
    initial_node = Node(my_king, None, 0)
    frontier.append(initial_node)
    reached[my_king] = initial_node

    while len(frontier) > 0:
        current = frontier.pop()
        for valid_move in board.actions(current.state):
            successor_state = board.move_king(current.state, valid_move)
            successor = Node(successor_state, current, board.grid[successor_state[0]][successor_state[1]])
            if successor.state in goals:
                return successor.get_path()
            if successor.state not in reached:
                frontier.append(successor)
                reached[successor.state] = successor
    return []
                

#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    grid = [[1 for j in range(cols)] for i in range(rows)] # Dictionary, label empty spaces as 1 (Default Step Cost)
    enemy_pieces = [] # List
    own_pieces = [] # List
    goals = [] # List

    handle.readline()  # Ignore number of obstacles
    for ch_coord in get_par(handle.readline()).split():  # Init obstacles
        r, c = from_chess_coord(ch_coord)
        grid[r][c] = -1 # Label Obstacle as -1

    handle.readline()  # Ignore Step Cost header
    line = handle.readline()
    while line.startswith("["):
        line = line[1:-2].split(",")
        r, c = from_chess_coord(line[0])
        grid[r][c] = int(line[1]) if grid[r][c] == 1 else grid[r][c] #Reinitialize step cost for coordinates with different costs
        line = handle.readline()
    
    line = handle.readline() # Read Enemy Position
    while line.startswith("["):
        line = line[1:-2]
        piece = add_piece(line)
        enemy_pieces.append(piece)
        line = handle.readline()

    # Read Own King Position
    line = handle.readline()[1:-2]
    piece = add_piece(line)
    own_pieces.append(piece)

    # Read Goal Positions
    for ch_coord in get_par(handle.readline()).split():
        r, c = from_chess_coord(ch_coord)
        goals.append((r, c))
    
    return rows, cols, grid, enemy_pieces, own_pieces, goals

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [piece, (r,c)]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)
    
### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: List of moves and nodes explored
def run_DFS():
    testcase = sys.argv[1]
    rows, cols, grid, enemy_pieces, own_pieces, goals = parse(testcase)
    moves = search(rows, cols, grid, enemy_pieces, own_pieces, goals)
    return moves

