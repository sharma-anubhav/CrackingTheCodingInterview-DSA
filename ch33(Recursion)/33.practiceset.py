# Given a 1xn tile floor. How many ways to fill that floor.

def ntiles(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return ntiles(n-1) +  ntiles(n-2)

# given a 3nx tile floor. How many ways 3x1 and 1x3:
# essentially the same
def ntiles3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    return ntiles3(n-1) +  ntiles3(n-3)   