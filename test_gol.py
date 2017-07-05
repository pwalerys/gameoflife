import unittest
from gol import Board

class gol_test(unittest.TestCase):

    def setUp(self):
        self.board = Board(3)

    def _scenario(self, coordinates, alive_neighbors, alive_at_the_beginning, alive_at_the_end):
        if alive_at_the_beginning:
            self.board.set_alive(*coordinates)
        else:
            self.board.set_dead(*coordinates)

        for neighbor in alive_neighbors:
            self.board.set_alive(*neighbor)

        self.board.next_step()

        if alive_at_the_end:
            self.assertTrue(self.board.is_alive(*coordinates), str(self.board))
        else:
            self.assertFalse(self.board.is_alive(*coordinates), str(self.board))

    def revive_scenario(self, coordinates, alive_neighbors):
        self._scenario(coordinates, alive_neighbors, alive_at_the_beginning=False, alive_at_the_end=True)

    def dying_scenario(self, coordinates, alive_neighbors):
        self._scenario(coordinates, alive_neighbors, alive_at_the_beginning=True, alive_at_the_end=False)

    def stays_dead_scenario(self, coordinates, alive_neighbors):
        self._scenario(coordinates, alive_neighbors, alive_at_the_beginning=False, alive_at_the_end=False)

    def stays_alive_scenario(self, coordinates, alive_neighbors):
        self._scenario(coordinates, alive_neighbors, alive_at_the_beginning=True, alive_at_the_end=True)

    def test_left_upper_corner_will_revive_when_all_surrounding_cells_are_alive(self):
        cell_coordinates = 0, 0
        alive_neighbors = [(0,1), (1,1), (1,0)]

        self.revive_scenario(cell_coordinates, alive_neighbors)

    def test_left_upper_corner_will_survive_when_only_two_cells_are_alive(self):
        cell_coordinates = 0, 0
        alive_neighbors = [(0,1), (1,1)]

        self.stays_alive_scenario(cell_coordinates, alive_neighbors)

    def test_left_upper_corner_will_survive_when_all_surrounding_cells_are_alive(self):
        cell_coordinates = 0, 0
        alive_neighbors = [(0,1), (1,1), (1,0)]

        self.stays_alive_scenario(cell_coordinates, alive_neighbors)

    def test_left_upper_corner_will_die_when_only_one_neighbor_is_alive(self):
        cell_coordinates = 0, 0
        alive_neighbors = [(0,1)]

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_left_upper_corner_will_not_revive_if_only_one_neighbor_is_alive(self):
        cell_coordinates = 0, 0
        alive_neighbors = [(0, 1)]

        self.stays_dead_scenario(cell_coordinates, alive_neighbors)

    def test_right_upper_corner_will_revive_if_three_neighbors_are_alive(self):
        cell_coordinates = 0, 2
        alive_neighbors = [(0,1), (1,1), (1,2)]

        self.revive_scenario(cell_coordinates, alive_neighbors)

    def test_right_upper_corner_will_die_if_one_neighbor_is_alive(self):
        cell_coordinates = 0, 2
        alive_neighbors = [(0,1)]

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_right_upper_corner_will_stay_alive_if_two_neighbors_are_alive(self):
        cell_coordinates = 0, 2
        alive_neighbors = [(0,1), (1,2)]

        self.stays_alive_scenario(cell_coordinates, alive_neighbors)

    def test_left_lower_corner_will_stay_alive_if_two_neighbors_are_alive(self):
        cell_coordinates = 2, 0
        alive_neighbors = [(1, 0), (1, 1)]

        self.stays_alive_scenario(cell_coordinates, alive_neighbors)

    def test_left_lower_corner_will_die_if_one_neighbor_is_alive(self):
        cell_coordinates = 2, 0
        alive_neighbors = [(2, 1)]

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_left_lower_corner_will_revive_if_three_neighbors_are_alive(self):
        cell_coordinates = 2, 0
        alive_neighbors = [(2, 1), (1, 1), (1, 0)]

        self.revive_scenario(cell_coordinates, alive_neighbors)

    def test_right_lower_corner_will_stay_alive_if_two_neighbors_are_alive(self):
        cell_coordinates = 2, 2
        alive_neighbors = [(2, 1), (1, 1)]

        self.stays_alive_scenario(cell_coordinates, alive_neighbors)

    def test_right_lower_corner_will_die_if_one_neighbor_is_alive(self):
        cell_coordinates = 2, 2
        alive_neighbors = [(2, 1)]

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_right_lower_corner_will_revive_if_three_neighbors_are_alive(self):
        cell_coordinates = 2, 2
        alive_neighbors = [(2, 1), (1, 1), (1, 2)]

        self.revive_scenario(cell_coordinates, alive_neighbors)

    def test_upper_edge_will_die_if_all_neighbors_are_dead(self):
        cell_coordinates = 0, 1
        alive_neighbors = []

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_upper_edge_will_revive_if_three_neighbors_are_alive(self):
        cell_coordinates = 0, 1
        alive_neighbors = [(0, 0), (1, 1), (0, 1)]

        self.revive_scenario(cell_coordinates, alive_neighbors)

    def test_lower_edge_will_die_if_one_neighbor_is_alive(self):
        cell_coordinates = 2, 1
        alive_neighbors = [(2, 0)]

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_lower_edge_will_survive_if_two_neighbors_are_alive(self):
        cell_coordinates = 2, 1
        alive_neighbors = [(2, 0), (1, 1)]

        self.stays_alive_scenario(cell_coordinates, alive_neighbors)

    def test_lower_edge_will_die_if_all_neighbors_are_alive(self):
        cell_coordinates = 2, 1
        alive_neighbors = [(2, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

        self.dying_scenario(cell_coordinates, alive_neighbors)

    def test_lower_edge_will_revive_if_three_neighbors_are_alive(self):
        cell_coordinates = 2, 1
        alive_neighbors = [(1, 1), (1, 2), (2, 2)]

        self.revive_scenario(cell_coordinates, alive_neighbors)



if __name__ == "__main__":
    unittest.main()
