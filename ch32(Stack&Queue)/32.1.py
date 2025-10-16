arr = [8, 4, 2, 2, 2, 4]

def my_append(arr, num):
    if len(arr) == 0:
        arr.append(num)

    elif num == arr[-1]:
        arr.pop()
        arr.my_append(arr, num)
    else:
        arr.append(num)
    return
    
def kcompress(arr):
    stack = []
    for ele in enumerate(arr):
        my_append(stack, ele)
    return stack