"""Unique Paths III
You are given an m x n integer array grid where grid[i][j] could be:
    1 representing the starting square. There is exactly one starting square.
    2 representing the ending square. There is exactly one ending square.
    0 representing empty squares we can walk over.
    -1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.
"""

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output = 2

def is_valid(graph, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(graph), len(graph[0])
    if 0<=cur_r<r and 0<=cur_c<c and graph[cur_r][cur_c]!=-1:
        return True
    return False

def get_nbr(node):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    cur_r, cur_c = node[0], node[1]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])
        

def find(grid):
    start, end, cnt = None, None, 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                start = (r, c)
            elif grid[r][c] == 2:
                end = (r, c)
            elif grid[r][c] == 0:
                cnt+=1
    return start, end, cnt

def unique_paths_3(grid):
    visited = set()
    start, end, no_obstacle_cnt = find(grid)

    def dfs(node, state):
        nonlocal path_cnt
        visited.add(node)
        if node == end and state == no_obstacle_cnt:
            path_cnt+=1
            visited.remove(node)
            return
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                if grid[nbr[0]][nbr[1]] == 0:
                    dfs(nbr, state+1)
                else:
                    dfs(nbr, state)
        visited.remove(node)
        return
    
    path_cnt = 0
    dfs(start, 0)
    return path_cnt

ans = unique_paths_3(grid)
print(ans)
