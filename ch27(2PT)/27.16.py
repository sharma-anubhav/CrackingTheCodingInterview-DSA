arr = ['b', 'a', 'd', 'r', 'e', 'v', 'i', 'e', 'w']
Output =  ['r', 'e', 'v', 'i', 'e', 'w', 'b', 'a', 'd']

def ps_swap(arr):
    p, s = 0, (len(arr)//3)
    while p<len(arr) and s<len(arr):
        arr[p],arr[s] = arr[s],arr[p]
        p+=1
        s+=1
    return arr

print(ps_swap(arr))










