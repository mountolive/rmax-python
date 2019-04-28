from .environment_outcome import EnvironmentOutcome


class TransitionProbability:
    u"""Object that defines a transition probability,
    contains the actual p value and the outcome of the transition
    as an EnvironmentOutcome"""

    def __init__(self, probability, env_outcome):
        self.probability = probability
        self.env_outcome = env_outcome
