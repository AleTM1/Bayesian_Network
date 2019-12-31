import math
from miscellaneous import Bayesian_Network as BN
from dataset_generator import dataset_gen as generator
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

    d = sum((int(q[i]) * (r[i] - 1)) for i in range(n))
    sommatoria = 0
    for i in range(n):
        for j in range(int(q[i])):
            for k in range(r[i]):
                sommatoria += (Nijk_array[i][j][k] + 1) * math.log2((Nijk_array[i][j][k] + 1) / (Nij_array[i][j] + 1))

    score = sommatoria - (d / 2) * math.log2(np.size(dataset, 0))
    return score


def main():
    bn = BN.BayesianNetwork(8)
    matrix = np.zeros((8, 8))
    matrix[0, 1] = 0  # mod [0,1] = 1
    matrix[1, 5] = 1
    matrix[3, 2] = 1  # mod [2,3] = 1
    matrix[2, 4] = 1
    matrix[3, 5] = 1
    matrix[4, 7] = 1
    matrix[5, 6] = 1
    matrix[5, 7] = 1
    bn.set_matrix(matrix)

    domini = [2, 2, 2, 2, 2, 2, 2, 2]

    states_path = '/home/alessandro/Documenti/IA/Datasets/Asia/states.csv'
    prob_table_path = '/home/alessandro/Documenti/IA/Datasets/Asia/prob.csv'
    structure_path = '/home/alessandro/Documenti/IA/Datasets/Asia/structure.csv'
    data = generator.importer.csv_to_numpy(states_path, prob_table_path, structure_path)
    dataset = generator.dataset_gen(data[0], data[1], data[2], 20000)
    print("Dataset generato")

    new_score = score_function(bn, domini, dataset)
    print(bn.get_matrix())
    print(new_score)
    print("+++")


if __name__ == '__main__':
    main()