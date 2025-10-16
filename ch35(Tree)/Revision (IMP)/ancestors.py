# if you notice carefully this is same as search. Just if search is True in a subtree we append.
def ancestors(root, node):
    ancestor_list = []
    def helper(root, node):
        if not root:
            return 
        
        if root == node:
            return True
        
        left = helper(root.left, node)
        if left:
            ancestor_list.append(root)
            return True
        right =  helper(root.right, node)
        if right:
            ancestor_list.append(root)
            return True
        return False
    helper(root, node)
    return ancestor_list