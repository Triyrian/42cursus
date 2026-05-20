from ex2.BattleStrategy import NormalStrategy, DefensiveStrategy, \
    AggressiveStrategy, BattleStrategy
from ex1.CreatureFactory2 import HealingCreatureFactory, \
    TransformCreatureFactory, CreatureFactory
from ex0.CreatureFactory import FlameFactory, AquaFactory


def battle(deck: list[tuple(CreatureFactory, BattleStrategy)]) -> None:
    print("*** Tournament***")
    print(f"{len(deck)} opponents involved")

    for i in range(len(deck)):
        for j in range(i + 1, len(deck)):
            factory1, strat1 = deck[i]
            factory2, strat2 = deck[j]

            deck1 = factory1.create_base()
            deck2 = factory2.create_base()

            print("\n* Battle *")
            print(deck1.describe())
            print(" vs.")
            print(deck2.describe())
            print(" now fight!")

            try:
                strat1.act(deck1)
                strat2.act(deck2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    fire = FlameFactory()
    water = AquaFactory()
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    normal_strat = NormalStrategy()
    def_strat = DefensiveStrategy()

    deck1 = [(fire, normal_strat), (heal, def_strat)]

    print("[ (Flameling+Normal), (Healing+defensive) ]")
    battle(deck1)

    print("\nTournament 1 (error)")
    ag_strat = AggressiveStrategy()

    deck2 = [(fire, ag_strat), (heal, def_strat)]

    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(deck2)

    print("\nTournament 2 (multiple)")

    superdeck = [(water, normal_strat), (heal, def_strat), (trans, ag_strat)]
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(superdeck)
