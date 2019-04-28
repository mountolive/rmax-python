from .base_model import BaseModel
from .interaction.multi_action import MultiAction
from itertools import product


class ModelHelper:
    u"""Simple helper class for filtering and misc"""

    def __init__(self, model):
        if not issubclass(model, BaseModel):
            raise TypeError('Passed instance is not a model')
        self.model = model

    def state_transition_model(self, action_types, state):
        multi_acts = self._get_actions_from_type(action_types, state)
        trans_modeled = self.model.transition_is_modeled
        return all(trans_modeled(state, action) for action in multi_acts)

    def unmodeled_actions(self, action_types, state):
        multi_acts = self._get_actions_from_type(action_types, state)
        trans_modeled = self.model.transition_is_modeled
        return [act for act in multi_acts if not trans_modeled(state, act)]

    def _get_actions_from_type(self, action_types, statei, n_agents=2):
        list_actions = map(lambda x: x.all_applicable_actions(state),
                           action_types)
        actions_set = set([a for li in list_actions for a in li])
        result_actions = []
        for vector in product(actions_set, repeat=n_agents):
            result_actions.append(MultiAction(vector))
        return result_actions
