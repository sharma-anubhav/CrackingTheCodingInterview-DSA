arr = [1, 7, 2, 3, 3, 5, 3]
pivot = 4

def partition(arr, pivot):
    s, w = 0,0
    while s<len(arr) and w<len(arr):
        if arr[s]<pivot:
            arr[w], arr[s] = arr[s], arr[w]
            s+=1
            w+=1
        else:
            s+=1
    return arr

print(partition(arr, pivot))