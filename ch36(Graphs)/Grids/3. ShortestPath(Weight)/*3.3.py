"""
You are given an n x n integer matrix grid, where each value grid[i][j] represents the elevation at point (i, j).
starts raining, and the water level rises over time.
At time t, the water level is equal to t, meaning any cell with elevation ≤ t is submerged (reachable).

You can swim from one square to another 4-directionally adjacent square (up, down, left, right) 
if and only if the elevation of both squares is at most t.

You can swim any distance in zero time (i.e., the only limiting factor is water level).
You must remain inside the grid during your swim.

Your goal is to determine the minimum time t required such that you can reach the bottom-right cell (n - 1, n - 1) 
starting from the top-left cell (0, 0).
"""

from heapq import heappop, heappush


grid = [[0, 2],
        [1, 3]]
# Output: 3

# grid = [[0,   1,  2,  3,  4],
#         [24, 23, 22, 21,  5],
#         [12, 13, 14, 15, 16],
#         [11, 17, 18, 19, 20],
#         [10,  9,  8,  7,  6]]
# Output: 16

def is_valid(graph, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(graph), len(graph[0])
    if 0<=cur_r<r and 0<=cur_c<c:
        return True
    return False

def get_nbr(node):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    cur_r, cur_c = node[0], node[1]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def swim(grid):
    s, e = (0,0), (len(grid)-1, len(grid[0])-1)
    visited = set()
    time = {s:0}
    pq = []
    heappush(pq, (0,s))

    while pq:
        t, node = heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        time[node] = t
        if node == e:
            return t
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                new_time = max(t, grid[nbr[0]][nbr[1]])
                heappush(pq, (new_time, nbr))
    return -1

ans = swim(grid)
print(ans)
        

