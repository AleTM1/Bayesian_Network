import math
import Bayesian_Network as BN
import numpy as np


def score_function(bayesian_network, domini, dataset):
    n = bayesian_network.get_n()
    r = domini
    q = np.ones(n)   # produttoria dei domini dei genitori della variabile i-esima
    parents = []
    for i in range(n):
        p = 1
        pp = bayesian_network.get_parents(i)
        if len(pp) > 0:
            parents.append(pp)
            for j in range(len(pp)):
                p = p * r[pp[j]]
        else:
            parents.append([])
        q[i] = p

    ij_array = []
    for i in range(n):
        if len(parents[i]) == 0:
            ij_actual = np.zeros((1, 1))
            ij_actual[0, 0] = -1
            ij_array.append(ij_actual)
        else:
            ij_actual = np.zeros((int(q[i]), len(parents[i])))
            act_q = q[i]
            for col in range(len(parents[i])):
                for row in range(int(q[i])):
                    ij_actual[row, col] = ((row - (row % (int(act_q) / (r[(parents[i])[col]])))) * r[(parents[i])[col]]) / (int(act_q))
                    ij_actual[row, col] = ij_actual[row, col] % (r[(parents[i])[col]])
                act_q = act_q / (r[(parents[i])[col]])
            ij_array.append(ij_actual)

    Nij_array = []
    Nijk_array = []
    for i in range(n):
        act_Nij = []
        act_Nijk_array = []
        for j in range(int(q[i])):
            count_ij = 0
            act_Nijk = np.zeros(r[i])
            for d in range(np.size(dataset, 0)):
                match = True
                for m in range(len(parents[i])):
                    if (dataset[d])[parents[i][m]] != ij_array[i][j][m]:
                        match = False
                        break
                if match:
                    count_ij += 1
                    act_Nijk[int(dataset[d][i])] += 1
            act_Nij.append(count_ij)
            act_Nijk_array.append(act_Nijk)
        Nijk_array.append(act_Nijk_array)
        Nij_array.append(act_Nij)

    #   funzione di calcolo

    sommatoria = 0
    for i in range(n):
        for j in range(int(q[i])):
            for k in range(r[i]):
                sommatoria += math.log2((math.gamma(1))/(math.gamma(1 + Nij_array[i][j])) * (math.gamma(1 + Nijk_array[i][j][k]))/(math.gamma(1)))

    return sommatoria


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

    new_score = score_function(bn, domini, data)
    print(new_score)


if __name__ == '__main__':
    main()