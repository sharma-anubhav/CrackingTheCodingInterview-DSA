def is_tree(graph):
    V = len(graph)
    visited  = set()
    def dfs(node, parent):
        visited.add(node)
        for nbr in graph[node]:
            if nbr in visited and nbr != parent:
                return False
            if nbr not in visited:
                if not dfs(nbr, node):
                    return False
        return True
    # cnt = 0
    # for i in range(V):
    #     if i not in visited:
    #         cnt+=1
    #         if not dfs(i, None):  ----> we dont need to calculate number of connected components. do dfs from 1 node and check len(visited)
    #             return False
    # if cnt>1:
    #     return False
    check = dfs(0, None)
    if len(visited)==V and check:
        return True
    return False

def run_tests():
  tests = [
      # Example tree
      [[[1, 2], [0, 3, 4], [0], [1], [1]], True],
      # Example not a tree - has a cycle
      [[[1], [2], [3], [1]], False],
      # Single node
      [[[]], True],
      # Two nodes connected
      [[[1], [0]], True],
      # Two nodes disconnected
      [[[], []], False],
      # Line graph
      [[[1], [0, 2], [1, 3], [2]], True],
      # Cycle
      [[[1, 3], [2, 0], [3, 1], [0, 2]], False],
      # Complete graph K4 (not a tree)
      [[[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], False],
      # Star graph
      [[[1, 2, 3, 4], [0], [0], [0], [0]], True],
  ]
  for graph, want in tests:
    got = is_tree(graph)
    print(got)
    assert got == want, f"\nis_tree({graph}): got: {got}, want: {want}\n"

run_tests()