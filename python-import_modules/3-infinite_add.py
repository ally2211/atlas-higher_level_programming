#!/usr/bin/python3
import sys


def main():
    # Get the arguments excluding the script name
    arguments = sys.argv[1:]

    # Initialize the sum
    total = 0

    # Calculate the sum of all arguments
    for arg in arguments:
        total += int(arg)

    # Print the result
    print(total)


if __name__ == "__main__":
    main()
