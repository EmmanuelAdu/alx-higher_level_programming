#!/usr/bin/python3
''' THIS PROGRAM PRINTS THE NO. AND LIST OF ARGUMENT '''


if __name__ == "__main__":
    import sys
    find_len = len(sys.argv) - 1
    if find_len == 0:
        print("0 arguments.")
    elif find_len == 1:
        print("{} argument:\n{}: {}".format(find_len, find_len, sys.argv[1]))
    else:
        print("{} arguments:".format(find_len))
        for i in range(1, find_len + 1):
            print("{}: {}".format(i, sys.argv[i]))
