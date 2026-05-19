#!/usr/bin/env python3
from alchemy.potions import strength_potion, healing_potion


def main() -> None:
    try:
        print("=== Distillation 0 ===")
        print("Direct access to alchemy/potions.py")
        print(f"Testing strength_potion: {strength_potion()}")
        print(f"Testing healing_potion: {healing_potion()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
