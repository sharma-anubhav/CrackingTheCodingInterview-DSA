class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        sefl.left = left
        self.right = right

def is_leaf(node):
    if not node:
        return False
    return not node.left and not node.right

def children(node):
    if not node:
        return []
    cs = []
    if node.left:
        cs.append(node.left)
    if node.right:
        cs.append(node.right)
    return cs

def grandchildren(node):
    if not node:
        return []
    gc = []
    gc.extend(children(node.left))
    gc.extend(children(node.right))
    return gc

## RECALL FROM THE RECURSION CHAPTER. Our aim is to move towards the base case in the subterms
## base case is that the node doesnt exist anymore.
## hence how can we acheice that? we tavel downwards towards leaf. making subtree small till it disappears
def sizeR(node):
    if not node:
        return 0
    return 1+size(node.left)+size(node.right)

def sizeI(node):
    if not node:
        return 0
    ## DFS
    s = []
    s.append(node)
    cnt = 1
    while s:
        ele = s.pop()
        if ele.left:
            s.append(ele.left)
            cnt+=1
        if ele.right:
            s.append(ele.right)
            cnt+=1
    return cnt


## similarly for height, base case is that we know height is 0 if node does not exist.
## Hence we move downards and collect & process the subproblems to give the result.
def height(root):
    if not root:
        return 0
    return 1+max(height(root.left), height(root.right)) # <---- we collect and accumulate/process from subrecursive calls to the top

    
## IF YOU NOTICE that visibility and intuitiveness is more if you explicit DFS
## if you use recursive then hard to track what is going on.
def depth_dfs_explicit(root, node):
    """
    We modify DFS to include height at every time in the stacks
    """
    if not root:
        return -1
    
    s = [(root, 0)]
    while s:
        ele, cur_depth = s.pop()
        if ele == node:
            return cur_depth
        if ele.right:   
            s.append((ele.right, cur_depth+1))
        if ele.left:
            s.append((ele.left, cur_depth+1))
    return -1

# Recursive Solution
def depth_dfs_recursive_count_down(root, node, height):
    if not root:
        return None
    if root == node:
        return height
    l_check = depth_dfs_recursive_count_down(root.left, node, height+1)
    r_check = depth_dfs_recursive_count_down(root.right, node, height+1)

    if l_check:
        return l_check # <---- we collect and propogate directly to the top.
    if r_check:
        return r_check
    return None

## ACCUMULATE LOGIC
def depth_dfs_recursive_count_up(root, node):
    if not root:
        return None
    
    if root == node:
        return 0  # depth of the node itself
    
    left = depth_dfs_recursive_count_up(root.left, node)
    if left is not None:
        return left + 1   # accumulate on the way back up
    
    right = depth_dfs_recursive_count_up(root.right, node)
    if right is not None:
        return right + 1
    
    return None

# BFS Solution (since its a searching task we can use BFS/DFS)
def depth_bfs(root, node):
    """
    Can be easily done but we usually stick to recusrive solitions/DFS for these.
    """
    return
    

def ancestors(root, node):
    """
    So this now turns to a modified DFS searching problem.
    the only difference is while progating backwards, we add to the ancesstors list which are a part.
    in some questions we might need to propogate additinal info.
    """
    ancestors = []
    def ancestors_helper(root, node, ancestors):
        if not root:
            return

        if root == node:
            ancestors.append(root)
            return True
        
        l_check = ancestors_helper(root.left, node, ancestors)
        if l_check:
            ancestors.append(root)
            return True
        
        r_check = ancestors_helper(root.right, node, ancestors)
        if r_check:
            ancestors.append(root)
            return True
        return False

def lca(root, node1, node2):
    """
    Highly ineficient but simple idea:
    Check if both nodes are under root. 
    Then move to node.left. if both under node.left then that is where lca is.
    otherwise node.right.
    Keep going untill you find.
    """
    def contains(root, node1):
        if not root or not node1:
            return False
        if root == node1:
            return True
        return contains(root.left, node1) or contains(root.right, node1)

    if not root:
        return None

    if root == node1 or root == node2:
        return root

    p_in_left = contains(root.left, node1)
    q_in_left = contains(root.left, node2)

    if p_in_left and q_in_left:
        return lca(root.left, node1, node2)

    p_in_right = contains(root.right, node1)
    q_in_right = contains(root.right, node2)

    if p_in_right and q_in_right:
        return lca(root.right, node1, node2)

    return root

## EFFICIENT BUT YOU WILL HAVE TO REMEMBER THE INTUITION
def lca(root, node1, node2):
    if not root:
        return None
    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:   # node1 in one side, node2 in the other
        return root
    return left if left else right

def distance(root, node1, node2):
    lca = lca(root, node1, node2)
    d = depth_dfs_recursive_count_up(node1)-depth_dfs_recursive_count_up(lca)+depth_dfs_recursive_count_up(node2)-depth_dfs_recursive_count_up(lca)
    return d

        
















    