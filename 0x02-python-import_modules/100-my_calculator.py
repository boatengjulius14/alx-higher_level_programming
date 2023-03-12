#!/usr/bin/python3
def calculator(argv):
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    calculator(sys.argv)
