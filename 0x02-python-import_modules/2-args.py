#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print(f"1 argument:")
    else:
        print(f"{count} arguments:")
    for i in range(count):
        print(f"{i + 1}: {argv[i + 1]}")
