"""
Shortest Path to Get All Keys
You are given an m x n grid where each cell can be:
'.' — empty cell
'#' — wall
'@' — starting point
lowercase letters 'a'–'f' — keys
uppercase letters 'A'–'F' — locks
You can move up, down, left, right (4-directionally), but:
You cannot move through walls (#).
You cannot move through a lock (A–F) unless you have its corresponding key.
If you move over a key, you collect it and keep it forever.
There are exactly k pairs of keys and locks for some 1 ≤ k ≤ 6, and each letter from 'a' to 'f' appears at most once (and so does its uppercase version).
Your goal:
Return the minimum number of moves needed to collect all keys.
If impossible, return -1.
"""


## CHECK HOW TO USE BITMASKING TO SOLVE THESE BETTER. IT CAN BE USEFUL TO REPRESENT STATE

from collections import deque
from heapq import heappop, heappush


grid = [
    "@.a..",
    "###.#",
    "b.A.B"
]
output = 8

def find(grid):
    start = None
    key_cnt = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                start = (r,c)
            elif grid[r][c] == ".":
                continue
            elif grid[r][c].islower():
                key_cnt+=1
    return start, key_cnt

def is_valid(grid, loc):
    cur_r, cur_c = loc[0], loc[1]
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c] != "#":
        return True
    return False

def get_nbr(node):
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def collect_keys_bfs(grid):
    start, key_cnt = find(grid)
    visited = set((start, ""))
    q = deque()
    q.append((0, start, ""))

    while q:
        steps, node, keys = q.popleft()
        if len(keys) == key_cnt:
            return steps
        for nbr in get_nbr(node):
            if not is_valid(grid, nbr):
                continue
            if grid[nbr[0]][nbr[1]] == "." and (nbr, keys) not in visited:
                visited.add((nbr, keys))
                q.append((steps+1, nbr, keys))
            if grid[nbr[0]][nbr[1]].islower() and grid[nbr[0]][nbr[1]] not in keys:
                new_keys = "".join(sorted(keys+grid[nbr[0]][nbr[1]]))
                if (nbr, new_keys) not in visited:
                    visited.add((nbr, new_keys))
                    q.append((steps+1, nbr, new_keys))
            if grid[nbr[0]][nbr[1]].isupper() and (nbr, keys) not in visited:
                lock = grid[nbr[0]][nbr[1]]
                lock_key = lock.lower()
                if lock_key in keys:
                    visited.add((nbr, keys))
                    q.append((steps+1, nbr, keys))
    return -1

def collect_keys_dijkstra(grid):
    start, key_cnt = find(grid)

    visited = set()
    pq = []
    heappush(pq, (0, start, ""))

    while pq:
        steps, node, keys = heappop(pq)
        if node in visited:
            continue
        visited.add((node, keys))
        if len(keys) == key_cnt:
            return steps
        for nbr in get_nbr(node):
            if not is_valid(grid, nbr):
                continue
            if grid[nbr[0]][nbr[1]] == "." and (nbr, keys) not in visited:
                heappush(pq, (steps+1, nbr, keys))
            if grid[nbr[0]][nbr[1]].islower() and grid[nbr[0]][nbr[1]] not in keys:
                new_keys = "".join(sorted(keys+grid[nbr[0]][nbr[1]]))
                if (nbr, new_keys) not in visited:
                    heappush(pq, (steps+1, nbr, new_keys))
            if grid[nbr[0]][nbr[1]].isupper() and (nbr, keys) not in visited:
                lock = grid[nbr[0]][nbr[1]]
                lock_key = lock.lower()
                if lock_key in keys:
                    heappush(pq, (steps+1, nbr, keys))
    return -1

ans = collect_keys_bfs(grid)
print(ans)
            



            

