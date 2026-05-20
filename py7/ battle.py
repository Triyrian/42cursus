from ex0.CreatureFactory import FlameFactory, AquaFactory, CreatureFactory


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    obj1 = f1.create_base()
    obj2 = f2.create_base()

    print(f"{obj1.describe()}\n vs.\n{obj2.describe()}\nfight!")
    print(f"{obj1.attack()} \n{obj2.attack()}")


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(f"{evolved.attack()}\n")


if __name__ == "__main__":

    fire = FlameFactory()
    water = AquaFactory()

    test_factory(fire)
    test_factory(water)
    battle(fire, water)
