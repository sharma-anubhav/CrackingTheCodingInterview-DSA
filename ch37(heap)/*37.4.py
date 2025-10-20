from collections import defaultdict
from heapq import heappush, heappop


class TopSongs:
    def __init__(self, k):
        self.heap = []
        self.k = k
        self.counter = defaultdict(int)
    
    def register_plays(self, title, plays):
        plays = plays
        if title in self.counter.keys():
            plays = self.counter[title]+plays
        self.counter[title]=plays
        heappush(self.heap, (-plays, title))
        
    def top_k(self):
        ans = []
        while len(ans)<self.k and self.heap:
            cnt, song = heappop(self.heap)
            if -1*cnt == self.counter[song]:
                ans.append(song)
        print(ans)
        # MIGHT HAVE TO ADD BACK SO. WE ARE LITERALLY POPPING THEM OFF AND NEVER ADDING THEM BACK

s = TopSongs(3)
s.register_plays("Boolean Rhapsody", 100)
s.register_plays("Boolean Rhapsody", 193)  # Total 293
s.register_plays("Coding In The Deep", 75)
s.register_plays("Coding In The Deep", 75)  # Total 150
s.register_plays("All About That Base Case", 200)
s.register_plays("All About That Base Case", 90)  # Total 290
s.register_plays("All About That Base Case", 1)   # Total 291
s.register_plays("Here Comes The Bug", 223)
s.register_plays("Oops! I Broke Prod Again", 274)
s.register_plays("All the Single Brackets", 132)
s.top_k()  # Returns ["All About That Base Case", "Boolean Rhapsody", "Oops! I Broke Prod Again"]