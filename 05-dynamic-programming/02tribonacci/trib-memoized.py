
# correct solution using memoization
def tribonacci(n):
  return _tribonacci(n, {})
# Our dictonary has keys that represent arguments to our recursive function
# the associated values will represent the return value for that argument
def _tribonacci(n, memo):

  # if sub tree value has been encountered
  if n in memo:
    return memo[n]

  if n == 0 or n == 1:
    return 0

  if n == 2:
    return 1

  # we will key into the memo using n!
  memo[n] = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
  print(memo[n])
  return memo[n] 

tribonacci(14) # -> 927
