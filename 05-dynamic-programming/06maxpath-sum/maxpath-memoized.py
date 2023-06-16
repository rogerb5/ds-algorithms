# correct recursive solution
grid = [
  [1, 3, 12],
  [5, 1, 1],
  [3, 6, 1],
]

def max_path_sum(grid):
  return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]

  # Out of bounds
  # if the row is the length of the grid we made it past bottom edge  
  # if we are just past the left border 
  if r == len(grid) or c == len(grid[0]): 
    return float('-inf') #-inf because we need max value logic

  # check exactly at the bottom right corner
  if r == len(grid) - 1 and c == len(grid[0]) - 1:
    return grid[r][c] # value at bottom right corner
  
  down = _max_path_sum(grid, r + 1, c, memo)
  right = _max_path_sum(grid, r, c + 1, memo)  
  
  memo[pos] = grid[r][c] + max(down, right)
  return memo[pos]
max_path_sum(grid) # 18
