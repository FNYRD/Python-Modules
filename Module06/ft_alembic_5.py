#!/usr/bin/env python3
from alchemy import create_air


def main() -> None:
    try:
        print("=== Alembic 5 ===")
        print("Accessing the alchemy module using 'from alchemy import ...'")
        print(f"Testing create_air: {create_air()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
