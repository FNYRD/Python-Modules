#!/usr/bin/env python3
import alchemy


def main() -> None:
    try:
        print("=== Transmutation 2 ===")
        print("Import alchemy module only")
        print(f"Testing lead to gold: {alchemy.lead_to_gold()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
