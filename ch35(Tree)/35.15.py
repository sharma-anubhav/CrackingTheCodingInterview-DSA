class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_duplicate_2(root):
    s = set()
    def helper(root):
        nonlocal s
        if not root:
            return False
        if root.val in s:
            return True
        else:
            s.add(root.val)
        return helper(root.left) or helper(root.right)
    return helper(root)

def has_duplicate(root):
    if not root:
        return False
    
    if root.left and root.left.val == root.val:
        return True
    if root.right and root.right.val == root.val:
        return True
    
    return has_duplicate(root.left) or has_duplicate(root.right)
               

## INSTEAD OF COMPLICATING WITHNEW LOGICS, this can also be turned into a in-rder traverasal 
# where if subsequent elements are same then we have True. Just like valid bst detection can also be turned into this.
def has_duplicate_3(root):
    prev = -1*float("inf")
    def helper(root):
        nonlocal prev
        if not root:
            return False
        
        l = helper(root.left)
        if l:
            return True
        if root.val == prev:
            return True
        else:
            prev = root.val
        return helper(root.right)
        
    return helper(root)

def has_duplicate_4(root):
    prev = -1*float("inf")
    ans = False
    def helper(root):
        nonlocal prev
        nonlocal ans
        if not root:
            return False
        
        helper(root.left)
        if root.val == prev:
            ans = True
        prev = root.val
        helper(root.right)
    helper(root)
    return ans 


def run_tests():
  # Example 1 - BST with duplicates
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

  # Example 4 - BST without duplicates
  root4 = Node(5,
               Node(2,
                    Node(1),
                    Node(4)),
               Node(8,
                    Node(6),
                    Node(9)))

  tests = [
      (root1, True),  # Has duplicates (9s)
      (root2, False),  # Empty tree has no duplicates
      (root3, False),  # Single node has no duplicates
      (root4, False),  # No duplicates
  ]

  for i, (root, want) in enumerate(tests):
    got = has_duplicate_3(root)
    print(got)
    assert got == want, f"\nhas_duplicate(root{
        i + 1}): got: {got}, want: {want}\n"
run_tests()