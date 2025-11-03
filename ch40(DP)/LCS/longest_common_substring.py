a = "abcde"
b = "abfce"

import numpy as np


def longest_common_substring(a, b):
    """
    Remember when you are carrying downwards, we need to track best. Becayuse it will not be returned at edge case.
    """
    n, m = len(a), len(b)
    best = 0
    def lcs_helper(i, j, cur_len):
        nonlocal best
        if i == n:
            return cur_len
        if j == m:
            return cur_len
        if a[i]==b[j]:
            best=max(best, cur_len+1)
            lcs_helper(i+1, j+1, cur_len+1)
        lcs_helper(i+1, j, 0)
        lcs_helper(i, j+1, 0)
        return 
    lcs_helper(0,0,0)
    return best

def longest_common_substring(a, b):
    n, m = len(a), len(b)
    best_till_now = 0
    def lcs_helper(i, j):
        nonlocal best_till_now
        if i == n:
            return 0
        if j == m:
            return 0
        if a[i]==b[j]:
            mx = 1+lcs_helper(i+1, j+1)
            if mx > best_till_now:
                best_till_now = mx
            return mx
        else:
            ## IMP I MISSED THIS
            lcs_helper(i+1, j)
            lcs_helper(i, j+1)
            return 0
    return lcs_helper(0,0)

def top_down(a, b):
    n, m = len(a), len(b)
    dp = np.full((n+1, m+1), 0)
    best = 0
    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if a[r] == b[c]:
                mx = 1+dp[r+1, c+1]
                if mx > best:
                    best = mx
                dp[r, c] = mx
            else:
                dp[r, c] = 0
    return best #OR np.max(dp)
            
ans = longest_common_substring(a, b)
ans = top_down(a, b)
print(ans)