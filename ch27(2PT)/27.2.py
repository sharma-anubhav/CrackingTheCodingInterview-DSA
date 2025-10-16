arr = [1, 2, 2, -1]

def ktest(arr):
    sp, fp = 0,0
    ss, fs = 0,0
    while sp < len(arr) and fp < len(arr):
        ss = ss+arr[sp]
        fs = fs+arr[fp]+arr[fp+1]
        if ss > fs:
            return False
        sp+=1
        fp+=2
    return True



