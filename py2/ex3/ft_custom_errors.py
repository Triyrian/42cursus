class GardenError(Exception):
    def __init__(self, default_msg="Unknown error"):
        super().__init__(default_msg)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_water():
    raise WaterError("Not enough water in the tank!")


def check_plant():
    raise PlantError("The tomato plant is wilting")


def check_garden():
    raise PlantError()


def ft_custom_errors():

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors..")
    for f in [check_plant, check_water, check_garden]:
        try:
            f()
        except GardenError as err:
            print(f"Caught GardenError : {err}")
    print("\nAll the custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("")
    ft_custom_errors()
