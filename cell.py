
from enum import Enum

class State(Enum):
    DEAD = 0
    ALIVE = 1

class Cell:
    NUMBER_OF_NEIGHBORS = 8

    def __init__(self, neighbors):
        assert len(neighbors) == self.NUMBER_OF_NEIGHBORS, "Cell has to have {} neighbors. Actual list: {}".format(self.NUMBER_OF_NEIGHBORS, neighbors)
        self.neighbors = neighbors
        self.next_state = State.DEAD
        self.state = State.DEAD

    def prepare_next_state(self):
        alive = [n for n in self.neighbors if n.state is State.ALIVE]
        self.next_state = State.ALIVE if len(alive) in [2, 3] else State.DEAD

    def update_state(self):
        self.state = self.next_state

    @property
    def alive(self):
        return self.state == State.ALIVE

    def set_alive(self):
        self.state = State.ALIVE

    def set_dead(self):
        self.state = State.DEAD

    def __str__(self):
        return 'X' if self.alive else 'O'
