arr1 = [1, 2, 3]
arr2 = [1, 3, 5]
# Output: [1, 3]

def sorted_intersection(a1, a2):
    l1, l2 = 0,0
    ans = []
    while l1<len(a1) and l2 < len(a2):
        if a1[l1]==a2[l2]:
            ans.append(a1[l1])
            l1+=1
            l2+=1
        elif a2[l2] < a1[l1]:
            l2+=1 
        elif a1[l1] < a2[l2]:
            l1+=1             
    return ans
print(sorted_intersection(arr1, arr2))

