from ex1.CreatureFactory2 import HealingCreatureFactory, \
    TransformCreatureFactory


def test_healing_factory(factory: HealingCreatureFactory) -> None:

    print("Testing Creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:

    print("\nTesting Creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    test_healing_factory(heal)
    test_transform_factory(trans)
