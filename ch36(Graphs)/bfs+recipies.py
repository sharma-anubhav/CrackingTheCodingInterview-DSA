# RECIPIE 1: BFS NORMAL # CORRECT
def bfs(graph, start):
    q = deque()
    distance = {start: 0}
    q.append(start)
    while q:
        ele = q.popleft()            
        for nbr in graph[ele]:
            if not nbr in distance:
                distance[nbr] = distance[ele]+1
                q.append(nbr)
    return distance

# # RECIPIE 1: INCORRECT
# def bfs(graph, start):
#     q = deque()
#     distance = {}
#     q.append((start, 0))
#     while q:
#         ele, dis = q.popleft()  
#         distance[ele] = dis    
#         for nbr in graph[ele]:
#             if not nbr in distance:
#                 q.append((nbr, dis+1))
#     return distance


#RECIPIE 2: Multi=source BFS
def bfs(graph, infected):
    distance_map = {}
    q = deque()
    for start in infected:
        distance_map[start] = 0
        q.append(start)
    
    while q:
        ele = q.popleft()
        for nbr in graph[ele]:
            if not nbr in distance_map:
                distance_map[nbr]= distance_map[ele]+1
                q.append(nbr)
    return distance_map