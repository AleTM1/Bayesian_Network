from structure_learn import score_function as score_f
from miscellaneous import Bayesian_Network as BN
import numpy as np
import copy


def BIC_hill_climbing(dominio, dataset):
    n = np.size(dominio, 0)
    bn_best = BN.BayesianNetwork(n)
    best_score = score_f.score_function(bn_best, dominio, dataset)
    print(best_score)
    for temp in range(n*2):
        print("Restart: ", temp + 1)
        bn = BN.BayesianNetwork(n)
        bn.generate_DAG()
        score = score_f.score_function(bn, dominio, dataset)
        while True:
            max_score = score
            for i in range(n):
                for j in range(0, n-i, 1):
                    if i != j:
                        bn1 = copy.deepcopy(bn)
                        bn2 = copy.deepcopy(bn)
                        bn3 = copy.deepcopy(bn)
                        score2 = 10000000
                        score3 = 10000000
                        if bn.get_matrix()[i][j] == 0 and bn1.add_link([i, j]):
                            score1 = score_f.score_function(bn1, dominio, dataset)
                            if score1 < score:
                                score = score1
                                bn = bn1
                        else:
                            if bn.get_matrix()[i][j] == 1:
                                bn2.remove_link([i, j])
                                score2 = score_f.score_function(bn2, dominio, dataset)
                            if bn.get_matrix()[i][j] == 1 and bn3.change_link([i, j]):
                                score3 = score_f.score_function(bn3, dominio, dataset)
                            if score2 < score3 and score2 < score:
                                bn = bn2
                                score = score2
                            elif score3 < score2 and score3 < score:
                                bn = bn3
                                score = score3
                print(bn.get_matrix())
                print(score)
                print(" ------------ ", i, " ------------ ")
            if max_score <= score:
                if max_score <= best_score:
                    best_score = max_score
                    bn_best = bn
                break
    return bn_best, best_score



