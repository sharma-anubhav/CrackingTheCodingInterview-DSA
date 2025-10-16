from re import M


arr1 = [2, 3, 3, 4, 5, 7]
arr2 = [3, 3, 9]
arr3 = [3, 3, 9]
# Output: [2, 3, 4, 5, 7, 9]

def threewaymerge(a1, a2, a3):
    ans = []
    l1, l2, l3 = 0,0,0
    
    while l1<len(a1) or l2 < len(a2) or l3 < len(a3):
        mn = float("inf")
        if l1<len(a1):
            mn = min(mn, a1[l1])
        if l2<len(a2):
            mn = min(mn, a2[l2])
        if l3<len(a3):
            mn = min(mn, a3[l3])
        
        if l1<len(a1) and a1[l1] == mn:
            l1+=1
        if l2<len(a2) and a2[l2] == mn:
            l2+=1
        if l3<len(a3) and a3[l3] == mn:
            l3+=1 
        if not ans or ans[-1]!=mn:
            ans.append(mn)
    return ans

print(threewaymerge(arr1, arr2, arr3))








