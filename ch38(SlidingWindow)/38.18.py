
def count_at_most_k_bad_days(sales, k):
    l,r = 0,0
    num_bad_days = 0
    cnt=0

    while r<len(sales):
        if num_bad_days<k or sales[r]>=10:
            if sales[r] < 10:
                num_bad_days+=1
            r+=1
            cnt+=r-l
        elif l == r:
            l+=1
            r+=1
        else:
            if sales[l] < 10:
                num_bad_days-=1
            l+=1
    return cnt

def run_tests():
  tests = [
      # Example from the book
      ([0, 20, 5], 1, 5),
      # Edge case - empty array
      ([], 1, 0),
      # Edge case - k = 0
      ([0, 20, 5], 0, 1),
      # Edge case - all good days
      ([10, 20, 30], 1, 6),
      # Edge case - all bad days
      ([0, 5, 8], 2, 5),
  ]
  for sales, k, want in tests:
    got = count_at_most_k_bad_days(sales, k)
    print(got)
    assert got == want, f"\ncount_at_most_k_bad_days({sales}, {k}): got: {
        got}, want: {want}\n"

run_tests()