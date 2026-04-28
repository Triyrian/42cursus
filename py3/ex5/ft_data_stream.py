import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "swim", "climb", "release"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    gen = gen_event()

    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for j in range(10):
        events.append(next(gen))

    print(f"Built list of 10 events: {events}")
# next manuellement dans la boucle jusqu'à plus rien
    for evolution in consume_event(events):
        print(f"Got event from list: {evolution}")
        print(f"Remains in list: {events}")
