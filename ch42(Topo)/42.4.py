from heapq import heappop, heappush
import math

def path_count(graph, start):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:   
                dfs(nbr)
        order.append(node)  # add after visiting all neighbors

    dfs(start)
    order = order[::-1] 

    dist = [0]*len(graph)
    dist[start] = 1

    for node in order:
        for nbr in graph[node]:
            new_count = + dist[node]
            dist[nbr] += new_count
    return dist

graph = [
  [1],        # Neighbors of node 0
  [],         # Neighbors of node 1
  [1],        # Neighbors of node 2
  [4],        # Neighbors of node 3
  [1, 2, 5],  # Neighbors of node 4
  [2]         # Neighbors of node 5
]
start = 4

# ans = path_count(graph, start)
# print(ans)
    

def run_tests():
  tests = [
      # Example from the book
      ([[1], [], [1], [4], [1, 2, 5], [2]], 4, [0, 3, 2, 0, 1, 1]),
      # Edge case: Single node graph
      ([[]], 0, [1]),
      ([[1], []], 0, [1, 1]),
      ([[1], [2], []], 1, [0, 1, 1]),
      ([[1, 2], [3], [3], []], 0, [1, 1, 1, 2]),
  ]

  for graph, start, want in tests:
    got = path_count(graph, start)
    assert got == want, f"\npath_count({graph}, {start}): got: {
        got}, want: {want}\n"

run_tests()
