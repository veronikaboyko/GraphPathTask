from collections import defaultdict
import heapq


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

    def bfs(self, start, goal):
        queue = [(start, [start])]
        visited = set()

        while queue:
            vertex, path = queue.pop(0)

            if vertex == goal:
                return path

            if vertex not in visited:
                visited.add(vertex)

                for neighbor, _ in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))

    def dfs(self, start, goal):
        stack = [(start, [start])]
        visited = set()

        while stack:
            vertex, path = stack.pop()

            if vertex == goal:
                return path

            if vertex not in visited:
                visited.add(vertex)

                for neighbor, _ in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))

    def dijkstra(self, start, goal):
        heap = [(0, start, [])]
        visited = set()

        while heap:
            (cost, vertex, path) = heapq.heappop(heap)

            if vertex not in visited:
                visited.add(vertex)
                path = path + [vertex]

                if vertex == goal:
                    return path

                for neighbor, w in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        heapq.heappush(heap, (cost + w, neighbor, path))

    def astar(self, start, goal):

        heap = [(0, start, [])]
        visited = set()

        while heap:
            (cost, vertex, path) = heapq.heappop(heap)

            if vertex not in visited:
                visited.add(vertex)
                path = path + [vertex]

                if vertex == goal:
                    return path

                for neighbor, w in self.get_neighbors(vertex):
                    if neighbor not in visited:
                        heuristic = self.get_heuristic(neighbor, goal)
                        heapq.heappush(heap, (cost + w + heuristic, neighbor, path))

    def get_heuristic(self, v, goal):
        return abs(v[0] - goal[0]) + abs(v[1] - goal[1])
