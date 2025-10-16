def roof(n):
    if n == 1:
        return 1
    return 2*roof(n-1)+1

def lego(n):
    if n == 1:
        return 1
    
    return 2*lego(n-1)+roof(n)

print(lego(1))
print(lego(2))
print(lego(3))
print(lego(4))
print(lego(5))








