import heapq
from path_recovery import reconstruct_path


class Dijkstra:
    def __init__(self, g):
        self.g = g
        self.frames = []

    def find_path(self, start, end=9):
        distances = {v: float('inf') for v in range(self.g.vertices)}
        distances[start] = 0
        previous = {v: None for v in range(self.g.vertices)}
        heap = [(0, start)]
        visited = []

        while heap:
            (cost, vertex) = heapq.heappop(heap)

            if vertex == end:
                path = reconstruct_path(previous, start, end)
                self.frames.append(
                    {'path': list(path),
                     'title': f'Dijkstra: The shortest path from {start} to {end} is {distances[end]}'})
                return path

            if vertex not in visited:
                visited.append(vertex)

                for neighbor, w in self.g.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_cost = cost + w
                        if new_cost < distances[neighbor]:
                            distances[neighbor] = new_cost
                            previous[neighbor] = vertex
                            heapq.heappush(heap, (new_cost, neighbor))
                            self.frames.append({'path': list(reconstruct_path(previous, start, neighbor)),
                                                'title': f'Dijkstra: Updating distance to {neighbor}'})

        self.frames.append({'path': [], 'title': f'Dijkstra: Path to {end} not found'})
        return []
