sets = [[1, 2, 3], [3, 2, 1], [1, 4, 5], [1, 2]]
sets = [[1, 2], [3, 4], [5, 6]]
sets = [[1, 2, 3], [4, 5]]

# NAICVE APPRAOCH. but good to think about. Maybe handle edge cases better.
def intersect(sets, i):
    if i == 0:
        intersect = set(sets[1])
    else:
        intersect = set(sets[0])
    for j in range(0, len(sets)):
        if j!=i:
            intersect = intersect.intersection(set(sets[j]))
            #Optionally simulate intersection for non python
            #intersect = set([ele for ele in sets[j] if ele in intersect])
    return len(intersect)
    
def largest(sets):
    maxi = 0
    idx = -1
    for i in range(len(sets)):
        cur_max=  intersect(sets, i)
        if cur_max >maxi:
            idx = i
            maxi  = cur_max
    return idx

print(largest(sets))

## OPTIMIZE THIS BY having frequency maps of each digit Think?
## THIS IS HARD TO THINK OF OFF THE TOP OF YOUR HEAD
## So to maximize the intersection of n-1 elements, we need to keep the sets that have the max number of elements
## with atleast n-1 or n appearances. 
## Hence we can create a map of counts of digits and remove the set with least count of n-1 or n elements.