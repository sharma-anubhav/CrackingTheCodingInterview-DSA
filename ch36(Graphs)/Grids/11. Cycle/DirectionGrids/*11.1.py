"""
Detect Cycles in 2D Grid
You are given a 2D array of characters grid of size m x n.
Your task is to determine if there exists a cycle consisting of the same character in the grid.
A cycle is defined as:
    A path that starts and ends at the same cell.
    The path must contain at least 4 cells.
    You can move up, down, left, or right (no diagonals).
    You can only move to an adjacent cell if it has the same character.
    You cannot move back to the cell you came from in the immediately previous move.
Return true if any such cycle exists, otherwise return false.
"""
from pydoc import visiblename


grid = [
    ["a","a","a","a"],
    ["a","b","b","a"],
    ["a","b","b","a"],
    ["a","a","a","a"]
]
#True

grid = [
    ["c","c","c","a"],
    ["c","d","c","c"],
    ["c","c","e","c"],
    ["f","c","c","c"]
]
#True 

def is_valid(grid, node, alpha):
    cur_r, cur_c = node[0], node[1]
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c] == alpha:
        return True
    return False

def get_nbr(node):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def detect_cycles(grid):
    def dfs(node, parent):
        nonlocal visited
        visited.add(node)
        alpha = grid[node[0]][node[1]]
        for nbr in get_nbr(node):
            if is_valid(grid, nbr, alpha):
                if nbr in visited and nbr != parent:
                    return True
                elif nbr not in visited:
                    if dfs(nbr, node):
                        return True
        return False

    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r,c) not in visited:
                if dfs((r,c), None):
                    return True
    return False

ans = detect_cycles(grid)
print(ans)