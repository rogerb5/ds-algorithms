# incorrect recursive solution
# test05 fails
# the key is during recursion is to choose dif
# quantities for your same coin
# this will avoid duplicate ways counted


# counting_change(4, [1, 2, 3]) # 4
# my index was 1 at coin value 2
# we want to choose different quantities of coin 2
# to subtract from the amount

# coins = coints[i] gives a single coin value

# amount 20 and current coin is 4
# 20 / 5 = 4 so we can take at most 4 5cent coins
# range function in python the second argument is exculive
# if want to include it do + 1
# // drops decmial value in python

# _countain_change(remainder, coins, i + 1)
# will return a number that shows different ways 
# of making the remainder

# we are branching for diffrent quantites of a single coin
def counting_change(amount, coins):
 return _counting_change(amount, coins, 0)

def _counting_change(amount, coins, i):
  if amount == 0:
   return 1

  if i == len(coins):
    return 0  

  coin = coins[i]

  total_ways = 0
  
  for qty in range(0, (amount // coin) + 1):
   remainder = amount - (qty * coin)
   total_ways += _counting_change(remainder, coins, i + 1)

  print(total_ways)
  return total_ways

counting_change(4, [1, 2, 3]) # 4
