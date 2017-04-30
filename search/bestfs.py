from __future__ import print_function
import sys
from collections import defaultdict
from PriorityQueue import PriorityQueue
from path_utils import *

def bestfs(graph, start_node, end_node, print_sets=True):
    open = PriorityQueue()
    open.push(start_node, 0)
    closed = []
    parents = defaultdict(lambda: None)
    costs = defaultdict(lambda: sys.maxsize)
    costs[start_node] = 0
    depth = -1
    while not open.is_empty():
        depth += 1
        if print_sets:
            print('Open: ', open)
            print('Closed: ', get_set_string(closed))
        current_node = open.pop()
        if current_node == end_node:
            return construct_path(end_node, parents, graph)
        children = graph.get_children(current_node)
        for child in children:
            temp_cost = graph.get_weight(current_node, child) + costs[current_node]
            if child not in open and child not in closed:
                open.push(child, graph.h(child))
                parents[child] = current_node
                costs[child] = temp_cost
            elif child in open:
                if temp_cost < costs[child]:
                    costs[child] = temp_cost
                    parents[child] = current_node
            elif child in closed:
                if temp_cost < costs[child]:
                    f_score = depth + graph.h(child)
                    closed.remove(child)
                    open.push(child, f_score)
        closed.append(current_node)
        open.reorder()
    return None, -1

