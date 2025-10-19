
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"
word = "FCS"

def is_valid(graph, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(graph), len(graph[0])
    if 0<=cur_r<r and 0<=cur_c<c:
        return True
    return False

def get_nbr(node):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    cur_r, cur_c = node[0], node[1]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])
        
def find_paths(grid, target):
    n = len(grid)
    start = (0,0)
    visited = set()
    def dfs(node, state):
        visited.add(node)
        state = state + grid[node[0]][node[1]]
        if target in state:
            print(state)
            return True
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited: 
                if dfs(nbr, state):
                    return True
        visited.remove(node)
        return False
    return dfs(start, "")

ans = find_paths(board, word)
print(ans)

