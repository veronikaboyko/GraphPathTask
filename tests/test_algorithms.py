import unittest
from graph import Graph
from algorithms import BFS, DFS, Dijkstra, BellmanFord


class TestGraph(unittest.TestCase):

    def setUp(self):

        self.directed_graph = Graph(10, directed=True)
        self.directed_graph.add_edge(0, 1, 2)
        self.directed_graph.add_edge(0, 2, 3)
        self.directed_graph.add_edge(1, 3, 4)
        self.directed_graph.add_edge(1, 4, 1)
        self.directed_graph.add_edge(2, 5, 2)
        self.directed_graph.add_edge(2, 6, 3)
        self.directed_graph.add_edge(3, 7, 2)
        self.directed_graph.add_edge(4, 7, 1)
        self.directed_graph.add_edge(5, 8, 4)
        self.directed_graph.add_edge(6, 8, 2)
        self.directed_graph.add_edge(7, 9, 3)

        self.undirected_graph = Graph(10, directed=False)
        self.undirected_graph.add_edge(0, 1, 2)
        self.undirected_graph.add_edge(0, 2, 3)
        self.undirected_graph.add_edge(1, 3, 4)
        self.undirected_graph.add_edge(1, 4, 1)
        self.undirected_graph.add_edge(2, 5, 2)
        self.undirected_graph.add_edge(2, 6, 3)
        self.undirected_graph.add_edge(3, 7, 2)
        self.undirected_graph.add_edge(4, 7, 1)
        self.undirected_graph.add_edge(5, 8, 4)
        self.undirected_graph.add_edge(6, 8, 2)
        self.undirected_graph.add_edge(7, 9, 3)

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

    def test_bfs(self):
        alg = BFS(self.directed_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 3, 7, 9])
        alg = BFS(self.undirected_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 3, 7, 9])

    def test_dfs(self):
        alg = DFS(self.directed_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 4, 7, 9])
        alg = DFS(self.undirected_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 4, 7, 9])

    def test_dijkstra(self):
        alg = Dijkstra(self.directed_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 4, 7, 9])
        alg = Dijkstra(self.undirected_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 4, 7, 9])

    def test_bellman_ford(self):
        alg = BellmanFord(self.directed_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 4, 7, 9])
        alg = BellmanFord(self.undirected_graph)
        self.assertEqual(alg.find_path(0, 9), [0, 1, 4, 7, 9])
        alg = BellmanFord(self.negative_graph)
        self.assertEqual(alg.find_path(0, 4), [0, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()
