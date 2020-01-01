import numpy as np
import networkx as nx
from miscellaneous import Bayesian_Network as BN


def get_parents(matrix, n, node_number):
    parents = []
    for i in range(n):
        if matrix[i, node_number] == 1:
            parents.append(i)
    return parents


def get_children(matrix, n, node_number):
    children = []
    for i in range(n):
        if matrix[node_number, i] == 1:
            children.append(i)
    return children


def path_finder_undirect_graph(src, dst, matrix):
    nx_graph = nx.from_numpy_matrix(matrix)
    return list(nx.all_simple_paths(nx_graph, source=src, target=dst))


def search_conditional_dependence(direct_matrix):
    n = np.size(direct_matrix, 0)
    #   coppie di nodi da confrontare
    couples = []
    for i in range(n):
        #   parto da i+1 per evitare duplicati (dato che la relazione è commutativa) ed evitare confronti con se stessi
        for j in range(i+1, n, 1):
            if j not in get_parents(direct_matrix, n, i) and j not in get_children(direct_matrix, n, i):
                couples.append([i, j])

    #   crea matrice indiretta
    undirect_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if direct_matrix[i, j] == 1:
                undirect_matrix[i, j] = 1
                undirect_matrix[j, i] = 1

    paths = []
    for link in couples:
        paths.append(path_finder_undirect_graph(link[0], link[1], undirect_matrix))

    #   creo la matrice delle dipendenze
    dependencies_arrays = []
    for p in paths:
        dep = []
        # cerco i nodi da cui p_src e p_dst dipendono condizionalmente dove p è uno dei cammini da paths_src e path_dst
        if len(p) > 0:
            for k in range(len(p)):
                dk = []
                pp = p[k]
                for node in range(1, len(pp) - 1, 1):
                    l1 = direct_matrix[pp[node - 1], pp[node]]
                    l2 = direct_matrix[pp[node], pp[node + 1]]
                    if (l1 == 1 and l2 == 1) or (l1 == 0 and l2 == 0) or (l1 == 0 and l2 == 1):
                        dk.append(pp[node])
                if len(dk) > 0:
                    dep.append(dk)
            dependencies_arrays.append(dep)
        else:
            dependencies_arrays.append([])

    #   cerco i nodi che inattivano tutti i sub_path
    intersection = []
    for dep in dependencies_arrays:
        if len(dep) == 0:
            intersection.append([])
        elif len(dep) == 1:
            intersection.append(dep[0])
        else:
            d = dep[0]
            for i in range(1, len(dep)):
                d = [value for value in d if value in dep[i]]
            intersection.append(d)

    for i in range(len(couples)):
        dependence = dependencies_arrays[i]
        if len(dependence) == 0:
            print("Il nodo ", couples[i][0], " ed il nodo ", couples[i][1], "sono marginalmente indipendenti")
        elif len(dependence) == 1:
            print("Il nodo ", couples[i][0], " ed il nodo ", couples[i][1], "sono condizionalmente indipendenti dato uno dei seguenti nodi: ", *dependence[0])
        else:
            if len(intersection[i]) > 0:
                print("Il nodo ", couples[i][0], " ed il nodo ", couples[i][1], "sono condizionalmente indipendenti dati i nodi: ", intersection[i][0])
            else:
                print("Il nodo ", couples[i][0], " ed il nodo ", couples[i][1], "sono condizionalmente indipendenti dati un nodo per ognuno dei seguenti gruppi: ", *dependence)


def main():

    matrix = np.zeros((8, 8))
    matrix[0, 1] = 0  # mod [0,1] = 1
    matrix[1, 5] = 1
    matrix[3, 2] = 1  # mod [2,3] = 1
    matrix[2, 4] = 1
    matrix[3, 5] = 1
    matrix[4, 7] = 1
    matrix[5, 6] = 1
    matrix[5, 7] = 1

    search_conditional_dependence(matrix)


if __name__ == '__main__':
    main()