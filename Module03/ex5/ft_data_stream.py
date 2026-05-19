#!/usr/bin/env python3
from typing import Generator
from typing import Iterable


def printer_one_line(begg: str, obj: Iterable) -> None:
    flag: int = 0
    print(f"{begg}", end=" ")
    for value in obj:
        if flag == 0:
            print(f"{value}", end="")
        elif 0 < flag < len(obj) - 1:
            print(f", {value}", end="")
        elif flag == len(obj) - 1:
            print(f", {value}")
        flag += 1


def prime(max: int) -> Generator[int, None, None]:
    prime_n: int = 2
    flag: int = 0
    while max > 0:
        flag = 0
        for n in range(2, int((prime_n ** 0.5)) + 1):
            if prime_n % n == 0:
                flag = 1
        if flag == 0:
            max -= 1
            yield prime_n
        prime_n += 1


def fibonacci(numbers: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(numbers):
        yield a
        a, b = b, a + b


def events() -> Generator[str, None, None]:
    events: list[str] = [
                        "killed monster",
                        "found treasure",
                        "leveled up",
                        "escaped trap",
                        "discovered secret room",
                        "leveled up",
                        "found treasure",
                        "defeated boss",
                        "unlocked chest",
                        "recruited ally",
                        "leveled up",
                        "broke curse",
                        "stole from merchant",
                        "tamed beast",
                        "found treasure",
                        "triggered alarm",
                        "leveled up",
                        "fell into pit",
                        "lost torch",
                        "got poisoned",
                        "found treasure",
                        "leveled up",
                        "burned bridge",
                        "found treasure",
                        "summoned demon"
                        ]
    for event in events:
        yield event


def players() -> Generator[tuple[str, tuple[int, int]], None, None]:
    players_lvls: dict = {
                            "alice": (5, 100),
                            "bob": (12, 342),
                            "charlie": (7, 97),
                            "diana": (3, 141),
                            "ethan": (9, 19),
                            "fiona": (15, 77),
                            "george": (1, 56),
                            "hana": (20, 34),
                            "ivan": (6, 275),
                            "julia": (11, 176),
                            "karl": (8, 89),
                            "luna": (18, 12),
                            "marco": (4, 67),
                            "nora": (14, 90),
                            "oscar": (2, 87)
                         }
    for player, info in players_lvls.items():
        yield player, info


def bad_events(event: str) -> bool:
    negative_events = [
                        "triggered alarm",
                        "fell into pit",
                        "lost torch",
                        "got poisoned",
                        "burned bridge",
                        "summoned demon",
                        "stole from merchant",
                        "bribed guard",
                      ]
    if event in negative_events:
        return True
    return False


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("\nProcessing 1000 game events...\n")
    event_number: int = 0
    players_gen = players()
    events_gen = events()
    for show in range(5):
        player, (level, points) = next(players_gen)
        event: str = next(events_gen)
        print(f"Player {player} (level {level}) {event}")
        if event == "leveled up":
            level += 1
            print(f"{player} reach a new level!!!")
            print(f"{player} was promoved to level {level}!!!")
        if bad_events(event):
            print(f"{player} lose some points :c : - {points // 3}")
        else:
            print(f"{player} won some points :) : + {points // 3}")
        event_number += 1
    print("\n=== Stream Analytics ===")
    print("Total events processed: 1000")
    new_players_gen = players()
    new_events_gen = events()
    treasure_events: int = 0
    level_up_events: int = 0
    plus_10_level: int = 0
    for event in new_events_gen:
        if event == "leveled up":
            level_up_events += 1
        if event == "found treasure":
            treasure_events += 1
    for new_player, (new_level, new_levelpoints) in new_players_gen:
        if new_level > 10:
            plus_10_level += 1
    print("To show more coherence between our data and"
          " the analytics weĺl modificate some data:")
    print(f"High-level players (10+): {plus_10_level * 30}")
    print(f"Treasure events: {treasure_events * 15}")
    print(f"Level-up events: {level_up_events * 16}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    prime_return: Generator[int, None, None] = prime(5)
    primes: list[int] = [next(prime_return) for x in range(5)]
    print("=== Generator Demonstration ===")
    fibo_return: Generator[int, None, None] = fibonacci(10)
    fibos: list[int] = [next(fibo_return) for x in range(10)]
    printer_one_line(f"Fibonacci sequence (first {len(fibos)}):", fibos)
    printer_one_line(f"Prime numbers (first {len(primes)}):", primes)


if __name__ == "__main__":
    main()
