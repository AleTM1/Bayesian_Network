import math
import Bayesian_Network as BN
import numpy as np


def score_function(bayesian_network, domini, dataset):
    n = bayesian_network.get_n()
    r = domini
    q = np.ones(n)
    for i in range(n):
        p = 1
        parents = bayesian_network.get_parents(i)
        if len(parents) > 0:
            for j in range(len(parents)):
                p = p * r[parents[j]]
        q[i] = p
    print(q)


def main():
    bn = BN.BayesianNetwork(4)
    mat = np.zeros((4, 4))
    mat[0, 1] = 1
    mat[0, 2] = 1
    mat[0, 3] = 1
    mat[1, 3] = 1
    bn.set_matrix(mat)

    domini = [2, 3, 2, 4]
    data = np.zeros((5, 4))
    data[1, 0] = 1
    data[1, 1] = 2
    data[1, 2] = 1
    data[1, 3] = 3
    data[2, 0] = 1
    data[2, 1] = 1
    data[2, 3] = 1
    data[4, 0] = 1
    data[4, 1] = 1
    data[4, 2] = 1
    data[4, 3] = 2

    score_function(bn, domini, data)


if __name__ == '__main__':
    main()