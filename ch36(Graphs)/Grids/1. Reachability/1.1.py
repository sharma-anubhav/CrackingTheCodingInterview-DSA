"""
Connectivity Problem. We cna use DFS/BFS but prefer DFS. 
DFS goes to each and every node! (not all paths remember)
Hence it can give a path if there exists. but not optimal
"""

"""
🧩 Problem Statement
You are given a square grid of size n × n, where each cell contains one of the following values:
    0 → Wall (cannot move through)
    1 → Source (starting point)
    2 → Destination (ending point)
    3 → Blank cell (can move through)
You can move up, down, left, or right from a cell — but cannot move diagonally or through walls.
Your task is to determine whether there exists a path from the source to the destination.

Return:
    1 if a path exists
    0 if no path exists
"""
# grid = [
#     [3,0,3,0,0],
#     [3,0,0,0,3],
#     [3,3,3,3,3],
#     [0,2,3,0,0],
#     [3,0,0,1,3]
# ]
grid = [
  [0, 3, 1, 0],
  [3, 0, 3, 3],
  [3, 3, 0, 3],
  [0, 2, 3, 0]
]

def find_s_d(grid):
    s, d = None, None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                s = (r,c)
            elif grid[r][c] == 2:
                d = (r, c)
    return s, d

def is_valid(loc, grid):
    cur_r, cur_c = loc
    r,c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]!=0:
        return True
    return False

def get_nbr(grid, node):
    directions  = [(1,0), (0,1), (-1, 0), (0,-1)]
    cur_r, cur_c = node
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def find_path(grid):
    s, d = find_s_d(grid)
    visited = set()
    def dfs(node, destination):
        nonlocal visited
        visited.add(node)
        if s == destination:
            return True
        for nbr in get_nbr(grid, node):
            if is_valid(nbr, grid) and not nbr in visited:
                if dfs(nbr, destination):
                    return True
    return dfs(s, d)

ans = find_path(grid)
print(ans)











