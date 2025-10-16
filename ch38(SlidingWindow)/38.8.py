sales = [0, 14, 7, 9, 0, 20, 10, 0, 10]

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




