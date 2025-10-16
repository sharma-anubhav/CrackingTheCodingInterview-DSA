"""
Problem 3: Largest Temperature Change
We are trying to install sensors that are sensitive to sudden temperature changes. 
The sensors should be fine as long as the temperature doesn't change too much within any k-day period.
Given an array temperatures with at least two integers, where each element represents the average temperature on a given day, 
and a number k with 2 ≤ k ≤ len(temperatures), return the maximum difference between average temperatures in a k-day period.
"""
from collections import deque

temperatures = [12, 13, 12, 13, 13, 12, 11, 12]
k = 3
Output =  2 
#The 3-day period with the maximum difference is [13, 12, 11], which has a difference of 13 - 11.

# temperatures = [10, 30]
# k = 2
# Output= 20


class MaxMinQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()
        self.min_queue = deque()
    
    def peek(self): #  O(1)
        return self.queue[0] if self.queue else None
    
    def size(self): #  O(1)
        return len(self.queue)

    def max(self): #  O(1)
        return self.max_queue[0] if self.max_queue else None
    
    def min(self):
        return self.min_queue[0] if self.min_queue else None
    
    def pop(self): #  O(1)
        if not self.queue:
            return None
        val = self.queue.popleft()
        if self.max_queue and val == self.max_queue[0]:
            self.max_queue.popleft()
        if self.min_queue and val == self.min_queue[0]:
            self.min_queue.popleft()
        return val
    
    def push(self, val): # worst case O(n)
        self.queue.append(val)
        while self.max_queue and self.max_queue[-1] < val:
            self.max_queue.pop()
        while self.min_queue and self.min_queue[-1] > val:
            self.min_queue.pop()
        self.max_queue.append(val)
        self.min_queue.append(val)
    

class Window:
    def __init__(self, l = 0, r = 0):
        self.l = l
        self.r = r
        self.queue = MaxMinQueue()

def temp(arr, k):
    ans = []
    w = Window()
    while w.r<len(arr):
        w.queue.push(arr[w.r])
        w.r+=1
        if w.r-w.l == k:
            ans.append(w.queue.max() - w.queue.min())
            w.l+=1
            w.queue.pop()
    return max(ans)

ans = temp(temperatures, k)
print(ans)

