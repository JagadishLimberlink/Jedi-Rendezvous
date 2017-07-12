import gym
from gym import wrappers
import numpy as np
from collections import deque

#Maintain the first successful path in a dictionary
spath = {}
found = False

env = gym.make('FrozenLake-v0')

episodes = 10000
total=0


for ep in range(episodes + 1):
    history = deque(maxlen=200)
    state = env.reset()
    done = False
    while not done:
	if found==True and (state in spath.keys()):
	   act = spath[state]
	else:
	   act = env.action_space.sample()

        state_new, r, done, _ = env.step(act)
	history.append([state, act, state_new, r])
        state = state_new
	if done: total+=r
    

    # Previous moves
    if total==1.0 and False==found:
    	while len(history):
        	state, act, state_new, r = history.pop()
	  	spath[state]=act 

    if total==1.0:
	found = True


print spath	
print total

