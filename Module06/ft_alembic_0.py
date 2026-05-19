#!/usr/bin/env python3
import elements


def main() -> None:
    try:
        print("=== Alembic 0 ===")
        print("Using: 'import ...' structure to access elements.py")
        print(f"Testing create_fire: {elements.create_fire()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
