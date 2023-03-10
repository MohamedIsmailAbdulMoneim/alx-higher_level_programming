#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    else if count == 1:
        print(f"1 argument:\n1: {argv[1]}")
    else:
        print(f"{count} arguments:\n")
        for i in range(count):
            print(f"{i + 1}: {argv[i + 1]}")
