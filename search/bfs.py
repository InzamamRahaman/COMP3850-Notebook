from __future__ import print_function
from Queue import Queue
from Stack import Stack

def get_path(parents, end_node):
    path = [end_node]
    current_node = end_node
    while current_node in parents:
        current_node = parents[current_node]
        path.append(current_node)
    return list(reversed(path))


def bfs(graph, start_node, end_node, print_sets=True):
    open = Queue()
    closed = Stack()
    parents = {}
    open.enqueue(start_node)
    while not open.is_empty():
        current_node = open.dequeue()
        if print_sets:
            print('Open: ', open)
            print('Closed: ', closed)
        if current_node == end_node:
            return get_path(parents, current_node)
        children = graph.get_children(current_node)
        closed.push(current_node)
        for child in children:
            if child not in open and child not in closed:
                open.enqueue(child)
                parents[child] = current_node
    return []


