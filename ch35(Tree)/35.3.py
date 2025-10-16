def aligned_path(node):
    max_till_now = 0
    max_chain = []
    def helper(node, depth):
        nonlocal max_till_now
        nonlocal max_chain
        if not node:
            return 0, []
        if node.val != depth:
            return 0, []
        chain  = [node.val]
        
        ll, lc = helper(node.left,depth+1)
        rl, rc = helper(node.right,depth+1)
        if ll>=rl:
            chain.extend(lc)
            curl = 1+ ll
            if ll>max_till_now:
                max_till_now = ll
                max_chain = chain
        elif rl>ll:
            chain.extend(rc)
            curl = 1+ rl
            if rl>max_till_now:
                max_till_now = rl
                max_chain = chain
        return curl, chain
    return max_till_now