#!/usr/bin/python3
"""This module reads from standard input and computes metrics
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
- Total file size up to that point
- Count of read status codes up to that point
"""


def print_stats(size, s_codes):
    """Print accumulated metrics

    Args:
         size (int): The accumulated read file size
         s_codes (dict): The accumulated count of status codes
    """
    print("File size: {}".format(size))
    for key in sorted(s_codes):
        print("{}: {}".format(key, s_codes[key]))


if __name__ == "__main__":
    import sys
    c = 0
    v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    s_codes = {}
    size = 0
    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(size, s_codes)
                c = 1
            else:
                c += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in v_codes:
                    if s_codes.get(line[-2], -1) == -1:
                        s_codes[line[-2]] = 1
                    else:
                        s_codes[line[-2]] += 1
            except IndexError:
                pass
        print_stats(size, s_codes)
    except KeyboardInterrupt:
        print_stats(size, s_codes)
        raise
