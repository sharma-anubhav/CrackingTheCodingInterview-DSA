def bst_search(root, val):
    if not root:
        return None
    
    if root.val == val:
        return root
    
    if root.val < val:
        return bst_search(root.left)
    else:
        return bst_search(root.right)

def bst_search(root, val):
    if not root:
        return None
    
    cur = root
    
    while cur:
        if cur.val == val:
            return root
        if val > cur.val:
            cur = cur.right
        else:
            cur = cur.left
    return None