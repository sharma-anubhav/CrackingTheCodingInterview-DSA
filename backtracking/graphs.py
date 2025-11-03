
"""
CHECK ALL POSSIBLE PATHS FORM START TO END
"""
def wrapper(graph, n1, n2):
    visited = set()
    paths = []

    def dfs(node, path):
        if node == n2:
            paths.append(path)
            return

        visited.add(node)
        for nbr in graph.get(node, []):
            if nbr not in visited:
                dfs(nbr, path + nbr)
        visited.remove(node)  #<<<--------- backtrack

    dfs(n1, n1)