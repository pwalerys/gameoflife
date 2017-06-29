import unittest
from cell import Cell, State

class CellTest(unittest.TestCase):

    def setUp(self):
        self.alive_cell = Cell([None]*Cell.MAX_NEIGHBORS)
        self.alive_cell.state = State.ALIVE

        self.dead_cell = Cell([None]*Cell.MAX_NEIGHBORS)
        self.dead_cell.state = State.DEAD

        self.assertNotEqual(self.alive_cell, self.dead_cell)

    def test_next_state_will_be_dead_if_all_neighbors_are_dead(self):
        cell = Cell([self.dead_cell]*Cell.MAX_NEIGHBORS)
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.DEAD)

    def test_next_state_will_be_dead_if_all_neighbors_are_alive(self):
        cell = Cell([self.alive_cell]*Cell.MAX_NEIGHBORS)
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.DEAD)

    def test_cell_will_survive_if_two_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*2 + [self.dead_cell]*(Cell.MAX_NEIGHBORS-2))
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.ALIVE)

    def test_cell_will_survive_if_three_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*3 + [self.dead_cell]*(Cell.MAX_NEIGHBORS-3))
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.ALIVE)

    def test_cell_will_die_if_only_one_neighbor_will_be_alive(self):
        cell = Cell([self.alive_cell]*1 + [self.dead_cell]*(Cell.MAX_NEIGHBORS-1))
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.DEAD)

    def test_cell_will_die_if_more_than_three_neighbors_will_be_alive(self):
        for alive, dead in zip(range(4, Cell.MAX_NEIGHBORS + 1), range(Cell.MAX_NEIGHBORS - 4, 3, -1)):
            cell = Cell([self.alive_cell]*alive + [self.dead_cell]*dead)
            cell.state = State.ALIVE

            cell.prepare_next_state()
            cell.update_state()

            self.assertEqual(cell.state, State.DEAD)


if __name__ == "__main__":
    unittest.main()
