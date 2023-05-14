import timeit
from graph import create_random_graph
from algorithms import BFS, DFS, Dijkstra, BellmanFord


class TestGraphTime:
    def __init__(self, d):
        self.data = [d]

    def test_bfs(self):
        print('BFS time')
        for d in self.data:
            for graph in d:
                a = BFS(graph)
                print(f'{timeit.timeit(lambda: a.find_path(0, 99), number=100):.5}')
        print()

    def test_dfs(self):
        print('DFS time')
        for d in self.data:
            for graph in d:
                a = DFS(graph)
                print(f'{timeit.timeit(lambda: a.find_path(0, 99), number=100):.5}')
        print()

    def test_dijkstra(self):
        print('dijkstra time')
        for d in self.data:
            for graph in d:
                a = Dijkstra(graph)
                print(f'{timeit.timeit(lambda: a.find_path(0, 99), number=100):.5}')
        print()

    def test_bellman_ford(self):
        print('bellman_ford time')
        for d in self.data:
            for graph in d:
                a = BellmanFord(graph)
                print(f'{timeit.timeit(lambda: a.find_path(0, 99), number=100):.5}')


if __name__ == '__main__':
    best_data_100 = create_random_graph(100, 0, (1, 10), True)
    best_data_500 = create_random_graph(500, 0, (1, 10), True)
    best_data_1000 = create_random_graph(1000, 0, (1, 10), True)
    worst_data_100 = create_random_graph(100, 1, (1, 10), True)
    worst_data_500 = create_random_graph(500, 1, (1, 10), True)
    worst_data_1000 = create_random_graph(1000, 1, (1, 10), True)
    rnd_data_100 = create_random_graph(100, 0.2, (1, 10), True)
    rnd_data_500 = create_random_graph(500, 0.2, (1, 10), True)
    rnd_data_1000 = create_random_graph(1000, 0.2, (1, 10), True)

    data = [best_data_100, best_data_500, best_data_1000, worst_data_100,
            worst_data_500, worst_data_1000, rnd_data_100, rnd_data_500,
            rnd_data_1000]

    test = TestGraphTime(data)
    test.test_bfs()
    test.test_dfs()
    test.test_dijkstra()
    test.test_bellman_ford()
