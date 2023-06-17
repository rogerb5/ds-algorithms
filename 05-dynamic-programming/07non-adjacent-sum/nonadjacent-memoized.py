# Correct memoized solution
nums = [2, 4, 5, 12, 7]

def non_adjacent_sum(nums):
 return _non_adjacent_sum(nums, 0, {})

# when we memoize we should encode
# all the arguments that change
# through the recursion as keys of your memo
def _non_adjacent_sum(nums, i, memo):
    if i in memo:
     return memo[i]
        
    if i >= len(nums):
     return 0
    
    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclude = _non_adjacent_sum(nums, i + 1, memo)
    
    print(max(include, exclude))
    memo[i] = max(include, exclude)
    return memo[i]

non_adjacent_sum(nums) # 16
