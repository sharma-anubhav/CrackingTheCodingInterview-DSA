"""
Problem 2: Sliding Window Max
Given a non-empty integer array, arr, and a subarray size, k, find the maximum element in each subarray of size k, from left to right.
"""

from collections import deque

arr = [10, 20, 30, 40, 30, 20, 10]
k = 2
Output = [20, 30, 40, 40, 30, 20]

class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()
    
    def peek(self): #  O(1)
        return self.queue[0] if self.queue else None
    
    def size(self): #  O(1)
        return len(self.queue)

    def max(self): #  O(1)
        return self.max_queue[0] if self.max_queue else None
    
    def pop(self): #  O(1)
        if not self.queue:
            return None
        val = self.queue.popleft()
        if self.max_queue and val == self.max_queue[0]:
            self.max_queue.popleft()
        return val
    
    def push(self, val): # worst case O(n)
        self.queue.append(val)
        while self.max_queue and self.max_queue[-1] < val:
            self.max_queue.pop()
        self.max_queue.append(val)
    

class Window:
    def __init__(self, l = 0, r = 0):
        self.l = l
        self.r = r
        self.queue = MaxQueue()

def swm(arr, k):
    ans = []
    w = Window()
    while w.r<len(arr):
        w.queue.push(arr[w.r])
        w.r+=1
        if w.r-w.l == k:
            ans.append(w.queue.max())
            w.l+=1
            w.queue.pop()
    return ans
            
ans = swm(arr, k)
print(ans)
