def search(root, node):
    if not root:
        return False, False
    if root == node:
        return True
    return search(root.left) or search(root.right)

