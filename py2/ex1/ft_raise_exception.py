def input_temperature(temp_str: str) -> int:
    if (0 <= int(temp_str) <= 40):
        return int(temp_str)
    else:
        temp = int(temp_str)
        if temp >= 20:
            max_limit = 40
        else:
            max_limit = 0
        raise ValueError(
            f"Caught input_temperature error: {temp_str}°C"
            f" is too hot for plants (max {max_limit}°C)"
                        )


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
    try:
        print("Input data is '100'")
        result = input_temperature("100")
    except ValueError as err1:
        print(f"{err1}")
        print("")
    try:
        print("Input data is '-50'")
        result = input_temperature("-50")
    except ValueError as err2:
        print(f"{err2}")
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperatur Checker ===")
    print("")
    test_temperature()
