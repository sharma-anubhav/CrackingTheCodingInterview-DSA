"""
Problem: Shortest Path in a Binary Matrix
You are given an n x n binary matrix grid. Return the length of the shortest clear path in the matrix. 
If there is no such path, return -1.

A clear path in a binary matrix is a path from the top-left cell (0, 0) to the bottom-right cell (n - 1, n - 1) such that:
All the visited cells of the path have a value of 0.
All adjacent cells of the path are 8-directionally connected (i.e., they share an edge or a corner).
"""

from collections import deque


grid = [[0,0,0],
        [1,1,0],
        [1,1,0]]
# Output: 4

def is_valid(grid, loc):
    cur_r, cur_c = loc
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]!=1:
        return True
    return False

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def shortest_path(grid):
    s, e = (0,0), (len(grid)-1, len(grid[0])-1)
    visited = set()
    q = deque()
    visited.add(s)
    q.append((s, 0))
    while q:
        node, dis = q.popleft()
        if node == e:
            return dis+1
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                visited.add(nbr)
                q.append((nbr, dis+1))
    return -1

def shortest_path(grid):
    s,  = (0,0)
    visited = set()
    dist = {s:0}
    q = deque()

    visited.add(s)
    q.append((s, 0))
    while q:
        node, dis = q.popleft()
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                visited.add(nbr)
                dist[nbr] = dis+1
                q.append((nbr, dis+1))
    return -1


ans = shortest_path(grid)
print(ans)