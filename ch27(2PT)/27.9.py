arr = [8, 4, 2, 6]
# Output:	[2, 4, 6, 8]

def sortvalley(arr):
    l, r = 0, len(arr)-1
    ans = [0]*len(arr)
    writer = len(ans)-1

    while l<=r:
        if arr[r]>arr[l]:
            ans[writer] = arr[r]
            r-=1
            writer -=1
        else:
            ans[writer] = arr[l]
            l+=1
            writer -=1
    return ans
print(sortvalley(arr))








