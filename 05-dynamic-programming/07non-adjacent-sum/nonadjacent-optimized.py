# incorrect optimized solution
# test04 times out error
# slice creates new copies in python
# lets use an extra argument i of numbers we consider

# i = 3, [a,b,c]
# i represents the logical start to the sum array being divided
# watch out with i + 2, so make a base case to ensure no bigger number
# than length of numbers array.

nums = [2, 4, 5, 12, 7]

def non_adjacent_sum(nums):
 return _non_adjacent_sum(nums, 0)


def _non_adjacent_sum(nums, i):
    if i >= len(nums):
     return 0
    
    include = nums[i] + _non_adjacent_sum(nums, i + 2)
    exclude = _non_adjacent_sum(nums, i + 1)
    
    print(max(include, exclude))
    return max(include, exclude)

non_adjacent_sum(nums) # 16
