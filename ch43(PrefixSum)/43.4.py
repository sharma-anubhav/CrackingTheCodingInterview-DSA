"""
Balance Point
Given an array of integers, arr, return the first balanced index, if there is any, or -1 otherwise. 
An index is balanced if the sum of the elements to its left is the same as the sum of the elements to its right.
"""

arr = [3, 5, -2, 7, 2, 2, 2]
Output=  3

def get_prefix_sum(arr): 
    n = len(arr)
    ps = [0]*n
    ps[0] = arr[0]
    for i in range(1, n):
        ps[i] = ps[i-1]+arr[i]
    return ps

def get_sufix_sum(arr):  
    n = len(arr)
    ps = [0]*n
    ps[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        ps[i] = ps[i+1]+arr[i]
    return ps

def balance(arr):
    pre_sum = get_prefix_sum(arr)
    suf_sum = get_sufix_sum(arr)

    for i in range(len(arr)):
        if pre_sum[i] == suf_sum[i]:
            return i
    return -1

ans = balance(arr)
print(ans)
