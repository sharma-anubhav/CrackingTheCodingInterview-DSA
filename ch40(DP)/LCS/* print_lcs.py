a = "abcdgh"
b = "abedfgh"

import numpy as np

# collect state in memo along with len
def print_longest_common_subsequence(a, b):
    n = len(a)
    m = len(b)
    memo = {}
    def lcs_helper(i, j):
        if i == n:
            return (0, "")
        if j == m:
            return (0, "")
        if(i, j) in memo:
            return memo[(i, j)]
        if a[i] == b[j]:
            l, s = lcs_helper(i+1, j+1)
            o1 = 1 + l
            s1 = s+a[i]
            memo[(i, j)] = (o1, s1)
            return memo[(i, j)]
        else:
            l1, s1 = lcs_helper(i+1, j)
            l2, s2 = lcs_helper(i, j+1)
            if l1 > l2:
                memo[(i, j)] = (l1, s1)
                return memo[(i, j)]
            memo[(i, j)] = (l2, s2)
            return memo[(i, j)]
    return lcs_helper(0,0)


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
                    r = r+1
                else:
                    c = c+1
        print(ans)
    return get_path(dp)



# ans = print_longest_common_subsequence(a, b)
ans = print_lcs_top_down(a, b)
print(ans)