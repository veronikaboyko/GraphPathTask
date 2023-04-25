from memory_profiler import memory_usage
from graph import Graph


if __name__ == '__main__':

    g = Graph(directed=False)
    for i in range(200):
        g.add_edge(i, i + 1, 1)

    pairs = [(1, 50), (10, 40), (20, 30), (25, 35), (15, 45)]

    for start, goal in pairs:
        print(f"\nStart: {start}, Goal: {goal}\n")

        # BFS
        memory_bfs = memory_usage((g.bfs, (start, goal)))
        print(f"BFS memory usage: {max(memory_bfs) - min(memory_bfs)} MB")

        # DFS
        memory_dfs = memory_usage((g.dfs, (start, goal)))
        print(f"DFS memory usage: {max(memory_dfs) - min(memory_dfs)} MB")

        # Dijkstra
        memory_dijkstra = memory_usage((g.dijkstra, (start, goal)))
        print(f"Dijkstra memory usage: {max(memory_dijkstra) - min(memory_dijkstra)} MB")

        # A-Star
        memory_astar = memory_usage((g.astar, ((0, 0), (20, 20))))
        print(f"A* memory usage: {max(memory_astar) - min(memory_astar)} MB")
