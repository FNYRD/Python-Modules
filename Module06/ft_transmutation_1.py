#!/usr/bin/env python3
import alchemy.transmutation


def main() -> None:
    try:
        print("=== Transmutation 1 ===")
        print("Import transmutation module directly")
        print(f"Testing lead to gold: {alchemy.transmutation.lead_to_gold()}")
    except AttributeError as e:
        print(f"Attribute error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
