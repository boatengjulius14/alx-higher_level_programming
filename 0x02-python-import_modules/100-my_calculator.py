#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculator(argv):
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    match op:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))


if __name__ == "__main__":
    import sys
    calculator(sys.argv)
