#!/usr/bin/python3
def _add():
    _sum = 0
    length = len(sys.argv) - 1
    for i in range(length):
        _sum += int(sys.argv[i+1])
    print(_sum)


if __name__ == "__main__":
    import sys
    _add()
