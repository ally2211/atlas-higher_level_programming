#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        a = 1 / a  # Invert the base for negative exponents
        b = abs(b)  # Use the absolute value of the exponent

    result = 1

    for _ in range(b):
        result *= a

    return round(result, 17)
