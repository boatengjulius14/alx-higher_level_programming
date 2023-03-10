#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if len(sys.argv) < 2:
        print("0 arguments.")
    elif len(sys.argv) < 3:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments".format(arg_len))
        for i in range(len(sys.argv)):
            if i > 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
