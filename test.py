import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 0)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 3)

        self.graph_dijkstra = Graph(directed=False)
        self.graph_dijkstra.add_edge(0, 1, 2)
        self.graph_dijkstra.add_edge(0, 3, 2)
        self.graph_dijkstra.add_edge(1, 2, 3)
        self.graph_dijkstra.add_edge(1, 4, 5)
        self.graph_dijkstra.add_edge(2, 5, 4)
        self.graph_dijkstra.add_edge(3, 4, 2)
        self.graph_dijkstra.add_edge(4, 5, 4)

        self.graph_negative = Graph()
        self.graph_negative.add_edge(0, 1, 1)
        self.graph_negative.add_edge(1, 2, -2)
        self.graph_negative.add_edge(2, 3, 2)
        self.graph_negative.add_edge(3, 4, -4)
        self.graph_negative.add_edge(2, 4, -5)
        self.graph_negative.add_edge(1, 3, -6)

        self.graph_negative_cycle = Graph()
        self.graph_negative_cycle.add_edge(0, 1, 1)
        self.graph_negative_cycle.add_edge(1, 2, 1)
        self.graph_negative_cycle.add_edge(2, 3, -2)
        self.graph_negative_cycle.add_edge(3, 4, -4)
        self.graph_negative_cycle.add_edge(4, 2, -5)

    def test_bfs(self):
        self.assertEqual(self.graph.bfs(2), [2, 0, 3, 1])
        self.assertEqual(self.graph.bfs(1), [1, 2, 0, 3])

    def test_dfs(self):
        self.assertEqual(self.graph.dfs(1), [1, 2, 3, 0])
        self.assertEqual(self.graph.dfs(2), [2, 3, 0, 1])

    def test_dijkstra(self):
        self.assertEqual(self.graph_dijkstra.dijkstra(0, 6), {0: 0, 1: 2, 2: 5, 3: 2, 4: 4, 5: 8})
        self.assertEqual(self.graph_dijkstra.dijkstra(5, 6), {0: 8, 1: 7, 2: 4, 3: 6, 4: 4, 5: 0})

    def test_bellman_ford(self):
        self.assertEqual(self.graph_dijkstra.bellman_ford(0, 6), {0: 0, 1: 2, 2: 5, 3: 2, 4: 4, 5: 8})
        self.assertEqual(self.graph_negative.bellman_ford(0, 5), {0: 0, 1: 1, 2: -1, 3: -5, 4: -9})
        self.assertEqual(self.graph_negative.bellman_ford(2, 5), {0: float('inf'), 1: float('inf'), 2: 0, 3: 2, 4: -5})


if __name__ == '__main__':
    unittest.main()
