def get_prefix_sum(arr): # prefix sum
    n = len(arr)
    ps = [0]*n
    ps[0] = arr[0]
    for i in range(1, n):
        ps[i] = ps[i-1]+arr[i]
    return ps

def get_sufix_sum(arr):   # suffix sum
    n = len(arr)
    ps = [0]*n
    ps[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        ps[i] = ps[i+1]+arr[i]
    return ps

def get_prefix_mul(arr):   # prefix product
    n = len(arr)
    pm = [1]*n
    pm[0] = arr[0]
    for i in range(1, n):
        pm[i] = pm[i-1]*arr[i]
    return pm

def get_sufix_mul(arr):  # suffix product
    n = len(arr)
    pm = [1]*n
    pm[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        pm[i] = pm[i+1]*arr[i]
    return pm