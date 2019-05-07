from .interaction.environment_outcome import EnvironmentOutcome
from .interaction.domain import Domain
from .interaction.transition_probability import TransitionProbability
from .model.base_model import BaseModel

from random import Random


class TabularRmaxModel(BaseModel):
    u"""Implementation of the Rmax model, based on the transition
    dynamics from a Tabular Model"""

    #TODO Check default value of confidence
    def __init__(self, domain, confidence=10):
        if isinstance(domain, Domain):
            raise TypeError("Must pass a correct Domain (sub)type")
        self.domain = domain
        self.state_nodes = {}
        self.terminal_states = set()
        self.confidence = confidence
        self.rand_generator = Random()
        self.

    def transition_is_modeled(self, state, actions):
        s_act_node = self.get_state_action_node(state, actions)
        if s_act_node and s_act_node.tries >= self.confidence:
            return True
        return False

    def transitions(self, state, actions):
        transitions = []
        s_act_node = self.get_state_action_node(state, actions)
        if not s_act_node:
            env_out = EnvironmentOutcome(0.0, state, actions,
                                         state, False)
            transitions.append(TransitionProbability(1.0, env_out))
        else:
            rew = s_act_node.sum_reward / s_act_node.tries
            for st in s_act_node.outcomes:
                p = float(s_act_node.outcomes[st]) / s_act_node.tries
                is_term = st in self.terminal_states
                env_out = EnvironmentOutcome(rew, state, actions,
                                             st, is_term)
                transitions.append(TransitionProbability(p, env_out))
        return transitions

    def update_model(self, env_outcome):
        #TODO: Fill
        pass

    def sample_by_enumeration(self, state, actions):
        trans_probs = self.transitions(state, actions)
        summ = 0
        next_float = self.rand_generator.random()
        for prob in trans_probs:
            summ += prob.probability
            if next_float < summ: return prob.env_outcome
        raise RMaxException("""There's an error regarding the
                               probability transitions.
                               Summation: %.2f""" % summ)

    def create_or_get_state_action_node(self, state, actions):
        state_node = self._get_state_node(state)
        if state_node: return state_node.get_action_node(actions)
        else:
            state_node = StateNode(state)
            self.state_nodes[state] = state_node
            act_typs = self.domain.action_types
            all_actions = ModelHelper.get_actions_from_type(act_typs,
                                                            state, self)
            for action in all_actions:
                st_ac_node = state_node.add_action_node(action)
                if action == actions: return st_act_node
        raise RMaxException("""Action not found for
                               model among all possible
                               courses of action: %s""" % actions)

    def get_state_action_node(self, state, actions):
        s_node = self._get_state_node(state)
        if s_node: return s_node.get_action_node(actions)

    # Pretending typing on dict
    def _get_state_node(self, state):
        self._check_if_state(state)
        return self.state_nodes[state]

    def _check_if_state(self, state):
        if not isinstance(state, State):
            raise TypeError("Must pass an instance of type State")


class RMaxException(Exception):
    u"""Named exception for the model"""
    pass
