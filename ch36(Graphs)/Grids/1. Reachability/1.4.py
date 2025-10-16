"""
Problem Statement:
Same maze rules as Maze I, but this time, return the shortest distance from the start to the destination. 
Distance is the number of steps the ball rolls (sum of all moves). If the destination cannot be reached, return -1.

We also want to print the path using U D L R
"""

from collections import deque

############## DONT DO THIS!!! Using State INSTEAD. Check 6.3 ####################

def is_valid(loc, grid):
    cur_r, cur_c = loc
    r,c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]!=1:
        return True
    return False

def get_nbr(grid, node):
    directions  = [(1,0), (0,1), (-1, 0), (0,-1)]
    # cur_r, cur_c = node
    for direction in directions:
        # yield 
        yield direction

def get_direction(start, end):
    if end[0] > start[0]:
        return "D"
    elif end[0] < start[0]:
        return "U"
    elif end[1] > start[1]:
        return "R"
    elif end[1] < start[1]:
        return "L"
    else:
        print("COUNDNT FIND DIRECTION FOR: ", start, end)

def escape(grid, start, destination):
    q = deque()
    parent = {start: None}
    visited = {start}
    q.append((start, 0))
    found = None

    while q:
        node, dis = q.popleft()
        if node == destination:
            found = True
            break
        for dir in get_nbr(grid, node):
            cur_dis = 0
            cur = node
            dr, dc = dir
            while is_valid((cur[0]+dr, cur[1]+dc), grid):
                cur = (cur[0]+dr, cur[1]+dc)
                cur_dis+=1
            if cur not in visited:
                q.append((cur, dis+cur_dis))
                visited.add(cur)
                parent[cur] = node
    
    ans = []
    if found:
        cur = destination
        while cur and parent[cur]:
            ans.append(get_direction(parent[cur], cur))
            cur = parent[cur]
        return ans[::-1]

    return "Impossible"

maze = [
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,1,0],
  [1,1,0,1,1],
  [0,0,0,0,0]
]
start = (0,4)
destination = (4,4)

# Output: 12
ans = escape(maze, start, destination)
print(ans)
            









