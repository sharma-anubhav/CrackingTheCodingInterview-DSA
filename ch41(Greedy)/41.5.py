meetings = [[2, 3], [1, 4], [2, 3], [3, 6], [8, 10]]


def few(meetings):
    meetings.sort(key=lambda x: x[1])
    min_e = meetings[0][1]
    count =0 
    for s,e in meetings[1:]:
        if s >= min_e:
            count+=1
            min_e = e
    return count

print(few(meetings))
