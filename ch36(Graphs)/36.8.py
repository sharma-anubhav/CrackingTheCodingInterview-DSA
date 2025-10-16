V = 4
edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 0, 2]]

def create_graph(edges):
    graph = [[] for _ in range(V)]
    for node, nbr, gain in edges:
        graph[node].append((nbr, gain))
        graph[nbr].append((node, gain))
    return graph

def create_id_map(graph):
    m = {}
    cc_id = 0
    visited = set()
    
    def dfs(node, m):
        visited.add(node)
        m[node] = cc_id
        for nbr, _ in graph[node]:
            if not nbr in visited:
                dfs(nbr, m)

    for node in range(len(graph)):
        if not node in visited:
            dfs(node, m)
            cc_id+=1
    return m, cc_id

def elevation(edges, V):
    graph = create_graph(edges)
    n2cc, total_cc = create_id_map(graph)

    sums = [0]* total_cc
    cnts = [0]* total_cc

    for node in range(len(graph)):
        for nbr, gain in graph[node]:
            if nbr < node:
                sums[n2cc[node]]+=gain
                cnts[n2cc[node]]+=1
    
    mx = 0
    for i in range(len(sums)):
        cur_avg = sums[i]/cnts[i]
        mx = max(mx, cur_avg)
    return mx
