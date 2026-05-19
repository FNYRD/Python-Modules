#!/usr/bin/env python3
class HealthyPlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def check_plant_health(sunlight_hours: int,
                       water_level: int,
                       plant_name: str = "") -> None:
    if plant_name == "":
        raise HealthyPlantError("Plant name cannot be empty!")
    elif 1 <= water_level <= 10 and 2 <= sunlight_hours <= 12:
        print(f"Plant '{plant_name}' is healthy!")
    elif sunlight_hours < 2:
        raise HealthyPlantError(f"Sunlight hours {sunlight_hours}"
                                " is too low (min 2)")
    elif sunlight_hours > 12:
        raise HealthyPlantError(f"Sunlight hours {sunlight_hours}"
                                " is too high (max 12)")
    elif water_level > 10:
        raise HealthyPlantError(f"Water level {water_level}"
                                " is too high (max 10)")
    elif water_level < 1:
        raise HealthyPlantError(f"Water level {water_level}"
                                " is too low (min 1)")


def test_plant_checks() -> None:
    try:
        print("Testing good values...")
        check_plant_health(10, 10, "tomato")
    except HealthyPlantError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting empty plant name...")
        check_plant_health(10, 10)
    except HealthyPlantError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad water level...")
        check_plant_health(10, 15, "lettuce")
    except HealthyPlantError as e:
        print(f"Error: {e}")
    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health(0, 10, "lettuce")
    except HealthyPlantError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


def main() -> None:
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()


if __name__ == "__main__":
    main()
