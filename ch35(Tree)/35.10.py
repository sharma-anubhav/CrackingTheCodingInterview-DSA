from collections import deque
import enum
from re import L

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def switch(reverse):
    return not reverse

# def zig_zag_order(root):
#     if not root:
#         return []

#     levels = []
#     DELIMITER = "#"
#     q = deque()
#     q.append(root)
#     q.append(DELIMITER)
    
#     reverse = False
#     level = []
   
#     while q:
#         ele = q.popleft()
#         if ele == DELIMITER:
#             if reverse:
#                 levels.append(level[::-1])
#             else:
#                 levels.append(level)
#             reverse = switch(reverse)
#             level = []
#             if q:
#                 q.append(DELIMITER)
#         else:
#             level.append(ele)  
#             if ele.left:
#                 q.append(ele.left)
#             if ele.right:
#                 q.append(ele.right)

#     return [node for level in levels for node in level]



def zig_zag_order(root):
    if not root:
        return []

    levels = []
    q = deque()
    q.append((root, 0))
    level = []
    cur_depth = 0

    while q:
        ele, depth = q.popleft()
        if depth!=cur_depth:
            levels.append(level[::-1] if cur_depth%2 != 0 else level)
            level = []
            cur_depth=depth
        level.append(ele)  
        if ele.left:
            q.append((ele.left, depth+1))
        if ele.right:
            q.append((ele.right, depth+1))

    if level:
        levels.append(level[::-1] if cur_depth % 2 != 0 else level)
        
    return [node for level in levels for node in level]

    
# Wrong approach. You cannot switch directions on DELIMITER. ITS LOGICALLY WRONG BUT EASY TO JUMP TO
# def zig_zag_order(root):
#     res = []
#     DELIMITER = "#"
#     if not root:
#         return 
    
#     q = deque()
#     direction = "L"
#     q.append(DELIMITER)
#     q.append(root)

#     while q:
#         ele = q.popleft()
#         if ele == DELIMITER:
#             direction = switch(direction)
#             if q:
#                 q.append(DELIMITER)
#         else:
#             res.append(ele)
#             if direction == "L":
#                 if ele.left:
#                     q.append(ele.left)
#                 if ele.right:
#                     q.append(ele.right)
#             else:
#                 if ele.right:
#                     q.append(ele.right)
#                 if ele.left:
#                     q.append(ele.left)
#     return res



def run_tests():
  # Example 1 from the book
  root1 = Node(1)
  root1.left = Node(2)
  root1.right = Node(3)
  root1.left.left = Node(4)
  root1.left.right = Node(5)
  root1.right.left = Node(6)
  root1.right.right = Node(7)

  # Example 2 - empty tree
  root2 = None

  # Example 3 - single node
  root3 = Node(1)

  # Example 4 - unbalanced tree
  root4 = Node(1)
  root4.left = Node(2)
  root4.left.left = Node(3)
  root4.left.left.left = Node(4)

  # Example 5 - complete binary tree
  root5 = Node(1)
  root5.left = Node(2)
  root5.right = Node(3)
  root5.left.left = Node(4)
  root5.left.right = Node(5)
  root5.right.left = Node(6)
  root5.right.right = Node(7)
  root5.left.left.left = Node(8)
  root5.left.left.right = Node(9)
  root5.left.right.left = Node(10)
  root5.left.right.right = Node(11)
  root5.right.left.left = Node(12)
  root5.right.right.left = Node(14)
  root5.right.right.right = Node(15)

  tests = [
      # Example 1 - basic tree
      (root1, [1, 3, 2, 4, 5, 6, 7]),
      # Example 2 - empty tree
      (root2, []),
      # Example 3 - single node
      (root3, [1]),
      # Example 4 - unbalanced tree
      (root4, [1, 2, 3, 4]),
      # Example 5 - complete binary tree
      (root5, [1, 3, 2, 4, 5, 6, 7, 15, 14, 12, 11, 10, 9, 8])
  ]

  for i, (root, want) in enumerate(tests):
    got = [node.val for node in zig_zag_order(root)]
    assert got == want, f"\nExample {
        i + 1}: zig_zag_order({root}): got: {got}, want: {want}\n"
run_tests()