# Incorrect solution
# All test do not pass

# sum_possible(amount - num, numbers)
# (8,[5, 12, 4])
# we will take the first iteration of 5, then subtract from 8
# we get 3 and we can make a recursive call
# 3 is passed into the recursive call
# we are wondering if 3 is possible using numbers in the array

# we do not need to modify the numbers list
# also to avoid infinite recursion
# lets say current amount is 8, and we are on the iteration
# on the for loop when num is 12
# 8 - 12 = -4 would give us negative recursion. So add a base case.

def sum_possible(amount, numbers):
    if amount < 0:
     return False
    
    if amount == 0:
     return True

    for num in numbers:
     if sum_possible(amount - num, numbers) == True:
      return True
    
    return False

sum_possible(8, [5, 12, 4]) # True, 4 + 4
