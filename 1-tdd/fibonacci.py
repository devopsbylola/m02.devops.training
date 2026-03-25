# define your solution
def fibonacci(n):
    # - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    if n < 0:
        raise ValueError("Input should be a non-negative integer!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

