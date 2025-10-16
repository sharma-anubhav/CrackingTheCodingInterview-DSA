"""
You are given an m x n grid filled with non-negative integers.
Your task is to find a path from the top-left corner (0, 0) to the bottom-right corner (m - 1, n - 1) 
that minimizes the sum of all numbers along its path.
You may only move right or down at any step.
"""

from collections import defaultdict
from heapq import heappush, heappop


def is_valid(grid, loc):
    cur_r, cur_c = loc
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c:
        return True
    return False

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]

def min_sum(grid):
    s, e = (0,0), (len(grid)-1, len(grid[0])-1)
    distance = {s:grid[s[0]][s[1]]}
    visited = set() ## <<<<<<------------ NEVER INIT IN DIJKSTRA IT WILL FAIL IN START
    pq = []
    heappush(pq, (grid[s[0]][s[1]], s))

    while pq:
        cost, node = heappop(pq)
        if node in visited:
            continue
        if node == e:
            return cost
        for nbr in get_nbr(node):
            if is_valid(grid, nbr):
                new_cost = cost+grid[nbr[0]][nbr[1]]
                if new_cost < distance.get(nbr, float("inf")):
                    distance[nbr] = new_cost
                    heappush(pq, (new_cost, nbr))
    print(distance)
    return -1

ans = min_sum(grid)
print(ans)