# correct solution
# amount variable changes over time it gets smaller and smaller
def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})

def _sum_possible(amount, numbers, memo):
  if amount in memo:
    return memo[amount]
  
  if amount < 0:
    return False
  
  if amount == 0:
    return True
  
  for num in numbers:
    if _sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True
    
  memo[amount] = False  
  return False

sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
