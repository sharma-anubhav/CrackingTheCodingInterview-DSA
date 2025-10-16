graph = [
  [1],
  [0, 2, 5],
  [1, 3, 4],
  [2],
  [2, 5],
  [1, 4]
]
# Output: [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5]]
"""
Plain DFS algo just add edges
"""
def spanning_tree_2(graph):
    visited = set()
    st = []
    def dfs(graph, node):
        nonlocal visited
        visited.add(node)
        for nbr in graph[node]:
            if not nbr in visited:
                st.append([node, nbr])
                dfs(graph, nbr)
    dfs(graph, 0)
    return st

def run_tests():
  tests = [
      # Example from the book
      [[1], [0, 2, 5], [1, 3, 4], [2], [2, 5], [1, 4]],
      # Single edge
      [[1], [0]],
      # Line graph
      [[1], [0, 2], [1]],
      # Star graph
      [[1, 2, 3], [0], [0], [0]],
      # Complete graph
      [[1, 2], [0, 2], [0, 1]],
      # Single node graph
      [[]]
  ]

  for graph in tests:
    got = spanning_tree_2(graph)
    print(got)
    # Since there can be multiple valid spanning trees,
    # we check that:
    # 1. We have V-1 edges
    # 2. Each edge connects valid nodes
    # 3. The edges form a tree (no cycles)
    V = len(graph)
    assert len(got) == V - 1, \
        f"\nspanning_tree({graph}): got wrong number of edges: {got}"

    # Check edges are valid
    for u, v in got:
      assert 0 <= u < V and 0 <= v < V, \
          f"\nspanning_tree({graph}): invalid node in edge {[u, v]}"
      assert v in graph[u] and u in graph[v], \
          f"\nspanning_tree({graph}): invalid edge {[u, v]}"

    # Check no cycles by counting reachable nodes
    adj = [[] for _ in range(V)]
    for u, v in got:
      adj[u].append(v)
      adj[v].append(u)

    visited = set()

    def dfs_check(node, parent):
      visited.add(node)
      for nbr in adj[node]:
        if nbr != parent:
          if nbr in visited:
            return False
          if not dfs_check(nbr, node):
            return False
      return True

    assert dfs_check(0, -1) and len(visited) == V, \
        f"\nspanning_tree({graph}): edges do not form a tree: {got}"
run_tests()