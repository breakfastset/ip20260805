from my_math_functions import *

def main():
    """Start of program."""
    a = 13
    b = 8
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
    print(f"'5' equal to 5 = {equal('5', 5)}")
    print(f"'  a  ' equal to 'a' = {equal('  a  ', 'a')}")

main()