from asyncio import futures
import math

furniture = [
  [1, 1, 9, 5],
  [12, 9, 20, 13],
  [16, 2, 22, 7],
  [24, 9, 26, 11],
  [29, 1, 31, 5]
]
d = 5

# Output: True

def get_distance(f1, f2):
    x1_min, y1_min, x1_max, y1_max = f1
    x2_min, y2_min, x2_max, y2_max = f2

    if x1_max >= x2_min and x2_max >= x1_min:
        x_dis = 0
    else:
        x_dis = min(abs(x1_min - x2_max), abs(x2_min - x1_max))

    if y1_max >= y2_min and y2_max >= y1_min:
        y_dis = 0
    else:
        y_dis = min(abs(y1_min - y2_max), abs(y2_min - y1_max))

    return math.sqrt(x_dis**2 + y_dis**2)


def can_reach(furniture, d):
    visited = set()
    def dfs(furniture, start):
        visited.add(start)
        if start == len(furniture)-1:
            return True
        for i, nbr in enumerate(furniture):
            if i != start and not i in visited:
                dis = get_distance(furniture[start], nbr)
                if dis <= d:
                    if dfs(furniture, i):
                        return True
        return False
    return dfs(furniture, 0)

def run_tests():
  tests = [
      # Example 1 from the book:
      [[[1, 1, 9, 5],
        [12, 9, 20, 13],
        [16, 2, 22, 7],
        [24, 9, 26, 11],
        [29, 1, 31, 5]], 5, True],
      # Example 2 from the book:
      [[[1, 1, 9, 5],
        [12, 9, 20, 13],
        [16, 2, 22, 7],
        [24, 9, 26, 11],
        [29, 1, 31, 5]], 4, False],

      [[[0, 0, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]], 0, True],
      [[[0, 0, 1, 1], [1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]], 1, True],
      [[[0, 0, 1, 1], [1, 1, 2, 2], [3, 3, 4, 4], [4, 4, 5, 5]], 1, False],
      [[[0, 0, 1, 1], [1, 1, 2, 2], [3, 3, 4, 4], [4, 4, 5, 5]], 2, True],
      # Single piece of furniture
      [[[0, 0, 1, 1]], 5, True],
      # Two pieces far apart
      [[[0, 0, 1, 1], [10, 10, 11, 11]], 5, False],
      # Two pieces just within reach
      [[[0, 0, 1, 1], [5, 5, 6, 6]], 5.7, True],
      # Two pieces just out of reach
      [[[0, 0, 1, 1], [5, 5, 6, 6]], 5.6, False],
      # Pieces in a line
      [[[0, 0, 1, 1], [1, 0, 2, 1], [2, 0, 3, 1]], 1.5, True],
  ]
  for furniture, d, want in tests:
    got = can_reach(furniture, d)
    assert got == want, f"\ncan_reach({furniture}, {d}): got: {
        got}, want: {want}\n"

run_tests()