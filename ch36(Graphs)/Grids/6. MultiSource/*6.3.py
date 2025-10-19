"""
You and several monsters are trapped in a labyrinth represented by a 2D grid.
You (A) can move one step up, down, left, or right per turn.
Each monster (M) also moves one step simultaneously in any direction.
Walls (#) are impassable.
Empty spaces (.) are walkable.
Your goal is to reach any boundary cell (top row, bottom row, leftmost column, or rightmost column) without ever being on the same cell as a monster, at any point — including the moment a monster moves into your cell.
You must find whether escape is possible.
If yes, print:
"YES"
The length of the path
The sequence of moves (U, D, L, R) that lead you to safety.
Your plan must work even if monsters know your path in advance.
"""

from collections import deque
from pydoc import visiblename

######### IMPORATANT FOR LEARNING 2 ways of path recreation and state in Dijkstra

grid = """
########
#M..A..#
#.#.M#.#
#M#..#..
#.######
""".strip().split('\n')

grid = [list(row) for row in grid]

output = """
YES
5
RRDDR
"""

def is_valid(graph, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(graph), len(graph[0])
    if 0<=cur_r<r and 0<=cur_c<c and graph[cur_r][cur_c]!= "#":
        return True
    return False

def get_monsters_exits_start(grid):
    monsters = []
    exits = []
    start = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "M":
                monsters.append((r, c))
            if grid[r][c] == "." and ((r == 0 or r == len(grid)-1 or (c == 0 or c == len(grid[0])-1))):
                exits.append((r,c))
            if grid[r][c] == "A":
                start = (r, c)

    return start, monsters, exits

############### Using State ####################

DIR2ALPHA = {(1,0): "D", (-1,0):"U", (0,1):"R", (0,-1):"L"}
## PATH CAN ALSO BE PASSED AS A STATE "LRLU" uptill now instead of passing parent.

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1]), direction

def escape(grid):
    start, monsters, exits = get_monsters_exits_start(grid)
    visited = set()
    q = deque()
    for monster in monsters:
        visited.add(monster)
        grid[monster[0]][monster[1]] = 0
        q.append((monster, 0))
    
    while q:
        node, time = q.popleft()
        for nbr, dir in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                grid[nbr[0]][nbr[1]] = time+1
                visited.add(nbr)
                q.append((nbr, time+1))
    
    visited = set()
    def dfs(node, time, p2n):
        visited.add(node)
        if grid[node[0]][node[1]] != "." and grid[node[0]][node[1]] <= time:
            return False, p2n
        if node in exits and (grid[node[0]][node[1]] == "." or grid[node[0]][node[1]] > time):
            return True, p2n
        for nbr, dir in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                escaped, local_p2n = dfs(nbr, time+1, p2n+DIR2ALPHA[dir])
                if escaped:
                    return True, local_p2n
        return False, p2n
    return dfs(start, 0, "")



############### Using parent tracking ####################

def get_nbr_2(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def path2dir(path):
    ans = []
    for i in range(len(path)-1):
        if path[i][0] < path[i+1][0]:
            ans.append("D")
        if path[i][0] > path[i+1][0]:
            ans.append("U")
        if path[i][1] < path[i+1][1]:
            ans.append("R")
        if path[i][1] > path[i+1][1]:
            ans.append("L")
    return ans

def escape2(grid):
    start, monsters, exits = get_monsters_exits_start(grid)
    visited = set()
    q = deque()
    for monster in monsters:
        visited.add(monster)
        grid[monster[0]][monster[1]] = 0
        q.append((monster, 0))
    
    while q:
        node, time = q.popleft()
        for nbr in get_nbr_2(node):
            if is_valid(grid, nbr) and nbr not in visited:
                grid[nbr[0]][nbr[1]] = time+1
                visited.add(nbr)
                q.append((nbr, time+1))
    
    visited = set()
    parent = {}
    def dfs(node, time, p):
        visited.add(node)
        parent[node] = p
        if grid[node[0]][node[1]] != "." and grid[node[0]][node[1]] <= time:
            return False, None
        if node in exits and (grid[node[0]][node[1]] == "." or grid[node[0]][node[1]] > time):
            return True, node
        for nbr in get_nbr_2(node):
            if is_valid(grid, nbr) and nbr not in visited:
                escaped, exit = dfs(nbr, time+1, node)
                if escaped:
                    return True, exit
        return False, None
    escaped, exit = dfs(start, 0, None)
    if escaped:
        path = []
        cur = exit
        while cur:
            path.append(cur)
            cur = parent[cur]
        return True, path2dir(path[::-1])
    else:
        return False, None



ans, path = escape(grid)
print(ans)
print(path)
            
        
        
