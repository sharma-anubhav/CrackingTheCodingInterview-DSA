"""
Problem: Number of Islands

You are given an m x n 2D binary grid grid which represents a map of:
'1' = land
'0' = water
Return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically (no diagonals).
You may assume all four edges of the grid are surrounded by water.
"""

from curses import nonl


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# Output = 1

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# OUTPUT = 3

def is_valid(grid, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(grid), len(grid[0])

    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]!="0":
        return True
    return False

def get_nbr(node):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def count_islands(grid):
    def dfs(node):
        nonlocal visited
        visited.add(node)
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                dfs(nbr)

    island_count = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            node = (r,c)
            if node not in visited and grid[node[0]][node[1]]=="1":
                island_count+=1
                dfs(node)
    return island_count

ans = count_islands(grid)
print(ans)