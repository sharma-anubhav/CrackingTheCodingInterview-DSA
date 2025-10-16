def overlap(root):
    visited = {}
    def helper(root, x, y):
        if not root:
            return
        if (x, y) not in visited.keys():
            visited[(x,y)]=1
        else:
            visited[(x,y)]+=1
        overlap(root.left, x+1,y)
        overlap(root.right,x, y+1)
    helper(root, 0,0)
    return max(visited.values())
