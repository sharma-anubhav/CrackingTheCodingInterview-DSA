
sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]

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











