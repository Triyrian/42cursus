import random

# liste et dicto de comprehension tah NSI
if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    initial_list = ['Alice', 'bob', 'Charlie', 'dylan',
                    'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    capitalized_list = [elem.capitalize() for elem in initial_list]
    capitlize_only = [elm for elm in initial_list if elm == elm.capitalize()]

    print(f"Initial list of players: {initial_list}")
    print(f"New list with all name capitalized: {capitalized_list}")
    print(f"New list of capitalized names only: {capitlize_only}")

    scores = {name: random.randint(0, 1000) for name in capitalized_list}
    print(f"Score dict: {scores}")

    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high_scores = {
        name: score
        for name, score in scores.items()
        if score > average
    }
    print(f"High scores: {high_scores}")
