from graph_animation import GraphAnimation
from graph import create_random_graph
import argparse


def read_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, help='Default or video')
    parser.add_argument('algorithm', type=str, help='bfs, dfs, dijkstra or bellman_ford')
    parser.add_argument('--vertices', type=int, default=10, help='Number of vertices in a graph')
    parser.add_argument('--edge_prob', type=float, default=0.2, help='Edge creation probability')
    parser.add_argument('--directed', type=str, default='False', help='Directed graph or not')
    parser.add_argument('--start', type=int, default=0, help='Starting vertex')
    return parser.parse_args()


def video_mode(g, args):
    graph_anim = GraphAnimation(g, args.algorithm)
    graph_anim.draw_graph()
    graph_anim.animate(0)


def default_mode(g, args):
    if args.algorithm == 'dijkstra':
        print(g.dijkstra(0))
    elif args.algorithm == 'bellman_ford':
        print(g.bellman_ford(0))
    elif args.algorithm == 'bfs':
        print(g.bfs(0))
    elif args.algorithm == 'dfs':
        print(g.dfs(0))


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
    main()
