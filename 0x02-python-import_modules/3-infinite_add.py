#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    index = 1
    summation = 0
    while index <= argv_count:
        summation += int(argv[index - 1])
        index += 1
    print("{:d}".format(summation))
