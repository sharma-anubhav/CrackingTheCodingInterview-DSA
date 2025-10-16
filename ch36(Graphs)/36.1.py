def validate(graph):
    V = len(graph)
    edges = set()
    for node, nbrs in enumerate(graph):
        for nbr in nbrs:
            if nbr < 0 or nbr >= V:
                return False
            if nbr == node:
                return False
            if (node, nbr) in edges:
                return False
            # if node not in graph[nbr]:
            #     return False
            if (nbr, node) in edges:
                edges.remove((nbr, node))
            else:
                edges.add((node, nbr))
    if len(edges) == 0:
        return True
    return False

def run_tests():
  tests = [
      # Valid cases
      [[[1], [0]], True],  # Simple valid graph
      [[[1, 2], [0, 2], [0, 1]], True],  # Triangle graph
      [[], True],  # Empty graph
      [[[]], True],  # Single isolated node

      # Invalid node index cases
      [[[2], [0]], False],  # Node index too large
      [[[-1], []], False],  # Negative node index

      # Self-loop cases
      [[[0], []], False],  # Self loop
      [[[1], [1]], False],  # Self loop in second node

      # Parallel edge cases
      [[[1, 1], [0, 0]], False],  # Same edge twice from first node
      [[[1], [0, 2, 0], [1]], False],  # Same edge twice from second node

      # Unmatched edge cases
      [[[1], []], False],  # Edge only in one direction
      [[[1, 2], [0], []], False],  # Some edges missing their pairs
      [[[1], [2], [0]], False],  # Cycle with unmatched edges
  ]
  for graph, want in tests:
    got = validate(graph)
    print(got)
    assert got == want, f"\nvalidate({graph}): got: {got}, want: {want}\n"

run_tests()
    