arr = [-5, -2, -1, 1, 1, 10]

def twosum(arr):
    l, r = 0,len(arr)-1
    target = 0
    while l<r:
        if arr[l] + arr[r] == target:
            print(arr[l], arr[r])
            return arr[l], arr[r]
        elif arr[l] + arr[r] < target:
            l+=1
        else:
            r-=1
    print(-1, -1)
    return -1, -1

twosum(arr)        
