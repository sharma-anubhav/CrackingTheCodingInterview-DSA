def next_greater_element(arr):
 n = len(arr)
 nge = [-1] * n
 stack = []

 for i in range(n - 1, -1, -1):
   while stack and arr[stack[-1]] <= arr[i]:
     stack.pop()
   if stack:
     nge[i] = stack[-1]
   stack.append(i)
 return nge

def next_greater_or_equal_element(arr):
  n = len(arr)
  nge = [-1] * n
  stack = []

  for i in range(n - 1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
      stack.pop()
    if stack:
      nge[i] = stack[-1]
    stack.append(i)
  return nge

def prev_greater_element(arr):
 n = len(arr)
 pge = [-1] * n
 stack = []

 for i in range(0, n):
   while stack and arr[stack[-1]] <= arr[i]:
     stack.pop()
   if stack:
     pge[i] = stack[-1]
   stack.append(i)
 return pge

def next_smaller_element(arr):
 n = len(arr)
 nse = [n] * n #<<<<<<-------- IMPPPPP CHECK WHYT THINKKK
 stack = []

 for i in range(n - 1, -1, -1):
   while stack and arr[stack[-1]] >= arr[i]:
     stack.pop()
   if stack:
     nse[i] = stack[-1]
   stack.append(i)
 return nse

def prev_smaller_element(arr):
 n = len(arr)
 pse = [-1] * n
 stack = []

 for i in range(0, n):
   while stack and arr[stack[-1]] >= arr[i]:
     stack.pop()
   if stack:
     pse[i] = stack[-1]
   stack.append(i)
 return pse



def nge(arr): # but mostly we want index so we can find length etc
    nge_arr = []
    stack = []
    n = len(arr)
    for i, ele in enumerate(arr[::-1]):
        while stack and arr[stack[-1]] <= ele: ### IMP REMEMBER TO HAVE <= not <
            stack.pop()
        if stack:
            nge_arr.append(stack[-1])
        else:
            nge_arr.append(-1)
        stack.append(n-i-1)
    return nge_arr[::-1]
  

def ngee(arr): # but mostly we want index so we can find length etc
    nge_arr = []
    stack = []
    n = len(arr)
    for i, ele in enumerate(arr[::-1]):
        while stack and arr[stack[-1]] < ele: ### IMP REMEMBER TO HAVE <= not <
            stack.pop()
        if stack:
            nge_arr.append(stack[-1])
        else:
            nge_arr.append(-1)
        stack.append(n-i-1)
    return nge_arr[::-1]

def nse(arr):
    nse_arr = []
    stack = []
    n = len(arr)
    for i, ele in enumerate(arr[::-1]):
        while stack and arr[stack[-1]] >= ele:
            stack.pop()
        if stack:
            nse_arr.append(stack[-1])
        else:
            nse_arr.append(-1)
        stack.append(n-i-1)
    return nse_arr[::-1]

def pge(arr):
    pge_arr = []
    stack = []
    for i, ele in enumerate(arr):
        while stack and arr[stack[-1]] <= ele:
            stack.pop()
        if stack:
            pge_arr.append(stack[-1])
        else:
            pge_arr.append(-1)
        stack.append(i)
    return pge_arr

def pse(arr):
    pse_arr = []
    stack = []
    for i, ele in enumerate(arr):
        while stack and arr[stack[-1]] >= ele:
            stack.pop()
        if stack:
            pse_arr.append(stack[-1])
        else:
            pse_arr.append(-1)
        stack.append(i)
    return pse_arr