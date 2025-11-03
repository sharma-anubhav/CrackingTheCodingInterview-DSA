def lis_recursive(nums):
    n = len(nums)
    memo = {}
    def helper(i, prev):
        if i == n:
            return 0
        if (i, prev) in memo:
            return memo[(i, prev)]
        not_take = helper(i + 1, prev)
        take = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + helper(i + 1, i)
        memo[(i, prev)] = max(take, not_take)
        return memo[(i, prev)]
    return helper(0, -1)
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis_recursive(arr))  # Output: 4


def lis_top_down_style(nums):
    n = len(nums)
    # dp[i][prev+1] = LIS length starting from index i, given previous index = prev
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # Base case: when i == n, LIS = 0  (already default)
    # Now fill table in reverse (like recursion unwinds)
    for i in range(n - 1, -1, -1):
        for prev in range(i - 1, -2, -1):  # -1 included
            # Option 1: not take nums[i]
            not_take = dp[i + 1][prev + 1]
            # Option 2: take nums[i]
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dp[i + 1][i + 1]
            dp[i][prev + 1] = max(take, not_take)

    return dp[0][0]