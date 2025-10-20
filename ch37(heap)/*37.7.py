from collections import defaultdict
from heapq import heapify, heappop, heappush


songs = [["Coding In The Deep", "A Dell"],
         ["Hello World", "A Dell"],
         ["Someone Like GNU", "A Dell"],
         ["Make You Read My Logs", "A Dell"],
         ["Hey Queue", "The Bugs"],
         ["Here Comes the Bug", "The Bugs"],
         ["Merge Together", "The Bugs"],
         ["Dirty Data", "Michael JSON"],
         ["Man in the Middle Attack", "Michael JSON"],
         ["Ring Of Firewalls", "Johnny Cache"]]

def playlist(s):
    songs = defaultdict(list)
    counter = defaultdict(int)
    for song, artist in s:
        counter[artist]+=1
        songs[artist].append(song)
    
    ans = []
    last_artist = None
    h = [(-count, artist) for artist, count in counter.items()]
    heapify(h)
    while h:
        c, a = heappop(h)
        if a != last_artist or not ans:
            ans.append((songs[a][-1*c-1], a))
            last_artist = a
            c = c+1
            if c:
                heappush(h, (c, a)) 
        else:
            if len(h) == 1:
                return []
            else:
                sc, sa = heappop(h)
                ans.append((songs[sa][-1*sc-1], sa))
                last_artist = sa
                sc = sc+1
                if sc:
                    heappush(h, (sc, sa))
                heappush(h, (c, a))
    return ans

ans = playlist(songs)
for song in ans:
    print(song)