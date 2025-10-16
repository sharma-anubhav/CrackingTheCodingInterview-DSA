def get_nbrs(loc):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    x, y = loc
    for dx, dy in directions:
        yield (x+dx, y+dy)

def is_valid(grid, loc):
    if loc[0] >=0 and loc[0] < len(grid) and loc[1] >=0 and loc[1] < len(grid[0]) and grid[loc[0]][loc[1]]==1:
        return True
    return False 

def dfs(grid, pos, visited):
    visited.add(pos)
    for nbr in get_nbrs(pos):
        if is_valid(grid, nbr) and not nbr in visited:
            dfs(grid, nbr, visited)

def count_islands(grid):
    visited = set()
    islands = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_valid(grid, (r, c)) and not (r, c) in visited:
                islands+=1
                dfs(grid, (r, c), visited)
    return islands