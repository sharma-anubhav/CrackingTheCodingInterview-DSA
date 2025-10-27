# This is just dfs
def topo_sort_dfs(graph):
    visited = set()
    order = []
    def dfs(node):
        visited.add(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:   
                dfs(nbr)
        order.append(node)  # add after visiting all neighbors

    for node in graph:
        if node not in visited:  
            dfs(node)

    return order[::-1]  # reverse postorder

    # USUALLY WE ITERATE ON THIS ORDER AND UPDATE DISTANCES OR GET PARENT MAP OR DO BOTH CHECK QUESTIOn

def kahns(graph, start):
    pq = []
    indeg = [0]*len(graph)

    for i in range(len(graph)):
        for nbr, weight in graph[i]:
            indeg[nbr]+=1


    start = None    
    for i in range(len(graph)):
        if indeg[i]==0:
            start = i
    
    topo = []
    heappush(pq, start)
    while pq:
        ele = heappop(pq)
        topo.append(ele)
        for nbr,_ in graph[ele]:
            indeg[nbr]-=1
            if indeg[nbr] == 0:
                heappush(pq, nbr)
    if len(topo)!= len(graph):
        return -1
    return topo


