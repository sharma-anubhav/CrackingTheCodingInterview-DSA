def invert(root):
  if not root:
    return None
  root.left, root.right = invert(root.right), invert(root.left)
  return root