arr = [1, 2, 2, -1]

def check_k(arr):
    n = len(arr)
    k = n//2
    s, f = 0,0
    ss, fs = 0,0
    while f<n and s<k:
        ss+=arr[s]
        fs+=arr[f]+arr[f+1]
        f+=2
        s+=1
        if fs<ss:
            return False
    return True



