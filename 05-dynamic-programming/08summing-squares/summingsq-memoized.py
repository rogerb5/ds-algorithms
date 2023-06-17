# incorrect recursive solution

# in the for loop
# we want the last iteration to be the square root
# we are iterating through all the possible squares
# we can subtract from n

# to prefrom that subtraction
# we do 1 + sq(n - square)
# that call will tell us the min squares
# required to generate the remaining n - square quant.


# if n - square gives us back number of squares
# required to make the remaining quantity
# The number of squares required to make the entire quantity n
# would be 1 + sq(n - square) we have count the current single square we subtracted

import math 

def summing_squares(n):
 if n == 0:
  return 0

 min_squares = float('inf')
 for i in range(1, math.floor(math.sqrt(n))+ 1):
  square = i * i
  
  num_squares = 1 + summing_squares(n - square)
  min_squares = min(num_squares, min_squares)

 print(min_squares)
 return min_squares

summing_squares(8) # 2
