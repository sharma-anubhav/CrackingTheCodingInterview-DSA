from collections import deque


graph = [
   [1],           # Node 0
   [0, 2, 5, 4],  # Node 1
   [1, 4, 5],     # Node 2
   [],            # Node 3
   [5, 2, 1],     # Node 4
   [1, 2, 4]      # Node 5
]
start = 0
queries = [1, 0, 3, 4]
# Output: [[0, 1], [0], [], [0, 1, 4]]


def shortest_path_queries(graph, start, queries):
    parent_map = {start: None}
    q = deque()
    q.append(0)

    while q:
        ele = q.popleft()
        for nbr in graph[ele]:
            if not nbr in parent_map:
                parent_map[nbr] = ele
                q.append(nbr)
    print(parent_map)

    ans = []
    for query in queries:
        path = []
        if query not in parent_map:
            ans.append(path)
            continue

        cur = query
        while cur!=None:
            path.append(cur)
            cur = parent_map[cur]
        ans.append(path[::-1])
    return ans


def run_tests():
  tests = [
      # Example
      [[[1], [0, 2, 5, 4], [1, 4, 5], [], [5, 2, 1], [1, 2, 4]], 0, [1, 0, 3, 4],
       [[0, 1], [0], [], [0, 1, 4]]],
      # Simple line graph
      [[[1], [0, 2], [1]], 0, [1, 2],
          [[0, 1], [0, 1, 2]]],
      # Disconnected components
      [[[1], [0], [3], [2]], 0, [1, 2, 3],
          [[0, 1], [], []]],
      # Complete graph
      [[[1, 2], [0, 2], [0, 1]], 0, [1, 2],
          [[0, 1], [0, 2]]],
      # Single node
      [[[]], 0, [0],
          [[0]]],
      # Empty queries
      [[[1], [0]], 0, [],
          []]
  ]
  for graph, start, queries, want in tests:
    got = shortest_path_queries(graph, start, queries)
    print(got)
    assert got == want, f"\nshortest_path_queries({graph}, {start}, {queries}): got: {
        got}, want: {want}\n"

run_tests()