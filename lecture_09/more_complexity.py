def print_n_numbers(n):
    """Print numbers from 0 to n-1."""
    for i in range(n):   # n
        print(i)         # n
    # Steps = 2n -> O(2n) -> O(n)

def print_exponential(n):
    """Print numbers from 1 to 2^n."""
    for i in range(1, 2**n + 1):
        print(i)
    # O(2^n)

def print_log(n):
    """Print from n to 1, halved each time."""
    while n > 0:
        print(n)
        n = n // 2
    # O(log n)

print_log(1000)