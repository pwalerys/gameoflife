
from enum import Enum

class State(Enum):
    DEAD = 0
    ALIVE = 1

class Cell:
    def __init__(self, neighbors):
        assert len(neighbors) == 8, "Cell has to have 8 neighbors. Actual list: ".format(neighbors)
        self.neighbors = neighbors
        self.next_state = State.DEAD
        self.state = State.DEAD

    def prepare_next_state(self):
        alive = [n for n in self.neighbors if n.state is State.ALIVE]
        self.next_state = State.ALIVE if len(alive) in [2, 3] else State.DEAD

    def update_state(self):
        self.state = self.next_state

