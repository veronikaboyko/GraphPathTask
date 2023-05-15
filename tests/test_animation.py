import unittest
from graph import Graph
from graph_animation import GraphAnimation


class TestGraphAnimation(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(10, directed=False)
        self.graph.add_edge(0, 1, 2)
        self.graph.add_edge(0, 2, 3)
        self.graph.add_edge(1, 3, 4)
        self.graph.add_edge(1, 4, 1)
        self.graph.add_edge(2, 5, 2)
        self.graph.add_edge(2, 6, 3)
        self.graph.add_edge(3, 7, 2)
        self.graph.add_edge(4, 7, 1)
        self.graph.add_edge(5, 8, 4)
        self.graph.add_edge(6, 8, 2)
        self.graph.add_edge(7, 9, 3)

    def test_graph_animation_bfs(self):
        animation = GraphAnimation(self.graph, 'bfs')
        self.assertEqual(animation.algorithm, 'bfs')
        self.assertEqual(animation.graph, self.graph)
        self.assertEqual(animation.nx_graph.number_of_nodes(), self.graph.vertices)
        self.assertEqual(animation.nx_graph.number_of_edges(), len(self.graph.get_edges()))

    def test_graph_animation_dfs(self):
        animation = GraphAnimation(self.graph, 'dfs')
        self.assertEqual(animation.algorithm, 'dfs')
        self.assertEqual(animation.graph, self.graph)
        self.assertEqual(animation.nx_graph.number_of_nodes(), self.graph.vertices)
        self.assertEqual(animation.nx_graph.number_of_edges(), len(self.graph.get_edges()))

    def test_graph_animation_dijkstra(self):
        animation = GraphAnimation(self.graph, 'dijkstra')
        self.assertEqual(animation.algorithm, 'dijkstra')
        self.assertEqual(animation.graph, self.graph)
        self.assertEqual(animation.nx_graph.number_of_nodes(), self.graph.vertices)
        self.assertEqual(animation.nx_graph.number_of_edges(), len(self.graph.get_edges()))

    def test_graph_animation_bellman_ford(self):
        animation = GraphAnimation(self.graph, 'bellman_ford')
        self.assertEqual(animation.algorithm, 'bellman_ford')
        self.assertEqual(animation.graph, self.graph)
        self.assertEqual(animation.nx_graph.number_of_nodes(), self.graph.vertices)
        self.assertEqual(animation.nx_graph.number_of_edges(), len(self.graph.get_edges()))


if __name__ == '__main__':
    unittest.main()
