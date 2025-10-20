from heapq import heapify, heappop


songs = [["All the Single Brackets", 132],
         ["Oops! I Broke Prod Again", 274],
         ["Coding In The Deep", 146],
         ["Boolean Rhapsody", 193],
         ["Here Comes The Bug", 291],
         ["All About That Base Case", 291]]
k = 3

def topksongs(songs, k):
    songs = [(-num, song) for song, num in songs]
    heapify(songs)
    ans = []
    for i in range(k):
        _, song = heappop(songs)
        ans.append(song)
    return ans

ans = topksongs(songs, k)
print(ans)