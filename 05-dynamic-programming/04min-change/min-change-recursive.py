# incorrect recursive solution
# all tests do not pass (test03)
def min_change(amount, coins):
    if amount < 0:
     return float("inf")
    
    if amount == 0:
      return 0

    min_coins = float("inf") #minization logic uses +inf
    
    for coin in coins:
     # we should get a number a minimum amount of coins
     # to get remaining quantitiy (amount-coin)
     # 1 is added to count the for coin in the loop
     num_coins = 1 + min_change(amount - coin, coins) # by - we should approach 0
     if num_coins < min_coins:
         min_coins = num_coins

    return min_coins

min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
