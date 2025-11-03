import numpy as np

## same as subset_sum just return 1 instead of true and accumulate
# Memoize
def subset_sum_cnt_memoized(arr, target):
    n = len(arr)
    memo = {}
    def subset_helper(len_remaining, sum_remaining):
        if sum_remaining == 0:
            return 1
        if len_remaining == 0:
            return 0
        if (len_remaining, sum_remaining) in memo:
            return memo[(len_remaining, sum_remaining)]
        yes = 0
        if sum_remaining-arr[len_remaining-1]>=0:
            yes = subset_helper(len_remaining-1, sum_remaining-arr[len_remaining-1])
        no = subset_helper(len_remaining-1, sum_remaining)
        memo[(len_remaining, sum_remaining)] = yes + no
        return memo[(len_remaining, sum_remaining)]
    return subset_helper(n, target)

def subset_sum_cnt_top_down(arr, target):
    n = len(arr)
    dp = np.full((n+1, target+1), 0)
    dp[0, :] = 0
    dp[:, 0] = 1
    
    for r in range(1, n+1):
        for c in range(1, target+1):
            yes = 0
            if c-arr[r-1] >=0:
                yes = dp[r-1, c-arr[r-1]]
            no = dp[r-1, c]
            dp[r][c] = yes + no

    for r in dp:
        print(r)
    return dp[n][target]

arr = [1,1,2,3,4,5,6,7,8]
target = 3
ans = subset_sum_cnt_top_down(arr, target)
print(ans)
