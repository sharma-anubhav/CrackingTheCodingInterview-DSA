# Grid Transport Shortest Path Problem

This document summarizes the discussion on solving a 2D grid shortest path problem with multiple modes of transport.

---

## Problem Statement

* You have a 2D grid.
* Each **mode of transport** has:

  * Allowed movement patterns (e.g., walk = 4-neighbour, bus = long jumps).
  * Per-move **cost/time**.
* Goal: reach from **Start** to **End**.
* Rules:

  * **Mode switching allowed**: optional, may incur cost.
  * **No switching**: pick one mode and stick with it.
* Objective: find the mode/path with **minimum cost/time**.

---

## Approach 1: Simple Grid with Cell Costs

If each cell has a traversal cost and movement is 4-directional:

```python
import heapq

def shortest_path_cell_costs(grid, start, target):
    R, C = len(grid), len(grid[0])
    sr, sc = start
    tr, tc = target
    INF = 10**18
    dist = [[INF]*C for _ in range(R)]
    pq = []
    dist[sr][sc] = grid[sr][sc]
    heapq.heappush(pq, (dist[sr][sc], sr, sc))

    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while pq:
        d, r, c = heapq.heappop(pq)
        if d != dist[r][c]:
            continue
        if (r,c) == (tr,tc):
            return d
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                nd = d + grid[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq, (nd, nr, nc))
    return None
```

---

## Approach 2: Multi-Mode Transport with Optional Switching

* State = (row, col, mode)
* Transitions:

  * Move using current mode.
  * Switch mode (if allowed) with additional cost.
* Dijkstra algorithm over state space.

```python
import heapq
from collections import defaultdict

def dijkstra_multimode(grid, start, target, modes, switch_cost):
    R, C = len(grid), len(grid[0])
    sr, sc = start
    tr, tc = target

    INF = 10**18
    dist = defaultdict(lambda: INF)
    pq = []

    for mode in modes:
        dist[(sr,sc,mode)] = 0
        heapq.heappush(pq, (0, sr, sc, mode))

    while pq:
        d, r, c, mode = heapq.heappop(pq)
        if d != dist[(r,c,mode)]:
            continue
        if (r,c) == (tr,tc):
            return d
        # Move with current mode
        move_cost = modes[mode]["move_cost"]
        for dr, dc in modes[mode]["moves"]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] is not None:
                nd = d + move_cost + grid[nr][nc]
                if nd < dist[(nr,nc,mode)]:
                    dist[(nr,nc,mode)] = nd
                    heapq.heappush(pq, (nd, nr, nc, mode))
        # Switch mode
        for m2 in modes:
            if m2 == mode: continue
            scost = switch_cost(mode, m2)
            nd = d + scost
            if nd < dist[(r,c,m2)]:
                dist[(r,c,m2)] = nd
                heapq.heappush(pq, (nd, r, c, m2))

    return None
```

### Example Usage

```python
grid = [[0]*5 for _ in range(5)]
grid[2][2] = None

modes = {
    "walk": {"moves":[(1,0),(-1,0),(0,1),(0,-1)], "move_cost": 1.0},
    "bike": {"moves":[(1,0),(-1,0),(0,1),(0,-1)], "move_cost": 0.6},
    "bus": {"moves":[(i,0) for i in range(-3,4) if i!=0] + [(0,i) for i in range(-3,4) if i!=0], "move_cost": 1.0}
}

def switch_cost(a,b):
    if a==b: return 0
    if b=="bike": return 2.0
    if b=="bus": return 1.0
    return 0.5

start = (0,0)
target = (4,4)
ans = dijkstra_multimode(grid, start, target, modes, switch_cost)
print("Min cost:", ans)
```

---

## Approach 3: Single Mode Only (No Switching)

* Run independent search for each mode.
* Pick the mode that reaches the target with **minimum cost/time**.

```python
import heapq

def shortest_with_mode(grid, start, target, moves, move_cost):
    R, C = len(grid), len(grid[0])
    sr, sc = start
    tr, tc = target

    dist = [[float('inf')]*C for _ in range(R)]
    dist[sr][sc] = 0
    pq = [(0,sr,sc)]

    while pq:
        d,r,c = heapq.heappop(pq)
        if (r,c) == (tr,tc):
            return d
        if d != dist[r][c]:
            continue
        for dr,dc in moves:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and grid[nr][nc]==0:
                nd = d + move_cost
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(pq,(nd,nr,nc))
    return None

# Example usage
grid = [
 [0,0,0,0],
 [1,1,0,1],
 [0,0,0,0],
 [0,1,1,0],
 [0,0,0,0]
]
start, target = (0,0),(4,3)

modes = {
  "walk": {"moves":[(1,0),(-1,0),(0,1),(0,-1)], "cost":1},
  "bike": {"moves":[(1,0),(-1,0),(0,1),(0,-1)], "cost":0.5},
  "knight": {"moves":[(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)], "cost":1}
}

results = {}
for mode,info in modes.items():
    res = shortest_with_mode(grid,start,target,info["moves"],info["cost"])
    results[mode] = res

print("All results:", results)
reachable = {m:c for m,c in results.items() if c is not None}
if reachable:
    best_mode = min(reachable, key=lambda m:reachable[m])
    print("Best mode:", best_mode, "with cost:", reachable[best_mode])
else:
    print("Target not reachable with any mode")
```

---

## Notes

* Obstacles: mark cells with `None` or `1` depending on implementation.
* Multi-metrics: can extend to track both fuel and time. Choose based on priority (e.g., minimize fuel, tie-break by time).
* Complexity:

  * For grid of size `R×C` and `M` modes: O((R*C*M) log(R*C*M)) with Dijkstra.
* Variants:

  * Cell number = allowed jump length → generate moves dynamically.
  * Cell number = forced mode → only allow that mode at that cell.
  * Move cost = distance / speed for realistic travel time.

---

This file captures both the **switching allowed** and **single-mode-only** approaches discussed.
