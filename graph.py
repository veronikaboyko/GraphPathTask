from collections import defaultdict, deque
import heapq
import random


class Graph:
    def __init__(self, vertices, directed=False):
        self.graph = defaultdict(list)
        self.vertices = vertices
        self.directed = directed
        self.weights = {}

    def add_edge(self, u, v, w=0):
        self.graph[u].append((v, w))
        self.weights[(u, v)] = w

        if not self.directed:
            self.graph[v].append((u, w))

    def get_neighbors(self, v):
        return self.graph[v]

    def _bfs(self, start):
        visited = set()
        queue = deque([(start, [start])])
        result = []
        frames = []

        while queue:
            vertex, path = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                frames.append({'path': list(path), 'title': f'BFS: Visiting {vertex}'})

                for neighbor, weight in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append((neighbor, new_path))
        frames.append({'path': [], 'title': f'BFS: Finished'})
        return result, frames

    def bfs(self, start):
        return self._bfs(start)[0]

    def bfs_frame(self, start):
        return self._bfs(start)[1]

    def _dfs(self, start):
        visited = set()
        stack = [(start, [start])]
        result = []
        frames = []

        while stack:
            vertex, path = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                frames.append({'path': list(path), 'title': f'DFS: Visiting {vertex}'})

                for neighbor, weight in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        stack.append((neighbor, new_path))
        frames.append({'path': [], 'title': f'DFS: Finished'})
        return result, frames

    def dfs(self, start):
        return self._dfs(start)[0]

    def dfs_frame(self, start):
        return self._dfs(start)[1]

    def _dijkstra(self, start):
        distances = {v: float('inf') for v in range(self.vertices)}
        distances[start] = 0
        heap = [(0, start)]
        visited = []
        frames = [{'path': [start], 'title': f'Dijkstra: Visiting {start}'}]

        while heap:
            (cost, vertex) = heapq.heappop(heap)

            if vertex not in visited:
                visited.append(vertex)
                frames.append({'path': list(visited), 'title': f'Dijkstra: Updating distance to {vertex}'})

                for neighbor, w in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_cost = cost + w
                        if new_cost < distances[neighbor]:
                            distances[neighbor] = new_cost
                            heapq.heappush(heap, (new_cost, neighbor))

        frames.append({'path': [], 'title': f'Dijkstra: Finished\n{distances}'})
        return distances, frames

    def dijkstra(self, start):
        return self._dijkstra(start)[0]

    def dijkstra_frame(self, start):
        return self._dijkstra(start)[1]

    def _bellman_ford(self, start):
        distances = {node: float('inf') for node in range(self.vertices)}
        distances[start] = 0
        pq = [(0, start)]
        visited_order = []
        frames = [{'path': [start], 'title': f'Bellman-Ford: Visiting {start}'}]

        while pq:
            (dist, u) = heapq.heappop(pq)
            visited_order.append(u)

            if dist > distances[u]:
                continue
            for v, w in self.graph[u]:
                alt = dist + w
                if alt < distances[v]:
                    distances[v] = alt
                    heapq.heappush(pq, (alt, v))
                    frames.append(
                        {'path': list(visited_order + [v]), 'title': f'Bellman-Ford: Updating distance to {v}'})

        for u in self.graph:
            for v, w in self.graph[u]:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    raise ValueError('Graph contains negative-weight cycle')

        frames.append({'path': [], 'title': f'Bellman-Ford: Finished\n{distances}'})
        return distances, frames

    def bellman_ford(self, start):
        return self._bellman_ford(start)[0]

    def bellman_ford_frame(self, start):
        return self._bellman_ford(start)[1]


def create_random_graph(n_vertices, edge_prob, weight_range, directed):
    graph = Graph(n_vertices, directed)
    for i in range(n_vertices):
        for j in range(i + 1, n_vertices):
            if random.random() < edge_prob:
                weight = random.randint(*weight_range)
                graph.add_edge(i, j, weight)

    return graph
