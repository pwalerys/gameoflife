import unittest
from cell import Cell, State

class CellTest(unittest.TestCase):

    def setUp(self):
        self.alive_cell = Cell([None]*8)
        self.alive_cell.state = State.ALIVE

        self.dead_cell = Cell([None]*8)
        self.dead_cell.state = State.DEAD

        self.assertNotEqual(self.alive_cell, self.dead_cell)

    def test_next_state_will_be_dead_if_all_neighbors_are_dead(self):
        cell = Cell([self.dead_cell]*8)
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.DEAD)

    def test_next_state_will_be_dead_if_all_neighbors_are_alive(self):
        cell = Cell([self.alive_cell]*8)
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.DEAD)

    def test_cell_will_survive_if_two_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*2 + [self.dead_cell]*6)
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.ALIVE)

    def test_cell_will_survive_if_three_neighbors_will_be_alive(self):
        cell = Cell([self.alive_cell]*3 + [self.dead_cell]*5)
        cell.state = State.ALIVE

        cell.prepare_next_state()
        cell.update_state()

        self.assertEqual(cell.state, State.ALIVE)


if __name__ == "__main__":
    unittest.main()
