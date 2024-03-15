#!/usr/bin/python3
import sys

def main():
    # Get the number of arguments excluding the script name
    args_count = len(sys.argv) - 1
    # Choose the right label for argument/arguments based on the count
    arg_label = "argument" if args_count == 1 else "arguments"

    # Print the number of arguments
    print(f"Number of {arg_label}{'.' if args_count == 0 else ':'}", args_count)

    # If there are arguments, print them
    if args_count > 0:
        print()  # Print a new line before listing the arguments
        for i, arg in enumerate(sys.argv[1:], start=1):  # Start counting from 1
            print(f"{i}: {arg}")

# Check if the script is being run directly or imported
if __name__ == "__main__":
    main()
