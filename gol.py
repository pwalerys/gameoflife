from tabulate import tabulate
from cell import Cell, Corner


class Board:

    def __init__(self, size):
        self.size = size
        no_neighbors = [None] * Cell.NUMBER_OF_NEIGHBORS
        self.board = [[Cell(no_neighbors) for _ in range(size)] for __ in range(size)]

        self.__init__corners(size)

    def __init__corners(self, size):
        self.__init_left_upper_corner()
        self.__init_left_lower_corner(size)
        self.__init_right_upper_corner(size)
        self.__init_right_lower_corner(size)

    def __init_right_lower_corner(self, size):
        row = size - 1
        col = size - 1
        self.board[row][col] = Corner(
            [self._get_left(row, col), self._get_upper(row, col), self._get_upper_left(row, col)])

    def __init_right_upper_corner(self, size):
        row = 0
        col = size - 1
        self.board[row][col] = Corner(
            [self._get_left(row, col), self._get_lower(row, col), self._get_lower_left(row, col)])

    def __init_left_lower_corner(self, size):
        row = size - 1
        col = 0
        self.board[row][col] = Corner(
            [self._get_right(row, col), self._get_upper(row, col), self._get_upper_right(row, col)])

    def __init_left_upper_corner(self):
        row = 0
        col = 0
        self.board[row][col] = Corner(
            [self._get_right(row, col), self._get_lower(row, col), self._get_lower_right(row, col)])

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
    board = Board(9)
