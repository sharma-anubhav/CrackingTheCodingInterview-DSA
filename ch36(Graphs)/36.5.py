from operator import concat
from pydoc import visiblename
from threading import local


graph = [
  [1],           # Node 0
  [0, 2, 5, 4],  # Node 1
  [1, 4, 5],     # Node 2
  [],            # Node 3
  [5, 2, 1],     # Node 4
  [1, 2, 4]      # Node 5
]
queries = [[0, 4], [0, 3]]

"""
We dont need the actual compnents. We just need numbers
"""
def connected_component_queries(graph, queries):
    visited = {}

    def dfs(node, cc_id):
        visited[node] = cc_id
        for nbr in graph[node]:
            if nbr not in visited:
                dfs(nbr, cc_id)
    
    cc_id = 0
    for i in range(len(graph)):
        if i not in visited:
            cc_id+=1
            dfs(i, cc_id)
    
    res = []
    for node1, node2 in queries:
        res.append(visited[node1] == visited[node2])
    return res

"""
Loop over each node and create a connected compnent if not in visited.
Then check queries. Basically the recipeie 2 for all conected components. 
"""
def connected_component_queries(graph, queries):
    connected_components = []
    visited = set()
        
    def dfs(graph, node):
        nonlocal s
        for nbr in graph[node]:
            if not nbr in visited:
                visited.add(nbr)
                s.add(nbr)
                dfs(graph, nbr)

    for node in range(len(graph)):
        if node not in visited:
            visited.add(node)
            s = {node}
            dfs(graph, node)
            connected_components.append(s)
    
    ans = []
    for n1, n2 in queries:
        for comonent in connected_components:
            if n1 in comonent and n2 in comonent:
                ans.append(True)
                break
            if n1 in comonent and not n2 in comonent:
                ans.append(False)
                break
    return ans




def run_tests():
  tests = [
      # Cycle graph with 6 nodes
      [[[1, 5], [0, 2, 4], [1, 3, 5], [2, 4], [1, 3, 5], [0, 2, 4]],
       [(0, 4), (0, 3)],
          [True, True]],
      # Example
      [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]],
       [(0, 4), (0, 3)],
          [True, False]],
      # Simple line graph
      [[[1], [0, 2], [1]],
          [(0, 2), (0, 1)],
          [True, True]],
      # Disconnected components
      [[[1], [0], [3], [2]],
          [(0, 1), (0, 2), (2, 3)],
          [True, False, True]],
      # Complete graph
      [[[1, 2], [0, 2], [0, 1]],
          [(0, 1), (1, 2), (0, 2)],
          [True, True, True]],
      # Single node
      [[[]],
          [(0, 0)],
          [True]],
      # Empty queries
      [[[1], [0]],
          [],
          []]
  ]
  for graph, queries, want in tests:
    got = connected_component_queries(graph, queries)
    print(got)
    assert got == want, f"\nconnected_component_queries({graph}, {queries}): got: {
        got}, want: {want}\n"

run_tests()