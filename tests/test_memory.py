import tracemalloc
from graph import create_random_graph
from algorithms import BFS, DFS, Dijkstra, BellmanFord


class TestGraphMemory:
    def __init__(self, d):
        self.data = [d]

    def test_bfs(self):
        print('BFS memory')
        for d in self.data:
            for graph in d:
                tracemalloc.start()
                a = BFS(graph)
                a.find_path(0, 99)
                mem = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                print(f'{mem / 10 ** 6:.5}')
        print()

    def test_dfs(self):
        print('DFS memory')
        for d in self.data:
            for graph in d:
                tracemalloc.start()
                a = DFS(graph)
                a.find_path(0, 99)
                mem = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                print(f'{mem / 10 ** 6:.5}')
        print()

    def test_dijkstra(self):
        print('dijkstra memory')
        for d in self.data:
            for graph in d:
                tracemalloc.start()
                a = Dijkstra(graph)
                a.find_path(0, 99)
                mem = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                print(f'{mem / 10 ** 6:.5}')
        print()

    def test_bellman_ford(self):
        print('bellman_ford memory')
        for d in self.data:
            for graph in d:
                tracemalloc.start()
                a = BellmanFord(graph)
                a.find_path(0, 99)
                mem = tracemalloc.get_traced_memory()[1]
                tracemalloc.stop()
                print(f'{mem / 10 ** 6:.5}')


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

    test = TestGraphMemory(data)
    test.test_bfs()
    test.test_dfs()
    test.test_dijkstra()
    test.test_bellman_ford()
