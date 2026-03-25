# define your solution
def factorial(n):
    """
     - factorial(0) = 1
   - factorial(1) = 1
   - factorial(n) = n * factorial(n-1)
   - Raise ValueError for negative numbers
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer!")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


