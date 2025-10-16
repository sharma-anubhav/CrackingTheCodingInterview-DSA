import math

points = [[0, 0], [0, 0]]
center1 = [0, 0]
center2 = [1, 1]

def distance(p1, p2):
    return math.sqrt(abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1]**2))

def minimise_penalties(points, c1, c2):
    penalties = [(distance(p, c1), distance(p, c2)) for p in points]
    penalties.sort(key= lambda x: max(x[0], x[1]), reverse=True)
    s = 0
    c1_cnt = 0
    c2_cnt = 0
    for i in range(len(points)):
        distances = penalties[i]
        if distances[0] < distances[1] and c1_cnt < len(points)/2:
            c1_cnt+=1
            s+=distances[0]
        elif distances[1] < distances[0] and c2_cnt < len(points)/2:
            c2_cnt+=1
            s+=distances[1]    
        else:
            if c1_cnt < len(points)/2:
                c1_cnt+=1
                s+=distances[0]
            else:
                c2_cnt+=1
                s+=distances[1]       
    return s             

print(minimise_penalties(points, center1, center2))

