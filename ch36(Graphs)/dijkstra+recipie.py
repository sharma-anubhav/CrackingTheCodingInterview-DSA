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
