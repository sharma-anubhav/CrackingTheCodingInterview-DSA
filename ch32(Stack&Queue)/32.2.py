arr = [1, 9, 9, 3, 3, 3, 4], k = 3

def my_append(arr, ele, k):
    if len(arr) == 0:
        arr.append(ele, 1)
    if ele != arr[-1]:
        arr.append((ele, 1))
    elif ele == arr[-1]:
        if arr[-1][1] == k-1:
            for i in range(k):
                arr.pop()
            arr.my_append(arr, k*ele, k)
        else:
            arr.append((ele, arr[-1][1]+1))


def kcompress(arr, k):
    stack = []
    for ele in arr:
        my_append(stack, ele, k)
    return stack