"""
Practice Problem: Walls and Gates
You are given an m x n grid (2D matrix) rooms where each cell can be one of:
-1 : A wall or an obstacle (cannot be traversed)
0 : A gate
INF : An empty room, represented by the integer 2147483647 (i.e. 2^31 - 1). You may assume that the distance to a gate is always less than INF.
Your task is to fill each empty room with the distance to its nearest gate. 
If it is impossible for the room to reach any gate, it should remain INF.

You must modify the rooms grid in place (i.e. do not return a new matrix).
You may move up, down, left, or right (4 directions).
"""

from collections import deque


rooms = [
  ["INF",  -1,   0,  "INF"],
  ["INF", "INF", "INF",  -1 ],
  ["INF",  -1, "INF",  -1 ],
  [  0,  -1, "INF", "INF"]
]

output = [
  [  3,  -1,   0,   1],
  [  2,   2,   1,  -1],
  [  1,  -1,   2,  -1],
  [  0,  -1,   3,   4]
]

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def is_valid(graph, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(graph), len(graph[0])
    if 0<=cur_r<r and 0<=cur_c<c and graph[cur_r][cur_c]!=-1:
        return True
    return False

def get_gates(grid):
    gates = []
    r, c = len(grid), len(grid[0])
    for ri in range(r):
        for ci in range(c):
            if grid[ri][ci] == 0:
                gates.append((ri, ci))
    return gates

def wag(grid):
    gates = get_gates(grid)
    visited = set()
    q = deque()

    for gate in gates:
        visited.add(gate)
        q.append((gate, 0))
    
    while q:
        node, d2g = q.popleft()
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                grid[nbr[0]][nbr[1]] = d2g+1
                visited.add(nbr)
                q.append((nbr,d2g+1))
    return grid

ans = wag(rooms)
for row in ans:
    print(row)
