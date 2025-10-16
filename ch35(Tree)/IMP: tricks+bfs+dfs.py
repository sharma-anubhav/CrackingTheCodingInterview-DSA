from collections import deque
from curses import nonl
from os import path
import queue
from webbrowser import get

def dfs(root):
    if not root:
        return -1
    
    print(root.value); # Search: if root.val == target.val: return True
    dfs(root.left)
    dfs(root.right)

def bfs(root):
    if not root:
        return -1

    q = deque()
    q.append((root, 0))

    while q:
        ele, depth = q.popleft()
        print(ele, depth) # Search: if root.val == target.val: return True
        if ele.left:
            q.append((ele.left, depth+1))
        if ele.right:
            q.append((ele.right, depth+1))
    return


# using this type 1 problems like lca, ancestors, distance, becomes type2.
# BUT THIS IS NOT OPTIMAL. OPTIMAL is standard dfs for these since it can early terminate just for the one that we need.
# This is helpeful where we might have to do multiiple dfs. 
def get_parent_map(root):
    parent_map = {}
    def dfs(root, parent, depth):
        if not root:
            return 
        parent_map[root] = (parent, depth)
        dfs(root.left, root, depth+1)
        dfs(root.right, depth+1)
    dfs(root, None, 0)
    return parent_map
        
def get_parent_map(root):
    parent_map = {}
    q = deque()
    q.append((root, None, 0))

    while q:
        ele, parent, depth = q.popleft()
        parent_map[ele] = (parent, depth)
        if ele.left:
            q.append((ele.left, ele, depth+1))
        if ele.right:
            q.append((ele.right, ele, depth+1))  
    return parent_map 

## BELOW ARE COMMON TASKS WITH STANDARD, PARENT_MAP, HACK METHODS
"""
LCA: Lowest common ancestor
1: Without parent map: Standard recursive dfs with passing state
2: With Map: bring noth nodes to same depth by moving upwards till both become same.
Edge case: Think when one node is not even present in both 1/2. will either break?
"""
def lca_wihout_map(root, n1, n2):
    if not root or not n1 or not n2:
        return None

    if root == n1 or root == n2:
        return root
    
    left = lca_wihout_map(root.left, n1, n2)
    right = lca_wihout_map(root.right, n1, n2)
    if left and right:
        return root
    return left if left else right

def lca_with_map(root, n1, n2):
    m = get_parent_map(root)
    
    while m[n1][1] > m[n2][1]:
        n1 = m[n1][0]
    while m[n2][1] > m[n1][1]:
        n2 = m[n2][0]
    while n1 and n2 and n1!=n2:
        n1 = m[n1][0]
        n2 = m[n2][0]
    if n1 and n2 and n1 == n2 :
        return n1
    else:
        return None

"""
Ancestor: List of nodes in path from root->node
1: Without parent map: DFS: Search Problem: Standard recursive dfs with passing state (Launch DFS wiht root and search for n2 while saving path.)
2: With Map: Go back up till root from node since you have parents.
"""
def ancestors_without_map(root, node):
    ancestors = []
    def dfs(root, node):
        if not root:
            return False
        if root == node:
            return True
        if dfs(root.left):
            ancestors.append(root)
            return True
        if dfs(root.right):
            ancestors.append(root)
            return True
        return False
    return ancestors
    
def ancestors_with_map(root, node):
    ancestors2 = []
    parent_map = get_parent_map(node)
    if not root or not node:
        return False
    parent = parent_map[node]
    while parent:
        ancestors2.append(parent)
        parent = parent_map[parent]
    return ancestors2


"""
DISTANCE AnD PATH BOTH PASS THROUGH LCA SO WE CAN SEND STUFF UPWARDS and COLLECT.
THIS IS HIGHLY OPTIMIZED SINGLE PASS BUT IT WILL BE HARD TO IMPLEMENT.
"""

