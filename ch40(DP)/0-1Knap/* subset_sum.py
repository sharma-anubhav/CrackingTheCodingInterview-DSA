arr = [2, 34, 12, 5, 1]
target = 8

import numpy as np
# lets not change the recusio. This is fine but let us stick to the original type so its easier for us to remember.
def subset_sum(arr, target):
    n = len(arr)
    def subset_helper(sum_till_now, i):
        if sum_till_now == target:
            return True
        if i == n:
            return False
        yes = False
        if sum_till_now+arr[i]<=target:
            yes = subset_helper(sum_till_now+arr[i], i+1)
        no = subset_helper(sum_till_now, i+1)
        return yes or no
    return subset_helper(0, 0)

# BRINGING BACK TO STANRD FORM
def subset_sum(arr, target):
    n = len(arr)
    def subset_helper(len_remaining, sum_remaining):
        if sum_remaining == 0:
            return True
        if len_remaining == 0:
            return False
        yes = False
        if sum_remaining-arr[len_remaining-1]>=0:
            yes = subset_helper(len_remaining-1, sum_remaining-arr[len_remaining-1])
        no = subset_helper(len_remaining-1, sum_remaining)
        return yes or no
    return subset_helper(n, target)

# Memoize
def subset_sum_memoized(arr, target):
    n = len(arr)
    memo = {}
    def subset_helper(len_remaining, sum_remaining):
        if sum_remaining == 0:
            return True
        if len_remaining == 0:
            return False
        if (len_remaining, sum_remaining) in memo:
            return memo[(len_remaining, sum_remaining)]
        yes = False
        if sum_remaining-arr[len_remaining-1]>=0:
            yes = subset_helper(len_remaining-1, sum_remaining-arr[len_remaining-1])
        no = subset_helper(len_remaining-1, sum_remaining)
        memo[(len_remaining, sum_remaining)] = yes or no
        return memo[(len_remaining, sum_remaining)]
    return subset_helper(n, target)

def subset_sum_top_down(arr, target):
    n = len(arr)
    dp = np.full((n+1, target+1), False)
    dp[0, :] = False
    dp[:, 0] = True  # MAKE SURE TRUE IS INITIALIZED AFTER FALSE
    
    for r in range(1, n+1):
        for c in range(1, target+1):
            yes = False
            if c-arr[r-1] >=0:
                yes = dp[r-1, c-arr[r-1]]
            no = dp[r-1, c]
            dp[r][c] = yes or no

    # r, c = n, target
    # ans = ""
    # while r>0 and c>0:
    #     yes = False
    #     if c-arr[r-1] >=0:
    #         yes = dp[r-1, c-arr[r-1]]
    #     no = no = dp[r-1, c]
    #     if yes:
    #         ans += str(arr[r-1])
    #         ans += "*"
    #         r, c= r-1, c-arr[r-1]
    #     elif no:
    #         r = r-1
    # print(ans)
    return dp[n][target]
    
ans = subset_sum_top_down(arr, target)
# ans = subset_sum_memoized(arr, target)
print(ans)
