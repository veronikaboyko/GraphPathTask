import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from algorithms import Algorithm, algorithm_dict


class GraphAnimation:
    def __init__(self, graph, algorithm):
        self.graph = graph
        self.algorithm = algorithm
        self.edges = graph.get_edges()
        self.weights = graph.get_weights()

        self.nx_graph = nx.Graph()
        self.nx_graph.add_nodes_from(range(graph.vertices))
        self.nx_graph.add_edges_from(self.edges)

        self.pos = nx.spring_layout(self.nx_graph)

        self.fig, self.ax = plt.subplots()

    def draw_graph(self):
        nx.draw(self.nx_graph, self.pos, with_labels=True, node_color='lightblue')

    def draw_path(self, path):

        nx.draw_networkx_nodes(self.nx_graph, self.pos, nodelist=path, node_color='blue')
        nx.draw_networkx_edges(self.nx_graph, self.pos, edgelist=list(zip(path, path[1:])),
                               edge_color='blue',
                               width=2)
        if self.algorithm == Algorithm.DIJKSTRA.value or self.algorithm == Algorithm.BELLMAN_FORD.value:
            nx.draw_networkx_edge_labels(self.nx_graph, self.pos, edge_labels=self.weights,
                                         font_color='black')

    def update(self, frame):
        self.ax.clear()
        self.draw_graph()
        self.draw_path(frame['path'])
        self.ax.set_title(frame['title'])

    def animate(self, start, end, mandatory_vertices):
        if self.algorithm in algorithm_dict:
            alg = algorithm_dict[self.algorithm](self.graph)
        else:
            raise ValueError('Algorithm not supported')

        path = alg.find_path(start, end, mandatory_vertices)
        frames = alg.frames

        ani = animation.FuncAnimation(self.fig, self.update, frames=frames, interval=1000, repeat=False)
        plt.show()
