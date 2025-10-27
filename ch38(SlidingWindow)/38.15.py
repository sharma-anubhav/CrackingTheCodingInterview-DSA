from collections import defaultdict

s1 = "helloworld"
s2 = "well"

class Window:
    def __init__(self, s2, l =0 , r =0):
        self.l  = l
        self.r = r 
        self.target_dict = defaultdict(int)
        for char in s2:
            self.target_dict[char]+=1

def must_grow(w):
    for value in w.target_dict.values():
        if value > 0:
            return True
    return False
    
def smallest_with_all(s1, s2):
    w = Window(s2)
    best_l = float("inf")
    best = None
    while True:
        if must_grow(w):
            if w.r == len(s1):
                break
            if s1[w.r] in s2:
                w.target_dict[s1[w.r]]-=1
            w.r+=1
        else:
            if w.r-w.l < best_l:
                best_l = w.r-w.l
                best = s1[w.l:w.r]
            if s1[w.l] in s2:
                w.target_dict[s1[w.l]]+=1
            w.l+=1
    if best_l == float("inf"):
        return -1
    return best_l

ans = smallest_with_all(s1, s2)
print(ans)

class Window:
    def __init__(self, s2, l=0, r=0):
        self.l = l
        self.r = r
        self.internal = defaultdict(int)
        for char in s2:
            self.internal[char]+=1

def mustgrow(window):
    if len(window.internal)!=0:
        return True
    return False

def shortest_with_all_letters(s1, s2):
    cur_window = Window(s2, 0, 0)
    smallest_window = Window(s2, 0, float("inf"))
    while True:
        if mustgrow(cur_window):
            if cur_window.r == len(s1):
                break
            if s1[cur_window.r] in cur_window.internal.keys():
                cur_window.internal[s1[cur_window.r]]-=1
                if cur_window.internal[s1[cur_window.r]] == 0:
                    del cur_window.internal[s1[cur_window.r]]
            cur_window.r+=1
        else:
            if cur_window.r-cur_window.l < smallest_window.r-smallest_window.l:
                smallest_window = Window(s2, cur_window.l, cur_window.r)
            #shrink
            if s1[cur_window.l] in s2:
                cur_window.internal[s1[cur_window.l]]+=1
            cur_window.l+=1
    if smallest_window.r == float("inf"):
        return -1
    return smallest_window.r-smallest_window.l

def run_tests():
  tests = [
      # Example 1 from the book
      ("helloworld", "well", 5),
      # Example 2 from the book
      ("helloworld", "weelll", -1),
      # Edge case - s2 is single character
      ("hello", "l", 1),
      # Edge case - s1 and s2 are same
      ("hello", "hello", 5),
      # s2 not in s1
      ("hello", "z", -1),
  ]
  for s1, s2, want in tests:
    got = smallest_with_all(s1, s2)
    print(got)
    assert got == want, f"\nshortest_with_all_letters({s1}, {s2}): got: {
        got}, want {want}\n"

run_tests()







