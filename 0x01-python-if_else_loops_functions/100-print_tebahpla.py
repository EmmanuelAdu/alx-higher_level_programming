#!/usr/bin/python3
'''This prints alphabt in reverse order alternating lower and uppercase'''


a = 0
for x in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(x - a)), end="")
    a = 32 if a == 0 else 0
