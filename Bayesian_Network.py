import numpy as np


class BayesianNetwork:
    def __init__(self, N):
        self.N = N
        self.matrix = np.zeros((N, N))
        for i in range(1, N, 1):
            self.matrix[0, i] = 1

    def set_matrix(self, new_matrix):
        self.matrix = new_matrix

    def get_n(self):
        return self.N

    def get_parents(self, node_number):
        parents = []
        for i in range(self.N):
            if self.matrix[i, node_number] == 1:
                parents.append(i)
        return parents


def main():
    """"
    bn = BayesianNetwork(4)
    mat = np.zeros((4, 4))
    mat[0, 1] = 1
    mat[0, 2] = 1
    mat[0, 3] = 1
    mat[1, 3] = 1
    bn.set_matrix(mat)
    """


if __name__ == '__main__':
    main()