import score_function as score_f
import Bayesian_Network as BN
import numpy as np
import copy


def BIC_hill_climbing(dominio, dataset):
    n = np.size(dominio, 0)
    bn = BN.BayesianNetwork(n)
    score = 10000000
    while True:
        max_score = score
        for i in range(n):
            for j in range(0, n-i, 1):
                print("i: ", i, " j: ", j)
                bn1 = copy.deepcopy(bn)
                bn2 = copy.deepcopy(bn)
                bn3 = copy.deepcopy(bn)
                score1 = 10000000
                score2 = 10000000
                score3 = 10000000
                if bn.get_matrix()[i][j] == 0 and bn1.add_link([i, j]):
                    score1 = score_f.score_function(bn1, dominio, dataset)
                    if score1 < score:
                        score = score1
                        bn = bn1
                else:
                    if bn.get_matrix()[i][j] == 1:
                        score2 = score_f.score_function(bn2.remove_link([i, j]), dominio, dataset)
                    if bn.get_matrix()[i][j] == 1 and bn3.change_link([i, j]):
                        score3 = score_f.score_function(bn3, dominio, dataset)
                    if score2 < score3 and score2 < score:
                        bn = bn2
                    elif score3 < score2 and score3 < score:
                        bn = bn3
        if max_score <= score:
            break
    return bn



