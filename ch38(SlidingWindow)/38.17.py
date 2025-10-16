
# projected_sales = [10, 0, 0, 0, 10, 0, 0, 10]
# k = 2

def max_se(sales, k):
    l2r = 0
    cur_k = k
    good_count = 0
    boosted = [0]*len(sales)
    while l2r<len(sales):
        if sales[l2r] >=10:
            l2r+=1
            good_count+=1
        elif sales[l2r]<10 and cur_k > 0:
            boosted[l2r]=1
            cur_k-=1
            l2r+=1
            good_count+=1
        else:
            break

    r2l = len(sales)-1
    while sales[r2l]>=10 and r2l > l2r:
        good_count+=1
        r2l-=1
    l2r-=1
    best = good_count
    # print("Best before shrinking: ", best)
    while r2l >= 0 and r2l > l2r:
        if sales[r2l] < 10 and cur_k > 0:
            # print("Got a boost: increasing from right")
            cur_k-=1
            r2l-=1
            good_count+=1
            best = max(good_count, best)
        elif sales[r2l] >=10:
            # print("Already good, increasing from right")
            r2l-=1
            good_count+=1
            best = max(good_count, best)
        else:
            if l2r < 0:
                break
            # print("right needs to borrow from left")
            if boosted[l2r]:
                # print("left releasing boost")
                cur_k+=1
            l2r-=1
            good_count-=1
    print(best)
    return best
    

# max_se(projected_sales, k)



def run_tests():
  tests = [
      # Example 1 from the book
      ([10, 0, 0, 0, 10, 0, 0, 10], 2, 5),
      # Example 2 from the book
      ([0, 10, 0, 10], 1, 3),
      # Example 3
      ([5, 5, 5], 2, 2),
      # Edge case - empty array
      ([], 1, 0),
      # Edge case - k=0
      ([5, 10, 5], 0, 0),
      # Edge case - all good days
      ([10, 10, 10], 1, 3),
      # Edge case - all bad days
      ([5, 5, 5], 2, 2),
      # Edge case - k >= number of bad days
      ([5, 10, 5, 10], 3, 4),
  ]

  for projected_sales, k, want in tests:
    got_two_pointers = max_se(
        projected_sales, k)
    assert got_two_pointers == want, f"\nmax_good_days_start_and_end_two_pointers({projected_sales}, {k}): got: {got_two_pointers}, want: {want}\n"

run_tests()