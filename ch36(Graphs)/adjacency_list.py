from collections import defaultdict


graph = [
    [1],
    [0, 2, 5, 4],
    [1, 4, 5],
    [],
    [5, 2, 1],
    [1, 2, 4]
]

def num_nodes(graph):
    return len(graph)

def num_edges(graph):
    sum = 0
    for n in graph:
        sum+=len(n)
    return sum//2

def degree(graph, node):
    return len(graph[node])

def neighbours(graph, node):
    return graph[node]

V, edge_list = 6, [[0,1], [1,2], [4,5], [2,4], [1,5]]
#This is not useful, we need a adjacency list

def build_adj_from_edge(edge_list, V):
    graph = [[] for _ in range(len(V))]
    for s, t in edge_list:
        graph[s].append(t)
        graph[t].append(t) # skip for directed graphs.
    return graph

# if graph is not named with 0-V
graph = defaultdict(list)