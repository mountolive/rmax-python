

class State:
    u"""Basic standarization of what should be a state
    of a game. Must be hashable"""

    def __init__(self, unique_name):
        self.name = unique_name

    def __eq__(self, other):
        if isinstance(other, State): return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)
