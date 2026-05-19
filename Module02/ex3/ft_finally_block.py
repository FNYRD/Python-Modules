#!/usr/bin/env python3
class PlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str) -> None:
        self.name: str = name


def checking_name(plant: Plant) -> None:
    if plant.name == "None":
        raise PlantError(f"Cannot water {plant.name} - invalid plant!")


def water_plants(plant_list: list[Plant]) -> None:
    print("Testing normal watering...\nOpening watering system")
    try:
        for plant in plant_list:
            checking_name(plant)
            print(f"Watering {plant.name}")
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plants: list[Plant] = []
    names: list[str] = ["tomato", "lettuce", "carrots"]
    for name in names:
        obj: Plant = Plant(name)
        plants.append(obj)
    water_plants(plants)
    print("Watering completed successfully!\n")
    plants_error: list[Plant] = []
    names_error: list[str] = ["tomato", "None", "carrots"]
    for name in names_error:
        obj2: Plant = Plant(name)
        plants_error.append(obj2)
    water_plants(plants_error)
    print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
