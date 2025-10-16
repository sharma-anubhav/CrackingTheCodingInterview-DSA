"""
Path With Minimum Effort:
You are a hiker preparing for an upcoming hike. 
You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).

You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
"""
from heapq import heappop, heappush


heights = [[1,2,2],
            [3,8,2],
            [5,3,5]]
# Output: 2

# heights = [[1,2,3],
#             [3,8,4],
#             [5,3,5]]
# Output: 1

def is_valid(grid, loc):
    r, c = len(grid), len(grid[0])
    cur_r, cur_c = loc[0], loc[1]
    if 0<=cur_r<r and 0<=cur_c<c:
        return True
    return False

def get_nbr(node):
    directions = [(1,0), (0,1), (0,-1), (-1,0)]
    for direction in directions:
        yield (node[0]+direction[0], node[1]+direction[1])

def min_effort(heights):
    s, e = (0,0), (len(heights)-1, len(heights[0])-1)
    visited = set()
    distance = {s:0}

    pq = []
    heappush(pq, (0, s))

    while pq:
        cost, node = heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        distance[node] = cost
        if node == e:
            return cost
        for nbr in get_nbr(node):
            if is_valid(heights, nbr) and nbr not in visited:
                new_cost = max(cost, abs(heights[node[0]][node[1]] - heights[nbr[0]][nbr[1]]))
                if new_cost < distance.get(nbr, float("inf")):
                    distance[nbr] = new_cost
                    heappush(pq, (new_cost, nbr))
    return -1

ans = min_effort(heights)
print(ans)









