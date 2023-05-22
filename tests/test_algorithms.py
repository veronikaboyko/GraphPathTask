import unittest
from graph import Graph
from algorithms import Algorithm, algorithm_dict
from parameterized import parameterized


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

    @parameterized.expand([
        (Algorithm.BFS.value, [0, 1, 3, 7, 9]),
        (Algorithm.DFS.value, [0, 1, 4, 7, 9]),
        (Algorithm.DIJKSTRA.value, [0, 1, 4, 7, 9]),
        (Algorithm.BELLMAN_FORD.value, [0, 1, 4, 7, 9])
    ])
    def test_directed_graph(self, algorithm, expected_path):
        if algorithm in algorithm_dict:
            alg = algorithm_dict[algorithm](self.directed_graph)
        else:
            raise ValueError('Algorithm not supported')

        path = alg.find_path(0, 9)
        self.assertEqual(path, expected_path)

    @parameterized.expand([
        (Algorithm.BFS.value, [0, 1, 3, 7, 9]),
        (Algorithm.DFS.value, [0, 1, 4, 7, 9]),
        (Algorithm.DIJKSTRA.value, [0, 1, 4, 7, 9]),
        (Algorithm.BELLMAN_FORD.value, [0, 1, 4, 7, 9])
    ])
    def test_undirected_graph(self, algorithm, expected_path):
        if algorithm in algorithm_dict:
            alg = algorithm_dict[algorithm](self.undirected_graph)
        else:
            raise ValueError('Algorithm not supported')

        path = alg.find_path(0, 9)
        self.assertEqual(path, expected_path)

    @parameterized.expand([
        (Algorithm.BELLMAN_FORD.value, [0, 1, 3, 4])
    ])
    def test_negative_graph(self, algorithm, expected_path):
        if algorithm in algorithm_dict:
            alg = algorithm_dict[algorithm](self.negative_graph)
        else:
            raise ValueError('Algorithm not supported')

        path = alg.find_path(0, 4)
        self.assertEqual(path, expected_path)


if __name__ == '__main__':
    unittest.main()
