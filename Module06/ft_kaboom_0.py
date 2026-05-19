#!/usr/bin/env python3
from alchemy.grimoire import light_spell_record


def main() -> None:
    try:
        print("=== Kaboom 0 ===")
        print("Using grimoire module directly")
        print(
            f"Testing record light spell: "
            f"{light_spell_record('Fantasy', 'Earth, wind and fire')}"
        )
    except (TypeError, ValueError) as e:
        print(f"Spell error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
