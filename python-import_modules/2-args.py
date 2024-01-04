#!/usr/bin/python3


from sys import argv


def main():

    arguments = argv[1:]
    num_arguments = len(arguments)

    if num_arguments != 1:
        print("{} arguments".format(num_arguments), end='')
    else:
        print("{} argument".format(num_arguments), end='')

    if num_arguments == 0:
        print('.')
    else:
        print(':')

    i = 1
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
