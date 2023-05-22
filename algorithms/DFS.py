class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.frames = []

    def find_path(self, start, end=9):
        visited = set()
        stack = [(start, [start])]

        while stack:
            vertex, path = stack.pop()

            if vertex == end:
                self.frames.append({'path': list(path), 'title': 'DFS: Finished'})
                return path

            if vertex not in visited:
                visited.add(vertex)
                self.frames.append({'path': list(path), 'title': f'DFS: Visiting {vertex}'})

                for neighbor, weight in self.graph.get_neighbors(vertex):
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        stack.append((neighbor, new_path))
        self.frames.append({'path': [], 'title': f'DFS: Path to {end} not found'})
        return []
