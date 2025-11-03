
import numpy as np

W = 51
w = [10, 20, 30]
v = [60, 100, 120]

"""
NOTE: If you see, we have two moving variables for which we create 2D grid.
How your recursion handles it depends how you will fill it up. 
NOTE: Base case of recursion is the initialization 0'/Val's in grid.
NOTE: You generally start filling based on your intersection of initialziation row, col. 
 - If 0th Row, 0th Col we fill top left to bottom right (max profit given full weight remaining and max len remaining to process)
 - if 0th Row, nth Col then top right to bottom left (max profit given full weight remaining and i am at start)
 - if nth Row, nth Col then bottom right to top left (...)
 - if nth Row, 0th Col then bottm left to top right (...)
 NOTE: All of these are cases we saw in recursion types.
"""

### NOW LETS MEMOIZE PLAIN AND SIMPLE :)
def knapsack(w, v, W):
    n = len(v)
    memo = {}
    def get_profit(weight_remaining, i):
        ## Doesnt matter what is cur_weight, nth element will return 0 since its out of index.
        if i == n:
            return 0     
        if weight_remaining == 0:
            return 0
        if (weight_remaining, i) in memo:
            return memo[(weight_remaining, i)]
        yes = -float("inf")
        if weight_remaining - w[i] >= 0:
            yes = v[i]+ get_profit(weight_remaining-w[i], i+1)
        no = get_profit(weight_remaining, i+1)
        memo[(weight_remaining, i)] =  max(yes, no)
        return memo[(weight_remaining, i)]
    return get_profit(W,0)

def knapsack_td(w, v, W):
    n = len(v)
    dp = np.full((W+1, n+1), 0)
    dp[:, 0] = 0
    dp[0, :] = 0
    for r in range(1, W+1):
        for c in range(n-1, -1,-1):
            yes = -float("inf")
            if r - w[c] >= 0:
                yes = v[c]+dp[r-w[c], c+1]
            no = dp[r, c+1]
            dp[r, c] = max(yes, no)
    return dp[W, 0]

### NOW LETS MEMOIZE PLAIN AND SIMPLE :)
def knapsack(w, v, W):
    n = len(v)
    memo = {}
    def get_profit(i, weight_remaining):
        ## Doesnt matter what is cur_weight, nth element will return 0 since its out of index.
        if i == n:
            return 0     
        if weight_remaining == 0:
            return 0
        if (i, weight_remaining) in memo:
            return memo[(i, weight_remaining)]
        yes = -float("inf")
        if weight_remaining - w[i] >= 0:
            yes = v[i]+ get_profit(i+1, weight_remaining-w[i])
        no = get_profit(i+1, weight_remaining)
        memo[(i, weight_remaining)] =  max(yes, no)
        return memo[(i, weight_remaining)]
    return get_profit(W,0)

def knapsack_td(w, v, W):
    n = len(v)
    dp = np.full((W+1, n+1), 0)
    dp[:, 0] = 0
    dp[0, :] = 0
    for r in range(n-1, -1,-1):
        for c in range(1, W+1):
            yes = -float("inf")
            if r - w[c] >= 0:
                yes = v[c]+dp[r-w[c], c+1]
            no = dp[r, c+1]
            dp[r, c] = max(yes, no)
    return dp[W, 0]

ans = knapsack_td(w, v, W)
print(ans)


## OLD
# def knapsack_top_down(max_weight, values, weights):
#     n = len(values)
#     # dp = [[0]*(max_weight+1)]*(n+1) <---- DONTTTTTT this is a nx1 not nxn. [0]*(max_weight+1) is treated as single objects
   
#     # dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]
#     # for r in range(n+1):
#     #     dp[r][0] = 1
#     # for c in range(max_weight+1):
#     #     dp[n][c] = 1

#     #OR use numpy
#     dp = np.full((n+1,max_weight+1), 0) # GOOD AND EASY TO MANIPULATE
#     dp[:, 0] = 0
#     dp[n, :] = 0

#     for r in range(n-1, -1, -1):
#         for c in range(1, max_weight+1):
#             if weights[r] <= c:
#                 dp[r][c] = max(dp[r][c], values[r]+dp[r+1][c-weights[r]])
#             dp[r][c] = max(dp[r][c], dp[r+1][c])
#     print(dp[0, max_weight])



# def knapsack_top_down(max_weight, values, weights):
#     n = len(values)
#     dp = np.full((n+1,max_weight+1), 0) 
#     dp[:, 0] = 0
#     dp[0, :] = 0

#     for r in range(1, n+1):
#         for c in range(1, max_weight+1):
#             if weights[r-1] <= c:
#                 dp[r][c] = max(dp[r][c], values[r-1]+dp[r-1][c-weights[r-1]])
#             dp[r][c] = max(dp[r][c], dp[r-1][c])
#     print(dp[n, max_weight])
# ans = knapsack_top_down(W, v, w)
# print(ans)