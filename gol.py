from tabulate import tabulate
from cell import Cell, Corner, Edge


class Board:

    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

        self._create_board()
        self.__init__corners(size)
        self.__init__edges(size)
        self.__init__cells()

    def _create_board(self):
        self._create_regular_cells()
        self._create_corners()
        self._create_edges()

    def _create_corners(self):
        dummy_neighbors = [None] * Corner.NUMBER_OF_NEIGHBORS
        self.board[0][0] = Corner(dummy_neighbors)
        self.board[0][self.size - 1] = Corner(dummy_neighbors)
        self.board[self.size - 1][0] = Corner(dummy_neighbors)
        self.board[self.size - 1][self.size - 1] = Corner(dummy_neighbors)

    def _create_edges(self):
        self._create_upper_edges()
        self._create_lower_edges()
        self._create_left_edges()
        self._create_right_edges()

    def _create_regular_cells(self):
        dummy_neighbors = [None] * Cell.NUMBER_OF_NEIGHBORS
        for row in range(1, self.size - 1):
            for column in range(1, self.size - 1):
                self.board[row][column] = Cell(dummy_neighbors)

    def _create_right_edges(self):
        dummy_neighbors = [None] * Edge.NUMBER_OF_NEIGHBORS
        column = self.size - 1
        for row in range(1, self.size - 1):
            self.board[row][column] = Edge(dummy_neighbors)

    def _create_left_edges(self):
        dummy_neighbors = [None] * Edge.NUMBER_OF_NEIGHBORS
        column = 0
        for row in range(1, self.size - 1):
            self.board[row][column] = Edge(dummy_neighbors)

    def _create_lower_edges(self):
        dummy_neighbors = [None] * Edge.NUMBER_OF_NEIGHBORS
        row = self.size - 1
        for column in range(1, self.size - 1):
            self.board[row][column] = Edge(dummy_neighbors)

    def _create_upper_edges(self):
        dummy_neighbors = [None] * Edge.NUMBER_OF_NEIGHBORS
        row = 0
        for column in range(1, self.size - 1):
            self.board[row][column] = Edge(dummy_neighbors)

    def __init__corners(self, size):
        self.__init_left_upper_corner()
        self.__init_left_lower_corner(size)
        self.__init_right_upper_corner(size)
        self.__init_right_lower_corner(size)

    def __init_right_lower_corner(self, size):
        row = size - 1
        col = size - 1
        self.board[row][col].neighbors = [self._get_left(row, col), self._get_upper(row, col), self._get_upper_left(row, col)]

    def __init_right_upper_corner(self, size):
        row = 0
        col = size - 1
        self.board[row][col].neighbors = [self._get_left(row, col), self._get_lower(row, col), self._get_lower_left(row, col)]

    def __init_left_lower_corner(self, size):
        row = size - 1
        col = 0
        self.board[row][col].neighbors =[self._get_right(row, col), self._get_upper(row, col), self._get_upper_right(row, col)]

    def __init_left_upper_corner(self):
        row = 0
        col = 0
        self.board[row][col].neighbors = [self._get_right(row, col), self._get_lower(row, col), self._get_lower_right(row, col)]

    def __init__edges(self, size):
        self.__init_upper_edge()
        self.__init_lower_edge()
        self.__init_left_edge()
        self.__init_right_edge()

    def __init_lower_edge(self):
        row = self.size - 1
        for column in range(1, self.size - 1):
            self.board[row][column].neighbors = [self._get_left(row, column),
                                                 self._get_upper_left(row, column),
                                                 self._get_upper(row, column),
                                                 self._get_upper_right(row, column),
                                                 self._get_right(row, column)]

    def __init_upper_edge(self):
        row = 0
        for column in range(1, self.size - 1):
            self.board[row][column].neighbors = [self._get_left(row, column),
                                                 self._get_lower_left(row, column),
                                                 self._get_lower(row, column),
                                                 self._get_lower_right(row, column),
                                                 self._get_right(row, column)]

    def __init_left_edge(self):
        row = 0
        for column in range(1, self.size - 1):
            self.board[row][column].neighbors = [self._get_left(row, column),
                                                 self._get_lower_left(row, column),
                                                 self._get_lower(row, column),
                                                 self._get_lower_right(row, column),
                                                 self._get_right(row, column)]

    def __init_right_edge(self):
        row = 0
        for column in range(1, self.size - 1):
            self.board[row][column].neighbors = [self._get_left(row, column),
                                                 self._get_lower_left(row, column),
                                                 self._get_lower(row, column),
                                                 self._get_lower_right(row, column),
                                                 self._get_right(row, column)]

    def __init__cells(self):
        for row in range(1, self.size - 1):
            for column in range(1, self.size - 1):
                self.board[row][column].neighbors = [self._get_upper(row, column),
                                                     self._get_upper_right(row, column),
                                                     self._get_right(row, column),
                                                     self._get_lower_right(row, column),
                                                     self._get_lower(row, column),
                                                     self._get_lower_left(row, column),
                                                     self._get_left(row, column),
                                                     self._get_upper_left(row, column)]

    def set_alive(self, row, column):
        self.board[row][column].set_alive()

    def set_dead(self, row, column):
        self.board[row][column].set_dead()

    def is_alive(self, row, column):
        return self.board[row][column].alive

    def __repr__(self):
        return tabulate(self.board, tablefmt="grid")

    def next_step(self):
        for row in self.board:
            for cell in row:
                cell.prepare_next_state()
        for row in self.board:
            for cell in row:
                cell.update_state()

    def _get_lower(self, row, column):
        return self.board[row+1][column]

    def _get_upper(self, row, column):
        return self.board[row-1][column]

    def _get_right(self, row, column):
        return self.board[row][column+1]

    def _get_left(self, row, column):
        return self.board[row][column-1]

    def _get_lower_left(self, row, column):
        return self.board[row+1][column-1]

    def _get_upper_left(self, row, column):
        return self.board[row-1][column-1]

    def _get_lower_right(self, row, column):
        return self.board[row+1][column+1]

    def _get_upper_right(self, row, column):
        return self.board[row-1][column+1]

if __name__ == "__main__":
    board = Board(3)
    print(board)
