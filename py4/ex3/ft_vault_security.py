def secure_archive(
    file_name: str, action: str = "r", write: str = ""
) -> tuple[bool, str]:
    try:
        if action == "r":
            with open(file_name, "r") as f:
                data = f.read()
            return (True, data)
        elif action == "w":
            with open(file_name, "w") as f:
                f.write(write)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid mode")
    except Exception as err:
        return (False, str(err))


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, content = secure_archive("ancient_fragment.txt")
    print((success, content))

    if success:
        print("\nUsing 'secure_archive' "
              "to write previous content to a new file:")
        print(secure_archive("new_fragment.txt", "w", content))
