#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory
from ex0.CreatureFactory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, AggressiveStrategy,
    DefensiveStrategy, InvalidStrategyError,
)
from ex2.BattleStrategy import BattleStrategy


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    # Create one creature per opponent, shared across all their battles
    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            c1, s1 = creatures[i]
            c2, s2 = creatures[j]
            print()
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        healing_factory = HealingCreatureFactory()
        transform_factory = TransformCreatureFactory()

        normal = NormalStrategy()
        aggressive = AggressiveStrategy()
        defensive = DefensiveStrategy()

        print("Tournament 0 (basic)")
        print(" [ (Flameling+Normal), (Healing+Defensive) ]")
        battle([(flame_factory, normal), (healing_factory, defensive)])

        print()
        print("Tournament 1 (error)")
        print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
        battle([(flame_factory, aggressive), (healing_factory, defensive)])

        print()
        print("Tournament 2 (multiple)")
        print(
            " [ (Aquabub+Normal), (Healing+Defensive), "
            "(Transform+Aggressive) ]"
        )
        battle([
            (aqua_factory, normal),
            (healing_factory, defensive),
            (transform_factory, aggressive),
        ])
    except (TypeError, AttributeError) as e:
        print(f"Factory error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
