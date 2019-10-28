import sys
import logging
from bonsai_ai import Brain, Config
from bonsai_gym import GymSimulator
from gym_brt.envs import QubeSwingupEnv

log = logging.getLogger("gym_simulator")
log.setLevel(logging.DEBUG)

class Qube(GymSimulator):
    environment_name = "CartPole-v0"  # Hacky, opens cartpole but never used
    simulator_name = "QubeSimulator"

    def __init__(self, brain):
        super(Qube, self).__init__(brain)
        self._env = QubeSwingupEnv(use_simulator=True, frequency=250)

    def gym_to_state(self, observation):
        state = {
            "theta": observation[0],
            "alpha": observation[1],
            "theta_dot": observation[2],
            "alpha_dot": observation[3],
        }
        return state

    def action_to_gym(self, inkling_action):
        return inkling_action["command"]


if __name__ == "__main__":
    # create a brain, openai-gym environment, and simulator
    config = Config(sys.argv)
    brain = Brain(config)
    sim = Qube(brain, skip_frame=SKIP_FRAME)
    sim.run_gym()
