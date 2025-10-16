from collections import defaultdict, deque

def protection(root):
    if not root:
        return None
    
    protection_map = defaultdict(float('inf'))
    nodes_in_level = defaultdict(int)
    node_to_index = {}

    q = deque()
    q.append([root, 0])

    while q:
        node, depth = q.popleft()
        nodes_in_level[depth]+=1
        node_to_index[node] = nodes_in_level[depth]-1

        protection_map[node] = min(protection_map[node], depth)
        protection_map[node] = min(protection_map[node], node_to_index[node])

        if node.left:
            q.append([node.left, depth+1])
        if node.right:
            q.append([node.right, depth+1])
    
    def height(node, depth):
        if not node:
            return 0
        height = 1+max(height(node.left, depth+1), height(node.right, depth+1))
        protection_map[node] = min(protection_map[node], height)
        protection_map[node] = min(protection_map[node], nodes_in_level[depth] - node_to_index[node])
        return height
    
    height(root, 0)
    return max(protection_map.values())

def run_tests():

  # Example from the book
  root1 = Node(1,
               Node(2,
                    Node(3,
                         Node(4,
                              Node(5, Node(6)),
                              Node(7, Node(8), Node(9))),
                         Node(10, Node(11))),
                    Node(12,
                         Node(13,
                              Node(14,
                                   Node(15),
                                   Node(16))))),
               Node(17,
                    Node(18, Node(
                        19, Node(20, Node(21)))),
                    Node(22, Node(23, Node(24, Node(25))))))

  def perfect_tree(height):
    if height == 1:
      return Node(1)
    return Node(1, perfect_tree(height - 1), perfect_tree(height - 1))

  tests = [
      (root1, 2),  # Book example (Example 1)
      (Node(1), 0),  # Single node (Example 2)
      # Linear tree (Example 3)
      (Node(1, Node(2, Node(3, Node(4)))), 0),
      (perfect_tree(1), 0),  # Perfect binary tree (Example 4)
      (perfect_tree(2), 0),  # Perfect binary tree (Example 5)
      (perfect_tree(3), 0),  # Perfect binary tree (Example 6)
      (perfect_tree(4), 1),  # Perfect binary tree (Example 7)
      (perfect_tree(5), 1),  # Perfect binary tree (Example 8)
      (perfect_tree(6), 2),  # Perfect binary tree (Example 9)
      (perfect_tree(7), 3),  # Perfect binary tree (Example 10)
      (perfect_tree(8), 3),  # Perfect binary tree (Example 11)
      (perfect_tree(9), 4),  # Perfect binary tree (Example 12)
  ]

  for i, (root, want) in enumerate(tests):
    got = most_protected_node(root)
    assert got == want, f"\nExample {
        i + 1}: most_protected_node(): got: {got}, want: {want}\n"


run_tests()