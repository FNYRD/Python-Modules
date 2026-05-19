#!/usr/bin/env python3
from elements import create_water


def main() -> None:
    try:
        print("=== Alembic 1 ===")
        print("Using: 'from ... import ...' structure to access elements.py")
        print(f"Testing create_water: {create_water()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
