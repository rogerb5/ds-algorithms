# correct memoized solution

import math

def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n in memo:
    return memo[n]
  
  if n == 0:
    return 0
  
  min_squares = float('inf')
  for i in range(1, math.floor(math.sqrt(n) + 1)):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(min_squares, num_squares)
  
  memo[n] = min_squares
  print(min_squares)
  return min_squares

summing_squares(8) # 2
