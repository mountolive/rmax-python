from abc import ABC, abstractmethod

class BaseModel(ABC):
    u""" Base Model class for validation purposes"""

    @abstractmethod
    def transition_is_modelled(self, state, actions):
        pass
