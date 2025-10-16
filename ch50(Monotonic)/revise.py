from collections import deque


def next_greater_ele(arr):
    n = len(arr)
    nge = [-1]*n
    stack = []

    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]] <= arr[i]: #<-- NOrice how we have <= here because we want strictly greater
            stack.pop()
        if stack:
            nge[i] = stack[-1]
        stack.append(i)
    return nge

class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()
    
    def max(self):
        return self.max_queue[0] if self.max_queue else None
    
    def push(self, val):
        self.queue.append(val)
        while self.max_queue and self.max_queue[-1]<val: #<--- Here we dont want to remove equal because it can very well be max ele
            self.max_queue.pop()
        self.max_queue.append(val)
        return
    
    def pop(self):
        val = self.queue.popleft()
        if self.max_queue and self.max_queue[0] == val:
            self.max_queue.popleft()
        return val
