from typing_extensions import Self


class Node:
    def __init__(self, value = None, left = None, right = None, parent = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def is_root(node):
    if node.parent:
        return True
    return False

def height(root):
    if not root:
        return 0
    return 1+max(height(root.left), height(root.right))

# Think of this as linked list. Maybe that helps
def ancestors(node):
    ancestor_list = []
    cur = node
    while cur and cur.parent:
        ancestor_list.append(cur.parent)
        cur = cur.parent
    return ancestor_list

def strict_ancestors(node):
    ancestor_list = []
    cur = node
    while cur and cur.parent:
        ancestor_list.append(cur)
        cur = cur.parent
    ancestor_list.append(cur)
    return ancestor_list

def depth(node):
    if not node:
        return 0
    if not node.parent:
        return 0
    return 1+depth(node.parent)

def lca(node1, node2):
    ## IDK basic naive one i thought. might be inefficient
    n1_ancestors = strict_ancestors(node1)
    n2_ancestors = strict_ancestors(node2)

    for ancestor in n2_ancestors:
        if ancestor in n1_ancestors:
            return ancestor.value
    return "Could Not Find"

def lca2(node1, node2):
    d1 = depth(node1)
    d2 = depth(node2)
    ## balane and move upwards in same loop
    while node1 != node2:
        if d1>d2:
            node1 = node1.parent
            d1-=1
        elif d2>d1:
            node2 = node2.parent    
            d2-=1
        else:
            node2 = node2.parent
            node1 = node1.parent       
    return node1.value

def lca3(node1, node2):
    # first balance the depths. then move both upwards till node same
    # different loops. 
    d1 = depth(node1)
    d2 = depth(node2)

    while d1>d2:
        node1 = node1.parent
        d1-=1
    while d2>d1:
        node2 = node2.parent
        d2-=1
    while node1!=node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1.value



def distance(root, node):
    return
    
# Distance1 : distance lca, node1 + distance lca, node2
# we can do depth(lca)-depth(node1) here 
def distance(node1, node2):
    lca_node = lca3(node1, node2)   # should return the node, not just lca value
    return depth(node1) + depth(node2) - 2 * depth(lca_node)

## or we can just traverse backwards and count distance from each node1, node2
def distance2(node1, node2):
    lca_node = lca3(node1, node2)
    d = 0
    while node1!=lca_node:
        node1 = node1.parent
        d+=1
    while node2!=lca_node:
        node2 = node2.parent
        d+=1
    return d



        
        




        















    