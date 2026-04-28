class plant():
    class __Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, {self.show_calls} show"
            )

    def __init__(self, name: str, height: float,
                 age: int, status: str) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._status = status
        self._stats = plant.__Stats()

    @classmethod
    def anonymous(cls) -> "plant":
        return cls("Unknown plant", 0.0, 0, "Anonymous")

    @staticmethod
    def older_year(age: int) -> bool:
        return age > 365

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"=== {self._status}")
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self.stats()

    def stats(self) -> None:
        print(f"[statistics for {self._name}]")
        self._stats.display()

    def grow(self) -> None:
        self._stats.grow_calls += 1
        self._height += 1.0

    def age(self) -> None:
        self._stats.age_calls += 1
        self._age += 1


class flower(plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, status: str = "Flower") -> None:
        super().__init__(name, height, age, status)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"=== {self._status}")
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if not self._bloomed:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")
        self.stats()

    def bloom(self) -> None:
        if not self._bloomed:
            print(f"[asking the {self._name} to grow and bloom]")
            self._stats.grow_calls += 1
            self._height += 8.0
            self._bloomed = True
            self.show()


class Seed(flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seed_count: int) -> None:
        super().__init__(name, height, age, color, "Seed")
        self.__seed_count = seed_count

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"=== {self._status}")
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Color: {self._color}")
        if not self._bloomed:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")
        print(f"Seeds: {self.__seed_count}")

    def bloom(self) -> None:
        if not self._bloomed:
            print(f"[make {self._name} grow, age and bloom]")
            self._stats.grow_calls += 1
            self._height += 30.0
            self._stats.age_calls += 1
            self._age += 20
            self._bloomed = True
            self.__seed_count = 42
            self.show()
            self.stats()


class tree(plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, "Tree")
        self.__trunk_diameter = trunk_diameter
        self.__shade = 0

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"=== {self._status}")
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def produce_shade(self) -> None:
        if self.__shade == 0:
            print(f"Trunk diameter: {self.__trunk_diameter}cm")
            self.stats()
            print(f"{self.__shade} shade")
            print(f"[asking the {self._name} to produce shade]")
            self.__shade += 1
        else:
            print(
                f"Tree {self._name} now produces a shade of {self._height}cm "
                f"long and {self.__trunk_diameter}cm wide."
            )
            self.stats()
            print(f"{self.__shade} shade")


def display_stats(p: plant) -> None:
    p.stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    age = 30
    print(f"Is {age} days more than a year? -> {plant.older_year(age)}")
    age = 400
    print(f"Is {age} days more than a year? -> {plant.older_year(age)}")
    print("")
    rose = flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print("")
    oak = tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    oak.produce_shade()
    print("")
    seed = Seed("Sunflower", 80.0, 45, "yellow", 0)
    seed.show()
    seed.bloom()
    print("")
    anon = plant.anonymous()
    anon.show()
