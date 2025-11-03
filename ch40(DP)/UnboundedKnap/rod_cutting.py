n = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]

## NAIVE THOUGHT
def rod_cutting(n, price):
    def cutting_helper(i, cur_len):
        if i == n:
            if cur_len!= 0:
                return price[cur_len-1]
            return 0
        yes = cutting_helper(i+1, cur_len+1)
        no = price[cur_len] + cutting_helper(i+1, 0)
        return max(yes, no)
    return cutting_helper(0, 0)

### NOW THINK we have optionns for cuts 1----n. Keep eating till you get to n
### GOOD UNBOUNDED KNAPSACK APPRACH
def rod_cutting(n, price):
    def cutting_helper(i, remaining):
        if i == n+1:
            return 0
        yes = 0
        if remaining - i >= 0:
            yes = price[i-1] + cutting_helper(i, remaining-i)
        no = cutting_helper(i+1, remaining)
        return max(yes, no)
    return cutting_helper(1, n)


ans = rod_cutting(n, prices)     
print(ans)