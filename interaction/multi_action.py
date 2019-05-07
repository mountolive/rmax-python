from collections.abc import Iterable


class MultiAction:
    u"""This class defines a tuple for actions where
    each index of the tuple corresponds to a given agent's
    action"""

    def __init__(self, actions):
        if not isinstance(actions, Iterable):
            raise TypeError("Must pass an iterable as actions")
        if not all(isinstance(action, Action) for action in actions):
            raise TypeError("Must pass an iterable of actions")
        self.actions = tuple(actions)

    def __eq__(self, other):
        if type(other) is not MultiAction: return False
        return self.actions == other.actions

    def __hash__(self):
        return hash(self.actions)

    def __str__(self):
        return "Action Vector ( %s )" % ",".join(self.actions)
