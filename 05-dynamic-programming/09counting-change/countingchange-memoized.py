# correct memoized solution
def counting_change(amount, coins):
 return _counting_change(amount, coins, 0, {})

# what arguments change 
# amount and index so use both as keys in the memoo
# memoization is taking the arguments that dictate 
# the output for a function and making it the keys for the memo

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
  
  if amount == 0:
    return 1
  
  if i == len(coins):
    return 0
  
  coin = coins[i]
  
  total_count = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_count += _counting_change(remainder, coins, i + 1, memo)
    
  memo[key] = total_count
  print(total_count)
  return total_count

counting_change(4, [1, 2, 3]) # 4
