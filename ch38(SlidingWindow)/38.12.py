from collections import defaultdict


best_seller = ["book1", "book1", "book2", "book1", "book3", "book1"]
k = 2

class Window:
    def __init__(self, l=0, r=0):
        self.l = l
        self.r = r
        self.internal = defaultdict(int)

def cangrow(window, bs, k):
    if bs[window.r] in window.internal.keys():
        return True
    elif bs[window.r] not in window.internal.keys() and len(window.internal)<k:
        return True
    return False

def max_at_most_k_distinct(bs, k):
    cur_window = Window()
    best_window = Window()

    while cur_window.r<len(bs):
        if cangrow(cur_window, bs, k):
            cur_window.internal[bs[cur_window.r]]+=1
            cur_window.r+=1
            if cur_window.r-cur_window.l > best_window.r-best_window.l:
                best_window = Window(cur_window.l, cur_window.r)
        elif cur_window.l == cur_window.r:
            cur_window.l+=1
            cur_window.r+=1
        else:
            cur_window.internal[bs[cur_window.l]]-=1
            if cur_window.internal[bs[cur_window.l]] == 0:
                del cur_window.internal[bs[cur_window.l]]
            cur_window.l+=1
    return best_window.r-best_window.l
# def cangrow(win):
#     if len(win.internal) == 0:
#         return True
#     if len(win.internal) == win.r-win.l:
#         return True 
#     return False

# def longestdistinct(bs, k):
#     cur_win = Window()
#     best = 0
#     while cur_win.r < len(bs):
#         if cangrow(cur_win):
#             cur_win.internal[bs[cur_win.r]]+=1
#             cur_win.r+=1
#             best = max(best, cur_win.r-cur_win.l)
#         else:
#             cur_win.internal[bs[cur_win.l]]-=1
#             if cur_win.internal[bs[cur_win.l]] == 0:
#                 del cur_win.internal[bs[cur_win.l]]
#             cur_win.l+=1
#     print(best)
#     return best

# longestdistinct(best_seller, k)


def run_tests():
  tests = [
      # Example from the book
      (["book1", "book1", "book2", "book1", "book3", "book1"], 2, 4),
      # Edge case - empty array
      ([], 1, 0),
      # Edge case - k=1
      (["book1", "book2", "book1"], 1, 1),
      # Edge case - k=len(best_seller)
      (["book1", "book2", "book3"], 3, 3),
      # Edge case - all same book
      (["book1", "book1", "book1"], 1, 3),
  ]
  for best_seller, k, want in tests:
    got = max_at_most_k_distinct(best_seller, k)
    print(got)
    assert got == want, f"\nmax_at_most_k_distinct({best_seller}, {k}): got: {
        got}, want {want}\n"

run_tests()
