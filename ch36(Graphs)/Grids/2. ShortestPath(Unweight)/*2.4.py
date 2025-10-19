"""
You are given an m x n integer matrix grid where:
Each cell is either:
0 : an empty cell you can move into, or
1 : an obstacle.
You can move up, down, left, or right to an adjacent cell if it’s within bounds.
You start at the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1).
You are also given an integer k, which represents the maximum number of obstacles you can eliminate during your path.
Return the minimum number of steps to reach the target, or -1 if it’s not possible.
"""

from collections import deque


def is_valid(grid, loc):
    cur_r, cur_c = loc
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c:
        return True
    return False

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def shoot_obstacle(grid, k):
    s, e = (0,0), (len(grid)-1, len(grid[0])-1)

    visited = set()
    q = deque()

    # visited.add(s) <-- We also need to add state in visited.
    visited.add((s, 0))
    q.append((s, 0, 0))

    while q:
        node, steps, destroyed = q.popleft()
        if node == e:
            return steps
        for nbr in get_nbr(node):
            if is_valid(grid, nbr):
                if grid[nbr[0]][nbr[1]] == 1:
                    if destroyed<k and (nbr, destroyed+1) not in visited:
                        visited.add((nbr, destroyed+1))
                        q.append((nbr, steps+1, destroyed+1))
                else:
                    if (nbr, destroyed) not in visited:
                        visited.add((nbr, destroyed))
                        q.append((nbr, steps+1, destroyed))
    return -1

grid = [
  [0,0,0],
  [1,1,0],
  [0,0,0],
  [0,1,1],
  [0,0,0]
]
k = 1
# Output: 6


ans = shoot_obstacle(grid, k)
print(ans)