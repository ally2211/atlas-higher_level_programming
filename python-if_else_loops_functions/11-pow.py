#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1  # Any number to the zero power is 1

    invert_base = False
    if b < 0:
        invert_base = True
        b = -b  # Make exponent positive

    result = 1.0
    # If the exponent is fractional, use Python's ** operator for simplicity
    if isinstance(b, float) and not b.is_integer():
        result = a ** b
    else:
        b = int(b)  # Ensure the exponent is treated as an integer
        for _ in range(b):
            result *= a

    if invert_base:
        result = 1.0 / result

    # Adjust the sign if the base was negative and the exponent is odd
    if a < 0 and b % 2 == 1:
        result = -result

    return result