arr = [6, 9, 12, 15, 18]
low = 9
high = 13
# Output: [10, 11, 13]

def rangefind(arr, low, high):
    l = 0
    ans = []
    while l<len(arr) and low <= high:
        if arr[l] < low:
            l+=1
        elif arr[l] == low:
            low+=1
        elif arr[l] > low:
            ans.append(low)
            low+=1
    if low <= high:
        ans.extend(range(low, high + 1))
    print(ans)
    return ans

rangefind(arr, low, high)