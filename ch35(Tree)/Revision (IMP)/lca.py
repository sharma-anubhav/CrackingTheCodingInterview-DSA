def lca(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return True
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)
    if left and right:
        return root
    if left:
        return root.left
    if right:
        return root.right
    return None

# This LCA is special!!!!!
def lca(root, node1, node2):
    if not root:
        return None, False, False

    if root == node1 and root == node2:
        return root, True, True

    lca_l, n1_l, n2_l = lca(root.left, node1, node2)
    if lca_l and n1_l and n2_l:
        return lca_l, n1_l, n2_l

    lca_r, n1_r, n2_r = lca(root.right, node1, node2)
    if lca_r and n1_r and n2_r:
        return lca_r, n1_r, n2_r

    found_n1 = n1_l or n1_r or (root == node1)
    found_n2 = n2_l or n2_r or (root == node2)

    if found_n1 and found_n2:
        return root, True, True

    return None, found_n1, found_n2


