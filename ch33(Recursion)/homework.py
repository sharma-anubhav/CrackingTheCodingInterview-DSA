# Problem Statement
# We wish to determine the number of ways we can place boards ranging from min to max meters in length end-to-end to total N meters. To avoid having positive lengths N which can’t be created with the given board lengths, we are allowed to saw the final board such that it is less than min meters in length.
# Implement the function combinations to compute the number of ways the boards can be arranged.
# Format for Custom Input
# Output Format
# Function combinations returns a long integer indicating the number of ways the boards can be arranged.
# Example
# Input
# 6
# 2
# 3
# Output
# 4
# Explanation
# min=2, max=3, and total=6. We can lay down boards as follows to total 6 meters, where an asterisk indicates that we cut the board:
# 2 2 2
# 2 3 1*
# 3 3
# 3 2 1*


def combinations(totallen : int, minlen : int, maxlen : int) -> int:
  m = {}
  def helper(len_remaining, minl, maxl):
    if len_remaining in m.keys():
      return m[len_remaining]

    if len_remaining == 0:
      return 1                ## <--- Possible
    
    if len_remaining < minl:
      return 1               ## <--- Possible

    sum = 0  ## <----- All possible for totallen remaining
    for option in range(minl, maxl+1):
      if option <= len_remaining:
        valid_option = helper(len_remaining-option, minl, maxl)
        if valid_option != 0:
          sum+=valid_option
      elif option > len_remaining:
        continue
    m[len_remaining] = sum
    return sum  # <---- Return total possibilities for totallen 

  return helper(totallen, minlen, maxlen)