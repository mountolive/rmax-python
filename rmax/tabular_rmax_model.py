from .interaction.environment_outcome import EnvironmentOutcome
from .interaction.domain import Domain
from .interaction.transition_probability import TransitionProbability
from .model.base_model import BaseModel


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

