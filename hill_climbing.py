import score_function as score_f
import Bayesian_Network as BN
import numpy as np


def BIC_hill_climbing(dominio, dataset):
    n = np.size(dominio, 0)
    bn = BN.BayesianNetwork(n)
    score = 1000000
    while True:
        max_score = score
        for i in range(n):
            for j in range(0, n-i, 1):


    return bn