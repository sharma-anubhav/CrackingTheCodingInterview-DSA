## GOOD QUESITON. 
# A lot of the height ideas do not work. We cannot propogate max at below directly upwards.
# what we do is, if current.val == depth only then we prpoogate max below it otherwise its 0. But we store in a global what is the max we have seen till now.
# global variable becomes a necessity.
def aligned(root):
    mx = 0
    def dfs(root, depth):
        nonlocal mx
        if not root:
            return 0
        if root.val == depth:
            l = 1+max(dfs(root.left, depth+1), dfs(root.right, depth+1))
            mx = max(mx, l)
            return l
        else:
            return 0
    dfs(root, 0)
    return mx



        
            
        