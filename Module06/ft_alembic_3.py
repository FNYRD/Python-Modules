#!/usr/bin/env python3
from alchemy.elements import create_air


def main() -> None:
    try:
        print("=== Alembic 3 ===")
        print(
            "Accessing alchemy/elements.py using"
            " 'from ... import ...' structure"
        )
        print(f"Testing create_air: {create_air()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
