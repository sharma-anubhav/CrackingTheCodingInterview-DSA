
class Heap:
    def __init__(self, data = None, compare = None):
        self.heap = []
        self.is_greater_priority = self._default_compare
    
        if compare:
            self.is_greater_priority = compare
        if data:
            self.heap = data
            self._heapify()

    def _default_compare(self, a, b):
        if a>b:
            return True
        return False

    def _get_left_idx(self, idx):
        return 2*idx+1
    
    def _get_right_idx(self, idx):
        return 2*idx+2

    def _get_parent_idx(self, idx):
        if idx == 0:
            return -1
        return (idx-1)//2
    
    def top(self):
        return self.heap[0] if self.heap else -1

    def bubble_up(self, idx):
        if idx == 0:
            return 
        pi = self._get_parent_idx(idx)
        if pi == -1:
            return 
        if self.is_greater_priority(self.heap[idx], self.heap[pi]):
            self.heap[idx], self.heap[pi] = self.heap[pi], self.heap[idx]
            self.bubble_up(pi)
    
    def bubble_down(self, idx):
        li, ri = self._get_left_idx(idx), self._get_right_idx(idx)
        if li >= len(self.heap):
            return   
        maxi = li
        
        if ri < len(self.heap) and self.is_greater_priority(self.heap[ri], self.heap[li]):
            maxi = ri
        
        if self.is_greater_priority(self.heap[maxi], self.heap[idx]):
            self.heap[idx], self.heap[maxi] = self.heap[maxi], self.heap[idx]
            self.bubble_down(maxi)
    
    def _heapify(self):
        for i in range(len(self.heap)//2, -1,-1):
            self.bubble_down(i)
    
    def push(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)
        return

    def pop(self):
        if not self.heap:
            return
        ele = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if self.heap:
            self.bubble_down(0)
        return ele
    
h = Heap([5,1,2,3,5])
print(h.heap)
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
