class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.cumulative = 0.0

    def grow(self) -> None:
        self.height += 0.8

    def grow_cumulative(self) -> None:
        self.cumulative += 0.8

    def grow_age(self) -> None:
        self.age += 1

    def show(self) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")
        for i in range(1, 8):
            self.grow()
            self.grow_age()
            self.grow_cumulative()
            print(f"=== Day {i} ===")
            print(f"{self.name}:{round(self.height, 1)}cm, {self.age} day old")
        print(f"Growth this week: {round(self.cumulative, 1)}cm")


def input_plant() -> Plant:
    name = input("nom de la plante: ")
    height = int(input("taille de la plante: "))
    age = int(input("age de la plante: "))
    return Plant(name, height, age)


if __name__ == "__main__":
    plantation = input_plant()
    plantation.show()
