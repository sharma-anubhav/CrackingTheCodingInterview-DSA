#RECEPIE 1: BASIC FIXED
"""
l, r = 0, 0
while r < len(arr):
    sum += arr[r]         # grow
    r += 1

    if r - l == k:        # if k window reached
        update_best(sum)  # check best
        sum -= arr[l]     # shrink
        l += 1
"""
def sale(arr, k=7):
    l, r = 0,0
    window_sum = 0
    best = 0
    while r < len(arr):
        window_sum+=arr[r]   # WE are adding r to window so computations like sum/avg should be done before increement
        r+=1
        if r-l == k:
            best = max(best, window_sum)
            window_sum-=arr[l] # WE are removing l to window so computations like sum/avg should be done before decrement
            l+=1
    return best

#RECEPIE 1: Complex Needs FIXED
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

#RECEPIE 2: Resetting 
"""
l, r = 0, 0
while r < len(arr):
    if is_valid_extension(arr, l, r):   # if can grow
        include(arr[r])                 #grow
        r += 1
        update_best_if_needed()         # check best
    else:
        reset_window_state()            # else Reset
        r += 1
        l = r                          
"""
"""
you check the validity of the entire window after adding otherwise reset.(41.6)
"""
def isgood(sales):
    if sales >= 10:
        return True
    return False

def bad(sales):
    l, r = 0,0
    mx = 0
    max_till_now = 0
    while r<len(sales):
        if isgood(sales[r]):
            r+=1
            max_till_now+=1
            if max_till_now > mx:
                mx = max_till_now
        else:
            r+=1
            l=r
            max_till_now=0
    return mx



#RECEPIE 3: Max Window
"""
l, r = 0, 0
while r < len(arr):
    if can_grow(arr, l, r):      # if can then grow 
        include(arr[r])          # Grow
        r += 1
        update_best(r - l)       # Update best
    elif l == r:
        l+=1
        r+=1
    else:
        remove(arr[l])
        l += 1                   # else shrink 
"""
# BASICALLY SAME INSTEAD OF RESET YOU SHRINK BY 1

def isbad(sale):
    if sale<10:
        return True
    return False

def cangrow(r, cur_cnt, sales):
    if isbad(sales[r]):
        cur_cnt+=1
        if cur_cnt <= 3:
            return True
        return False
    return True

def atmost(sales):
    l, r = 0,0
    cur_cnt = 0
    best = 0
    while r<len(sales):
        if cangrow(r, cur_cnt, sales):
            if isbad(sales[r]): cur_cnt+=1
            r+=1
            best = max(best, r-l)
        else:
            if isbad(sales[l]): cur_cnt-=1
            l+=1
    print(best)
    return best
atmost(sales)

# RECEPIE 4: MIN WINDOW
"""
## Remember if we direclty break while w.r < len(arr) then we miss last shrinking opportunity
while True:
    if must_grow:
        if r == len(arr):
            break
        grow()
    else:
        update_best()
        shrink()
"""
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

## COUNTING SUBARRAY PROBLEMS:
# RECIPIE 1: At most (same as maximum)
# RECIPIE 2: At least = Total i.e (n*n-1)/2 - at most
# RECIPIE 3: Exactly : atmost(k)-atmost(k-1)
