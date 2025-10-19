""" Longest Cycle in a Graph
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a 0-indexed array edges of size n, where edges[i] is the node that node i points to. If there is no outgoing edge from node i, then edges[i] == -1.
Return the length of the longest cycle in the graph. If no cycle exists, return -1.
A cycle is a path that starts and ends at the same node.
"""
edges = [3,3,4,2,3]
Output= 3
# Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
# The length of this cycle is 3, so 3 is returned.
# edges = [2,-1,3,1]
# Output = -1

""" Notes / Hints
Each node has at most one outgoing edge, so every connected component is either:
a directed chain that ends at -1, or
a directed cycle possibly with trees (inbound chains) feeding into cycle nodes.
You can detect cycles by doing a traversal from each unvisited node, tracking visit time / depth or using coloring (0=unvisited, 1=visiting, 2=visited).
When you find a back-edge to a node in the current traversal (visiting state), compute cycle length by using the recorded depth/time of that node.
"""
 

def longest_cycle(edges):
    def dfs(node, pos):
        visited.add(node)
        current[node] = pos
        nbr = edges[node]
        if nbr == -1:
            return -1
        if nbr in current.keys():
            return pos-current[nbr]+1
        if nbr not in visited.keys():
            return dfs(nbr, pos+1)
        return -1
    
    visited = set()
    mx = -1
    for i in range(len(edges)):
        if i not in visited:
            current = {}
            mx = max(mx, dfs(i, 1))
    return mx

ans = longest_cycle(edges)
print(ans)