#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        print("99")
    else:
        print("{:02}".format(num), end=", ")
