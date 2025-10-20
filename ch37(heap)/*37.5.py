from collections import defaultdict
import heapq
from heapq import heappush, heappop


class PopularSongs:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.counter = {}
        self.median = None        
    
    def register_plays(self, title, plays):
        max_l = len(self.max_heap)
        min_l = len(self.min_heap)
        self.counter[title] = plays
        
        if not self.max_heap or plays <= -self.max_heap[0]:
            heappush(self.max_heap, -plays)
        else:
            heappush(self.min_heap, plays)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        
    def median_my(self):
        max_l = len(self.max_heap)
        min_l = len(self.min_heap)
        if max_l>min_l:
            return -self.max_heap[0]
        elif min_l>max_l:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
    
    def is_popular(self, song):
        if song not in self.counter:
            return False
        plays = self.counter[song]
        if plays > self.median_my():
            print("True")
            return True
        print("False")
        return False

p = PopularSongs()
p.register_plays("Boolean Rhapsody", 193)
p.is_popular("Boolean Rhapsody")                   # Returns False
p.register_plays("Coding In The Deep", 140)
p.register_plays("All the Single Brackets", 132)
p.is_popular("Boolean Rhapsody")                   # Returns True
p.is_popular("Coding In The Deep")                 # Returns False
p.is_popular("All the Single Brackets")            # Returns False
p.register_plays("All About That Base Case", 291)
p.register_plays("Oops! I Broke Prod Again", 274)
p.register_plays("Here Comes The Bug", 223)
p.is_popular("Boolean Rhapsody")                   # Returns False
p.is_popular("Here Comes The Bug")                 # Returns True