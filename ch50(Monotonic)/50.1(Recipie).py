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
    
mq = MaxMinQueue()
mq.push(3)
mq.push(1)
mq.push(5)
print(mq.max())  # 5
mq.pop()
print(mq.max())  # 5
mq.pop()
print(mq.max())  # 5
mq.pop()
print(mq.max())  # None
