# JUST CHANGE i+1 to i in YES CASE.
W = 51
w = [10, 20, 30]
v = [60, 100, 120]

"""Get profit tells us: 
Given cur_weight, i elements processed, what is the current profit. 

- States tracked: Current weight, current index, current profit
- Returns: Final profit value
- Problem: cur_profit makes memoization harder (3D state space)
"""
def knapsack(w, v, W):
    n = len(v)
    def get_profit(cur_weight, i, cur_profit):
        if i == n:
            return cur_profit
        if cur_weight == W:
            return cur_profit
        yes = -float("inf")
        if cur_weight + w[i] <= W:
            yes = get_profit(cur_weight+w[i], i, cur_profit+v[i])
        no = get_profit(cur_weight, i+1, cur_profit)
        return max(yes, no)
    return get_profit(0,0,0)

ans = knapsack(w, v, W)
print(ans)
            

"""Get profit tells us: 
Given cur_weight of what is the max profit i can get moving forward from ith element. 

- States tracked: Current weight used, current index
- Returns: Maximum profit from this state forward
- Better: Only 2D state space, profit computed in return value
"""
def knapsack(w, v, W):
    n = len(v)
    def get_profit(cur_weight, i):
        ## Doesnt matter what is cur_weight, nth element will return 0 since its out of index.
        if i == n:
            return 0
        if cur_weight == W:
            return 0   
        yes = -float("inf")
        if cur_weight + w[i] <= W:
            yes = v[i]+ get_profit(cur_weight+w[i], i)
        no = get_profit(cur_weight, i+1)
        return max(yes, no)
    return get_profit(0,0)

ans = knapsack(w, v, W)
print(ans)
            
        
"""Get profit tells us: 
Given cur_weight that is remaining of what is the Maximum profit achievable moving forward.

- States tracked: Remaining capacity, current index
- Returns: Maximum profit achievable moving forward from i
- Best for DP: Natural mapping to classic DP table
"""
def knapsack(w, v, W):
    n = len(v)
    def get_profit(weight_remaining, i):
        ## Doesnt matter what is cur_weight, nth element will return 0 since its out of index.
        if i == n:
            return 0     
        if weight_remaining == 0:
            return 0
        yes = -float("inf")
        if weight_remaining - w[i] >= 0:
            yes = v[i]+ get_profit(weight_remaining-w[i], i)
        no = get_profit(weight_remaining, i+1)
        return max(yes, no)
    return get_profit(W,0)

ans = knapsack(w, v, W)
print(ans)

"""Get profit tells us: 
Given weight_remaining and len of array remaining, what is the max profit i can get

- States tracked: Remaining capacity, remaining items
- Returns: Maximum profit
- Alternative view: Processes array in reverse
"""
def knapsack(w, v, W):
    n = len(v)
    def get_profit(weight_remaining, length_remaining):
        ## Doesnt matter what is cur_weight, nth element will return 0 since its out of index.
        if length_remaining == 0:
            return 0   
        if weight_remaining == 0:
            return 0     
        yes = -float("inf")
        if weight_remaining - w[length_remaining-1] >= 0:
            yes = v[length_remaining-1] + get_profit(weight_remaining-w[length_remaining-1], length_remaining-1)
        no = get_profit(weight_remaining, length_remaining-1)
        return max(yes, no)
    return get_profit(W,n)

ans = knapsack(w, v, W)
print(ans)
            
"""
Before writing DP code, ask:
- What does my function return? (Max profit? Boolean? Count?)
- What are my states? (What parameters uniquely define a subproblem?)
- What's my recurrence relation? (How do smaller subproblems combine?)
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
            yes = v[i]+ get_profit(weight_remaining-w[i], i)
        no = get_profit(weight_remaining, i+1)
        memo[(weight_remaining, i)] =  max(yes, no)
        return memo[(weight_remaining, i)]
    return get_profit(W,0)

ans = knapsack(w, v, W)
print(ans)