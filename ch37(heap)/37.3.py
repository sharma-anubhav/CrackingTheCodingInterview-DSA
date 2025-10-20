from heapq import heappush, heappop


class TopSongs:
    def __init__(self, k):
        self.heap = []
        self.k = k
    
    def register_plays(self, title, plays):
        heappush(self.heap, (-plays, title)) ## We only need to maintain topk
        if len(self.heap) > self.k:
            heappop(self.heap)
            
    def top_k(self):
        top_songs = []
        for _, title in self.min_heap:
            top_songs.append(title)
        return top_songs
    # def top_k(self):
    #     ans = []
    #     k = min(self.k, len(self.heap))
    #     for i in range(k):
    #         _, song = heappop(self.heap)
    #         ans.append(song)
    #     print(ans)

s = TopSongs(3)
s.register_plays("Boolean Rhapsody", 193)
s.register_plays("Coding In The Deep", 146)
s.top_k()  # Returns ["Coding In The Deep", "Boolean Rhapsody"]
s.register_plays("All About That Base Case", 291)
s.register_plays("Here Comes The Bug", 223)
s.register_plays("Oops! I Broke Prod Again", 274)
s.register_plays("All the Single Brackets", 132)
s.top_k()  # Returns ["All About That Base Case", "Here Comes The Bug", "Oops! I Broke Prod Again"]