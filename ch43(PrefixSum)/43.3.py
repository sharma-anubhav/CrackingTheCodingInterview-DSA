"""
Problem 43.3 - Exclusive Product
Get asked this question by our AI Interviewer
Interview now
Given an array of non-negative integers, arr, return an array with the same length where index i contains the product of all the elements in arr except arr[i]. 
Since the values could be very large, return them modulo 10^9 + 7. IMPORTANT
"""

arr = [1, 3, 2, 1]
Output= [6, 2, 3, 6]

arr = [0, 1, 0]
Output= [0, 0, 0]

"""
Obvious approahc is to calvulate total product and divide each.
But product can become large

luckily we can find modulo for each and multiply them. It works for A/S/M but not D
So we might be able to get prefix multiplication using this trick but we cannot divide to get final ans.

Hence we calculate suffix-product too. and multiple prefix-product and suffix-product. ### THIS CAN BE HARD TO THINK OF IN EXAM!
"""

#only practicing prefixmul and postfixmul arr
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