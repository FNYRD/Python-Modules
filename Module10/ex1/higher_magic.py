#!/usr/bin/env python3
try:
    from collections.abc import Callable
    from data_generator import FuncMageDataGenerator
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def fireball(target: str, attack: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, attack: int) -> str:
    return f"Heals {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def response(target: str, attack: int) -> tuple:
        return (spell1(target, attack), spell2(target, attack))
    return response


def meteor(target: str, attack: int) -> str:
    return f"{target} was hit by {attack} points of impact"


def tornado(target: str, attack: int) -> str:
    return f"{target} was hit by {attack} points of impact"


def earthquake(target: str, attack: int) -> str:
    return f"{target} was hit by {attack} points of impact"


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_function(target: str, attack: int) -> str:
        return base_spell(target, attack * multiplier)
    return new_function


def powerful(target: str, attack: int) -> bool:
    return attack > 50


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def just_powerfull(target: str, attack: int) -> str:
        if condition(target, attack):
            return spell(target, attack)
        return "Spell fizzled"
    return just_powerfull


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_attack(target: str, attack: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, attack))
        return results
    return sequence_attack


def main() -> None:
    try:
        generator: FuncMageDataGenerator = FuncMageDataGenerator()
        generator.generate_spells()
        print("Testing spell_combiner..")
        fun: Callable = spell_combiner(fireball, heal)
        combined: tuple = fun("Dragon", 50)
        print(f"Combined spell result: {combined[0]}, {combined[1]}")

        print("\nTesting power_amplifier..")
        print(f"Before: {meteor("Dragon", 3)}")
        aplified: Callable = power_amplifier(meteor, 10)
        print(f"After: {aplified("Dragon", 3)}")

        print("\nTesting conditional_caster..")
        power_ful: str = conditional_caster(powerful, meteor)
        print(f"How works: {power_ful("Dragon", 60)}")
        print(f"How doesn't work: {power_ful("Dragon", 40)}")

        print("\nTesting spell_sequence..")
        sequencer: Callable = spell_sequence([meteor, earthquake, tornado])
        print(f"List of results: {sequencer("Dragon", 200)}")
    except TypeError as e:
        print(f"Invalid spell or argument type: {e}")
    except ValueError as e:
        print(f"Invalid value: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
