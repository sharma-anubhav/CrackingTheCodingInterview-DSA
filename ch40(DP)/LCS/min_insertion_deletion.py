a = "heap"
b = "pea"
# convert a to b
import numpy as np

# ALSO SAME AS LCS. Just find lcs(a, b)
# ans = len(a)-len(lcs) i.e deletions + len(b)-len(lcs) i.e inseritions
# example. we need remove h, p and add p. since lcs is ea

def lcs_top_down(a, b):
    n, m = len(a), len(b)
    dp = np.full((n+1, m+1), 0)

    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if a[r]==b[c]:
                dp[r][c] = 1+dp[r+1, c+1]
            else:
                dp[r,c] = max(dp[r+1, c], dp[r, c+1])
    return dp[0, 0]

def convert(a, b):
    lcs = lcs_top_down(a, b)
    return len(a)+len(b)-2*(lcs)

ans = convert(a, b)
print(ans)
