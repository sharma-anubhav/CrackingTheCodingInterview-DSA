def expression_tree(root):
    if not root:
        return
    
    if root.kind == "num":
        return root.num
    
    if root.kind == "sum":
        compute = 0
        for child in root.children:
            compute+=expression_tree(child)
    if root.kind == "mul":
        compute = 1
        for child in root.children:
            compute*=expression_tree(child)
    if root.kind == "max":
        compute = -1*float("inf")
        for child in root.children:
            compute = max(compute, expression_tree(child))
    if root.kind == "min":
        compute = float("inf")
        for child in root.children:
            compute = min(compute, expression_tree(child))
    return compute