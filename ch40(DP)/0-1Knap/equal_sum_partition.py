arr = [2, 5, 11, 5]
#true

import numpy as np
# very basic
def equal_sum_partition(arr):
    n = len(arr)
    def partition_helper(i, s1, s2):
        if i == n:
            return s1 == s2
        yes = partition_helper(i+1, s1+arr[i], s2)
        no = partition_helper(i+1, s1, s2+arr[i])
        if yes or no:
            return True
        return False
    return partition_helper(0,0,0)

# remove redundant s2 and memoize
### IF TOU THINK ABOUT IT IT IS SAME AS SUBNSET SUM. s2 is total_sum - s1(target)
### if we get even 1 total//2 then there exists a subarray.
def equal_sum_partition_memoized(arr):
    n = len(arr)
    total = sum(arr)
    memo = {}
    def partition_helper(i, s1):
        if i == n:
            return s1 == total-s1
        if (i,s1) in memo:
            return memo[(i,s1)]
        yes = partition_helper(i+1, s1+arr[i])
        no = partition_helper(i+1, s1)
        memo[(i,s1)] = yes or no
        return memo[(i,s1)]
    return partition_helper(0,0)

# bring it into standard format. flip the requiremetns.
def equal_sum_partition_standard(arr):
    n = len(arr)
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total//2
    memo = {}
    def partition_helper(len_remaining, target_remaining):
        if len_remaining == 0:
            return False
        if target_remaining == 0:
            return True
        yes = False
        if target_remaining - arr[len_remaining-1]>=0:
            yes = partition_helper(len_remaining-1, target_remaining - arr[len_remaining-1])
        no = partition_helper(len_remaining-1, target_remaining)
        return yes or no
    return partition_helper(n,target)

# top down
def equal_sum_partition_top_down(arr):
    n = len(arr)
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total//2

    dp = np.full((n+1, target+1), False)
    dp[0, :] = False
    dp[:, 0] = True
    
    for r in range(1, n+1):
        for c in range(1, target+1):
            yes = False
            if c-arr[r-1] >=0:
                yes = dp[r-1, c-arr[r-1]]
            no = dp[r-1, c]
            dp[r][c] = yes or no
    for r in dp:
        print(r)
    return dp[n][target]

ans = equal_sum_partition(arr)
print(ans)
