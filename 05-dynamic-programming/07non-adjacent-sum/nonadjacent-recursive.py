# incorrect recursive solution
# we should think of this is a nbinary decision process

# The slice if the array ([a, b, c, d])
# a + ([c, d])
# b is not passed to the next recursive call because
# that can give an adjacent sum, we avoid index 1

nums = [2, 4, 5, 12, 7]

def non_adjacent_sum(nums):
    if len(nums) == 0:
     return 0

    # two branches coming from any particular mode
    include = nums[0] + non_adjacent_sum(nums[2:])
    exclude = non_adjacent_sum(nums[1:])
    
    print(max(include, exclude))
    return max(include, exclude)

non_adjacent_sum(nums) # 16
