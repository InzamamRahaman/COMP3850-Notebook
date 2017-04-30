def get_set_string(s):
    s_temp = list(map(str, s))
    s_temp = reversed(s_temp)
    acc = '{' + ','.join(s_temp) + '}'
    return acc

def construct_path(end_node, parents, graph):
    path, acc = construct_path_helper(end_node, parents, graph)
    path.append(end_node)
    return path, acc

def construct_path_helper(end_node, parents, graph):
    parent = parents[end_node]
    if parent:
        acc_list, acc_cost = construct_path_helper(parent, parents, graph)
        acc_list.append(parent)
        acc_cost += graph.get_weight(parent, end_node)
        return acc_list, acc_cost
    return [], 0