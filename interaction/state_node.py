from .multi_action import MultiAction
from .state_action_node import StateActionNode


class StateNode:
    u"""Bookeeping class for states"""

    def __init__(self, state):
        self.state = state
        self.action_nodes = {}

    # These methods are made to have a way to enforce
    # a dict from actions to StateActionNode

    def get_action_node(self, actions):
        self._check_if_action(actions)
        return self.action_nodes[actions]

    def add_action_node(self, actions):
        self._check_if_action(actions)
        state_action_node = StateActionNode(actions)
        self.action_nodes[actions] = state_action_node
        return state_action_node

    def _check_if_action(self, actions):
        if not isinstance(action, MultiAction):
            raise TypeError("Must pass an instance of type MultiAction")

