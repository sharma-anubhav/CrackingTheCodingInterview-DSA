arr = [1, 3, 5]
#output = 1
"""
s1+s2 = total
s1-s2 = s1-total+s1
"""
# # REALLLYYYY BADDDDD!!!
# def min_subset_sum_diff(arr):
#     n = len(arr)
#     total = sum(arr)
#     best_till_now = float("inf")
#     def subset_helper(sum_till_now, i):
#         nonlocal best_till_now
#         if i == n:
#             best_till_now = min(best_till_now, abs(2*sum_till_now-total))
#             return best_till_now 
#         yes = subset_helper(sum_till_now + arr[i], i+1)
#         no = subset_helper(sum_till_now, i+1)
#         return best_till_now
#     return subset_helper(0,0)

## GOODDDDD!!!!!!
def min_subset_sum_diff(arr):
    n = len(arr)
    total = sum(arr)
    def subset_helper(sum_till_now, i):
        if i == n:
            return abs(2*sum_till_now-total)
        yes = subset_helper(sum_till_now + arr[i], i+1)
        no = subset_helper(sum_till_now, i+1)
        return min(yes, no)
    return subset_helper(0,0)

# lets memoize
## GOODDDDD!!!!!!
def min_subset_sum_diff_memo(arr):
    n = len(arr)
    total = sum(arr)
    memo = {}
    def subset_helper(sum_till_now, i):
        if i == n:
            return abs(2*sum_till_now-total)
        if (sum_till_now, i) in memo:
            return memo[(sum_till_now, i)]
        yes = subset_helper(sum_till_now + arr[i], i+1)
        no = subset_helper(sum_till_now, i+1)
        memo[(sum_till_now, i)]= min(yes, no)
        return memo[(sum_till_now, i)]
    return subset_helper(0,0)

# lets convert to standard form
"""
sum_remaining = total-s1
s1 = total-sum_remaining
s2 = total - s1
s1 - s2 = 2*s1 - total
        = total-2sum_remaining
"""
def min_subset_sum_diff_memoized_standard_memoized(arr):
    n = len(arr)
    total = sum(arr)
    memo = {}
    def subset_helper(len_remaining, sum_remaining):
        if len_remaining == 0:
            return abs(2*sum_remaining - total) 
        if (len_remaining, sum_remaining) in memo:
            return memo[(len_remaining, sum_remaining)]
        yes = subset_helper(len_remaining-1, sum_remaining - arr[len_remaining-1])
        no = subset_helper(len_remaining-1, sum_remaining)
        memo[(len_remaining, sum_remaining)] =  min(yes, no)
        return  memo[(len_remaining, sum_remaining)]
    return subset_helper(n,total)

def min_subset_sum_diff_memoized_standard_memoized(arr):
    n = len(arr)
    total = sum(arr)
    memo = {}
    def subset_helper(len_remaining, sum_till_now):
        if len_remaining == 0:
            return abs(total - 2*sum_till_now)
        if (len_remaining, sum_till_now) in memo:
            return memo[(len_remaining, sum_till_now)]
        yes = subset_helper(len_remaining-1, sum_till_now + arr[len_remaining-1])
        no = subset_helper(len_remaining-1, sum_till_now)
        memo[(len_remaining, sum_till_now)] = min(yes, no)
        return memo[(len_remaining, sum_till_now)]
    return subset_helper(n,0)

# clever trick
# for top down we just do subset sum and check all possible subset sums till half.

# IMP TO NOTE THE Float("inf") initialization
def min_subset_sum_diff_dp_tabulation(arr):
    n = len(arr)
    total = sum(arr)
    dp = [[float('inf')] * (total + 1) for _ in range(n + 1)]
    for s in range(total + 1):
        dp[0][s] = abs(2*s - total)

    for i in range(1, n + 1):
        for s in range(total + 1):
            no = dp[i-1][s]            
            yes = float('inf')
            if s >= arr[i-1]:
                yes = dp[i-1][s - arr[i-1]]
            dp[i][s] = min(yes, no)
    return dp[n][0] 

ans = min_subset_sum_diff_memoized_standard_memoized_top_down(arr)
print(ans)