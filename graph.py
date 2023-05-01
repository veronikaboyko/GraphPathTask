from collections import defaultdict, deque
import heapq
import random


class Graph:
    def __init__(self, directed=True):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, w=0):
        self.graph[u].append((v, w))

        if not self.directed:
            self.graph[v].append((u, w))

    def get_neighbors(self, v):
        return self.graph[v]

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor, weight in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        stack = [(start, [start])]
        result = []

        while stack:
            vertex, path = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)

                for neighbor, weight in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        stack.append((neighbor, new_path))

        return result

    def dijkstra(self, start, vertices):
        distances = {v: float('inf') for v in range(vertices)}
        distances[start] = 0
        heap = [(0, start)]
        visited = set()

        while heap:
            (cost, vertex) = heapq.heappop(heap)

            if vertex not in visited:
                visited.add(vertex)

                for neighbor, w in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_cost = cost + w
                        if new_cost < distances[neighbor]:
                            distances[neighbor] = new_cost
                            heapq.heappush(heap, (new_cost, neighbor))

        return distances

    def bellman_ford(self, start, vertices):
        distances = {node: float('inf') for node in range(vertices)}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            (dist, u) = heapq.heappop(pq)
            if dist > distances[u]:
                continue
            for v, w in self.graph[u]:
                alt = dist + w
                if alt < distances[v]:
                    distances[v] = alt
                    heapq.heappush(pq, (alt, v))

        for u in self.graph:
            for v, w in self.graph[u]:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    raise ValueError('Graph contains negative-weight cycle')

        return distances


def create_random_graph(n_vertices, edge_prob, weight_range, directed):
    graph = Graph(directed)
    for i in range(n_vertices):
        for j in range(i + 1, n_vertices):
            if random.random() < edge_prob:
                weight = random.randint(*weight_range)
                graph.add_edge(i, j, weight)

    return graph
