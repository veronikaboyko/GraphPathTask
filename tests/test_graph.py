import unittest
from graph import Graph, create_random_graph


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(5)

    def test_add_edge(self):
        self.graph.add_edge(0, 1, 5)
        self.assertEqual(self.graph.get_edges(), [(0, 1)])
        self.assertEqual(self.graph.get_weights(), {(0, 1): 5})

        self.graph.add_edge(1, 2, 3)
        self.assertEqual(self.graph.get_edges(), [(0, 1), (1, 2)])
        self.assertEqual(self.graph.get_weights(), {(0, 1): 5, (1, 2): 3})

        self.graph.add_edge(2, 3)
        self.assertEqual(self.graph.get_edges(), [(0, 1), (1, 2), (2, 3)])
        self.assertEqual(self.graph.get_weights(), {(0, 1): 5, (1, 2): 3, (2, 3): 0})

    def test_get_neighbors(self):
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)

        neighbors = self.graph.get_neighbors(0)
        self.assertEqual(neighbors, [(1, 0), (2, 0)])

        neighbors = self.graph.get_neighbors(1)
        self.assertEqual(neighbors, [(0, 0), (3, 0)])

        neighbors = self.graph.get_neighbors(2)
        self.assertEqual(neighbors, [(0, 0)])

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
