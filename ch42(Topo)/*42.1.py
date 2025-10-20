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

    dist = [float("inf")]*len(graph)
    dist[start] = 0

    for node in order:
        for nbr, weight in graph[node]:
            new_weight = dist[node]+weight
            if new_weight<dist[nbr]:
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

# ans = distance(graph, start)
# print(ans)

def run_tests():
  tests = [
    # Example from the book
    ([[[1, 10]], 
      [], 
      [[1, 10]], 
      [[4, 12]], 
      [[1, 11], 
       [2, 21], 
       [5, 14]], 
       [[2, -30]]], 
       4, 
       [math.inf, -6, -16, math.inf, 0, 14]),
    # Edge case: Single node graph
    ([[]], 0, [0]),
    # Edge case: Disconnected graph
    ([[[1, 5]], [], [[3, 2]], []], 0, [0, 5, math.inf, math.inf]),
    # Edge case: Graph with negative weights
    ([[[1, -1]], [[2, -2]], []], 0, [0, -1, -3]),
    # Edge case: Start node with no outgoing edges
    ([[[1, 2]], [[2, 3]], []], 2, [math.inf, math.inf, 0]),
  ]

  for graph, start, want in tests:
    got = distance(graph, start)
    assert got == want, f"\ndistance({graph}, {start}): got: {got}, want: {want}\n"

run_tests()