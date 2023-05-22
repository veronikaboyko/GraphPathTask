from collections import deque


class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.frames = []

    def find_path(self, start, end=9):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            vertex, path = queue.popleft()

            if vertex == end:
                self.frames.append({'path': list(path), 'title': 'BFS: Finished'})
                return path

            if vertex not in visited:
                visited.add(vertex)
                self.frames.append({'path': list(path), 'title': f'BFS: Visiting {vertex}'})

                for neighbor, weight in self.graph.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append((neighbor, new_path))

        self.frames.append({'path': [], 'title': f'BFS: Path to {end} not found'})
        return []
