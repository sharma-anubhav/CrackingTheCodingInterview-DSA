class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def is_bst(root):
    def helper(root):
        if not root:
            return (True, 1*float("inf"), -1*float("inf"))
        
        l, l_min, l_max = helper(root.left) 
        r, r_min, r_max = helper(root.right)

        if l and r and root.val >= l_max and root.val <= r_min:
            return (True, min(l_min, root.val), max(r_max, root.val))
        return (False, -1, -1)
    valid, _, _ = helper(root)
    return valid

def is_bst_2(root):
    prev = -1*float("inf")
    def helper(root):
        nonlocal prev
        if not root:
            return True
        l = helper(root.left)
        if not l:
            return False
        if(root.val) >= prev:
            prev = root.val
        else:
            return False
        return helper(root.right)

    return helper(root)

# NO EARLY STOPPING. Just traverse and check in the end
def is_bst_3(root):
    prev = -1*float("inf")
    ans = True
    def helper(root):
        nonlocal prev
        nonlocal ans
        if not root:
            return True
        helper(root.left)
        if(root.val) < prev:
            ans = False
        helper(root.right)
    helper(root)
    return ans




def run_tests():
  # Example 1 - valid BST
  root1 = Node(5,
               Node(2,
                    None,
                    Node(4)),
               Node(9,
                    Node(9,
                         None,
                         Node(9)),
                    Node(11)))

  # Example 2 - empty tree
  root2 = None

  # Example 3 - single node
  root3 = Node(1)

  # Example 4 - invalid BST (right child smaller than parent)
  root4 = Node(5,
               Node(2),
               Node(4))

  # Example 5 - invalid BST (left child larger than parent)
  root5 = Node(5,
               Node(6),
               Node(7))

  tests = [
      (root1, True),  # Valid BST
      (root2, True),  # Empty tree is valid
      (root3, True),  # Single node is valid
      (root4, False),  # Invalid - right child smaller than parent
      (root5, False),  # Invalid - left child larger than parent
  ]

  for i, (root, want) in enumerate(tests):
    got = is_bst_2(root)
    print(got)
    assert got == want, f"\nis_bst(root{i + 1}): got: {got}, want: {want}\n"
run_tests()