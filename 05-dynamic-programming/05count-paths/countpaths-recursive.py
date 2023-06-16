# incorrect recursive solution
# test07 fails
# it is an exponential solution
grid = [
  ["O", "O"],
  ["O", "O"],
]

def count_paths(grid):
 return _count_paths(grid, 0, 0)

def _count_paths(grid, r, c):
    # check for grid bounds
    # if row or columns are out of bounds
    # or if we are inbounds but position
    # but we hit a wall X
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
     return 0

    # goal is bottom right
    # there is only one way to get to the br from br
    # if row is the last row and last column
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
     return 1

     # method eventually reach a base ase
     # number of paths to get to the target going downward
    down_count = _count_paths(grid, r + 1, c)

     # method eventually reach a base ase
     # number of paths to get to the target going  rightward
    right_count = _count_paths(grid, r, c + 1)

    return down_count + right_count

count_paths(grid)
