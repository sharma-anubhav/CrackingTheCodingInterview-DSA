"""
Problem Statement:
You are given an m × n maze represented as a 2D grid:
    0 → empty space
    1 → wall
You are given a 
    start [sx, sy] 
    destination [dx, dy]. 
The ball rolls in one direction until hitting a wall. It cannot stop in the middle of an empty space.
Return true if the ball can stop exactly at the destination, otherwise false.
"""

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

def escape(grid, start, destination):
    visited = set()
    def dfs(node, destination):
        visited.add(node)
        if node == destination:
            return True
        for dir in get_nbr(grid, node):
            cur = node
            dr, dc = dir
            while is_valid((cur[0]+dr, cur[1]+dc), grid):
                cur = (cur[0]+dr, cur[1]+dc)
            if cur not in visited:
                if dfs(cur, destination):
                    return True
        return False
    return dfs(start, destination)


# maze = [
#   [0,0,1,0,0],
#   [0,0,0,0,0],
#   [0,0,0,1,0],
#   [1,1,0,1,1],
#   [0,0,0,0,0]
# ]
# start = (0,4)
# destination = (4,4)
# # Output: true

maze = [
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,1,0],
  [1,1,0,1,1],
  [0,0,0,0,0]
]
start = (0,4)
destination = (3,2)

# Output: false

ans = escape(maze, start, destination)
print(ans)




            







