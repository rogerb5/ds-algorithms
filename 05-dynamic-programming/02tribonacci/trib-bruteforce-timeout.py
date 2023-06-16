# incorrect solution
# all tests do not pass
def tribonacci(n):
  if n == 0 or n == 1:
    return 0

  if n == 2:
    return 1

  return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

tribonacci(1)
