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