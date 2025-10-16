"""
Problem 6: Largest Rectangle
You have an n×n mosaic made of blue and red tiles, where n > 0. 
You are given an array of integers, tiles, of length n, where tiles[i] indicates the number of blue tiles in column i of the mosaic (columns are 0-indexed). 
For each column, all the blue tiles are contiguously at the bottom, and the red tiles are contiguously at the top.

Return the size of the largest rectangle that can be formed using only blue tiles. The rectangle cannot contain partial tiles.
"""
tiles = [1, 2, 3]
Output= 4
# The mosaic is 3x3, and it looks like:
#The largest blue rectangle is 2x2 at the bottom left corner.

tiles = [2, 1, 2]
Output= 3

# tiles = [1, 2, 5, 2, 1]
# Output= 6

def next_smaller_element(arr):
 n = len(arr)
 nse = [n] * n
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

def rectagle(tiles):
    nse = next_smaller_element(tiles)
    pse = prev_smaller_element(tiles)
    print(tiles)
    print(nse)
    ans = []
    for i in range(len(nse)):
        l = tiles[i]
        w = nse[i]-pse[i]-1
        ans.append(l*w)
    return max(ans)

ans = rectagle(tiles)
print(ans)