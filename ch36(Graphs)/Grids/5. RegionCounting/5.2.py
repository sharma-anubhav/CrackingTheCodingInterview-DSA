"""
Max Area of Island
You are given an m x n binary matrix grid.
An island is a group of 1s (representing land) connected 4-directionally (up, down, left, right).
The area of an island is the total number of 1s connected together.
Return the maximum area of an island in the grid.
If there is no island, return 0.
"""

from collections import defaultdict


grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
#output = 6

def is_valid(grid, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(grid), len(grid[0])

    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]!=0:
        return True
    return False

def get_nbr(node):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def max_area(grid):
    def dfs(node, id):
        nonlocal visited
        visited.add(node)
        island2count[id]+=1
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                dfs(nbr, id)

    island2count = defaultdict(int)
    visited = set()
    island_id = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            node = (r,c)
            if node not in visited and grid[node[0]][node[1]]==1:
                dfs(node, island_id)
                island_id+=1
    return max(island2count.values())

ans = max_area(grid)
print(ans)

