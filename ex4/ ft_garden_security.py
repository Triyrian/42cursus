class plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: int) -> None:
        if (new_height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if (new_age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = new_age
        print(f"Age updated: {new_age} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def state(self) -> None:
        print(
            f"Current state: {self._name}: {self._height}cm {self._age}"
            "days old"
            )


def input_plant(name: str, height: float, age: int) -> plant:
    print(f"Created: {name}: {height}cm, {age} days old")
    return plant(name, height, age)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = input_plant("Rose", 15.0, 10)
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-1)
    rose.set_age(-1)
    print("")
    rose.state()
