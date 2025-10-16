from collections import defaultdict, deque
import dis
from math import dist
from this import d


# graph = [
#     [1, 4],   # Node 0
#     [0, 2],   # Node 1
#     [1, 3],   # Node 2
#     [2, 4],   # Node 3
#     [0, 3]    # Node 4
# ]
# node1 = 0
# node2 = 2
# node3 = 4

# Output: 3

def bfs(graph, start, n1, n2, n3):
    q = deque()
    distance = {start: 0}
    q.append(start)
    while q:
        ele = q.popleft()            
        for nbr in graph[ele]:
            if not nbr in distance:
                distance[nbr] = distance[ele]+1
                q.append(nbr)
    return distance

# def walking_distance_to_coffee(graph, n1, n2, n3):
#     mn = float("inf")
#     for node in range(len(graph)):
#         print("Doing bfs for node: ", node)
#         cur_steps = bfs(graph, node, n1, n2, n3)
#         print("steps from node: ", node, " are: ", cur_steps)
#         mn = min(cur_steps, mn)
#     return mn

"""
Optimized way would be:
Doo BFS from each 3 friend. And add the distances from each to all other nodes. Minimunm one wins!!
"""

def walking_distance_to_coffee(graph, n1, n2, n3):
    mn = float("inf")
    ans = defaultdict(int)
    for node in [n1, n2, n3]:
        distances = bfs(graph, node, n1, n2, n3)
        for key in distances.keys():
            ans[key]+=distances[key]
    return min(ans.values())


def run_tests():
  tests = [
    # Example from the book
      ([
      [1, 14],        # 0: Outer ring connections
      [0, 2],         # 1
      [1, 3],         # 2
      [2, 4],         # 3
      [3, 5, 19],     # 4: Connector from outer to inner ring
      [4, 6],         # 5
      [5, 7],         # 6
      [6, 8],         # 7
      [7, 9, 21],     # 8: Connector from outer to inner ring
      [8, 10],        # 9
      [9, 11],        # 10
      [10, 12],       # 11
      [11, 13],       # 12
      [12, 14],       # 13
      [0, 13, 15],    # 14: Connector from outer to inner ring
      [14, 16],       # 15
      [15, 17],       # 16
      [16, 18, 20],   # 17: Center node connections
      [17, 19],       # 18
      [18, 4],        # 19
      [17, 21],       # 20
      [8, 20]         # 21
      ], 14, 4, 8, 9),
      # Cycle with 5 nodes
      ([[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]], 0, 2, 4, 3),
      # Simple line graph
      ([[1], [0, 2], [1]], 0, 1, 2, 2),
      # Star graph - optimal meeting point is center
      ([[1], [0, 2, 3, 4], [1], [1], [1]], 0, 2, 3, 3),
      # Complete graph - can meet at any node
      ([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], 0, 1, 2, 2),
      # Edge case - all start at same node
      ([[1], [0]], 0, 0, 0, 0),
      # Edge case - two start at same node
      ([[1], [0, 2], [1]], 0, 0, 2, 2),
  ]
  for graph, node1, node2, node3, want in tests:
    got = walking_distance_to_coffee(graph, node1, node2, node3)
    print(got)
    print("Wanted:", want)
    assert got == want, f"\nwalking_distance_to_coffee({graph}, {node1}, {node2}, {
        node3}): got: {got}, want: {want}\n"
run_tests()

