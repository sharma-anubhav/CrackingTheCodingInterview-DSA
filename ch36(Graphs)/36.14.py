from collections import deque

maze = [
  "...X.O",
  "OX.X..",
  "...X..",
  ".X....",
  "XOX.XX"
]

def is_valid(grid, pos):
    if pos[0]>=0 and pos[0]<len(grid) and pos[1]>=0 and pos[1]<len(grid[0]):
        return True
    return False

def get_nbrs(pos):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        yield pos[0]+dx, pos[1]+dy

def bfs(grid, exits):
    distances_map = {}
    q = deque()
    for exit in exits:
        q.append(exit)
        distances_map[exit] = 0
    
    while q:
        ele = q.popleft()
        for nbr in get_nbrs(ele):
            if is_valid(grid, nbr) and nbr not in distances_map:
                if grid[nbr[0]][nbr[1]] == 'X':
                    distances_map[nbr] = -1
                    continue
                if grid[nbr[0]][nbr[1]] == 'O':
                    distances_map[nbr] = 0
                    continue
                else:
                    distances_map[nbr] = distances_map[ele]+1
                    q.append(nbr)
    return distances_map

def get_exits(grid):
    exits = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                exits.append((i, j))
    return exits

def exit_distances(grid):
    exits = get_exits(grid)
    distance_map = bfs(grid, exits)
    ans = [[-1]*len(grid[0]) for _ in range(len(grid))]
    for pos, dis in distance_map.items():
        ans[pos[0]][pos[1]] = dis
    return ans

def run_tests():
  tests = [
      # Example from book
      [["...X.O",
        "OX.X..",
        "...X..",
        ".X....",
        "XOX.XX"],
       [
          [1, 2, 3, -1, 1, 0],
          [0, -1, 4, -1, 2, 1],
          [1, 2, 3, -1, 3, 2],
          [2, -1, 4, 5, 4, 3],
          [-1, 0, -1, 6, -1, -1]]],
      # Single exit
      [["...",
        ".O.",
        "..."],
          [[2, 1, 2],
           [1, 0, 1],
           [2, 1, 2]]],
      # Multiple exits
      [["O.O",
        "...",
        "O.O"],
          [[0, 1, 0],
           [1, 2, 1],
           [0, 1, 0]]],
      # Walls blocking direct paths
      [["O.X.",
        "XX..",
        "...O"],
          [[0, 1, -1, 2],
           [-1, -1, 2, 1],
           [3, 2, 1, 0]]],
      # Single cell
      [["O"],
          [[0]]]
  ]

  for maze_rows, want in tests:
    maze = [list(row) for row in maze_rows]
    got = exit_distances(maze)
    print(got)
    assert got == want, f"\nexit_distances({maze_rows}): got: {
        got}, want: {want}\n"

run_tests()