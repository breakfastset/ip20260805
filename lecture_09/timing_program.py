import time

def fibonacci(n):
    """Fibonacci numbers are defined as follows:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # exponential growth -> O(2^n)

def fibonacci2(n):
    """Return the nth Fibonacci number with a loop."""
    if n == 0 or n == 1:
        return n
    else:
        num_1 = 0
        num_2 = 1
        for i in range(2, n+1):
            num = num_1 + num_2
            num_1 = num_2
            num_2 = num
        return num

def main():
    nth_term = 40
    start_time = time.time()
    print(fibonacci(nth_term))
    end_time = time.time()
    print("Time taken: ", end_time - start_time)

    print("----")
    start_time = time.time()
    print(fibonacci2(nth_term))
    end_time = time.time()
    print("Time taken: ", end_time - start_time)

if __name__ == '__main__':
    main()