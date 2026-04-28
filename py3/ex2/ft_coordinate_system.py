import math


def euclidean(tpl: tuple, tpl2: tuple) -> float:
    return math.sqrt(
        (tpl2[0] - tpl[0])**2 + (tpl2[1] - tpl[1])**2 + (tpl2[2] - tpl[2])**2)


def get_player_pos() -> tuple:
    str = input("Enter new coordinates as floats in format 'x, y, z': ")
    tup_list = []
    list = str.split(",")
    if len(list) != 3:
        print("Invalid syntax")
        return (get_player_pos())
    for element in list:
        if element == "":
            print("Invalid syntax")
            return (get_player_pos())
        try:
            for element in list:
                tup_list.append(float(element.strip()))
        except ValueError:
            print("Invalid syntax")
            return (get_player_pos())
    return tuple(tup_list)


if __name__ == "__main__":
    print("=== Game Coordinates System ===\n")
    print("Get a first set of coordinates")
    cor1 = get_player_pos()
    print(f"Got a first tuple: {cor1}")
    print(f"It includes: X={cor1[0]}, Y={cor1[1]}, Z={cor1[2]}")

    cor0 = (0, 0, 0)
    print(f"Distance to center:{round(euclidean(cor0, cor1), 4)}")
    print("\nGet a second set of coordinates")

    cor2 = get_player_pos()
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(euclidean(cor1, cor2), 4)}"
        )
