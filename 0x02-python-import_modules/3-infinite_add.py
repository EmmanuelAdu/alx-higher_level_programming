#!/usr/bin/python3
'''This function adds infinite numbers or all arguments'''


if __name__ == "__main__":
    import sys

    sum_all = 0
    find_len = len(sys.argv) - 1
    for i in range(1, find_len + 1):
        sum_all += int(sys.argv[i])
    print("{}".format(sum_all))
