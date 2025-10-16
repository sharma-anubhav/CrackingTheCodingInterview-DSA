arr = [1, 2, 3, 4, 5]
Output= [2, 4, 1, 3, 5]

def partiysort(arr):
    s,w = 0,0
    while s < len(arr) and w < len(arr):
        if arr[s]%2 == 0:
            arr[w], arr[s] = arr[s], arr[w]
            # s+=1
            w+=1
        else:
            s+=1
    return arr

print(partiysort(arr))











