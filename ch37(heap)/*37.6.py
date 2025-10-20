from heapq import heappop, heappush


genres = [
  [ # Pop
    ["Coding In The Deep", 123],
    ["Someone Like GNU",    99],
    ["Hello World",         98]
  ],
  [ # Country
    ["Ring Of Firewalls",  217]
  ],
  [ # Rock
    ["Boolean Rhapsody",   184],
    ["Merge Together",     119],
    ["Hey Queue",          102]
  ]
]
k = 5

def topk_genre(genres, k):
    heaps = []
    for g in genres:
        h = []
        for song, plays in g:
            heappush(h, (-plays, song))
        heaps.append(h)
    
    for i in range(k):
        max_rn = 0
        max_i = -1
        for i, h in enumerate(heaps):
            if h and -h[0][0] > max_rn:
                max_rn = -h[0][0]
                max_i = i
        if max_i == -1:
            return 
        _, song = heappop(heaps[max_i])
        print(song)
        
topk_genre(genres, k)
            
            
