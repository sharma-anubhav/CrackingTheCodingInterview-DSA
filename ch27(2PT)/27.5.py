s = "haDrRAHd"

def reversematchcase(s):
    l, r = 0, len(s)-1
    while l < len(s) and r >=0:
        if not s[l].islower():
            l+=1
        elif not s[r].isupper():
            r-=1
        else:
            if s[l] != s[r].lower():
                return False
            l+=1
            r-=1
    return True
print(reversematchcase(s))