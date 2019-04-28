

class EnvironmentOutcome:
    u"""Tuple class that holds the data related to a given
    state transition in the game"""

    def __init__(self, probability, reward, start_state,
                 actions, end_state, terminated):
        self.probability = probability
        self.reward = reward
        self.actions = actions
        self.start_state = start_state
        self.end_state = end_state
        self.terminated = terminated
