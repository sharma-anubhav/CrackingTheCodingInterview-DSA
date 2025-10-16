def plaindrime(s):
    return s == s[::-1]

def palindrome(s):
    l, r = 0, len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

print(palindrome("naan"))