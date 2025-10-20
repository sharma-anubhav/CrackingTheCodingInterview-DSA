def contains(c1, c2):
    if c2[0][0]+c2[1] >= c1[0][0]+c1[1]:
        print(c1, c2)
        print(f"1{c2[0][0]}-{c2[1]} >= {c1[0][0]}-{c1[1]}")
        return False
    if c2[0][0]-c2[1] <= c1[0][0]-c1[1]:
        print(c1, c2)
        print(f"2{c2[0][0]}-{c2[1]} <= {c1[0][0]}-{c1[1]}")
        return False    
    if c2[0][1]+c2[1] >= c1[0][1]+c1[1]:
        print(c1, c2)
        print(f"3{c2[0][1]}-{c2[1]} >= {c1[0][1]}-{c1[1]}")
        return False
    if c2[0][1]-c2[1] <= c1[0][1]-c1[1]:
        print(c1, c2)
        print(f"4{c2[0][1]}-{c2[1]} <= {c1[0][1]}-{c1[1]}")
        return False 
    return True 

def nested_circles(circles):
    circles = sorted(circles, key = lambda x: x[1], reverse= True)
    for i in range(len(circles)-1):
        if not contains(circles[i], circles[i+1]):
            return False
    return True

circles = [((5,3),3), ((5,3),2), ((4,4),5)]
print(nested_circles(circles))