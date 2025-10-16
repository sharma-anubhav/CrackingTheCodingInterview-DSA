def kbst(root, k):
    count = 0
    def inorder(root, k):
        nonlocal count
        if not root:
            return None
        
        l = inorder(root.left, k)
        if l:
            return l
        if count==k:
            return root.val
        else:
            count+=1
        return inorder(root.right, k)
    return inorder(root, k)

# SImpler version without early stops
def kbst_2(root, k):
    count = 0
    ans = None
    def inorder(root, k):
        nonlocal count
        nonlocal ans
        if not root:
            return None
        
        inorder(root.left, k)
        if count==k:
            ans = root.val
        count+=1
        inorder(root.right, k)
    inorder(root, k)
    return ans


        
        

       
            

