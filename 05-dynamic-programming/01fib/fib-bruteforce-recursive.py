# recursive fib.
# O(2^n) run time not optimal
def fib(n):
  if n == 0 or n == 1:
    print(n)
    return n

  return fib(n - 1) + fib(n - 2)

fib(0)
