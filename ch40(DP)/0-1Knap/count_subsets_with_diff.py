def min_subset_sum_diff(arr, target):
    n = len(arr)
    total = sum(arr)
    def subset_helper(sum_till_now, i):
        if i == n:
            if abs(2*sum_till_now-total) == target:
                return 1
            return 0
        yes = subset_helper(sum_till_now + arr[i], i+1)
        no = subset_helper(sum_till_now, i+1)
        return yes+no
    return subset_helper(0,0)