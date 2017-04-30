from __future__ import print_function
from Graph import Graph
from astar import astar
from dfs import dfs
from bfs import bfs
from bestfs import bestfs

if __name__ == '__main__':
    graph = Graph.default_graph()
    start_node = 's'
    end_node = 't'
    path, cost = astar(graph, start_node, end_node)
    if cost == -1:
        print('No path found between ', start_node, ' and ', end_node)
    else:
        print('Path: ', path)
        print('Cost: ', cost)
