#!/usr/bin/env python3


class PlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class HealthyPlantError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, sunlight: int, water_level: int,
                 name: str = "") -> None:
        self.name: str = name
        self.sunlight: int = sunlight
        self.water_level: int = water_level


class GardenManager:
    def __init__(self, water_tank: int) -> None:
        self.water_tank: int = water_tank
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        if plant.name == "":
            raise PlantError("Pls use a little your brain,"
                             " the plant has no name")
        else:
            print(f"Added {plant.name} successfully")
            self.plants.append(plant)

    def watering(self) -> None:
        print("Watering plants...\nOpening watering system")
        for plant in self.plants:
            plant.water_level += 1
            self.water_tank -= 1
            print(f"Watering {plant.name} - success")
        print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        for plant in self.plants:
            if 1 <= plant.water_level <= 10 and 2 <= plant.sunlight <= 12:
                print(f"{plant.name}: healthy (water: {plant.water_level},"
                      f" sun: {plant.sunlight})")
            elif plant.sunlight < 2:
                raise HealthyPlantError(f"Error checking {plant.name}: "
                                        f"Sunlight hours {plant.sunlight}"
                                        " is too low (min 2)")
            elif plant.sunlight > 12:
                raise HealthyPlantError(f"Error checking {plant.name}: "
                                        f"Sunlight hours {plant.sunlight}"
                                        " is too high (max 12)")
            elif plant.water_level > 10:
                raise HealthyPlantError(f"Error checking {plant.name}: "
                                        f"Water level {plant.water_level}"
                                        " is too high (max 10)")
            elif plant.water_level < 1:
                raise HealthyPlantError(f"Error checking {plant.name}: "
                                        f"Water level {plant.water_level}"
                                        " is too low (min 1)")

    def taking_sun(self) -> None:
        for plant in self.plants:
            plant.sunlight += 1

    def testing_water(self) -> None:
        if self.water_tank < 50:
            raise GardenError("Caught GardenError: Not enough water in tank")


def test_garden_management() -> None:
    print("Adding plants to garden...")
    garden: GardenManager = GardenManager(40)
    try:
        plants: list[Plant] = [
            Plant(5, 8, "tomato"),
            Plant(5, 15, "lettuce"),
            Plant(5, 20),
        ]
        for plant in plants:
            garden.add_plant(plant)
    except PlantError as e:
        print(f"{e}")
    print("\nWatering plants...")
    garden.watering()
    try:
        print("\nChecking plant health...")
        garden.check_plant_health()
    except HealthyPlantError as e:
        print(f"{e}")
    try:
        print("\nTesting error recovery...")
        garden.testing_water()
    except GardenError as e:
        print(f"{e}")
    print("System recovered and continuing...\n\n"
          "Garden management system test complete!")


def main() -> None:
    test_garden_management()


if __name__ == "__main__":
    main()
