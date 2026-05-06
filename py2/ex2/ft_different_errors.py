def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 42  # err
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except (ValueError) as err0:
            print(f"Caught ValueError: {err0}")
        except (ZeroDivisionError) as err1:
            print(f"Caught ZeroDivisionError: {err1}")
        except FileNotFoundError as err2:
            print(f"Caught FileNotFoundError: {err2}")
        except TypeError as err3:
            print(f"Caught TypeError: {err3}")
        i += 1

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
