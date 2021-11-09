import numpy as np
from numpy.random import default_rng
import seaborn as sns
from matplotlib import pyplot as plt

# A script to simulate telegraph noise alternating between states 0 (state A) and 1 (state B) 

if __name__ == "__main__":
    # number of time steps in the experiment
    num_time_steps = 500

    # assume initial state is 0 (state A)
    curr_state = 0

    # transition probabilities
    k_a = 0.02 # a --> b
    k_b = 0.06 # b --> a
    
    transition_probabilities = (k_a, k_b)

    # the list of noise values
    noise = [0]

    rng = default_rng()
    for _ in range(num_time_steps):
        if rng.uniform() < transition_probabilities[curr_state]:
            # transition to the opposite state
            curr_state = (curr_state + 1) % 2
        noise.append(curr_state)
            
    sns_plot = sns.lineplot(x = range(num_time_steps + 1), y = noise)
    plt.show()

    sns_plot.figure.savefig("telegraph_noise_example.png")
