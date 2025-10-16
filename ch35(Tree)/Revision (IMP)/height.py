def height(root):
    if not root:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)
    return 1+ max(lh, rh)