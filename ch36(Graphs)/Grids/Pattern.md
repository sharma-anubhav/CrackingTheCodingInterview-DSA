1. Reachability:
- DFS/BFS

2. Unweighted Shortest path (BFS)
2.1 Normal
    - visited(node), queue(steps, node)
2.2 We have a state
    - visited(node, state) , queue(steps, node, state)
2.3 Heuristic
    - A*
2.4 All destinations:
    - Distance vector instead of visited.

3. Weighted Shortest path (Dijkstra)
3.1 Normal
    - Visited(node), PQ(cost, node)
3.2 State
    - Visited(node, state), PQ(cost, node, state)
3.3 Heuristic
    - A*
3.4 All destinations:
    - Distance vector instead of visited.