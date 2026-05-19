#!/usr/bin/env python3
import alchemy


def main() -> None:
    try:
        print("=== Distillation 1 ===")
        print("Using: 'import alchemy' structure to access potions")
        print(f"Testing strength_potion: {alchemy.strength_potion()}")
        print(f"Testing heal alias: {alchemy.heal()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
