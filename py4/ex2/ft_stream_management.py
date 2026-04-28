import sys


def readline(file_name: str) -> list[str]:
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
        print("---\n\n" + "".join(content) + "\n\n---")
        print(f"File '{file_name}' closed.\n")
        return content
    except FileNotFoundError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {err}")
    except PermissionError as err:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {err}")
    return []


def data_arch() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_name>")
        return

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    lines = readline(file_name)
    if not lines:
        return

    print("Transform data:")
    print("---\n")
    for line in lines:
        print(f"{line.rstrip("\n")}#")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()

    if (new_file):
        try:
            print(f"Saving data to '{new_file}'")
            with open(new_file, "w") as nf:
                nf.writelines(line.rstrip("\n") + "#\n" for line in lines)
            print(f"Data saved in file '{new_file}'.")
        except PermissionError as err:
            sys.stderr.write("[STDERR] Error opening file "
                             f"'{new_file}': {err}\n")
            print("Data not saved.")
        else:
            print("Not saving data.")


if __name__ == "__main__":
    data_arch()
