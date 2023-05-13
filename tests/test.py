import unittest
from graph import *


class TestGraph(unittest.TestCase):
    def setUp(self):

        self.directed_graph = Graph(5, directed=True)
        self.directed_graph.add_edge(0, 1, 2)
        self.directed_graph.add_edge(0, 2, 3)
        self.directed_graph.add_edge(1, 3, 4)
        self.directed_graph.add_edge(2, 3, 1)
        self.directed_graph.add_edge(2, 4, 5)
        self.directed_graph.add_edge(3, 4, 6)

        self.undirected_graph = Graph(5, directed=False)
        self.undirected_graph.add_edge(0, 1, 2)
        self.undirected_graph.add_edge(0, 2, 3)
        self.undirected_graph.add_edge(1, 3, 4)
        self.undirected_graph.add_edge(2, 3, 1)
        self.undirected_graph.add_edge(2, 4, 5)
        self.undirected_graph.add_edge(3, 4, 6)

        self.negative_graph = Graph(5, directed=True)
        self.negative_graph.add_edge(0, 1, 2)
        self.negative_graph.add_edge(0, 2, 3)
        self.negative_graph.add_edge(1, 3, -4)
        self.negative_graph.add_edge(2, 3, 1)
        self.negative_graph.add_edge(2, 4, 5)
        self.negative_graph.add_edge(3, 4, 6)

        self.negative_cycle_graph = Graph(3, directed=True)
        self.negative_cycle_graph.add_edge(0, 1, 1)
        self.negative_cycle_graph.add_edge(1, 2, -2)
        self.negative_cycle_graph.add_edge(2, 0, -3)

        self.random_directed_graph = create_random_graph(10, 0.5, (1, 10), directed=True)

        self.random_undirected_graph = create_random_graph(10, 0.5, (1, 10), directed=False)

    def test_bfs(self):
        self.assertEqual(self.directed_graph.bfs(0), [0, 1, 2, 3, 4])
        self.assertEqual(self.undirected_graph.bfs(0), [0, 1, 2, 3, 4])

    def test_dfs(self):
        self.assertEqual(self.directed_graph.dfs(0), [0, 2, 4, 3, 1])
        self.assertEqual(self.undirected_graph.dfs(0), [0, 2, 4, 3, 1])

    def test_dijkstra(self):
        self.assertEqual(self.directed_graph.dijkstra(0), {0: 0, 1: 2, 2: 3, 3: 4, 4: 8})
        self.assertEqual(self.undirected_graph.dijkstra(0), {0: 0, 1: 2, 2: 3, 3: 4, 4: 8})

    def test_bellman_ford(self):

        self.assertEqual(self.directed_graph.bellman_ford(0), {0: 0, 1: 2, 2: 3, 3: 4, 4: 8})
        self.assertEqual(self.directed_graph.bellman_ford(4),
                         {0: float('inf'), 1: float('inf'), 2: float('inf'), 3: float('inf'), 4: 0})

        self.assertEqual(self.undirected_graph.bellman_ford(0), {0: 0, 1: 2, 2: 3, 3: 4, 4: 8})
        self.assertEqual(self.undirected_graph.bellman_ford(4),
                         {0: 8, 1: 10, 2: 5, 3: 6, 4: 0})

    def test_create_random_graph(self):
        n_vertices = 5
        edge_prob = 0.5
        weight_range = (1, 10)
        directed = True
        graph = create_random_graph(n_vertices, edge_prob, weight_range, directed)
        self.assertEqual(graph.vertices, n_vertices)
        for node, neighbors in graph.graph.items():
            self.assertIsInstance(neighbors, list)
            for neighbor in neighbors:
                self.assertIsInstance(neighbor[0], int)
                self.assertIsInstance(neighbor[1], int)
                self.assertGreaterEqual(neighbor[1], weight_range[0])
                self.assertLessEqual(neighbor[1], weight_range[1])


if __name__ == '__main__':
    unittest.main()
