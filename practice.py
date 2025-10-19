def get_nge(arr):
    n = len(arr)
    nga = [-1]*n
    stack = []

    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            nga[i] = stack[-1]
        stack.append(i)
    return nga