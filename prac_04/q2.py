from my_math_functions import *
from sys import argv

def main():
    """Start of program."""
    a = float(argv[1])
    b = float(argv[2])
    print(f"{a} is odd? {odd(a)}")
    print(f"{b} is odd? {odd(b)}")
    print("--" * 20)
    print(f"{a} ^ 2 = {sqr(a)}")
    print(f"{b} ^ 2 = {sqr(b)}")
    print("--" * 20)
    print(f"{a} to power of {b} = {pow(a, b)}")
    print("--" * 20)
    print(f"Quotient of {a} / {b} = {intdiv(a, b)}")
    print("--" * 20)
    print(f"{a} equal to {b} = {equal(a, b)}")

main()