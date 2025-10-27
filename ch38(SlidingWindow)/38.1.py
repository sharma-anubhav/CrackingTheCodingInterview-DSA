sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]

class Window:
    def __init__(self, l =0 , r =0):
        self.l  = l
        self.r = r 
        self.sum  = 0

def most_weekly_sales(sales):
    w = Window()
    best = -1
    while w.r < len(sales):
        w.sum += sales[w.r]
        w.r +=1
        if w.r-w.l == 7:
            best = max(best, w.sum)
            w.sum -= sales[w.l]
            w.l+=1
    return best

ans = most_weekly_sales(sales)
print(ans)


def sale(arr, k=7):
    l, r = 0,0
    window_sum = 0
    best = 0
    while r < len(arr):
        window_sum+=arr[r]
        r+=1
        if r-l == k:
            best = max(best, window_sum)
            window_sum-=arr[l]
            l+=1
    return best

print(sale(sales))











