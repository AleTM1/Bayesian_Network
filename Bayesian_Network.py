import numpy as np


class BayesianNetwork:
    def __init__(self, N):
        self.N = N
        self.matrix = np.zeros((N, N))
        """""
        for i in range(0, N, 1):
            self.matrix[1, i] = 1
        self.matrix[1, 1] = 0
    
        self.matrix[1, 2] = 1
        self.matrix[23, 24] = 1
        """""

    def set_matrix(self, new_matrix):
        self.matrix = new_matrix

    def get_matrix(self):
        return self.matrix

    def get_n(self):
        return self.N

    def get_parents(self, node_number):
        parents = []
        for i in range(self.N):
            if self.matrix[i, node_number] == 1:
                parents.append(i)
        return parents

    def get_children(self, node_number):
        children = []
        for i in range(self.N):
            if self.matrix[node_number, i] == 1:
                children.append(i)
        return children

    def add_link(self, link):
        if search_path_bfs(link[1], link[0], self):
            return False
        self.matrix[link[0], link[1]] = 1
        return True

    def remove_link(self, link):
        self.matrix[link[0], link[1]] = 0

    def change_link(self, link):
        self.matrix[link[0], link[1]] = 0
        if search_path_bfs(link[0], link[1], self):
            self.matrix[link[0], link[1]] = 1
            return False
        self.matrix[link[1], link[0]] = 1
        return True


def search_path_bfs(v, u, bn):
    visited = [False] * (bn.get_n())
    queue = [v]
    visited[v] = True
    while len(queue) > 0:
        node = queue.pop(0)
        if node == u:
            return True
        for i in bn.get_children(node):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False


def main():
    """""
    bn = BayesianNetwork(4)
    mat = np.zeros((4, 4))
    mat[0, 1] = 1
    mat[0, 2] = 1
    mat[0, 3] = 1
    mat[1, 3] = 1
    bn.set_matrix(mat)
    print(mat)
    if bn.change_link([0, 1]):
        print("Cambiato")
        print(bn.get_matrix())
    else:
        print("Rimasto")
        print(bn.get_matrix())
    """


if __name__ == '__main__':
    main()