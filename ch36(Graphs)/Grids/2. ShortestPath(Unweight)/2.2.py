"""
On an infinite chessboard, a knight starts at position (0, 0). The knight can move in eight possible ways, same as in chess:
Given a target position (x, y), return the *** minimum number *** of moves the knight needs to reach (x, y) from (0, 0).
The board is infinite in all directions.
"""

from collections import deque


moves = [
(2, 1),
(2, -1),
(-2, 1),
(-2, -1),
(1, 2),
(1, -2),
(-1, 2),
(-1, -2)
]

def can_reach(loc, end):
    con = 10
    if loc[0]-con <= end[0] <= loc[0]+con and loc[1]-con <= end[1] <= loc[1]+con:
        return True
    return False

def get_nbr(loc, moves):
    cur_r, cur_c = loc[0], loc[1]
    for move in moves:
        yield (cur_r+move[0], cur_c+move[1])

def min_moves(start, end):
    visited = set()
    q = deque()

    visited.add(start)
    q.append((start, 0))

    while q:
        loc, mvs = q.popleft()
        if loc == end:
            return mvs
        for nbr in get_nbr(loc, moves):
            if can_reach(nbr, end):
                if nbr not in visited:
                    visited.add(nbr)
                    q.append((nbr, mvs+1))
    return -1

ans = min_moves((0,0), (-1,-1))
print(ans)
        
