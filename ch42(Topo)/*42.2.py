from heapq import heappop, heappush
import math

def distance(graph, start, goal):
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

    parents = {start:None}
    for node in order:
        for nbr, weight in graph[node]:
            new_weight = dist[node]+weight
            if new_weight<dist[nbr]:
                dist[nbr] = new_weight
                parents[nbr] = node
            
    print(graph)
    print(parents)
    cur = goal
    if goal not in order:
        return []
    path = []
    while cur != None:
        path.append(cur)
        cur = parents[cur]

    return path[::-1]
    

graph = [
  [[1, 10]],                    # Neighbors of node 0
  [],                           # Neighbors of node 1
  [[1, 10]],                    # Neighbors of node 2
  [[4, 12]],                    # Neighbors of node 3
  [[1, 11], [2, 21], [5, 14]],  # Neighbors of node 4
  [[2, -30]]                    # Neighbors of node 5
]
start = 4
goal = 1

ans = distance(graph, start, goal)
print(ans)

def run_tests():
  tests = [
      # Example from the book
      ([[[1, 10]], [], [[1, 10]], [[4, 12]], [
       [1, 11], [2, 21], [5, 14]], [[2, -30]]], 4, 1, [4, 5, 2, 1]),
      # Edge case: Single node graph
    #   ([[]], 0, 0, [0]),
      # Edge case: Disconnected graph
      ([[[1, 5]], [], [[3, 2]], []], 0, 3, []),
      # Edge case: Graph with negative weights
      ([[[1, -1]], [[2, -2]], []], 0, 2, [0, 1, 2]),
      # Edge case: Start node with no outgoing edges
      ([[[1, 2]], [[2, 3]], []], 2, 0, []),
  ]

  for graph, start, goal, want in tests:
    got = distance(graph, start, goal)
    assert got == want, f"\nshortest_path({graph}, {start}, {goal}): got: {got}, want: {want}\n"

run_tests()