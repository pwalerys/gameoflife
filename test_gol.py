import unittest
from gol import Board

class gol_test(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)

    def test_next_step_will_set_alive_left_corner_when_all_surrounding_cells_are_alive(self):
        self.board.set_alive(0, 1)
        self.board.set_alive(1, 1)
        self.board.set_alive(1, 0)

        self.board.next_step()

        self.assertTrue(self.board.is_alive(0, 0))

    def test_next_step_will_leave_left_corner_dead_when_only_two_cells_are_alive(self):
        self.board.set_alive(0, 1)
        self.board.set_alive(1, 1)

        self.board.next_step()

        self.assertFalse(self.board.is_alive(0, 0))

    def test_next_step_will_leave_left_corner_alive_when_only_two_cells_are_alive(self):
        self.board.set_alive(0, 0)
        self.board.set_alive(0, 1)
        self.board.set_alive(1, 1)

        self.board.next_step()

        self.assertTrue(self.board.is_alive(0, 0))


if __name__ == "__main__":
    unittest.main()
