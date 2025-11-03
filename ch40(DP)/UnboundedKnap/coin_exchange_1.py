coins = [1,2,3]
target = 5

import numpy as np
# subset sum but we are not limited.

def coin_exchange(coins, target):
    memo = {}
    def total_ways(i, remaining):
        if i  == len(coins):
            return 0
        if remaining == 0:
            return 1
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        yes = 0
        if remaining - coins[i] >= 0:
            yes = total_ways(i, remaining - coins[i])
        no = total_ways(i+1, remaining)
        memo[(i, remaining)] = yes+no
        return memo[(i, remaining)]
    return total_ways(0, target)

def ce_top_down(coins, target):
    n = len(coins)
    dp = np.full((n+1, target+1), 0)
    dp[:, 0] = 1
    for r in range(n-1, -1, -1):
        for c in range(1, target+1):
            yes = 0
            if c-coins[r] >=0:
                yes = dp[r,  c-coins[r]]
            no = dp[r+1, c]
            dp[r][c] = yes+no
    for row  in dp:
        print(row)
    return dp[0, target]


ans = coin_exchange(coins, target)
ans = ce_top_down(coins, target)
print(ans)