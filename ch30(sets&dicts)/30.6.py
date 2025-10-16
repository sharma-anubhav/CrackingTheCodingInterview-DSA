arr = [4, 10, 3, 100, 5, 2, 10000]

def squares(arr):
    d = dict()
    ans = []
    for i, ele in enumerate(arr):
        d[ele] = i

    for i, ele in enumerate(arr):
        target = ele*ele
        if target in d.keys() and d[target] != i:
            ans.append([d[target], i])
    return ans

print(squares(arr))