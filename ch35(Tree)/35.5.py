def triangle(root):
    count = 0
    def helper(root):
        nonlocal count
        if not root:
            return 0,0
        
        ll, lr = triangle(root.left)
        rl, rr = triangle(root.right)
        count += min(ll, rr)
        return 1+ll, 1+rr
    helper(root)
    return count

# Strict triangles (nothing in between)
count = 0
def triangle(root):
    global count
    if not root:
        return False, False

    cur_left, cur_right = False, False
    if root.left:
        l_analysis = triangle(root.left)
        cur_left = True
    if root.right:
        r_analysis = triangle(root.right)
        cur_right = True
    
    if cur_left and cur_right:
        if l_analysis[0] and not l_analysis[1] and r_analysis[1] and not r_analysis[0]:
            count+=1
        return True, True
    elif cur_left and not cur_right:
        if l_analysis[0] and not l_analysis[1]:
            return True, False
        return False, False
    elif cur_right and not cur_left:
        if r_analysis[1] and not r_analysis[0]:
            return False, True
        return False, False
    elif not cur_left and not cur_right:
        return False, False
            
    

    

    