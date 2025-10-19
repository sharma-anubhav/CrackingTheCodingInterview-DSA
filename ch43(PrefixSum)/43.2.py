"""
YouTube Video Reception
A YouTuber has fetched the number of likes and dislikes of a video each day since its publication. We say a day is positive if it has more likes than dislikes.

We are given:

Two arrays, likes and dislikes, of length n, representing the likes and dislikes on each day.
An array periods of length p, where each element is a pair [l, r] with 0 ≤ l ≤ r < n. Each pair represents a time period from day l to day r inclusive.
Return an array, results, of length p, where results[i] is the number of positive days during period[i].
"""

likes    = [6, 3, 4, 8, 7, 2, 6, 5, 0, 1]
dislikes = [6, 0, 8, 0, 0, 0, 1, 8, 0, 2]
periods  = [[0, 1], [0, 5], [5, 8], [3, 3]]

Output: [1, 4, 2, 1]

def get_ps(arr1, arr2):
    ps = [0]*len(arr1)
    if arr1[0]>arr2[0]:
        ps[0] = 1
    for i in range(1, len(arr1)):
        if arr1[i]>arr2[i]:
            ps[i] = ps[i-1]+1
        else:
            ps[i] = ps[i-1]
    return ps

def good_days(likes, dislikes, periods):
    ps = get_ps(likes, dislikes)
    ans = []
    for p in periods:
        l, r  = p[0], p[1]
        if l == 0:
            ans.append(ps[r])
        else:
            ans.append(ps[r]-ps[l-1])
    return ans

ans = good_days(likes, dislikes, periods)
print(ans)