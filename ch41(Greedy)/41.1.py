arr = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 9]]

def dontoverlap(intervals):
    intervals.sort(key = lambda x: x[1])
    chosen = []
    for s, e in intervals:
        if len(chosen)==0 or chosen[-1][1] < e:
            chosen.append([s, e])
    return chosen