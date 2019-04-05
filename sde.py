#!/usr/bin/python

def adjacent_nodes(graph, node):
    adjacents = []

    for edge in graph:
        if edge[0] == node:
            adjacents.append(edge[1])
        elif edge[1] == node:
            adjacents.append(edge[0])
        else:
            pass

    return adjacents

# Recieves a graph with a matrix representation, where the
# nodes are from 1 to N.
#
def dfs(graph, nodes_count):
    stack = []
    visited = [False] * nodes_count

    if len(graph) == 0: return 0

    stack.append(1)
    while len(stack) > 0:
        current = stack.pop()
        visited[current-1] = True
        can_go_to = adjacent_nodes(graph, current)
        for node in can_go_to:
            if node not in visited:
                visited[node-1] = True

    return sum(visited)

def sum_costs(graph):
    total = 0

    for edge in graph:
        if len(edge) > 2:
            total += edge[2]

    return total

def newEdges(graph, nodes_count, possible_new_roads, op):
    components = nodes_count - dfs(graph, nodes_count)

    if components > 1 and len(possible_new_roads) > 0:
        possible_road = possible_new_roads.pop()
        p_1_optimal = newEdges(graph, nodes_count, list(possible_new_roads), op)

        new_possible_graph = graph + [possible_road]
        p_2_optimal = newEdges(new_possible_graph, nodes_count, possible_new_roads, op)

        optimal = op(p_1_optimal, p_2_optimal)
        return optimal

    if components == 1:
        return sum_costs(graph)
    else:
        return 9999


print(
    newEdges([[1,4],[2,3],[1,5]], 6, [[1,6,5],[4,3,10],[1,2,2],[4,5,5]], min)
)
