Updated to work with Gymnasium

# Gymnasium Environment Example
Simple GriddWorld environment and wrappers example.

[Tutorial](https://www.gymlibrary.dev/content/environment_creation)

### Environments
This repository hosts the examples that are shown [on the environment creation documentation](https://gymnasium.farama.org/tutorials/environment_creation/).

- `GridWorldEnv`: Simplistic implementation of gridworld environment

### Wrappers
This repository hosts the examples that are shown [on wrapper documentation](https://gymnasium.farama.org/api/wrappers/).
- `ClipReward`: A `RewardWrapper` that clips immediate rewards to a valid range
- `DiscreteActions`: An `ActionWrapper` that restricts the action space to a finite subset
- `RelativePosition`: An `ObservationWrapper` that computes the relative position between an agent and a target
- `ReacherRewardWrapper`: Allow us to weight the reward terms for the reacher environment


Doumentation [the documentation repo](https://github.com/Farama-Foundation/Gymnasium/blob/main/docs/tutorials/gymnasium_basics/environment_creation.py)


# Run
```console
git clone https://github.com/javier-acosta-m/gymnasium-examples.git
cd gym-examples
python -m venv env
Linux:
source env/bin/activate
Windows:
env\Scripts\activate
pip install -e .
python run_test.py
```
