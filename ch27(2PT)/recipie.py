# There are patterns/variations. Read and practice all 

# Start Opposite:
# 	Left/right 
# Both start same side:
# 	Slow/fast
# 	2 pointers, each in different list (merge sort types)
# 	Seeker writer (IMP)


# RECEIPIE 1 (left right):
def fun(s):
    l, r = 0, len(s)-1 
    while l<r:           #<---- Might need <= in some scenarios
        if s[l]!=s[r]: 
            return False
        l+=1
        r-=1
    return True

# RECEPIE 2: (Same side)
def sorted_intersection(a1, a2):
    l1, l2 = 0,0
    ans = []
    while l1<len(a1) and l2 < len(a2): #<<<---- We usually want and since if one is at the edge we should not overflow
        if a1[l1]==a2[l2]:
            ans.append(a1[l1])
            l1+=1
            l2+=1
        elif a2[l2] < a1[l1]:
            l2+=1 
        elif a1[l1] < a2[l2]:
            l1+=1             
    return ans

# RECEPIE 3: (Same side)
def partiysort(arr):
    s,w = 0,0
    while s < len(arr) and w < len(arr):
        if arr[s]%2 == 0:
            arr[w], arr[s] = arr[s], arr[w]
            s+=1
            w+=1. # <--- move writer+seeker when found 
        else:
            s+=1  # <----- Move seeker if not
    return arr
