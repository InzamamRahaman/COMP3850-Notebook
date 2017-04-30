from __future__ import print_function
from Stack import Stack



def get_path(parents, end_node):
    path = [end_node]
    current_node = end_node
    while current_node in parents:
        current_node = parents[current_node]
        path.append(current_node)
    return list(reversed(path))


def dfs(graph, start_node, end_node, print_sets=True, depth_limit=-1):
    open = Stack()
    closed = Stack()
    open.push(start_node)
    parents = {}
    depth = {start_node:0}
    while not open.is_empty():
        if print_sets:
            print('Open: ', open)
            print('Closed: ', closed)
        current_node = open.pop()
        if current_node == end_node:
            return get_path(parents, current_node)
        if depth_limit == -1 or (depth_limit > -1 and depth[current_node] <= depth_limit):
            children = graph.get_children(current_node)
            closed.push(current_node)
            for child in children:
                if child not in open and child not in closed:
                    open.push(child)
                    parents[child] = current_node
                    depth[child] = depth[current_node] + 1
    return []

