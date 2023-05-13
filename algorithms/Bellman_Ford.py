import heapq
from path_recovery import reconstruct_path


class BellmanFord:
    def __init__(self, g):
        self.g = g
        self.frames = []

    def find_path(self, start, end=9):
        distances = {node: float('inf') for node in range(self.g.vertices)}
        distances[start] = 0
        previous = {node: None for node in range(self.g.vertices)}
        pq = [(0, start)]

        while pq:
            (dist, u) = heapq.heappop(pq)

            if dist > distances[u]:
                continue

            for v, w in self.g.graph[u]:
                alt = dist + w
                if alt < distances[v]:
                    distances[v] = alt
                    previous[v] = u
                    heapq.heappush(pq, (alt, v))
                    self.frames.append(
                        {'path': list([v]), 'title': f'Bellman-Ford: Updating distance to {v}'})

        for u in self.g.graph:
            for v, w in self.g.graph[u]:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    raise ValueError('Graph contains negative-weight cycle')

        if end is not None:
            path = reconstruct_path(previous, start, end)
            self.frames.append(
                {'path': list(path),
                 'title': f'Bellman-Ford: The shortest path from {start} to {end} is {distances[end]}'})
            return path

        self.frames.append({'path': [], 'title': f'Bellman-Ford: Path to {end} not found'})
        return []
