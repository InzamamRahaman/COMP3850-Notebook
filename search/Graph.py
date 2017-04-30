from collections import defaultdict


class Graph(object):

    def __init__(self, edgelist, f):
        self.children = defaultdict(list)
        self._f = f
        self.weight = defaultdict(dict)
        for u, v, w in edgelist:
            self.children[u].append(v)
            self.children[v].append(u)
            self.weight[u][v] = w
            self.weight[v][u] = w

    def get_children(self, u):
        return self.children[u]

    def get_weight(self, u, v):
        return self.weight[u][v]

    def h(self, node):
        return self._f(node)

    @staticmethod
    def default_graph():
        edgelist = [
            ('s', 'e', 2),
            ('e', 'f', 5),
            ('f', 'g', 2),
            ('g', 't', 2),
            ('t', 'd', 3),
            ('d', 'c', 3),
            ('c', 'b', 2),
            ('b', 'a', 2),
            ('a', 's', 2)
        ]

        h_dict = {
            's': 0,
            'e': 7,
            'f': 4,
            'g': 2,
            't': 0,
            'd': 3,
            'c': 4,
            'b': 4,
            'a': 5
        }

        def h(node):
            return h_dict[node]

        graph = Graph(edgelist, h)
        return graph


