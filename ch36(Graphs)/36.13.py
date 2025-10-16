grid = [
  [0, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 0, 1, 1]
]
# Output: 3

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

## NOT GOOD APPRAOCH TRY USING RECIPIES
def count_islands_2(grid):
    visited = set()
    islands = 0
    def dfs(loc):
        nonlocal islands
        visited.add(loc)
        flag = 1
        if grid[loc[0]][loc[1]]==0:
            return
        else:
            for nbr in get_nbrs(loc):
                if not is_valid(grid, nbr):
                    continue
                if not nbr in visited:
                    if grid[nbr[0]][nbr[1]] == 1:
                        flag = 0
                    dfs(nbr)
            if flag:
                islands+=1

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                dfs((r, c))
    return islands


def run_tests():
  tests = [
      # Example 1 from the book
      ([[0, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 1]], 3),
      # Example 2 from the book
      ([[]], 0),
      # Edge case - single cell
      ([[1]], 1),
      # Edge case - all water
      ([[0, 0], [0, 0]], 0),
      # Edge case - all land
      ([[1, 1], [1, 1]], 1),
      # Multiple islands
      ([[1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]], 4)
  ]
  for grid, want in tests:
    got = count_islands(grid)
    assert got == want, f"\ncount_islands({grid}): got: {got}, want: {want}\n"

run_tests()