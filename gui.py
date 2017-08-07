from tkinter import Tk, Canvas, ALL
from collections import namedtuple
from threading import Thread
from time import sleep
from gol import Board

Point = namedtuple("Point", "x y".split())


class GameOfLife(Thread):
    def __init__(self, board_size, window):
        self.board = Board(board_size)
        self.window = window
        self.alive = True
        super(GameOfLife, self).__init__()

    def run(self):
        sleep(1)
        while self.alive:

            for x in range(self.board.size):
                for y in range(self.board.size):
                    if self.board.is_alive(x, y):
                        self.window.draw_alive(x, y)
                    else:
                        self.window.draw_dead(x, y)
            self.board.next_step()
            sleep(1)


class Window:
    def __init__(self, root, width, height, points_per_line):
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        self.canvas.canvas = self.canvas
        self.canvas.data = {}
        self.points_per_line = points_per_line
        self.alive_squares = dict()

        self._draw_grid()

    def _draw_grid(self):
        for begin, end in self._horizontal_line_coordinates:
            self.canvas.create_line(begin.x, begin.y, end.x, end.y)

        for begin, end in self._vertical_line_coordinates:
            self.canvas.create_line(begin.x, begin.y, end.x, end.y)

    @property
    def _horizontal_line_coordinates(self):
        y = 0

        while y < self.height:
            y = y + self.height / self.points_per_line
            begin = Point(0, y)
            end = Point(self.width, y)
            yield begin, end

    @property
    def _vertical_line_coordinates(self):
        x = 0

        while x <= self.width:
            begin = Point(x, 0)
            end = Point(x, self.height)

            yield begin, end
            x = x + self.width / self.points_per_line

    def draw_dead(self, x, y):
        try:
            rectangle = self.alive_squares[(x, y)]
            self.canvas.delete(rectangle)
            del self.alive_squares[(x, y)]
        except KeyError:
            pass

    def draw_alive(self, x, y):
        if (x, y) in self.alive_squares:
            return

        left_corner = Point(x*self.width/self.points_per_line, y*self.height/self.points_per_line)
        right_corner = Point((x+1)*self.width/self.points_per_line, (y+1)*self.height/self.points_per_line)
        rectangle = self.canvas.create_rectangle(left_corner.x, left_corner.y, right_corner.x, right_corner.y, fill="green")
        self.alive_squares[(x, y)] = rectangle


def run():
    root = Tk()
    window = Window(root, 500, 500, 32)
    root.canvas = window.canvas
    game_of_life = GameOfLife(32, window)
    game_of_life.board.set_alive(5, 5)
    game_of_life.board.set_alive(6, 5)
    game_of_life.board.set_alive(7, 5)
    game_of_life.board.set_alive(8, 5)
    game_of_life.board.set_alive(9, 5)
    game_of_life.board.set_alive(10, 5)
    game_of_life.board.set_alive(11, 5)

    game_of_life.start()

    root.mainloop()
    game_of_life.alive = False

if __name__ == "__main__":
    run()
