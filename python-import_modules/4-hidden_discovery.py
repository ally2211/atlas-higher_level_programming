#!/usr/bin/python3
import py_compile
import sys
import dis


def main():
    # Load the compiled module
    try:
        module = __import__('hidden_4')
    except ImportError:
        sys.exit(1)

    # Get the names defined in the module
    module_names = dir(module)

    # Filter and print the names
    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)


if __name__ == "__main__":
    main()
