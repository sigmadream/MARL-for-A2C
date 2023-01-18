"""
RWare Test
"""

import gym
import time


env = gym.make("rware:rware-small-4ag-v1")

obs_space = env.observation_space
action_space = env.action_space

num_steps = 1500

obs = env.reset()

for step in range(num_steps):
    action = env.action_space.sample()

    # apply the action
    obs, reward, done, info = env.step(action)

    # Render the env
    env.render()

    # Wait a bit before the next frame unless you want to see a crazy fast video
    time.sleep(0.001)

    # If the epsiode is up, then start another one
    if done:
        env.reset()

env.close()
