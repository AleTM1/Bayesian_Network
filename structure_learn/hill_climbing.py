from structure_learn import score_function as score_f
from miscellaneous import Bayesian_Network as BN
import numpy as np
import copy


def BIC_hill_climbing(dominio, dataset, t):
    n = np.size(dominio, 0)
    bn_best = BN.BayesianNetwork(n)
    best_score = score_f.score_function(bn_best, dataset)
    for temp in range(t):
        print("Restart: ", temp + 1)
        temp_bn = BN.BayesianNetwork(n)
        temp_bn.generate_DAG()
        temp_score = score_f.score_function(temp_bn, dataset)
        best_action_score = temp_score
        best_action_bn = temp_bn
        while True:
            #   cerco l'azione sulla matrice che massimizzi lo score e salvo la struttura
            for i in range(n):
                for j in range(n):
                    if i != j:
                        bn1 = copy.deepcopy(temp_bn)
                        bn2 = copy.deepcopy(temp_bn)
                        bn3 = copy.deepcopy(temp_bn)
                        score2 = -10000000000
                        score3 = -10000000000
                        if temp_bn.get_matrix()[i][j] == 0 and bn1.add_link([i, j]):
                            score1 = score_f.score_function(bn1, dataset)
                            if score1 > best_action_score:
                                best_action_score = score1
                                best_action_bn = bn1
                        else:
                            if temp_bn.get_matrix()[i][j] == 1:
                                bn2.remove_link([i, j])
                                score2 = score_f.score_function(bn2, dataset)
                            if temp_bn.get_matrix()[i][j] == 1 and bn3.change_link([i, j]):
                                score3 = score_f.score_function(bn3, dataset)
                            if score2 > score3 and score2 > best_action_score:
                                best_action_bn = bn2
                                best_action_score = score2
                            elif score3 > score2 and score3 > best_action_score:
                                best_action_bn = bn3
                                best_action_score = score3
            #   aggiorno se ho un miglioramento e mi fermo se non esiste un'azione che incrementa lo score
            if best_action_score > temp_score:
                temp_score = best_action_score
                temp_bn = best_action_bn
            else:
                if temp_score > best_score:
                    best_score = temp_score
                    bn_best = temp_bn
                    print("+++ AGGIORNO +++")
                print(temp_bn.get_matrix())
                print("---------- score: ", temp_score, " -------------")
                break

    return bn_best, best_score



