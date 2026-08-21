def odd(x):
    """Return True if x is odd, False otherwise."""
    # return x % 2 == 1 or x % 2 == -1
    return not x % 2 == 0

def sqr(x):
    """Return square of x."""
    return x ** 2    # return x * x

def pow(x, y):
    """Return x to the power of y."""
    return x ** y

def intdiv(x, y):
    """Return the quotient of x divided by y."""
    return x // y    # integer division (all decimals are truncated)

def equal(x, y):
    """Return True if string representations of x and y are equal."""
    return str(x).strip() == str(y).strip()  # strip() removes surrounding white spaces

