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


def input_plant(name: str, height: float, age: int) -> Plant:
    print(f"Created: {name}: {height}cm, {age} days old")
    return Plant(name, height, age)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant1 = input_plant("Rose", 25.0, 30)
    plant2 = input_plant("Oak", 200.0, 365)
    plant3 = input_plant("Cactus", 5.0, 90)
    plant4 = input_plant("Sunflower", 80.0, 45)
    plant5 = input_plant("Fern", 15.0, 120)
