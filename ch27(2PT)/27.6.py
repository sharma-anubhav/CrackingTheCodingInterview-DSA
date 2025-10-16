def merge(a1, a2):
    l1, l2 = 0,0
    ans = []
    while l1<len(a1) and l2 < len(a2):
        if a1[l1]<=a2[l2]:
            ans.append(a1[l1])
            l1+=1
        elif a2[l2] < a1[l1]:
            ans.append(a2[l2])
            l2+=1           
    while l1<len(a1):
        ans.append(a1[l1])
        l1+=1  
    while l2<len(a2):
        ans.append(a2[l2])
        l2+=1    
    return ans
print(merge(arr1, arr2))