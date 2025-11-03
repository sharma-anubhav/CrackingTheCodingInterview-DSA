import numpy as np

#min number of coinds
coins = [1,2,3]
target = 5

def coin_exchange(coins, target):
    n = len(coins)
    memo = {}
    def min_coins(i, remaining):
        if remaining == 0:
            return 0
        if i == n:
            return float("inf")-1 ### 1+infinite might create overflow
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        yes = float("inf")-1
        if remaining - coins[i] >= 0:
            yes = 1+min_coins(i, remaining-coins[i])
        no = min_coins(i+1, remaining)
        memo[(i, remaining)] =  min(yes, no)
        return memo[(i, remaining)]
    return min_coins(0, target)

ans = coin_exchange(coins, target)
print(ans)

