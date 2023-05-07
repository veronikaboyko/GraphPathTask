import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from graph import Graph


class GraphAnimation:
    def __init__(self, graph: Graph, algorithm):
        self.graph = graph
        self.algorithm = algorithm
        self.edges = []
        self.weights = {}
        for i in range(graph.vertices):
            for j in graph.graph[i]:
                self.edges.append((i, j[0]))
                self.weights[(i, j[0])] = j[1]
        self.pos = nx.spring_layout(nx.Graph(self.edges))
        self.fig, self.ax = plt.subplots()

    def draw_graph(self):
        nx.draw(nx.Graph(self.edges), self.pos, with_labels=True, node_color='lightblue')

    def draw_path(self, path):
        try:
            nx.draw_networkx_nodes(nx.Graph(self.edges), self.pos, nodelist=path, node_color='blue')
            nx.draw_networkx_edges(nx.Graph(self.edges), self.pos, edgelist=list(zip(path, path[1:])),
                                   edge_color='blue',
                                   width=2)
            if self.algorithm == 'dijkstra' or self.algorithm == 'bellman_ford':
                nx.draw_networkx_edge_labels(nx.Graph(self.edges), self.pos, edge_labels=self.weights,
                                             font_color='black')
        except nx.NetworkXError as err:
            print(f'Error: {err}Try to create another graph.')

    def update(self, frame):
        if self.algorithm == 'dijkstra' or self.algorithm == 'bellman_ford':
            self.ax.clear()
        self.draw_graph()
        self.draw_path(frame['path'])
        self.ax.set_title(frame['title'])

    def animate(self, start):
        if self.algorithm == 'dijkstra':
            frames = self.graph.dijkstra_frame(start)
        elif self.algorithm == 'bellman_ford':
            frames = self.graph.bellman_ford_frame(start)
        elif self.algorithm == 'bfs':
            frames = self.graph.bfs_frame(start)
        elif self.algorithm == 'dfs':
            frames = self.graph.dfs_frame(start)
        else:
            raise ValueError('Algorithm not supported')

        ani = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=1000, repeat=False)
        plt.show()
