graph = [
   [1, 3],       # Node 0
   [0, 2],       # Node 1
   [1, 3],       # Node 2
   [0, 2]        # Node 3
]
heights = [4.0, 1.0, 3.0, 2.0]

from collections import defaultdict


def max_hilliness(graph, heights):
    visited = {}
    cc2sum = defaultdict(int)
    cc2cnt = defaultdict(int)

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
    
    for node in range(len(graph)):
        cc_id = visited[node]
        for nbr in graph[node]:
            if node < nbr:
                cc2sum[cc_id]+=abs(heights[nbr]-heights[node])
                cc2cnt[cc_id]+=1
            
    mx = 0
    for id, sum in cc2sum.items():
        cnt = cc2cnt[id]
        cur = sum/cnt
        mx = max(mx, cur) 
    return mx


# NO NEED TO GET ACTIUAL COMPONENTS LIKE BELOW APPROACH
def get_compnent_avg(graph, heights, component):
    sum = 0
    cnt = 0
    visited_edges = set()
    for node in component:
        for nbr in graph[node]:
            edge  = (min(nbr, node), max(nbr, node))
            if edge not in visited_edges:
                visited_edges.add(edge)
                sum += abs(heights[node] - heights[nbr])
                cnt +=1
    if cnt == 0:
        return 0
    return sum/cnt

def max_hilliness(graph, heights):
    visited = set()
    components = []
    def dfs(graph, node, component):
        visited.add(node)
        component.add(node)
        for nbr in graph[node]:
            if not nbr in visited:
                dfs(graph, nbr, component)
    
    for i in range(len(graph)):
        if i not in visited:
            component = set()
            dfs(graph, i, component)
            components.append(component)
    
    mx = 0
    for component in components:
        avg = get_compnent_avg(graph, heights, component)
        mx = max(mx, avg)
    return mx

def run_tests():
  tests = [
      # Example
      [[[1, 3], [0, 2], [1, 3], [0, 2]], [4, 1, 3, 2], 2],
      # Single node component
      [[[]], [5], 0],
      # Two disconnected components
      [[[1], [0], [3], [2]], [1, 4, 2, 5], 3],
      # All nodes same height
      [[[1, 2], [0, 2], [0, 1]], [3, 3, 3], 0],
      # Line graph
      [[[1], [0, 2], [1]], [1, 5, 2], 3.5],
      # Complete graph
      [[[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
       [1, 4, 7, 10], (3 + 6 + 9 + 3 + 6 + 3) / 6]
  ]
  for graph, heights, want in tests:
    got = max_hilliness(graph, heights)
    print(got)
    assert abs(
        got - want) < 0.0001, f"\nmax_hilliness({graph}, {heights}): got: {got}, want: {want}\n"

run_tests()

    