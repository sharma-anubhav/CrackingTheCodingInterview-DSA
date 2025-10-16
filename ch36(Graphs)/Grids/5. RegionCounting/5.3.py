"""
Flood Fill
You are given an m x n grid of integers image, where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color.
Perform a flood fill on the image starting from pixel image[sr][sc].
Flood Fill Rules:
Begin with the starting pixel and change its color to color.
Perform the same for each pixel adjacent (up, down, left, right) that has the same original color as the starting pixel.
Continue until no more adjacent pixels of the original color remain.
Return the modified image after the flood fill.
"""

image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
]
sr = 1
sc = 1
color = 2

output=[
    [2,2,2],
    [2,2,0],
    [2,0,1]
]

def is_valid(grid, loc, initial_color):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]==initial_color:
        return True
    return False

def get_nbr(node):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def flood_fill(grid, sr, sc, color):
    initial_node = (sr, sc)
    initial_color = grid[sr][sc]
    visited = set()
    def dfs(node):
        visited.add(node)
        grid[node[0]][node[1]] = color
        for nbr in get_nbr(node):
            if is_valid(grid, nbr, initial_color) and nbr not in visited:
                dfs(nbr)
    dfs(initial_node)
    print(visited)
    return grid

for r in image:
    print(r)
ans = flood_fill(image, sr, sc, color)
print("--"* 5)
for r in ans:
    print(r)

