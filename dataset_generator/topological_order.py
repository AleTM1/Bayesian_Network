import numpy as np


def starter_set(structure_matrix, n):
    #   cerca i nodi senza archi entranti
    nodes = []
    for j in range(n):
        no_parents = True
        for i in range(n):
            if structure_matrix[i, j] == 1:
                no_parents = False
                break
        if no_parents:
            nodes.append(j)
    return nodes


def get_children(structure_matrix, n, node_number):
    children = []
    for i in range(n):
        if structure_matrix[node_number, i] == 1:
            children.append(i)
    return children


def has_parents(structure_matrix, n, node_number):
    for i in range(n):
        if structure_matrix[i, node_number] == 1:
            return True
    return False


# Kahn's algorithm
def topological_ord(structure_matrix):
    n = np.size(structure_matrix, 0)
    explored = np.zeros(n)
    act_set = starter_set(structure_matrix, n)
    k = 0
    while len(act_set) != 0:
        node = act_set.pop()
        explored[k] = node
        k += 1
        for m in get_children(structure_matrix, n, node):
            structure_matrix[node, m] = 0
            if not has_parents(structure_matrix, n, m):
                act_set.append(m)
    return explored


def main():
    matrix = np.zeros((8, 8))
    matrix[0, 1] = 1
    matrix[1, 5] = 1
    matrix[2, 3] = 1
    matrix[2, 4] = 1
    matrix[3, 5] = 1
    matrix[4, 7] = 1
    matrix[5, 6] = 1
    matrix[5, 7] = 1

    print(topological_ord(matrix))


if __name__ == '__main__':
    main()