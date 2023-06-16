# memoized fib.
# O(n) run time is optimal for this problem
def fib(n):
  memo = {} 
  return _fib(n, memo) #memo is passed to all our recursive calls

# helper function
def _fib(n, memo):
  if n == 0 or n == 1:
    return n

  # if a key is inside a memo
  if n in memo: 
    return memo[n]

  # store info to the memo  
  memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo) 
  return memo[n]

fib(35) # -> 9227465
