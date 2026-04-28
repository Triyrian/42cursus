import sys


def ft_inventory_system() -> None:

    inventory: dict[str, int] = {}

    for element in sys.argv[1:]:
        temp_list = element.split(":")

        if len(temp_list) != 2:
            print(f"Error - invalid parameter '{element}'")
            continue

        name = temp_list[0]
        quantity_str = temp_list[1]

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantitINT = int(quantity_str)
        except ValueError as err:
            print(f"Quantity error for '{name}' : {err}")
            continue

        inventory[name] = quantitINT

    if len(inventory) == 0:
        print("No valid items in inventory!")
        return

    print(f"Got inventory {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for name, quantity in inventory.items():
        res = (quantity / total) * 100
        print(f"Item {name} represents {round(res, 1)}%")

    max_item: str | None = None
    min_item: str | None = None
    for name, quantity in inventory.items():
        if max_item is None or quantity > inventory[max_item]:
            max_item = name
        if min_item is None or quantity < inventory[min_item]:
            min_item = name
    if max_item is not None and min_item is not None:
        print("Item most abundant: "
              f"{max_item} with quantity {inventory[max_item]}")
        print("Item least abundant: "
              f"{min_item} with quantity {inventory[min_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    ft_inventory_system()
