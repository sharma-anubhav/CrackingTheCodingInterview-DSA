sales = [8, 9, 20, 0, 9]

class Window:
    def __init__(self, l, r, last=None):
        self.l = l
        self.r = r
        self.last = last

def isgood(sales):
    if sales <10:
        return 0
    return 1

def alternating(sales):
    cur_win = Window(0,0)
    best_win = Window(-1,-1)

    while cur_win.r<len(sales):
        if cur_win.last == None or cur_win.last != isgood(sales[cur_win.r]):
            cur_win.last = isgood(sales[cur_win.r])
            cur_win.r+=1
            if cur_win.r-cur_win.l >= best_win.r-best_win.l:
                best_win = Window(cur_win.l, cur_win.r, cur_win.last)
        else:
            cur_win.l = cur_win.r
            cur_win.last = None
    print(best_win.r-best_win.l, best_win.l, best_win.r)
    return best_win.r-best_win.l

alternating(sales)