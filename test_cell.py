import unittest
from cell import Cell, Corner

class CellTest(unittest.TestCase):

    def setUp(self):
        self.alive_cell = Cell([None]*Cell.NUMBER_OF_NEIGHBORS)
        self.alive_cell.set_alive()

        self.dead_cell = Cell([None]*Cell.NUMBER_OF_NEIGHBORS)
        self.dead_cell.set_dead()

        self.assertNotEqual(self.alive_cell, self.dead_cell)

    def test_next_state_will_be_dead_if_all_neighbors_are_dead(self):
        cell = Cell([self.dead_cell]*Cell.NUMBER_OF_NEIGHBORS)
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertFalse(cell.alive)

    def test_next_state_will_be_dead_if_all_neighbors_are_alive(self):
        cell = Cell([self.alive_cell]*Cell.NUMBER_OF_NEIGHBORS)
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertFalse(cell.alive)

    def test_cell_will_survive_if_two_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*2 + [self.dead_cell]*(Cell.NUMBER_OF_NEIGHBORS-2))
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertTrue(cell.alive)

    def test_cell_will_survive_if_three_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*3 + [self.dead_cell]*(Cell.NUMBER_OF_NEIGHBORS-3))
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertTrue(cell.alive)

    def test_cell_will_die_if_only_one_neighbor_will_be_alive(self):
        cell = Cell([self.alive_cell]*1 + [self.dead_cell]*(Cell.NUMBER_OF_NEIGHBORS-1))
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertFalse(cell.alive)

    def test_cell_will_revive_if_three_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*3+ [self.dead_cell]*(Cell.NUMBER_OF_NEIGHBORS-3))
        cell.set_dead()

        cell.prepare_next_state()
        cell.update_state()

        self.assertTrue(cell.alive)

    def test_cell_will_not_revive_if_two_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*2 + [self.dead_cell]*(Cell.NUMBER_OF_NEIGHBORS-2))
        cell.set_dead()

        cell.prepare_next_state()
        cell.update_state()

        self.assertFalse(cell.alive)


    def test_cell_will_die_if_more_than_three_neighbors_will_be_alive(self):
        for alive, dead in zip(range(4, Cell.NUMBER_OF_NEIGHBORS + 1), range(Cell.NUMBER_OF_NEIGHBORS - 4, 3, -1)):
            cell = Cell([self.alive_cell]*alive + [self.dead_cell]*dead)
            cell.set_alive()

            cell.prepare_next_state()
            cell.update_state()

            self.assertFalse(cell.alive)


class CornerTest(unittest.TestCase):

    def setUp(self):
        self.alive_cell = Cell([None]*Cell.NUMBER_OF_NEIGHBORS)
        self.alive_cell.set_alive()

        self.dead_cell = Cell([None]*Cell.NUMBER_OF_NEIGHBORS)
        self.dead_cell.set_dead()

        self.assertNotEqual(self.alive_cell, self.dead_cell)

    def test_corner_will_survive_if_all_neighbors_will_be_alive(self):
        cell = Corner([self.alive_cell]*Corner.NUMBER_OF_NEIGHBORS)
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertTrue(cell.alive)

    def test_corner_will_survive_if_two_neighbors_will_be_alive(self):
        cell = Corner([self.alive_cell]*2 + [self.dead_cell]*(Corner.NUMBER_OF_NEIGHBORS-2))
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertTrue(cell.alive)

    def test_corner_will_die_if_all_neighbors_will_be_dead(self):
        cell = Corner([self.dead_cell]*Corner.NUMBER_OF_NEIGHBORS)
        cell.set_alive()

        cell.prepare_next_state()
        cell.update_state()

        self.assertFalse(cell.alive)

if __name__ == "__main__":
    unittest.main()
