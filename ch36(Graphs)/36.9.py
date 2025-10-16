V = 4

cables = [
  [0, 2],
  [1, 3],
  [0, 1],
  [1, 2]
]

def find_cc(ccs, node):
    for i, cc in enumerate(ccs):
        if node in cc:
            return i
    return -1

def first_time_all_connected(V, cables):
    ccs = []
    for i, (node, nbr) in enumerate(cables):
        inode = find_cc(ccs, node)
        inbr = find_cc(ccs, nbr)
        if inode == inbr and inode != -1:
            continue
        if inode == inbr and inode == -1:
            ccs.append({node, nbr})
            continue
        if inode != inbr and inode != -1 and inbr!= -1:
            s1 = ccs[inode]
            s2 = ccs[inbr]
            s3 = s1 | s2
            ccs.remove(s1)
            ccs.remove(s2)
            ccs.append(s3)
            if len(s3) == V:
                return i
        if inode == -1:
            ccs[inbr].add(node)
            if len(ccs[inbr]) == V:
                return i
        else:
            ccs[inode].add(nbr)
            if len(ccs[inode]) == V:
                return i
    return -1

def run_tests():
  tests = [
      # Case from picture - becomes connected after cables[2].
      (4, [(0, 2), (1, 3), (0, 1), (1, 2)], 2),
      # Edge case - never gets fully connected
      (3, [(0, 1)], -1),
      # Edge case - gets connected with final cable
      (3, [(0, 1), (1, 2)], 1),
      # Larger test case
      (5, [(0, 1), (2, 3), (1, 2), (3, 4), (0, 4)], 3),
      # Edge case - redundant cables don't affect result
      (4, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 0)], 3),
      # No edges added.
      (4, [], -1),
      # One edge added.
      (4, [(0, 1)], -1),
  ]
  for V, cables, want in tests:
    got = first_time_all_connected(V, cables)
    assert (
        got == want
    ), f"first_time_all_connected({V}, {cables}): got: {got}, want {want}\n"
    # got = first_time_all_connected_union_find(V, cables)
    # assert (
    #     got == want
    # ), f"first_time_all_connected_union_find({V}, {cables}): got: {got}, want {want}\n"

run_tests()