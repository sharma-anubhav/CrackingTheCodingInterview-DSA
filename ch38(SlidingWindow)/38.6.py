arr = [1, 2, 3, -2, 1]
Output = 6

class Window:
    def __init__(self, l, r, sum=0):
        self.l = l
        self.r = r
        self.sum = sum
    
    def __eq__(self, other):
        return self.sum == other.sum

    def __lt__(self, other):
        return self.sum < other.sum
    
    def __gt__(self, other):
        return self.sum > other.sum
    
def cangrow(arr, window):
    s = window.sum+arr[window.r]
    if s > 0:
        return True
    return False
    
def maxss(arr):
    cur_window = Window(0,0)
    best_window = Window(-1,-1)
    while cur_window.r<len(arr):
        if cangrow(arr, cur_window):
            cur_window.sum+=arr[cur_window.r]
            cur_window.r+=1
            if cur_window>best_window:
                best_window = Window(cur_window.l, cur_window.r, cur_window.sum)
        else:
            cur_window = Window(cur_window.r+1, cur_window.r+1, 0)
    print(best_window.sum)
    return best_window.sum

maxss(arr)

        
