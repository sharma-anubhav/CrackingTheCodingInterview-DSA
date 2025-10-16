sales = [8, 1, 3, 7]
k = 2

class Window:
    def __init__(self, l=-1, r=-1, sum=0):
        self.sum = sum
        self.l = l
        self.r = r

def most_sales_in_k(arr, k):
    best = Window()
    window_sales = Window(0,0,0)

    while window_sales.r < len(arr):
        window_sales.sum += arr[window_sales.r]
        window_sales.r += 1
        if window_sales.r - window_sales.l == k:
            if window_sales.sum >= best.sum:
                best = Window(window_sales.l, window_sales.r, window_sales.sum)
            window_sales.sum -= arr[window_sales.l]
            window_sales.l += 1
    return best.l, best.sum

print(most_sales_in_k(sales, k))