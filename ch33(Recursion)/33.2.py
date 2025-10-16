arr = [1, [2, 3], [4, [5]], 6]

#helper method. But this can get confusing because we had to go back to the main non helper. 
def nested_sum(arr):
    def ns_helper(i):
        if i>=len(arr):
            return 0
        if isinstance(arr[i], int):
            return arr[i]+ns_helper(i+1)
        else:
            return nested_sum(arr[i])+ns_helper(i+1)
    return ns_helper(0)

# So this is hard to visualize but we are technically doing the same thing.
# But if you think about it, we are moving towards the base case which is to make arr an int by iteration
# Second thing we are taking care is to handle returns correctly. we cannot just return directly. we have to sum up 
# all the returns before returning.

## THis is a tricky base case. Easy to over complicate
def nested_sum2(arr):
    if isinstance(arr, int):
        return arr
    tmp = 0
    for ele in arr:
        tmp+=nested_sum(ele)

ans = nested_sum(arr)
print(ans)


# But if you think about this, this is essentially same as q1. This logic is more likely what
# you can comfortably think in a interview.
def ns2(arr):
    if len(arr) <1:
        return 0
    if isinstance(arr[0], int):
        return arr[0]+ns2(arr[1:])
    else:
        return ns2(arr[0]) + ns2(arr[1:])