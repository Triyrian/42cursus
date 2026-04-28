import random

all_achievements = {
    'Crafting Genius', 'Strategist', 'World Savior',
    'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter',
    'Unstoppable', 'First Steps', 'Collector Supreme',
    'Untouchable', 'Sharp Mind', 'Boss Slayer'}


def gen_player_achievements() -> set:
    n = random.randint(4, 8)
    choose = random.sample(list(all_achievements), n)
    return set(choose)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    players = {"Alice": alice, "Bob": bob, "Charlie": charlie, "Dylan": dylan}
    for name, p in players.items():
        print(f"Player {name}: {p}")

    print(f"\nAll distinct achievements: {alice.union(bob, charlie, dylan)}")
    print(
        "\nCommon achievements : "
        f"{alice.intersection(bob, charlie, dylan)}\n"
         )
    for name, achievement in players.items():
        others = set().union(*(value for key, value in players.items()
                               if key != name))
        only = achievement.difference(others)
        print(f"Only {name} has : {only}\n")
    for name, a in players.items():
        miss = set()
        miss = all_achievements - a
        print(f"{name} is missing : {miss}")
