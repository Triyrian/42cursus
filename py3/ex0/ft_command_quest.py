import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc = len(sys.argv)
    if (argc <= 1):
        print("No argument provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        for element in range(0, len(sys.argv) - 1):
            print(f" Argument {element + 1}: {sys.argv[element + 1]}")
    print(f"Total arguments: {argc}\n")
