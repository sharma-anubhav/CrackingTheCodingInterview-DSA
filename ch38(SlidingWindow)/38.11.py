from math import ceil

projected_sales = [5, 5, 15, 0, 10]
k = 12

class Window:
    def __init__(self, n, l = 0, r = 0):
        self.l = l
        self.r = r

        self.boosted_cnt = 0
        self.boosted = [0]*n

def cangrow(window, sales):
    if sales[window.r] >= 10:
        return True, 0
    else:
        needed = 10-sales[window.r]
        k_needed = needed
        k_available = k-window.boosted_cnt
        if k_needed <= k_available:
            return True, k_needed
        return False, 0

def boost(sales, k):
    n = len(sales)
    cur_win = Window(n)
    longest = 0

    while cur_win.r < n:
        grow, k_needed = cangrow(cur_win, sales)
        if grow:
            if sales[cur_win.r] >= 10:
                cur_win.r+=1
            else:
                cur_win.boosted_cnt+=k_needed
                cur_win.boosted[cur_win.r]=k_needed
                cur_win.r+=1
            longest = max(longest, cur_win.r-cur_win.l)
        else:
            if cur_win.boosted[cur_win.l]>0:
                cur_win.boosted_cnt-=cur_win.boosted[cur_win.l]
                cur_win.boosted[cur_win.l]=0
            cur_win.l+=1
    print(longest)
    return longest

boost(projected_sales, k)
