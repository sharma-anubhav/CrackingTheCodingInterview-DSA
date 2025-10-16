"""
Rotting Oranges
You are given an m x n grid where each cell can have one of three values:
0 → empty cell
1 → fresh orange
2 → rotten orange
Every minute, any fresh orange that is 4-directionally adjacent (up, down, left, right) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If it is impossible to rot all oranges, return -1.
"""
from collections import deque


# grid = [
#   [2,1,1],
#   [1,1,0],
#   [0,1,1]
# ]
# output = 4

grid = [
  [2,1,1],
  [0,1,1],
  [1,0,1]
]
output = -1

def is_valid(graph, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(graph), len(graph[0])
    if 0<=cur_r<r and 0<=cur_c<c and graph[cur_r][cur_c]!=2 and graph[cur_r][cur_c]!=0:
        return True
    return False

def get_nbr(node):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    cur_r, cur_c = node[0], node[1]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def find_rotten(grid):
    rotten_tomatoes = []
    fresh_count=0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                rotten_tomatoes.append((r,c))
            if grid[r][c] == 1:
                fresh_count += 1
    return rotten_tomatoes, fresh_count

def rotten(grid):
    rotten_tomatoes, fresh_count = find_rotten(grid)

    q = deque()
    visited = set()

    for tomato in rotten_tomatoes:
        q.append((tomato, 0))
        visited.add(tomato)
    last_time = -1
    infected_count = 0
    while q:
        loc, t = q.popleft()
        for nbr in get_nbr(loc):
            if is_valid(grid, nbr) and nbr not in visited:
                visited.add(nbr)
                infected_count+=1
                q.append((nbr, t+1))
                last_time = t+1
    if infected_count < fresh_count:
        last_time = -1
    return last_time

ans = rotten(grid)
print(ans)




