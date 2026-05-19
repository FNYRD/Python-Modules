#!/usr/bin/env python3
try:
    from data_generator import FuncMageDataGenerator
    from typing import List, Dict, Any
except ImportError as e:
    print(f"An error happened importing the modules\n{e}")


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: '* ' + s + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    return {'max_power': max(mages, key=lambda m: m['power'])['power'],
            'min_power': min(mages, key=lambda m: m['power'])['power'],
            'avg_power': round(sum(m['power'] for m in mages)
                               / len(mages), 2)}


def main() -> None:
    try:
        generator: FuncMageDataGenerator = FuncMageDataGenerator()
        print("Testing artifact sorter...")
        artifacts: list[dict] = artifact_sorter(generator.generate_artifacts())
        mages: List[Dict[str, Any]] = generator.generate_mages()
        spells: List[str] = generator.generate_spells()
        print(f"{artifacts[0]['name']} ({artifacts[0]['power']}) comes before"
              f" {artifacts[1]['name']} ({artifacts[1]['power']})")
        print("\nTesting power filter...")
        print("As you can see all the power values are"
              " >= than the min value = 80")
        print(power_filter(mages, 80))
        print("\nTesting spell transformer...")
        print(f"Before: {spells}\nAfter:", end=" ")
        for spell in spell_transformer(spells):
            print(spell, end=" ")
        print("\n")
        print("Testing mage stats...")
        print(f"Stats: {mage_stats(mages)}")
    except (KeyError, TypeError, IndexError) as e:
        print(f"Invalid data format: {e}")
    except ValueError as e:
        print(f"Data processing error: {e}")


if __name__ == "__main__":
    main()
