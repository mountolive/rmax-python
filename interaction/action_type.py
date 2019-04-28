from abc import ABC, abstractmethod


class ActionType(ABC):
    u""" This class states the filtering base for each state's
    actions"""

    @abstractmethod
    def all_applicable_actions(self, state):
        pass
