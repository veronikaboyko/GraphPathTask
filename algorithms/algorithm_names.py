from enum import Enum
from algorithms import BFS, DFS, BellmanFord, Dijkstra


class Algorithm(Enum):
    BFS = 'bfs'
    DFS = 'dfs'
    DIJKSTRA = 'dijkstra'
    BELLMAN_FORD = 'bellman_ford'


algorithm_dict = {
    Algorithm.DIJKSTRA.value: Dijkstra,
    Algorithm.BELLMAN_FORD.value: BellmanFord,
    Algorithm.BFS.value: BFS,
    Algorithm.DFS.value: DFS,
}
