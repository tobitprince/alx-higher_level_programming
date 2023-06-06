#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 9):
        print("{:d}{:d}".format(i, j), end=",")
print("{:d}".format(79), end=",")
print("{:d}".format(89))