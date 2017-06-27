from tabulate import tabulate

ALIVE = 'X'

class Board:

    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]

    def set_alive(self, x, y):
        self.board[x][y] = 'X'

    def is_alive(self, x, y):
        return self.board[x][y] == 'X'

    def __repr__(self):
        return tabulate(self.board, tablefmt="grid")

    def next_step(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == 0:
                    if j == 0:
                        self._update_left_corner()

    def _update_left_corner(self):
        if self.board[0][1] is ALIVE and \
           self.board[1][0] is ALIVE and \
           self.board[1][1] is ALIVE:
            self.board[0][0] = ALIVE





if __name__ == "__main__":
    print(Board(9))
