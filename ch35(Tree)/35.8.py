from collections import deque

def left_view(root):
    if not root:
        return
    q = deque()
    q.append(root)
    q.append("#")

    while q:
        ele = q.popleft()
        if ele == "#":
            if q:
                q.append("#")
                print(q[0])
        else:
            lc, rc = ele.left, ele.right
            if lc:
                q.append(lc)
            if rc:
                q.append(rc)
    return