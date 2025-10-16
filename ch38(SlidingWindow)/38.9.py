projected_sales = [5, 0, 20, 0, 5]
k = 2

class Window:
    def __init__(self, n, l = 0, r = 0):
        self.l = l
        self.r = r

        self.boosted_cnt = 0
        self.boosted = [0]*n

def cangrow(window, sales):
    if sales[window.r] >= 10:
        return True
    else:
        if window.boosted_cnt < k:
            return True
        return False


def boost(sales, k):
    n = len(sales)
    cur_win = Window(n)
    longest = 0

    while cur_win.r < n:
        if cangrow(cur_win, sales):
            if sales[cur_win.r] >= 10:
                cur_win.r+=1
            else:
                cur_win.boosted_cnt+=1
                cur_win.boosted[cur_win.r]=1
                cur_win.r+=1
            longest = max(longest, cur_win.r-cur_win.l)
        else:
            if cur_win.boosted[cur_win.l]==1:
                cur_win.boosted_cnt-=1
                cur_win.boosted[cur_win.l]=0
            cur_win.l+=1
    print(longest)
    return longest

boost(projected_sales, k)

