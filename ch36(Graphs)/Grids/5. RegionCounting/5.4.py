"""
Surrounded Regions
You are given an m x n matrix board containing the characters 'X' and 'O'.
You need to capture regions that are completely surrounded by 'X'.
Definitions:
    Connect: 
        Two cells are connected if they are adjacent horizontally or vertically.
    Region: 
        A region is a group of 'O' cells connected together.
    Surrounded Region: 
        A region is surrounded if none of its 'O' cells touch the border (edges of the board).
    To capture such a region:
        Replace all 'O's in that region with 'X' — in place.
        You do not need to return anything.
"""

board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]

output = [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
]

def is_valid(grid, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c] == "O":
        return True
    return False

def get_nbr(node):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def capture(grid):
    def dfs(node, component):
        nonlocal visited
        touches_border = False
        visited.add(node)
        component.append(node)
        if node[0] in [0, len(grid)-1] or node[1] in [0, len(grid[0])-1]:
            touches_border = True
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                if dfs(nbr, component):
                    touches_border = True
        return touches_border

    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            node = (r,c)
            if is_valid(grid, node) and node not in visited:
                component = []
                touches_border = dfs(node, component)
                if not touches_border:
                    for loc in component:
                        grid[loc[0]][loc[1]] = "X"
    return grid


for r in board:
    print(r)
ans = capture(board)
print("--"* 6)
for r in ans:
    print(r)
