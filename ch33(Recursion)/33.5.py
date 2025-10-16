arr = [3, -9, 2, 4, -1, 5, 5, -4]

def laminar(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    return max(laminar(arr[:n//2]), laminar(arr[n//2:]), sum(arr))

ans = laminar(arr)
print(ans)
        

## To optimize this we can send the sum along with the best till now and add sums from both sizes instead of having to compute it.
## Propogate sums