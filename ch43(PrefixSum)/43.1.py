"""
Channel Views:
A YouTuber wants to analyze their channel's performance to see if viewer engagement varies during certain times of the year. 
We are given:
    An array, views, of length n > 0, where views[i] represents the number of views on day i.
    An array, periods, of length p > 0, where each element is a pair [l, r] with 0 ≤ l ≤ r < n. 
    Each pair represents a time period from day l to day r inclusive.
Return an array, results, of integers with length p, where result[i] is the number of views during period i.
"""

views = [3, 5, 4, 8, 7, 2, 5, 3, 2, 3]
periods = [[0, 1], [0, 5], [5, 8], [3, 3]]
Output= [8, 29, 12, 8]

def get_ps(arr):
    ps = [arr[0]]*len(arr)
    for i in range(1, len(arr)):
        ps[i] = ps[i-1]+arr[i]
    return ps

def channel_views(arr):
    ps = get_ps(arr)

    ans = []
    for period in periods:
        l, r = period[0], period[1]
        if l == 0:
            ans.append(ps[r])
        else:
            ans.append(ps[r]-ps[l-1])
    return ans

ans = channel_views(views)
print(ans)