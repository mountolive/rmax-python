from .base_model import BaseModel
from .interaction.multi_action import MultiAction
from itertools import product


class ModelHelper:
    u"""Simple helper class for filtering and misc"""

    @staticmethod
    @check_model
    def state_transition_model(cls, action_types, state, model=None):
        multi_acts = cls.get_actions_from_type(action_types, state)
        trans_modeled = model.transition_is_modeled
        return all(trans_modeled(state, action) for action in multi_acts)

    @staticmethod
    @check_model
    def unmodeled_actions(cls, action_types, state, model=None):
        multi_acts = cls.get_actions_from_type(action_types, state)
        trans_modeld = model.transition_is_modeled
        return [act for act in multi_acts if not trans_modeld(state, act)]

    @staticmethod
    @check_model
    def get_actions_from_type(cls, action_types, state,
                              model=None, n_agents=2):
        list_actions = map(lambda x: x.all_applicable_actions(state),
                           action_types)
        actions_set = set([a for li in list_actions for a in li])
        result_actions = []
        for vector in product(actions_set, repeat=n_agents):
            result_actions.append(MultiAction(vector))
        return result_actions

    def check_model(func):
        def check_and_call(*args, **kwargs):
            model = kwargs['model']
            if not issubclass(model, BaseModel):
                raise TypeError('Passed instance is not a model')
            return func(*args, **kwargs)
        return check_and_call


