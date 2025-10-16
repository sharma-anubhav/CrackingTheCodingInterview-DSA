from collections import deque


def depth(root, val):
    def helper(root, val, depth):
        if not root:
            return None
        if root.val == val:
            return depth
        left = helper(root.left, val, depth+1)
        if left:
            return left
        right = helper(root.right, val, depth+1)
        if right:
            return right
        return None        
    return helper(root, val, 0)

def depth(root, node):
    if not root:
        return -1
    
    q = deque()
    q.append((root, 0))

    while q:
        node, depth = q.popleft()
        if node == root:
            return depth
        if node.left:
            q.append((node.left, depth+1))
        if node.right:
            q.append((node.right, depth+1))
    return -1
