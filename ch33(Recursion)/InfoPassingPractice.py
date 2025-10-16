## In recursion you can pass info downwards and collect and process info that is sent upwards by subproblems.
## these can have many variants. So this is practice for them
## Sometimes you also need global variables.

# Commonly Scenarios:
# - count_down: 
#   You send info down incrementing. No need to increment on the way up. Just process if needed or pass through.
# - count_up: 
#   Or you collect from lower results, process and increment.
# - Iteration:
#   problems where you send index downwards to instead of slicing the array/string. You usually count_up with these.
#   here along with the if arr not none base case, we check index > len(arr). Rest remains the same


# EXAMPLE 1: HEIGHT
# So here count_up appraoch is easier to understand!!!
# however both still work
from itertools import count


def height_tree_count_up(root):
    """
    Here up collect was effective
    """
    if not root:
        return 0
    l_h = height_tree_count_up(root.left)
    r_h = height_tree_count_up(root.right)
    return 1+ max(l_h, r_h)

def height_tree_count_down(root):
    """
    Sending height down and returning directly the actual final height that will be propogated up
    """
    def helper(root, height):
        if not root:
            return height  # returning 0 would be wrong and hence easy to miss.
        l_h = helper(root, height+1)
        r_h = helper(root, height+1)
        return max(l_h, r_h)
    return helper(root, 0)



# EXAMPLE 2: DEPTH: This becomes a searching problem :)
# Just retur True False first. Then replace the true's with the 0/1
# Notice that the differene is we pass stright up when found instead of adding 1 and propogating up.
# Other than that its the same.
def depth_node_count_up(root, node):
    if not root:
        return False
    if root == node: # extra condition for saecrching using DFSs.
        return 0
    l_d = depth_node_count_up(root.left, node)
    if l_d:
        return 1+l_d
    r_d = depth_node_count_up(root.right, node)
    if r_d:
        return 1+r_d
    return False

def depth_node_count_down(root, node):
    def helper(root, node, depth):
        if not root:
            return False
        if root == node:
            return depth
        l_d = depth_node_count_down(root.left, node, depth+1)
        if l_d:
            return l_d
        r_d = depth_node_count_down(root.right, node, depth+1)
        if r_d:
            return r_d
    return helper(root, node, 0)



# EXAMPLE 3: Count
def count_ele_occurance_count_up(root, node):
    if not root:
        return 0
    
    l_c = count_ele_occurance_count_up(root.left, node)
    r_c = count_ele_occurance_count_up(root.right, node)

    if root == node:
        return 1+l_c+r_c
    return l_c+r_c

## here down Propogate up FAILS!!!!!
def count_ele_occurance_count_down(root, node):
    def helper(root, node, count):
        if not root:
            return count
        if root == node:
            count+=1   
        l_c = helper(root.left, node, count)
        r_c = helper(root.right, node, count)
        return max(l_c, r_c) # <---- Thiss is wrong!!!!
    return helper(root, node, 0)

  
## Add GLOBAL variable to fix the issue
def count_ele_occurance_count_down(root, node):
    global count
    count = 0
    def helper(root, node):
        if not root:
            return
        if root == node:
            count+=1   
        l_c = helper(root.left, node)
        r_c = helper(root.right, node)
    helper(root, node, 0)      
    return count


