import numpy as np
from numpy.random import default_rng
import seaborn as sns
from matplotlib import pyplot as plt

if __name__ == "__main__":
    rng = default_rng()

    # sample of size 10,000 drawn from an exponential distribution
    sample = rng.exponential(1, 10000)
    sns.displot(sample)
    plt.show()
