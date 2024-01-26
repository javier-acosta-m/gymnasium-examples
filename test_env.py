import gymnasium
import gym_examples
import numpy as np
import random

# create Taxi environment
env = gymnasium.make('gym_examples/GridWorld-v0', render_mode="human")

# create a new instance of taxi, and get the initial state
state = env.reset()

num_steps = 50
for s in range(num_steps+1):
    print(f"step: {s} out of {num_steps}")

    # sample a random action from the list of available actions
    action = env.action_space.sample()

    # perform this action on the environment
    env.step(action)

    # print the new state
    env.render()

# end this instance of the taxi environment
env.close()