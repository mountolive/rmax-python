

class Action:
    u"""Base class for actions. Must be hashable"""

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Action): return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

