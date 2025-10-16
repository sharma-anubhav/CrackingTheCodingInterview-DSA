from collections import deque
from curses import window


class ViewCounter:
    def __init__(self, window):
        self.queues = {"subscriber": deque(), "follower": deque(), "guest": deque()}
        self.window = window
    
    def join(self, t, v):
        self._remove_old(t)
        self.queues[v].append(t)
        return
    
    def get_viewers(self, t, v):
        self._remove_old(t)
        return len(self.queues[v])
    
    def _remove_old(self, t):
        for q in self.queues.values():
            while q and q[0] < t-self.window:
                q.pop()
