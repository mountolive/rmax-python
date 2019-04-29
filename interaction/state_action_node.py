from collections import Counter
from .multi_action import MultiAction


class StateActionNode:
    u"""Class that does bookeeping of joint actions/states
    results"""

    def __init__(self, actions, state=None):
        if not isinstance(actions, MultiAction):
            raise TypeError("actions must be of type MultiAction")
        self.actions = actions
        self.sum_reward = 0.0
        self.tries = 0
        self.outcomes = Counter()
        if state: self.outcomes[state] += 1

    def update(self, state, reward):
        self.tries += 1
        self.sum_reward += reward
        self.outcomes[state] += 1



