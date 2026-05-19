#!/usr/bin/env python3
import alchemy.elements


def main() -> None:
    try:
        print("=== Alembic 2 ===")
        print("Accessing alchemy/elements.py using 'import ...' structure")
        print(f"Testing create_earth: {alchemy.elements.create_earth()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
