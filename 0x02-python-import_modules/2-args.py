#!/usr/bin/python3

import sys

if __name__ == "__main__":

    num_args = len(sys.argv) - 1

    print(f"{num_args} ", end="")

    if num_args == 0:
        # Print a new line
        print("arguments.")
    elif (num_args == 1):
        print("argument:")
        print(f"{num_args}: {sys.argv[1]}")

    elif (num_args > 1):
        print(f"arguments:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
