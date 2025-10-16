from collections import deque
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def most_prolific_level(root):

    if not root:
        return -1
    if not root.left and not root.right:
        return -1

    q = deque()
    q.append("Bitch")
    q.append(root)
    nodes = 0
    children = 0
    cur_depth = -1
    fucker = (cur_depth,-1)

    while q:
        ele = q.popleft()

        if ele == "Bitch":
            if cur_depth != -1 and children/nodes > fucker[1]:
                fucker = (cur_depth, children/nodes)
            nodes, children = 0,0
            cur_depth+=1
            if q:
                q.append("Bitch")
        else:
            nodes+=1
            if ele.left:
                children+=1
                q.append(ele.left)
            if ele.right:
                children+=1
                q.append(ele.right)
    return fucker[0]

def most_prolific_level_2(root):

    if not root:
        return -1
    if not root.left and not root.right:
        return -1

    q = deque()
    q.append((root, 0))
    nodes = 0
    children = 0
    cur_depth = 0
    most_prolific = (0,0)

    while q:
        ele, depth = q.popleft()
        if depth!=cur_depth:
            if children/nodes > most_prolific[1]:
                most_prolific = (cur_depth, children/nodes)
            nodes, children = 0,0
            cur_depth = depth
        nodes+=1
        if ele.left:
            children+=1
            q.append((ele.left, depth+1))
        if ele.right:
            children+=1
            q.append((ele.right, depth+1))
    ## LAST LAYER CHECK
    if nodes > 0 and children / nodes > most_prolific[1]:
        most_prolific = (cur_depth, children / nodes)
    
    return most_prolific[0]
            
        
def run_tests():
  # Test 1
  root1 = Node(5,
               Node(2,
                    None,
                    Node(6)),
               Node(9,
                    Node(9,
                         None,
                         Node(1)),
                    Node(8)))

  # Test 2: Empty tree
  root2 = None

  # Test 3: Single node
  root3 = Node(1)

  # Test 4: Perfect binary tree
  root4 = Node(1,
               Node(2,
                    Node(4),
                    Node(5)),
               Node(3,
                    Node(6),
                    Node(7)))

  # Test 5: Unbalanced tree
  root5 = Node(1,
               Node(2,
                    Node(4,
                         Node(8),
                         Node(9)),
                    Node(5)),
               Node(3))

  # Test 6: Example from the book
  root6 = Node(1,
               Node(2,
                    Node(4,
                         Node(8),
                         Node(9)),
                    Node(5,
                         None,
                         Node(11))),
               None)
  # Test 7
  root7 = Node(1,
               Node(2,
                    Node(4,
                         Node(8),
                         Node(9))))
  tests = [
      (root1, 0),
      (root2, -1),  # Empty tree
      (root3, -1),  # Single node has no parent-child relationships
      # Level 0->1 has prolificness 2, level 1->2 also 2 but we take smallest level
      (root4, 0),
      (root5, 0),
      (root6, 1),
      (root7, 2),
  ]

  for i, (root, want) in enumerate(tests):
    got = most_prolific_level_2(root)
    print(got)
    assert got == want, f"\nmost_prolific_level(root{
        i + 1}): got: {got}, want: {want}\n"
    
run_tests()