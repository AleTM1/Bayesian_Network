from dataset_generator import topological_order as top_ord
import numpy as np
import copy
import random
import math


def get_parents(structure_matrix, n, node_number):
    parents = []
    for i in range(n):
        if structure_matrix[i, int(node_number)] == 1:
            parents.insert(0, i)
    return parents


def dataset_gen(dominio, structure_matrix, probabilities, n):
    random.seed()
    ordered_array = top_ord.topological_ord(copy.deepcopy(structure_matrix))
    dataset = np.zeros((n, len(dominio)))
    for i in range(n):
        for j in range(len(ordered_array)):
            value = random.random()
            if len(probabilities[int(ordered_array[j])]) == 1:
                if value <= probabilities[int(ordered_array[j])]:
                    dataset[i, int(ordered_array[j])] = 1
                else:
                    dataset[i, int(ordered_array[j])] = 0
            else:
                index = 0
                parents = get_parents(structure_matrix, len(dominio), ordered_array[j])
                for k in range(int(math.log2(len(probabilities[int(ordered_array[j])])))):
                    index += dataset[i, parents[k]] * (2**k)
                if value <= probabilities[int(ordered_array[j])][int(index)]:
                    dataset[i, int(ordered_array[j])] = 1
                else:
                    dataset[i, int(ordered_array[j])] = 0
    return dataset
