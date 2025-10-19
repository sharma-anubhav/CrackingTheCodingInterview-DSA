"""All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: 
graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).
"""

graph = [[1,2],[3],[3],[]]
Output = [[0,1,3],[0,2,3]]


def find_paths(graph):
    n = len(graph)
    start = 0
    target = n-1

    paths = []
    def dfs(node, cur_path):
        cur_path.append(node)
        if node == target:
            paths.append(cur_path.copy())
            cur_path.pop()
            return
        for nbr in graph[node]:
            dfs(nbr, cur_path)
        cur_path.pop()
        return
    cur_path = []
    dfs(start, cur_path)
    return paths

ans = find_paths(graph)
print(ans)


