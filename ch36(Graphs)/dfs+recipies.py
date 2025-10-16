"""
RECIPE of ALL THE DFS's:
1. map/set outside
2. dfs(graph, node)
3. - visited.add(node) OR map[node] = id/parent
4. - loop on nbrs and do dfs if not in visited/map

Using this we can do dfs/get parentmap/get connected components/ get node2cc map
"""
def wrapper(graph, start):
    visited = set()
    def dfs(graph, start):
        visited.add(start)
        for nbr in graph[start]:
            if not nbr in visited:
                dfs(graph, nbr)
    dfs(graph, start)

def get_parent_map(graph, start):
    """
    Potential usage: Finding path (although it can be done directly with DFS), cycle detection
    """
    parent_map = {}
    def dfs(graph, node, parent):
        parent_map[node] = parent
        for nbr in graph[node]:
            if not nbr in parent_map.keys():
                dfs(graph, nbr, node)
    dfs(graph, start, None)

# SEARCH USING DFS RECIPIE:
def wrapper(graph, n1, n2):
    visited = set()
    cur_path = []
    def dfs(n1):
        visited.add(n1)
        if n1 == n2:
            cur_path.append(n1)
            return True
        for nbr in graph[n1]:
            if not nbr in visited:
                if dfs(nbr):
                    cur_path.append(nbr)
                    return True
    if dfs(n1):
        return cur_path[::-1]  
    return []


#RECIPEI 2: COnnected components shared visited
def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr, component)

    for node in range(len(graph)):
        if node not in visited:
            component = set()
            dfs(node, component)
            components.append(component)

    return components

## RECIPIE 3: node->ccid
# It is easy to get confused where to add node and where neughbours.
# remember we add node outside dfs hence we add node oursidew and nbr inside the dfs
def wrapper(graph):
    connected_component = 0
    visited = set()
    n2cc = {}

    def dfs(graph, node):
        visited.add(node) #<<<<----------------
        n2cc[node] = connected_component #<<<<----------------
        for nbr in graph[node]:
            if not nbr in visited:
                dfs(graph, nbr)
    
    for node in range(len(graph)):
        if not node in visited:
            dfs(graph, node)
            connected_component+=1
