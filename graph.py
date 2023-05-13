from collections import defaultdict
import random


class Graph:
    def __init__(self, vertices, directed=False):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.directed = directed
        self._weights = {}
        self._edges = []

    def add_edge(self, u, v, w=0):
        self.graph[u].append((v, w))
        self._weights[(u, v)] = w
        self._edges.append((u, v))

        if not self.directed:
            self.graph[v].append((u, w))

    def get_neighbors(self, v):
        return self.graph[v]

    def get_weights(self):
        return self._weights

    def get_edges(self):
        return self._edges


def create_random_graph(n_vertices, edge_prob, weight_range, directed):
    graph = Graph(n_vertices, directed)
    for i in range(n_vertices):
        for j in range(i + 1, n_vertices):
            if random.random() < edge_prob:
                weight = random.randint(*weight_range)
                graph.add_edge(i, j, weight)

    return graph
