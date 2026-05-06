class Plant():
    def __init__(self, name: str, height: float,
                 age: int, status: str) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._status = status

    def show(self) -> None:
        print(f"=== {self._status}")
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, "Flower")
        self.__color = color
        self.__bloomed = False

    def bloom(self) -> None:
        print(f" Color: {self.__color}")
        if not (self.__bloomed):
            print(f"{self._name} has not bloomed yet")
            print(f"[asking the {self._name} to bloom]")
            self.__bloomed = True
            return
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, "Tree")
        self.__trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f" Trunk diameter: {self.__trunk_diameter}cm")
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm "
            f"long and {self.__trunk_diameter}cm wide."
            )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age, "Vegetable")
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value

    def harvest(self) -> None:
        print(f"Harvest season: {self.__harvest_season}")
        print(f"Nutritonal value: {self.__nutritional_value}")
        print(f"[make {self._name} grow and age for 20 days]")
        self._height += 42
        self._age += 20
        self.__nutritional_value += 20
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Harvest season: {self.__harvest_season}")
        print(f"Nutritonal value: {self.__nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    first_flower = Flower("Rose", 15.0, 10, "red")
    first_flower.show()
    first_flower.bloom()
    first_flower.bloom()
    print("")
    first_tree = Tree("Oak", 200.0, 365, 5.0)
    first_tree.show()
    first_tree.produce_shade()
    print("")
    first_vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    first_vegetable.show()
    first_vegetable.harvest()
