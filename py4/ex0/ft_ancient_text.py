import sys


def data_arch() -> None:
    print("=== Cyber Archives Recovery ===")

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_name>")
        return

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    try:
        f = open(file_name, "r")
        content = f.read()
        print(f"---\n\n{content}\n\n---")
        f.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError as err1:
        print(f"Error opening file '{file_name}': {err1}\n")
    except PermissionError as err2:
        print(f"Error opening file '{file_name}': {err2}\n")


if __name__ == "__main__":
    data_arch()
