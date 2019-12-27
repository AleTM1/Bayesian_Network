import math
import Bayesian_Network
import numpy as np


def score_function(bayesian_network, domini, dataset):
    n = bayesian_network.get_n()
    r = domini
    q = np.array(n)
    for j in range(n):
        p = 1

