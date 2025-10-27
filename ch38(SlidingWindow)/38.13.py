#Check book. Good Question but time consuming.

"""
My approaach would be to implement fixed k size searching. then search from n-1 then n-2 going down.
This can be optimized by using binary search instead of going down by 1.
"""
s = "murmurmur"

class Window:
    def __init__(self, l =0 , r =0):
        self.l  = l
        self.r = r 
        self.s = set() 


def is_repeated(word, k):
    print(f"Validating for {k}")
    w = Window()
    while w.r < len(word):
        w.r +=1
        if w.r-w.l == k:
            new_s = word[w.l:w.r]
            if new_s in w.s:
                return True
            w.s.add(new_s)
            w.l+=1
    return False

def is_before(word, k):
    if is_repeated(word, k):
        return True
    return False

def max_repeated_substring(word):
    n = len(word)
    l, r = 1, n-1
    while r-l > 1:
        mid = (l+r)//2
        if is_before(word, mid):
            l = mid
        else:
            r = mid
    return l

s = "murmurmur"
ans = max_repeated_substring(s)
print(ans)
