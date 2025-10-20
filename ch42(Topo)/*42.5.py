seconds = [10, 20, 30]
imports = [
  [],
  [],
  [0, 1]
]

def compile_time(seconds, graph):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:   
                dfs(nbr)
        order.append(node)  # add after visiting all neighbors

    for node in range(len(graph)):
        if node not in visited:
            dfs(node)

    order = order # why ont we reverse?
    print(order)
    dist = [0]*len(graph)

    for node in order:
        nbrs = graph[node]
        if not nbrs:
            dist[node] = seconds[node]
        else:
            dist[node] = seconds[node]+max([dist[n] for n in nbrs])
    return max(dist)

# ans = distance(imports, seconds)
# print(ans)

def run_tests():
  tests = [
      # Example from the book
      ([10, 20, 30], [[], [], [0, 1]], 50),
      # Example from the book
      ([10, 20, 30], [[], [], []], 30),
      # Single package
      ([10], [[]], 10),
      # Linear dependency
      ([10, 20, 30], [[1], [2], []], 60),
      # Complex dependencies
      ([5, 10, 15, 20], [[], [0], [1], [0, 2]], 50),
  ]

  for seconds, imports, want in tests:
    got = compile_time(seconds, imports)
    print("Got: ", got)
    assert got == want, f"\ncompile_time({seconds}, {imports}): got: {
        got}, want: {want}\n"

run_tests()