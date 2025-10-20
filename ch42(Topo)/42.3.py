from heapq import heappop, heappush
import math

def distance(graph, start):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for nbr, _ in graph[node]:
            if nbr not in visited:   
                dfs(nbr)
        order.append(node)  # add after visiting all neighbors

    dfs(start)

    order = order[::-1]
    dist = [-float("inf")]*len(graph)
    dist[start] = 0

    for node in order:
        for nbr, weight in graph[node]:
            new_weight = dist[node]+weight
            if new_weight>dist[nbr]:
                dist[nbr] = new_weight
    return dist
    

graph = [
  [[1, 10]],                    # Neighbors of node 0
  [],                           # Neighbors of node 1
  [[1, 10]],                    # Neighbors of node 2
  [[4, 12]],                    # Neighbors of node 3
  [[1, 11], [2, 21], [5, 14]],  # Neighbors of node 4
  [[2, -30]]                    # Neighbors of node 5
]
start = 4

ans = distance(graph, start)
print(ans)

