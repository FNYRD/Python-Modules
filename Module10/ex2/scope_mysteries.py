#!/usr/bin/env python3
try:
    from typing import Dict, Any
    from collections.abc import Callable
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def mage_counter() -> Callable:
    called: int = 0

    def count() -> int:
        nonlocal called
        called += 1
        return called
    return count


def spell_accumulator(initial_power: int) -> Callable:
    def new_total(new_amount: int) -> int:
        nonlocal initial_power
        initial_power += new_amount
        return initial_power
    return new_total


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        try:
            return memory[key]
        except KeyError:
            return "Memory not found"
    return {'store': store, 'recall': recall}


def main() -> None:
    try:
        counter_a: Callable = mage_counter()
        counter_b: Callable = mage_counter()
        print("Testing mage counter...")
        print(f"counter_a call 1: {counter_a()}")
        print(f"counter_a call 2: {counter_a()}")
        print(f"counter_b call 1: {counter_b()}\n")

        print("Testing spell accumulator......")
        add_acumulator: Callable = spell_accumulator(100)
        print(f"Base 100, add 20: {add_acumulator(20)}")
        print(f"Base 100, add 30: {add_acumulator(30)}")

        print("\nTesting enchantment factory...")
        frozen: Callable = enchantment_factory("Frozen")
        flaming: Callable = enchantment_factory("Flaming")
        print(f"{frozen("Sword")}")
        print(f"{frozen("Shield")}")
        print(f"{flaming("gun")}")

        print("\nTesting memory vault...")
        functions: dict[str, Callable] = memory_vault()
        print("Store 'secret' = 42")
        functions['store']('secret', 42)
        print(f"Recall 'secret': {functions['recall']('secret')}")
        print(f"Recall 'unknown': {functions['recall']('recall')}")
    except TypeError as e:
        print(f"Invalid argument type: {e}")
    except ValueError as e:
        print(f"Invalid value: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
