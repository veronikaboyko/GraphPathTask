from graph_animation import GraphAnimation
from algorithms import algorithm_dict
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
    parser.add_argument('--end', type=int, default=9, help='Finish vertex')
    parser.add_argument('--mandatory_vertices', nargs='+', type=int, help='List of mandatory vertices')
    return parser.parse_args()


def video_mode(g, args):
    graph_anim = GraphAnimation(g, args.algorithm)
    graph_anim.draw_graph()
    graph_anim.animate(args.start, args.end, args.mandatory_vertices)


def default_mode(g, args):
    algorithm_name = args.algorithm.lower()
    if algorithm_name in algorithm_dict:
        algorithm = algorithm_dict[algorithm_name](g)
        print(algorithm.find_path(args.start, args.end, args.mandatory_vertices))
    else:
        raise ValueError('Algorithm not supported')


def main():
    args = read_input()
    modes = {
        'video': video_mode,
        'default': default_mode,
    }

    mode_name = args.mode.lower()
    if mode_name in modes:
        mode = modes[mode_name]
        directed = args.directed.lower() == 'true'
        g = create_random_graph(args.vertices, args.edge_prob, (1, 10), directed)
        mode(g, args)
    else:
        raise ValueError('Mode not supported')


if __name__ == '__main__':
    main()
