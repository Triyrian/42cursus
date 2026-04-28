class GardenError(Exception):
    def __init__(self, default_msg="Unknown error"):
        super().__init__(default_msg)


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:

    list1 = ["Tomato", "Lettuce", "Carrots"]
    list2 = ["Tomato", "lettuce"]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for element in list1:
            water_plant(element)
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for element in list2:
            water_plant(element)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("")
    test_watering_system()
