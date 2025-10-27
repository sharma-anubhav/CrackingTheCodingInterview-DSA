def rotate(arr, k):
    n = len(arr)
    k = k%n
    p1 = 0
    ans = [None]*n
    while p1 < n:
        ans[(p1+k)%n] = arr[p1]
        p1+=1
    return ans
