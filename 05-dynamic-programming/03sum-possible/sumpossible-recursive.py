# incorrect solution
# All test do not pass
def sum_possible(amount, numbers):
    if amount < 0:
     return False
    
    if amount == 0:
     return True

    for num in numbers:
    # avoid infinite recursion
     #if num <= amount
         if sum_possible(amount - num, numbers) == True:
             return True
    
    return False

sum_possible(8, [5, 12, 4])
