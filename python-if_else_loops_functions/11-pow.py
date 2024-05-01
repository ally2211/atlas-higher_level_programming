#!/usr/bin/python3
from decimal import Decimal, getcontext, localcontext

from decimal import Decimal, getcontext

# Set the precision globally
getcontext().prec = 50

def pow(a, b):
    a = Decimal(a)
    b = Decimal(b)

    if b == 0:
        return Decimal(1)  # Any number to the zero power is 1
    if b < 0:
        a = 1 / a  # Invert the base for negative exponents
        b = -b  # Make exponent positive

    result = Decimal(1)
    is_negative = a < 0 and (b % 2 != 0)  # Check if the result should be negative

    # If the exponent is not an integer, use the Decimal's `**` operator to handle fractional powers
    if not b % 1 == 0:
        result = a ** b
    else:
        for _ in range(int(b)):
            result *= a

    if is_negative:
        result = -result  # Adjust the sign if needed

    return result