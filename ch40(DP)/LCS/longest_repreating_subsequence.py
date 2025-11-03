import numpy as np
a = "aggtab" 
b = "gxtxayb"

# its same as lcs but we with slight restriction that i!=j
def longest_repreating_subsequence(a, b):
    n = len(a)
    m = len(b)
    memo = {}
    def lcs_helper(i, j):
        if i == n:
            return 0
        if j == m:
            return 0
        if(i, j) in memo:
            return memo[(i, j)]
        if a[i] == b[j] and i!=j: #<<<-------------- ADD
            o1 = 1 + lcs_helper(i+1, j+1)
            memo[(i, j)] = o1
            return memo[(i, j)]
        else:
            o2 = lcs_helper(i+1, j)
            o3 = lcs_helper(i, j+1)
            memo[(i, j)] = max(o2, o3)
            return memo[(i, j)]
    return lcs_helper(0,0)

def lrs_top_down(a, b):
    n, m = len(a), len(b)
    dp = np.full((n+1, m+1), 0)

    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if a[r]==b[c] and r!=c:
                dp[r][c] = 1+dp[r+1, c+1]
            else:
                dp[r,c] = max(dp[r+1, c], dp[r, c+1])
    for r in dp:
        print(r)
    return dp[0, 0]

ans = longest_common_subsequence(a, b)
ans = lcs_top_down(a, b)
print(ans)