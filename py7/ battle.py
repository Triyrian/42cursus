from ex0.CreatureFactory import FlameFactory, AquaFactory, CreatureFactory


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    f1 = fire.create_base()
    f2 = water.create_base()

    print(f"{f1.describe()}\n vs.\n{f2.describe()}\nfight!")
    print(f"{f1.attack()} \n{f2.attack()}")


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
