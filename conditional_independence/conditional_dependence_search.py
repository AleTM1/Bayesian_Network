import numpy as np
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


def search_path_bfs(v, u, matrix, n):
    visited = [False] * n
    queue = [v]
    visited[v] = True
    path = [v]    ###################
    while len(queue) > 0:
        node = queue.pop(0)
        if node == u:
            path.append(u)  ###################
            print(path) ###################
            return True
        for i in get_children(matrix, n, node):
            if not visited[i]:
                path.append(i)  ###################
                queue.append(i)
                visited[i] = True
    return False


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

    #   creo la matrice delle dipendenze
    dependencies = []
    for link in couples:
        if not search_path_bfs(link[0], link[1], undirect_matrix, n):
            dependencies.append([])
        else:
            # TODO
            dependencies.append([-1, -1])

    print(couples)
    print(dependencies)


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