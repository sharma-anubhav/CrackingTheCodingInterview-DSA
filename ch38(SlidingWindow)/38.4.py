from collections import defaultdict, deque

best_seller = ["book3", "book1", "book3", "book3", "book2"]
k = 3

class Window:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.internal = defaultdict(int)

def has_enduring_best_seller_streak(arr, k):
    cur_window = Window(0,0)
    while cur_window.r< len(arr):
        cur_window.internal[arr[cur_window.r]]+=1
        cur_window.r+=1
        if cur_window.r-cur_window.l == k:
            if len(cur_window.internal.keys())==1:
                return True
            cur_window.internal[arr[cur_window.l]]-=1
            if cur_window.internal[arr[cur_window.l]] == 0:
                del cur_window.internal[arr[cur_window.l]]
            cur_window.l+=1
    return False


def run_tests():
  tests = [
      # Example 1 from the book
      (["book3", "book1", "book3", "book3", "book2"], 3, False),
      # Example 2 from the book
      (["book3", "book1", "book3", "book3", "book2"], 2, True),
      (["book1", "book1", "book2", "book1"], 2, True),
      # Edge case - k=1
      (["book1", "book2"], 1, True),
      # Edge case - k=len(best_seller)
      (["book1", "book1", "book1"], 3, True),
      # no same sequence possible
      (["book1", "book2", "book1"], 2, False),
  ]
  for best_seller, k, want in tests:
    got = has_enduring_best_seller_streak(best_seller, k)
    print(got)
    assert got == want, f"\nhas_enduring_best_seller_streak({best_seller}, {k}): got: {
        got}, want {want}\n"
    # got = has_enduring_best_seller_streak_2(best_seller, k)
    # assert got == want, f"\nhas_enduring_best_seller_streak_2({best_seller}, {k}): got: {
    #     got}, want {want}\n"

run_tests()