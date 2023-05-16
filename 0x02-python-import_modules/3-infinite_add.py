#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    adnum = 0
    for i in range(1, len(argv)):
        adnum = adnum + int(argv[i])
    print("{}".format(adnum))
