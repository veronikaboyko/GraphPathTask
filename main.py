from graph_animation import GraphAnimation
from graph import create_random_graph, Graph
import argparse
from algorithms import BFS, DFS, Dijkstra, BellmanFord


def read_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, help='Default or video')
    parser.add_argument('algorithm', type=str, help='bfs, dfs, dijkstra or bellman_ford')
    parser.add_argument('--vertices', type=int, default=10, help='Number of vertices in a graph')
    parser.add_argument('--edge_prob', type=float, default=0.2, help='Edge creation probability')
    parser.add_argument('--directed', type=str, default='False', help='Directed graph or not')
    parser.add_argument('--start', type=int, default=0, help='Starting vertex')
    parser.add_argument('--end', type=int, default=9, help='Finish vertex')
    return parser.parse_args()


def video_mode(g, args):
    graph_anim = GraphAnimation(g, args.algorithm)
    graph_anim.draw_graph()
    graph_anim.animate(args.start, args.end)


def default_mode(g, args):
    if args.algorithm == 'dijkstra':
        a = Dijkstra(g)
    elif args.algorithm == 'bellman_ford':
        a = BellmanFord(g)
    elif args.algorithm == 'bfs':
        a = BFS(g)
    elif args.algorithm == 'dfs':
        a = DFS(g)
    else:
        raise ValueError('Algorithm not supported')
    print(a.find_path(args.start, args.end))


def main():
    args = read_input()
    directed = args.directed.lower() == 'true'

    g = create_random_graph(args.vertices, args.edge_prob, (1, 10), directed)
    if args.mode == 'video':
        video_mode(g, args)
    elif args.mode == 'default':
        default_mode(g, args)
    else:
        raise ValueError('Mode not supported')


if __name__ == '__main__':
    negative_cycle_graph = Graph(3, directed=True)
    negative_cycle_graph.add_edge(0, 1, 1)
    negative_cycle_graph.add_edge(1, 2, -2)
    negative_cycle_graph.add_edge(2, 0, -3)
    alg = BellmanFord(negative_cycle_graph)
    print(alg.find_path(0, 2))

    main()
