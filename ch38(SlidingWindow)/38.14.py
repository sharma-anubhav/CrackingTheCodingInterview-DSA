sales = [5, 10, 15, 5, 10]

class Window:
    def __init__(self, l = 0, r = 0):
        self.l = l
        self.r = r
        self.sum = 0


def canshrink(window):
    if window.l < window.r  and window.sum - sales[window.l] >= 20:
        return True
    return False

# def shortest_over_20_sales(sales):
#     cur_window = Window()
#     smallest_window = Window(0,float("inf"))

#     while cur_window.r<len(sales):
#         if canshrink(cur_window):
#             cur_window.sum -= sales[cur_window.l]
#             cur_window.l+=1
#         else:
#             cur_window.sum += sales[cur_window.r]
#             cur_window.r+=1
#         if cur_window.sum > 20:
#             if cur_window.r - cur_window.l < smallest_window.r - smallest_window.l:
#                 smallest_window = Window(cur_window.l, cur_window.r)
#     if smallest_window.r == float("inf"):
#         return -1
#     return smallest_window.r-smallest_window.l


def mustgrow(window, sales):
    if window.sum <= 20:
        return True
    return False

def shortest_over_20_sales(sales):
    cur_window = Window()
    smallest_window = Window(0,float("inf"))

    while True:
        if mustgrow(cur_window, sales):
            if cur_window.r ==len(sales):
                break
            cur_window.sum+=sales[cur_window.r]
            cur_window.r+=1
        else:
            if cur_window.r-cur_window.l < smallest_window.r-smallest_window.l:
                smallest_window = Window(cur_window.l, cur_window.r)
            cur_window.sum-=sales[cur_window.l]
            cur_window.l+=1
    if smallest_window.r == float("inf"):
        return -1 
    return smallest_window.r-smallest_window.l


def run_tests():
  tests = [
      # Example 1 from the book
      ([5, 10, 15, 5, 10], 2),
      # Example 2 from the book
      ([5, 10, 4, 5, 10], 4),
      # Example 3 from the book
      ([5, 5, 5, 5], -1),
      # Edge case - empty array
      ([], -1),
      # Edge case - single element over 20
      ([21], 1),
      # Edge case - exactly 20 sales not enough
      ([10, 10], -1),
  ]
  for sales, want in tests:
    got = shortest_over_20_sales(sales)
    print(got)
    assert got == want, f"\nshortest_over_20_sales({sales}): got: {
        got}, want {want}\n"

run_tests()
                
