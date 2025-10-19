from heapq import heappop, heappush


def is_valid(grid, loc):
    cur_r, cur_c = loc
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c and grid[cur_r][cur_c]!=1:
        return True
    return False

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (-1,1), (1,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def shortest_path(grid):
    s = (0,0)
    visited = set() # Visited means final. In BFS its final as soon as you put in the queue but in dijkstra its final once you take it out.
    dist = {s:grid[s[0]][s[1]]}
    pq = []
    heappush(pq, (grid[s[0]][s[1]], s))
    while pq:
        cost, node = heappop(pq)
        if node in visited:
            continue
        # Stop early if we reach target
        # if node == target:
        #     return cost
        visited.add(node)
        dist[node] = cost
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                new_cost = cost + grid[nbr[0]][nbr[1]] ##<<<---- Always cost+grid[nbr] VIMP
                heappush(pq, (new_cost, nbr))
    return -1


def shortest_path(grid):
    s = (0,0)
    visited = set() # Visited means final. In BFS its final as soon as you put in the queue but in dijkstra its final once you take it out.
    dist = {s:grid[s[0]][s[1]]}
    pq = []
    heappush(pq, (grid[s[0]][s[1]], s))
    while pq:
        cost, node = heappop(pq)
        if node in visited:
            continue
        # Stop early if we reach target
        # if node == target:
        #     return cost
        visited.add(node)
        dist[node] = cost
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                new_cost = cost + grid[nbr[0]][nbr[1]] ##<<<---- Always cost+grid[nbr] VIMP
                if new_cost < dist.get(nbr, float('inf')): #<<----- Optimization to just  add only good ones to pq
                    dist[nbr] = new_cost
                    heappush(pq, (new_cost, nbr))
    return -1


def is_valid(grid, loc):
    cur_r, cur_c = loc
    r, c = len(grid), len(grid[0])
    if 0<=cur_r<r and 0<=cur_c<c:
        return True
    return False

def get_nbr(node):
    cur_r, cur_c = node[0], node[1]
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    for direction in directions:
        yield (cur_r+direction[0], cur_c+direction[1])

def shoot_obstacle(grid, k):
    s, e = (0,0), (len(grid)-1, len(grid[0])-1)
    distance = {(s, 0): grid[s[0]][s[1]]}
    pq = []
    heappush(pq, (grid[s[0]][s[1]], s, 0))
    visited = set()

    while pq:
        cost, node, destroyed = heappop(pq)
        if (node, destroyed) in visited:
            continue
        visited.add((node, destroyed))
        distance[(node, destroyed)] = cost

        if node == e:
            return cost

        for nbr in get_nbr(node):
            if not is_valid(grid, nbr):
                continue
            new_cost = cost+grid[nbr[0]][nbr[1]]
            if grid[nbr[0]][nbr[1]] == 1:
                if destroyed<k and (nbr, destroyed+1) not in visited and new_cost < distance.get((nbr, destroyed+1), float("inf")):
                    distance[(nbr, destroyed+1)] = new_cost
                    heappush(pq,(new_cost, nbr, destroyed+1))
            else:
                if (nbr, destroyed) not in visited and new_cost < distance.get((nbr, destroyed), float("inf")):
                    distance[(nbr, destroyed)] = new_cost
                    heappush(pq,(new_cost, nbr, destroyed))
    return -1

grid = [
  [0,0,0],
  [1,1,0],
  [0,0,0],
  [0,1,1],
  [0,0,0]
]
k = 1
# Output: 6


ans = shoot_obstacle(grid, k)
print(ans)