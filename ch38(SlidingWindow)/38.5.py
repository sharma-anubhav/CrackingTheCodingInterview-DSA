"""
Given an array, sales, where sales[i] is the number of sales on the i-th day, find the most consecutive days with no bad days.
A bad day is a day with fewer than 10 sales.
"""

sales = [0, 14, 7, 12, 10, 20]
# Output: 3. The subarray [12, 10, 20] has no bad days.

def cangrow(sales):
    if sales >= 10:
        return True
    return False

def bad(sales):
    l, r = 0,0
    mx = 0
    max_till_now = 0
    max_l = -1
    max_r = -1
    while r<len(sales):
        if cangrow(sales[r]):
            r+=1
            max_till_now+=1
            if max_till_now > mx:
                mx = max_till_now
                max_l = l
                max_r = r
        else:
            r+=1
            l=r
            max_till_now=0
    print(mx, max_l, max_r)
    return mx

bad(sales)