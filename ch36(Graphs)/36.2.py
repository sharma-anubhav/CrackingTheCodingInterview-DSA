# without dict normal recursion
def path(graph, n1, n2):
    visited = set()
    path = []
    def dfs(node, target):
        nonlocal path
        visited.add(node)
        if node == target:
            path.append(node)
            return True
        for nbr in graph[node]:
            if nbr not in visited:
                if dfs(nbr, target):
                    path.append(node)
                    return True
        return False
    dfs(n1, n2)
    return path[::-1]

# with parent map
def get_parent_dict(graph, n1):
    parent_dict = {}
    def dfs(node, parent):
        nonlocal parent_dict
        parent_dict[node] = parent
        for nbr in graph[node]:
            if nbr not in parent_dict:
                dfs(nbr, node)
    dfs(n1, None)
    return parent_dict

def path(graph, n1, n2):
    d = get_parent_dict(graph, n1)
    cur = n2
    path = []
    if n2 not in d:
        return []
    while cur and cur != n1:
        path.append(cur)
        cur = d[cur]
    if cur == n1:
        print("Found")
        path.append(n1)
        return path[::-1]
    return []


def run_tests():
  tests = [
      # Example 1 from book - graph from Figure 8
      [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, 4, [0, 1, 4]],
      # Example 2 from book - graph from Figure 8, no path exists
      [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, 3, []],
      # Simple line graph
      [[[1], [0, 2], [1]], 0, 2, [0, 1, 2]],
      # Cycle graph
      [[[1, 3], [0, 2], [1, 3], [0, 2]], 0, 2, [0, 1, 2]],
      # Disconnected graph
      [[[1], [0], [3], [2]], 0, 2, []],
      # Complete graph
      [[[1, 2], [0, 2], [0, 1]], 0, 2, [0, 2]]
  ]
  for graph, node1, node2, want in tests:
    got = path(graph, node1, node2)
    print(got)
    # For this problem, there can be multiple valid paths
    # So we need to verify:
    # 1. If want is empty, got should be empty
    # 2. If want is not empty:
    #    - got should start with node1 and end with node2
    #    - got should be a valid path in the graph
    #    - got should not have duplicates
    if not want:
      assert not got, f"\npath({graph}, {node1}, {node2}): got: {
          got}, want empty path\n"
      continue

    assert got[0] == node1 and got[-1] == node2, \
        f"\npath({graph}, {node1}, {node2}): path {
        got} should start with {node1} and end with {node2}\n"

    # Verify path is valid
    for i in range(len(got) - 1):
      assert got[i + 1] in graph[got[i]], \
          f"\npath({graph}, {node1}, {node2}): invalid path {
          got} - no edge between {got[i]} and {got[i + 1]}\n"

    # Verify no duplicates
    assert len(got) == len(set(got)), \
        f"\npath({graph}, {node1}, {node2}): path {got} contains duplicates\n"

run_tests()