"""
Distance: Distance between n1-n2
X2X: Hack: Launch DFS from n1 as root and calculate depth of n2. #### NOT POSSIBLE SINCE TREE ONLY GO DOWNWARDS SO WE CANNOT LAUNCH THIS DFS
3: With parent map: Find LCA using map. ALreadt have depths from the map for all 3 nodes Return d(n1)+d(n2)-2*d(lca)
4: Without parent Map: BAD: Find LCA, Find Depths of lca node, n1, n2. Return d(n1)+d(n2)-2*d(lca). 
                     : Optimized: Standard Recursive that can return everything in single pass.

"""
def distance_without_map(root, n1, n2):
    # NOT NEEDED
    # BAD: implement depth, lca. then get lca and call depth for n1, n2, lca node
    # GOOD:COLLECT FROM LCA RECURSION.
    def lca(root, n1, n2, depth):
        if not root:
            return None, None, None
        if root == n1 and root == n2:
            return depth, depth, depth
        
        llca, left_n1, left_n2 = lca(root.left, n1, n2, depth+1)
        if llca:
            return llca, left_n1, left_n2
        rlca, right_n1, right_n2 = lca(root.right, n1, n2, depth+1)
        if rlca:
            return rlca, right_n1, right_n2
        
        if left_n1: d1 = left_n1
        if right_n1: d1 = right_n1
        if root == n1: d1 = (root, depth)
        else: d1 = None

        if left_n2: d2 = left_n2
        if right_n2: d2 = right_n2
        if root == n2: d2 = depth
        else: d2 = None
        
        if d1 and d2:
            return depth, d1, d2
        return None, d1, d2

    dlca, dn1, dn2 = lca(root, n1, n2, 0)
    if dlca:
        return dn1+dn2-2*dlca
    return None


def distance_with_map(root, n1, n2):
    # Get parent_map. Get lca using map. Then you have depths for lca and n1 and n2 from the map
    parent_map = get_parent_map(root)
    lca = lca_with_map(root, n1, n2)
    distance = parent_map[n1][1]-parent_map[n2][1]-2*parent_map[lca][1]
    return distance
        

def distance_with_dfs_hack(root, n1, n2):# WARNING
    # launch dfs from n1 as root and get depth. 
    #### NOT POSSIBLE SINCE TREE ONLY GO DOWNWARDS SO WE CANNOT LAUNCH THIS DFS 
    return

"""
Path: nodes in path from n1-n2
X2X: Hack: Launch DFS from n1 as root and search for n2 and save path along the way #### NOT POSSIBLE SINCE TREE ONLY GO DOWNWARDS SO WE CANNOT LAUNCH THIS DFS
3: With parent map: Go back up untill Lca and combine paths
4: Without parent Map: BAD: combine lca-n1, lca-n2
                     : Optimized: Standard Recursive that can return everything in single pass.
"""
def path_with_map(root, n1, n2):
    # move up till lca from both n1 and n2 and combine
    parent_map = {}
    def get_parent_map(root, parent, depth):
        nonlocal parent_map
        if not root:
            return
        parent_map[root] = (parent, depth)
        get_parent_map(root.left, root, depth+1)
        get_parent_map(root.right, root, depth+1)
    parent_map(root, None, 0)

    def lca_helper(root, n1, n2):
        nonlocal parent_map
        n1_path = []
        n2_path = []
        d1 = parent_map[n1][1]
        d2 = parent_map[n2][1]
        while d1 > d2:
            n1 = parent_map[n1][0]
            n1_path.append(n1)
            d1-=1
        while d2 > d1:
            n2 = parent_map[n2][0]
            n2_path.append(n2)
            d2-=1
        while n1 != n2:
            n1 = parent_map[n1][0]
            n1_path.append(n1)
            d1-=1     
            n2 = parent_map[n2][0]
            n2_path.append(n2)
            d2-=1  
        n1_path.extend(reversed(n2_path[:-1]))
        return n1_path
    return lca_helper(root, n1, n2)
    

def path_without_map(root, n1, n2):
    def dfs(node):
        if not node:
            return None, None, None 

        path_n1 = [node] if node == n1 else None
        path_n2 = [node] if node == n2 else None

        l_path, l_n1, l_n2 = dfs(node.left)
        r_path, r_n1, r_n2 = dfs(node.right)

        if l_path:
            return l_path, None, None
        if r_path:
            return r_path, None, None

        if l_n1: path_n1 = [node] + l_n1
        if r_n1: path_n1 = [node] + r_n1
        if l_n2: path_n2 = [node] + l_n2
        if r_n2: path_n2 = [node] + r_n2

        if path_n1 and path_n2:
            full_path = path_n1 + path_n2[::-1][1:]  
            return full_path, None, None

        return None, path_n1, path_n2

    path, _, _ = dfs(root)
    return path


def path_with_dfs_hack(root, n1, n2): # WARNING
    # launch search from n1 as root till n2 
    # #### NOT POSSIBLE SINCE TREE ONLY GO DOWNWARDS SO WE CANNOT LAUNCH THIS DFS
    return
