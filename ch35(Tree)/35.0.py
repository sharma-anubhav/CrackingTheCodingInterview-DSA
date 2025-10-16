dia = 0
def diameter(root):
    def helper(root):
        global dia
        if not root:
            return 0
        
        ll = helper(root.left) # helper returns height n
        rl = helper(root.right)
        dia = max(dia, ll+rl)
        return 1+max(ll, rl)
    helper(root)
    return dia

# extend this to include actual path.

# Another idea is to do dfs/bfs get any node at max depth and with that node as root, do another node and get depth.
