
class plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print("=== Garden Plant Registery ===")
        print(f"{self.name}: {self.height}, {self.age} days old")


def input_plant() -> plant:
    name = input("nom de la plante:")
    height = int(input("taille de la plante:"))
    age = int(input("age de la plante:"))
    return plant(name, height, age)


if __name__ == "__main__":
    plantation = input_plant()
    plantation.show()
