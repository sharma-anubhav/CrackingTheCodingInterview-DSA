jumping_points = [1803, 1861, 1863, 1865, 1920, 1929, 1941, 1964, 2001, 2021]
k = 4
max_age = 45

def timetravel(jp, k, max_age):
    jumps = [(jp[i+1]-jp[i], i) for i in range(len(jp)-1)]
    jumps.sort(key = lambda x: x[0], reverse=True)
    jump_indexes = set()
    for i in range(k):
        _, index = jumps[i]
        jump_indexes.add(index)
    
    cur_age = 0
    for i in range(len(jp)-1):
        if i not in jump_indexes:
            cur_age+=(jp[i+1]-jp[i])
    return cur_age <= max_age

print(timetravel(jumping_points, k, max_age))
