#!/usr/bin/env python3
class Plant:
    def __init__(self, Name: str, Height: int, Age: int) -> None:
        self.name: str = Name
        self.height: int = Height
        self.age: int = Age


def main() -> None:
    information: list[tuple[str, int, int]] = [
                ("Black Baccara", 30, 1),
                ("Queen of Night", 45, 1),
                ("Saguaro", 15, 1),
                ("Romero", 7, 1),
                ("Buganvilla", 12, 1)
                ]

    plants: list[Plant] = []
    print("=== Plant Factory Output ===")
    for name, height, age in information:
        instance = Plant(name, height, age)
        plants.append(instance)
        print(f"Created: {instance.name} ({instance.height} cm,"
              f"{instance.age} days)")
    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
