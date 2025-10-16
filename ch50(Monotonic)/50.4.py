"""
Problem 4: Longest Stable Period
We are planning an expedition, and we don't know exactly how many days it will take. 
Since we don't want to carry too many different types of clothes, we want to know the longest period of time when temperatures are stable, 
meaning that they don't change by more than t degrees. That will be the ideal time for our expedition.

Given an array, temperatures, with at least two integers, where each element represents the average temperature on a given day, 
and a number t, return the length of the longest subarray where the difference between the maximum and minimum temperature is at most t.
"""
from collections import deque

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

def can_expand(arr, t, w):
    if not w.queue.queue:
        return True
    cur_max = w.queue.max()
    cur_min = w.queue.min()
    ele = arr[w.r]
    cur_max = max(cur_max, ele)
    cur_min = min(cur_min, ele)
    if cur_max-cur_min <= t:
        return True
    return False

def stable(arr, t):
    w = Window()
    max_stable = 0
    while w.r < len(arr):
        if can_expand(arr, t, w):
            w.queue.push(arr[w.r])
            w.r+=1
            max_stable = max(max_stable, w.r-w.l)
        elif w.r == w.l:
            w.r+=1
            w.l+=1
        else:
            max_stable = max(max_stable, w.r-w.l)
            w.l+=1
            w.queue.pop()
    return max_stable

temperatures = [12, 16, 14, 15, 13, 17]
t = 3
Output = 4
#The longest stable period is [16, 14, 15, 13].

# temperatures = [30, 10]
# t = 100
# Output = 2

# temperatures = [30, 10]
# t = 1
# Output = 1


ans = stable(temperatures, t)
print(ans)





