from pdb import run

"""
Naive Solution. DFS FROM EVERY NODE
"""
def strongly_connected(graph):
    def dfs(graph, node):
        nonlocal visited
        for nbr in graph[node]:
            if not nbr in visited:
                visited.add(nbr)
                dfs(graph, nbr)
    
    V = len(graph)
    for i in range(V):
        visited = {i}
        dfs(graph, i)
        if len(visited)!= V:
            return False
    return True

"""
OPTIMIZED:
Do dfs from node 0. if it can reach everyone. 
Reverse graph and do bfs again. if again then strongly connected
"""

def run_tests():
  tests = [
      # Example strongly connected
      [[[1], [2], [0]], True],
      # Example not strongly connected
      [[[1], [2], []], False],
      # Single node
      [[[]], True],
      # Two nodes, strongly connected
      [[[1], [0]], True],
      # Two nodes, not strongly connected
      [[[1], []], False],
      # Cycle of 4 nodes
      [[[1], [2], [3], [0]], True],
      # Almost cycle of 4 nodes, missing one edge
      [[[1], [2], [3], []], False],
      # Complete graph
      [[[1, 2], [0, 2], [0, 1]], True],
  ]
  for graph, want in tests:
    got = strongly_connected(graph)
    assert got == want, f"\nstrongly_connected({graph}): got: {
        got}, want: {want}\n"

run_tests()


        