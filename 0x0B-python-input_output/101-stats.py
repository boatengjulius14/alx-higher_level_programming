#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


def metrics_print(size, status_codes):
    """prints computed metrics"""
    print("File size: {}".format(size))
    for i in sorted(statuscodes):
        print("{}: {}".format(i, statuscodes[i]))


if __name__ == "__main__":
    import sys

    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    statuscodes = {}
    size = 0
    count = 0

    try:
        for i in sys.stdin:
            if count != 10:
                count += 1
            else:
                metrics_print(size, statuscodes)
                count = 1
            i = i.split()
            try:
                size += int(i[-1])
            except (ValueError, IndexError):
                pass

            try:
                if i[-2] in possible_codes:
                    if statuscodes.get(i[-2], -1) != -1:
                        statuscodes[i[-2]] += 1
                    else:
                        statuscodes[i[-2]] = 1
            except IndexError:
                pass
        metrics_print(size, statuscodes)
    except KeyboardInterrupt:
        metrics_print(size, statuscodes)
        raise
