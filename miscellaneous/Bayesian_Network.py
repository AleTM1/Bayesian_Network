import numpy as np
import random


class BayesianNetwork:
    def __init__(self, N):
        random.seed()
        self.max_parents = 3
        self.max_children = 3
        self.N = N
        self.matrix = np.zeros((N, N))

    def generate_DAG(self):
        n = int(self.N)
        k = 0
        while k < n:
            link = [random.randint(0, self.N - 1), random.randint(0, self.N - 1)]
            if self.matrix[link[0], link[1]] == 0 and link[0] != link[1] and self.add_link(link):
                k += 1

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
        if len(self.get_parents(link[1])) >= self.max_parents or len(self.get_children(link[0])) >= self.max_children or search_path_bfs(link[1], link[0], self):
            return False
        self.matrix[link[0], link[1]] = 1
        return True

    def remove_link(self, link):
        self.matrix[link[0], link[1]] = 0

    def change_link(self, link):
        self.matrix[link[0], link[1]] = 0
        if len(self.get_parents(link[0])) >= self.max_parents or len(self.get_children(link[1])) >= self.max_children or search_path_bfs(link[0], link[1], self):
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
