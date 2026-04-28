def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    result = input_temperature("25")
    print("Input data is '25'")
    print(f"Temperature is now {result}°C")
    print("")
    try:
        print("Input data is 'abc'")
        result = input_temperature("abc")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
        print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
