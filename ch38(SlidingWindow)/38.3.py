from collections import defaultdict, deque


best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"]
k = 3

class Window:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.internal = defaultdict(int)

def bestseller(arr, k):
    cur_window = Window(0,0)
    while cur_window.r< len(arr):
        cur_window.internal[arr[cur_window.r]]+=1
        cur_window.r+=1
        if cur_window.r-cur_window.l == k:
            if len(cur_window.internal.keys())==k:
                return True
            cur_window.internal[arr[cur_window.l]]-=1
            if cur_window.internal[arr[cur_window.l]] == 0:
                del cur_window.internal[arr[cur_window.l]]
            cur_window.l+=1
    return False

print(bestseller(best_seller, k))







