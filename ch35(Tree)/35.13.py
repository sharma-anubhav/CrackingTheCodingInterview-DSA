import math

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_closest(root, val):
    if not root:
        return -1*(float("inf"))
    mtn = float('inf')
    mval = None
    cur = root
    while cur:
        if cur.val == val:
            return val
        if cur.val > val:
            diff = abs(val-cur.val)
            if diff<mtn:
                mtn = diff
                mval= cur.val
            if diff == mtn and cur.val<mval:
                mval = cur.val
            cur = cur.left
        elif cur.val < val:
            diff = abs(val-cur.val)
            if diff<mtn:
                mtn = diff
                mval= cur.val
            if diff == mtn and cur.val<mval:
                mval = cur.val
            cur = cur.right
    return mval



def run_tests():
  # Test 1
  root1 = Node(5,
               Node(2,
                    None,
                    Node(4)),
               Node(9,
                    Node(9,
                         None,
                         Node(9)),
                    Node(11)))

  # Test 2: Empty tree
  root2 = None

  # Test 3: Single node
  root3 = Node(1)

  # Test 4: Perfect BST
  root4 = Node(4,
               Node(2,
                    Node(1),
                    Node(3)),
               Node(6,
                    Node(5),
                    Node(7)))

  # Test 5: Unbalanced BST
  root5 = Node(5,
               Node(3,
                    Node(2,
                         Node(1),
                         None),
                    Node(4)),
               None)

  # Example from the book
  root6 = Node(8,
               Node(6,
                    Node(5,
                         Node(2),
                         Node(6)),
                    Node(8,
                         Node(8),
                         Node(8))),
               Node(12,
                    Node(10,
                         Node(9),
                         None),
                    None))
  tests = [
      (root1, 6, 5),  # Closest to 6 is 5
      (root1, 9, 9),  # Exact match
      (root1, 3, 2),  # Closest to 3 is 2
      (root1, 4, 4),  # Exact match
      (root2, 1, -math.inf),  # Empty tree
      (root3, 1, 1),  # Single node, exact match
      (root3, 2, 1),  # Single node, closest is 1
      (root4, 5, 5),  # Perfect BST, exact match
      (root4, 8, 7),  # Perfect BST, closest is 7
      (root5, 1, 1),  # Unbalanced BST, exact match at leaf
      (root5, 5, 5),  # Unbalanced BST, exact match at root
      (root5, 6, 5),  # Unbalanced BST, closest is 5
      (root6, 9, 9),
      (root6, 13, 12),
      (root6, 1, 2),
      (root6, 8, 8),
      (root6, 6, 6),
      (root6, 7, 6),
      (root6, 11, 10),
      (root6, 4, 5),
  ]

  for i, (root, target, want) in enumerate(tests):
    got = find_closest(root, target)
    print(got)
    assert got == want, f"\nfind_closest(root{
        i + 1}, {target}): got: {got}, want: {want}\n"

run_tests()