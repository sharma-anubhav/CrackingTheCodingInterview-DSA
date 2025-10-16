s = "((a+b)*[c-d]-{e/f})"
brackets = ["()", "[]", "{}"]
# Output: True


def custom_brackets(s, brackets):
    opening2closing = {bracket[0]:bracket[1] for bracket in brackets}
    closing2opening = {bracket[1]:bracket[0] for bracket in brackets}
    stack = []

    for c in s:
        if c in opening2closing.keys():
            stack.append(c)
        if c in closing2opening.keys():
            if not stack or stack[-1]!=closing2opening[c]:
                return False
            if stack and stack[-1]==closing2opening[c]:
                stack.pop()
    if len(stack)>0:
        return False
    return True