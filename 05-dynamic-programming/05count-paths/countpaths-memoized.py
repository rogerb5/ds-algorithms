# Correct memoized solution
# it is an exponential solution

# Note:
# Once the recursion solution is found
# we want the keys of the memo to be the argument
# to the function that actually changes.
# row and column always change, so the combination
# can be modeled with a tuple

grid = [
  ["O", "O"],
  ["O", "O"],
]

def count_paths(grid):
 return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
    pos = (r, c) #r, c are stored as apair as keys of the memo
    if pos in memo:
     return memo[pos]
    
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
     return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
     return 1
    
    down_count = _count_paths(grid, r + 1, c, memo)
    right_count = _count_paths(grid, r, c + 1, memo)

    memo[pos] = down_count + right_count
    return memo[pos]

count_paths(grid)
