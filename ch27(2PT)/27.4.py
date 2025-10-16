s = "Bob wondered, 'Now, Bob?'"
# Output: true

def palindrome(s):
    l, r = 0, len(s)-1
    while l<r:
        if not s[l].isalpha():
            l+=1
        elif not s[r].isalpha():
            r-=1
        else:
            if s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
    return True
print(palindrome(s))