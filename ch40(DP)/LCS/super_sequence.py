#shortest super sequence
a = "aggtab" 
b = "gxtxayb"


import numpy as np
def print_lcs_top_down(a, b):
    n, m = len(a), len(b)
    dp = np.full((n+1, m+1), 0)

    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if a[r]==b[c]:
                dp[r][c] = 1+dp[r+1, c+1]
            else:
                dp[r,c] = max(dp[r+1, c], dp[r, c+1])
    for r in dp:
        print(r)

    # Think of traversal from top to bottom how we got there and now that have the valies how we can go
    def get_path(dp):
        r, c = 0,0
        ans= ""
        while r < n and c < m:
            if a[r] == b[c]:
                ans+=a[r]
                r = r+1
                c = c+1
            else:
                if dp[r+1, c] >= dp[r,c+1]:
                    ans+=a[r]
                    r = r+1
                else:
                    ans+=b[c]
                    c = c+1
        print(ans)
    return get_path(dp)
### Shortest Super Sequence is the SAME as LCS!! i.e m+n-LCS

ans = print_lcs_top_down(a, b)
print(ans)