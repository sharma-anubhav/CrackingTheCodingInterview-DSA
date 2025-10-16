def distance(root, node1, node2):    
    return depth(node1)+depth(node2)-2*(depth(lca))

# HOW DO WE DO THIS IN A SINGLE PASS
def lca_helper_for_distance(root, node1, node2, depth):
    if not root:
        return (None, depth), (False,-1), (False ,-1)

    if root == node1 and root == node2:
        return (root, depth), (True, depth), (True, depth)

    lca_l, n1_l, n2_l = lca_helper_for_distance(root.left, node1, node2, depth+1)
    if lca_l and n1_l[0] and n2_l[0]:
        return lca_l, n1_l, n2_l

    lca_r, n1_r, n2_r = lca_helper_for_distance(root.right, node1, node2, depth+1)
    if lca_r and n1_r[0] and n2_r[0]:
        return lca_r, n1_r, n2_r

    found_n1 = n1_l[0] or n1_r[0] or (root == node1)
    found_n2 = n2_l[0] or n2_r[0] or (root == node2)

    if n1_l[0]:
        final_n1 = n1_l
    elif n1_r[0]:
        final_n1 = n1_r
    elif root == node1:
        final_n1 = (True, depth)
    else:
        final_n1 = (False, -1)

    if n2_l[0]:
        final_n2 = n2_l
    elif n2_r[0]:
        final_n2 = n2_r
    elif root == node2:
        final_n2 = (True, depth)
    else:
        final_n2 = (False, -1)


    if found_n1 and found_n2:
        return (root, depth), final_n1, final_n2

    return (None, depth), final_n1, final_n2