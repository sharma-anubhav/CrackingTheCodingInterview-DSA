def dijkstra(grid):
    s = (0,0)
    visited = set() 
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

# prims is same as dijkstra with only differenec that we do not push cost+grid[nbr] but only grid[nbr]
# intuition is that we only want to connect chepest node that has not yet been connected to our current.
def prims(grid):
    s = (0,0)
    visited = set() 
    pq = []
    total_cost = 0
    heappush(pq, (grid[s[0]][s[1]], s))
    while pq:
        cost, node = heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        total_cost+=cost
        for nbr in get_nbr(node):
            if is_valid(grid, nbr) and nbr not in visited:
                heappush(pq, (grid[nbr[0]][nbr[1]], nbr)) # <- The only difference is we only push (weight(nbr) and not  cost+weight(mbr)
    return total_cost

def dijkstra(grid):
    s, e = (0,0), (len(grid)-1, len(grid[0])-1)
    
    distance = defaultdict(lambda: float('inf')) # <-- acts as visited set
    distance[s]= grid[s[0]][s[1]]
    pq = []
    heappush(pq, (grid[s[0]][s[1]], s)) # <-- acts as queue

    while pq:
        cost, node = heappop(pq)
        if node == e:
            return cost
        if cost > distance[node]: # <-- skip outdated
            continue
        for nbr in get_nbr(node):
            if is_valid(grid, nbr):
                new_cost = cost+grid[nbr[0]][nbr[1]]  # <-- udpated count
                if new_cost < distance[nbr]: # <-- insert valid ones
                    distance[nbr] = new_cost
                    heappush(pq, (new_cost, nbr))
    print(distance)
    return -1

