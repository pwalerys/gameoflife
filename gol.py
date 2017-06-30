from tabulate import tabulate
from cell import Cell


class Board:

    def __init__(self, size):
        self.size = size
        no_neighbors = [None] * Cell.NUMBER_OF_NEIGHBORS
        self.board = [[Cell(no_neighbors)] * size] * size
        for row in range(self.size):
            for column in range(self.size):
                if row == 0:
                    if column == 0:
                        self.board[row][column].neighbors[0] = self.board[0][1]
                        self.board[row][column].neighbors[1] = self.board[1][1]
                        self.board[row][column].neighbors[2] = self.board[1][0]
                    elif column == self.size - 1:
                        pass
                    else:
                        pass
                elif row == self.size - 1:
                    if column == 0:
                        pass
                    elif column == self.size - 1:
                        pass
                    else:
                        pass
                else:
                    pass

    def set_alive(self, x, y):
        self.board[x][y].set_alive()

    def is_alive(self, x, y):
        return self.board[x][y].alive

    def __repr__(self):
        return tabulate(self.board, tablefmt="grid")

    def next_step(self):
        for row in self.board:
            for cell in row:
                cell.prepare_next_state()
        for row in self.board:
            for cell in row:
                cell.update_state()



if __name__ == "__main__":
    print(Board(9))
