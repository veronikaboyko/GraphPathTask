import timeit
from graph import Graph


if __name__ == '__main__':
    graph = Graph()
    for i in range(1, 51):
        for j in range(i + 1, 51):
            graph.add_edge(i, j)

    pairs = [(1, 50), (10, 40), (20, 30), (25, 35), (15, 45)]

    for start, goal in pairs:
        print(f"\nStart: {start}, Goal: {goal}\n")

        # BFS
        bfs_time = timeit.timeit(lambda: graph.bfs(start, goal), number=100)
        print(f"BFS time: {bfs_time}")

        # DFS
        dfs_time = timeit.timeit(lambda: graph.dfs(start, goal), number=100)
        print(f"DFS time: {dfs_time}")

        # Dijkstra
        dijkstra_time = timeit.timeit(lambda: graph.dijkstra(start, goal), number=100)
        print(f"Dijkstra time: {dijkstra_time}")

        # A-Star
        astar_time = timeit.timeit(lambda: graph.astar((0, 0), (20, 20)), number=100)
        print(f"A-Star time: {astar_time}")
