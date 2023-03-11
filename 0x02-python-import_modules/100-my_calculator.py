#!/usr/bin/python3
def calculator(argv):
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    match argv[2]:
        case '+':
            result = add(int(argv[1]), int(argv[3]))
        case '-':
            result = sub(int(argv[1]), int(argv[3]))
        case '*':
            result = mul(int(argv[1]), int(argv[3]))
        case '/':
            result = div(int(argv[1]), int(argv[3]))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))


if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    calculator(sys.argv)
